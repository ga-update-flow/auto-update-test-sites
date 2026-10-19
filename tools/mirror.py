"""Static mirror of a server-rendered site for auto-update-flow testing.

usage: py mirror.py <start_url> <out_dir> [max_pages]

Pass 1 crawls (same-site pages + every asset/document they reference) and saves raw files.
Pass 2 rewrites internal links in HTML/CSS to relative paths so the copy works from any URL.
"""
import hashlib
import json
import mimetypes
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote, unquote, urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
DOC_EXT = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".zip", ".csv", ".rtf", ".odt", ".txt"}
SKIP_PAGE = re.compile(r"/(wp-json|xmlrpc\.php|wp-admin|wp-login\.php|feed|embed)(/|$)|/(day|month|week|photo|map|summary)/\d{4}-|/events/(month|list|week|day|photo|map)/?$|/events/.*/\d{4}-\d{2}(-\d{2})?/?$")
KEEP_REL = {"stylesheet", "icon", "shortcut", "apple-touch-icon", "preload", "modulepreload", "mask-icon", "manifest"}
MAX_BYTES = 80 * 1024 * 1024
URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I)
IMPORT_RE = re.compile(r"@import\s+(['\"])(.*?)\1", re.I)

S = requests.Session()
S.headers["User-Agent"] = UA


def bare(host):
    return host.lower().removeprefix("www.")


def canon(url):
    p = urlsplit(url)
    return urlunsplit(("https", p.netloc.lower(), p.path or "/", p.query, ""))


def clean_seg(s):
    return re.sub(r'[<>:"|?*\\]', "_", s)[:120]


def local_path(url, ctype, site_host):
    p = urlsplit(url)
    path = unquote(p.path) or "/"
    base = "" if bare(p.netloc) == site_host else "_ext/" + p.netloc + "/"
    ext = os.path.splitext(path)[1].lower()
    if "html" in ctype:
        if path.endswith("/"):
            path += "index.html"
        elif ext not in (".html", ".htm"):
            path += "/index.html"
    elif path.endswith("/") or not ext:
        path = path.rstrip("/") + "/index" + (mimetypes.guess_extension(ctype.split(";")[0].strip()) or ".bin")
    if p.query and "html" not in ctype and (base or not ext):
        stem, e = os.path.splitext(path)
        path = f"{stem}_{hashlib.md5(p.query.encode()).hexdigest()[:8]}{e}"
    segs = [clean_seg(x) for x in path.strip("/").split("/")]
    return base + "/".join(segs)


def fetch(url):
    for _ in range(6):
        try:
            r = S.get(url, timeout=30, stream=True)
            if r.status_code in (429, 503):
                time.sleep(min(int(r.headers.get("retry-after", 20)), 90))
                continue
            body = b""
            for chunk in r.iter_content(65536):
                body += chunk
                if len(body) > MAX_BYTES:
                    return url, r.url, r.status_code, r.headers.get("content-type", ""), None
            return url, r.url, r.status_code, r.headers.get("content-type", ""), body
        except requests.RequestException:
            time.sleep(1)
    return url, url, 0, "", None


def css_refs(text, base_url):
    out = [m.group(2) for m in URL_RE.finditer(text)] + [m.group(2) for m in IMPORT_RE.finditer(text)]
    return [urljoin(base_url, u.strip()) for u in out if u.strip() and not u.strip().startswith(("data:", "#", "about:"))]


def html_refs(soup, base_url, site_host):
    """Yield (url, kind) for everything the page references. kind: page|asset"""
    def abs_(u):
        u = (u or "").strip()
        if not u or u.startswith(("#", "mailto:", "tel:", "javascript:", "data:", "sms:")):
            return None
        return urljoin(base_url, u)

    for t in soup.find_all(True):
        n = t.name
        if n in ("a", "area"):
            u = abs_(t.get("href"))
            if u:
                ext = os.path.splitext(urlsplit(u).path)[1].lower()
                same = bare(urlsplit(u).netloc) == site_host
                if ext in DOC_EXT:
                    yield u, "asset"
                elif same and urlsplit(u).scheme in ("http", "https"):
                    yield u, ("asset" if ext and ext not in (".html", ".htm", ".php") else "page")
        elif n == "link":
            rel = {r.lower() for r in (t.get("rel") or [])}
            if rel & KEEP_REL and abs_(t.get("href")):
                yield abs_(t.get("href")), "asset"
        elif n == "script":
            u = abs_(t.get("src"))
            if u and bare(urlsplit(u).netloc) == site_host:
                yield u, "asset"
        for attr in ("src", "data-src", "data-lazy-src", "poster", "data-bg", "data-background"):
            if n in ("img", "source", "video", "audio", "input", "div", "section", "span", "track") and abs_(t.get(attr)):
                yield abs_(t.get(attr)), "asset"
        for attr in ("srcset", "data-srcset", "data-lazy-srcset"):
            if t.get(attr):
                for cand in t[attr].split(","):
                    u = abs_(cand.strip().split(" ")[0]) if cand.strip() else None
                    if u:
                        yield u, "asset"
        if t.get("style"):
            for u in css_refs(t["style"], base_url):
                yield u, "asset"
        if n == "style" and t.string:
            for u in css_refs(t.string, base_url):
                yield u, "asset"


def crawl(start, out, max_pages, seeds=(), mapping=None):
    site_host = bare(urlsplit(start).netloc)
    mapping, failed, skipped = dict(mapping or {}), [], []
    seen = set(mapping)
    queue = []
    for u in [start, *seeds]:
        c = canon(u)
        if c not in seen:
            seen.add(c)
            queue.append((c, "page"))
    pages = 0
    with ThreadPoolExecutor(int(os.environ.get('WORKERS', 8))) as pool:
        while queue:
            batch, queue = queue[:40], queue[40:]
            for (orig, kind), (_, final, status, ctype, body) in zip(batch, pool.map(fetch, [u for u, _ in batch])):
                if body is None or status >= 400 or status == 0:
                    failed.append({"url": orig, "status": status})
                    continue
                final_c = canon(final)
                if kind == "page" and bare(urlsplit(final_c).netloc) != site_host:
                    skipped.append(orig)
                    continue
                if final_c in mapping:
                    mapping[orig] = mapping[final_c]
                    continue
                lp = local_path(final_c, ctype, site_host)
                dest = os.path.join(out, lp.replace("/", os.sep))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(body)
                mapping[orig] = mapping[final_c] = lp
                new = []
                if "html" in ctype:
                    pages += 1
                    print(f"[{pages}] {final_c}", flush=True)
                    soup = BeautifulSoup(body, "html.parser")
                    new = list(html_refs(soup, final_c, site_host))
                elif "css" in ctype:
                    new = [(u, "asset") for u in css_refs(body.decode("utf-8", "replace"), final_c)]
                for u, k in new:
                    c = canon(u)
                    if c in seen or SKIP_PAGE.search(urlsplit(c).path):
                        continue
                    if k == "page" and (urlsplit(c).query or pages + sum(1 for _, kk in queue if kk == "page") >= max_pages):
                        continue
                    seen.add(c)
                    queue.append((c, k))
    return site_host, mapping, failed, skipped


def make_ref(mapping, from_local, url, base_url):
    full = urljoin(base_url, url.strip())
    frag = urlsplit(full).fragment
    to = mapping.get(canon(full))
    if not to:
        return None
    if to.endswith("/index.html") or to == "index.html":
        tdir = to[: -len("index.html")]
        r = os.path.relpath(tdir or ".", os.path.dirname(from_local) or ".").replace(os.sep, "/")
        r = "./" if r == "." else r + "/"
    else:
        r = os.path.relpath(to, os.path.dirname(from_local) or ".").replace(os.sep, "/")
    return quote(r, safe="/-._~%") + (("#" + frag) if frag else "")


def rewrite_css(text, mapping, from_local, base_url):
    def sub_url(m):
        u = m.group(2).strip()
        r = None if u.startswith("data:") else make_ref(mapping, from_local, u, base_url)
        return f"url({m.group(1)}{r}{m.group(1)})" if r else m.group(0)

    def sub_imp(m):
        r = make_ref(mapping, from_local, m.group(2), base_url)
        return f"@import {m.group(1)}{r}{m.group(1)}" if r else m.group(0)

    return IMPORT_RE.sub(sub_imp, URL_RE.sub(sub_url, text))


def rewrite_all(out, mapping, orig_by_local, only=None):
    for lp in sorted(only if only is not None else set(mapping.values())):
        path = os.path.join(out, lp.replace("/", os.sep))
        base_url = orig_by_local[lp]
        if lp.endswith((".html", ".htm")) and "html" in (mimetypes.guess_type(lp)[0] or ""):
            soup = BeautifulSoup(open(path, "rb").read(), "html.parser")

            def fix(tag, attr):
                v = tag.get(attr)
                if v and not v.strip().startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                    r = make_ref(mapping, lp, v, base_url)
                    if r:
                        tag[attr] = r

            for t in soup.find_all(True):
                for a in ("href", "src", "data-src", "data-lazy-src", "poster", "data-bg", "data-background"):
                    if t.has_attr(a):
                        fix(t, a)
                for a in ("srcset", "data-srcset", "data-lazy-srcset"):
                    if t.get(a):
                        parts = []
                        for cand in t[a].split(","):
                            bits = cand.strip().split(" ", 1)
                            r = make_ref(mapping, lp, bits[0], base_url) if bits[0] else None
                            parts.append(" ".join([r or bits[0]] + bits[1:]))
                        t[a] = ", ".join(parts)
                if t.get("style"):
                    t["style"] = rewrite_css(t["style"], mapping, lp, base_url)
                if t.name == "style" and t.string:
                    t.string = rewrite_css(t.string, mapping, lp, base_url)
            open(path, "w", encoding="utf-8").write(str(soup))
        elif lp.endswith(".css"):
            text = open(path, "rb").read().decode("utf-8", "replace")
            open(path, "w", encoding="utf-8").write(rewrite_css(text, mapping, lp, base_url))


if __name__ == "__main__":
    start, out = sys.argv[1], sys.argv[2]
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 400
    os.makedirs(out, exist_ok=True)
    mpath = os.path.join(out, "_manifest.json")
    old_files, old_failed, mapping, seeds = {}, [], {}, []
    if os.environ.get("SUPPLEMENT") and os.path.exists(mpath):
        # fill gaps in an existing mirror: only fetch what the manifest doesn't already have
        prev = json.load(open(mpath))
        old_files, old_failed = prev["files"], prev["failed"]
        mapping = {canon(u): lp for lp, u in old_files.items()}
    if os.environ.get("SITEMAP") or os.environ.get("SUPPLEMENT"):
        from check_sitemap import sitemap_urls
        seeds = [u for u in sitemap_urls(start.rstrip("/") + "/sitemap_index.xml") if not SKIP_PAGE.search(urlsplit(u).path)]
        print(f"seeding {len(seeds)} sitemap URLs", flush=True)
    host, mapping, failed, skipped = crawl(start, out, cap, seeds, mapping)
    orig_by_local = dict(old_files)
    for u, lp in mapping.items():
        orig_by_local.setdefault(lp, u)
    rewrite_all(out, mapping, orig_by_local, only=set(orig_by_local) - set(old_files) if old_files else None)
    json.dump({"start": start, "files": orig_by_local, "failed": old_failed + failed,
               "skipped_offsite_redirects": skipped}, open(mpath, "w"), indent=1)
    print(f"done: {len(orig_by_local)} files, {len(old_failed + failed)} failed")
