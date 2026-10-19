"""Compare a site's sitemap against a mirror's manifest.

usage: py check_sitemap.py <site_root_url> <mirror_dir>
Prints sitemap URLs that were not mirrored (pages and uploaded documents/media).
"""
import json
import os
import re
import sys
import time
from urllib.parse import urlsplit, urlunsplit

import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"}


def norm(u):
    p = urlsplit(u.strip())
    host = p.netloc.lower().removeprefix("www.")
    return urlunsplit(("https", host, p.path.rstrip("/") or "/", p.query, ""))


def get(url):
    for _ in range(5):
        r = requests.get(url, headers=UA, timeout=30)
        if r.status_code == 429:
            time.sleep(30)
            continue
        return r.text
    return ""


def sitemap_urls(url):
    text = get(url)
    locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", text)
    if "<sitemapindex" in text:
        out = []
        for loc in locs:
            out += sitemap_urls(loc)
            time.sleep(1)
        return out
    return locs


if __name__ == "__main__":
    root, mirror = sys.argv[1], sys.argv[2]
    manifest = json.load(open(os.path.join(mirror, "_manifest.json")))
    have = {norm(u) for u in manifest["files"].values()}
    urls = sitemap_urls(root.rstrip("/") + "/sitemap_index.xml")
    want = [u for u in dict.fromkeys(urls)]
    missing = [u for u in want if norm(u) not in have]
    print(f"sitemap URLs: {len(want)}  mirrored: {len(want) - len(missing)}  missing: {len(missing)}")
    for u in missing:
        print("MISSING", u)
