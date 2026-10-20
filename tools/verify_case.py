"""Verify that a test-case branch changes CONTENT ONLY, never the website itself.

usage: py verify_case.py <site_repo_dir> <case_branch> [--base baseline-v1] [--allow-docs] [--allow-delete] [--json]

Rules checked against the baseline:
  1. Only .html pages (and, with --allow-docs, added/changed .pdf documents) may differ. Any change to CSS, JS, images,
     fonts, manifest or other files fails. Deleting a page needs --allow-delete (the 404 case).
  2. For every modified HTML page the structural skeleton must be identical: same block tags with the same attributes
     in the same order. Text, <br>, <strong>/<em>/<span> and similar inline markup may change.
     With --allow-docs, the href of a link may change (new document file name), but no link may be added or removed.
Prints PASS/FAIL, the changed files and a visible-text diff (the answer key for the flow).
"""
import difflib
import re
import subprocess
import sys

from bs4 import BeautifulSoup, Comment

INLINE = {"br", "strong", "b", "em", "i", "span", "u", "small", "mark", "sup", "sub", "wbr"}
args = sys.argv[1:]
repo, branch = args[0], args[1]
base = args[args.index("--base") + 1] if "--base" in args else "baseline-v1"
allow_docs, allow_delete, as_json = "--allow-docs" in args, "--allow-delete" in args, "--json" in args


def git(*a):
    return subprocess.run(["git", "-C", repo, "-c", "core.quotepath=false", *a], capture_output=True, check=True).stdout


def skeleton(html, ignore_href):
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for t in soup.find_all(True):
        if t.name in INLINE:
            continue
        attrs = dict(t.attrs)
        if ignore_href and t.name == "a":
            attrs.pop("href", None)
        out.append((t.name, tuple(sorted((k, " ".join(v) if isinstance(v, list) else v) for k, v in attrs.items()))))
    return out


def visible_lines(html):
    soup = BeautifulSoup(html, "html.parser")
    for x in soup(["script", "style", "noscript"]):
        x.decompose()
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    return [l.strip() for l in re.sub(r"[ \t\r]+", " ", soup.get_text("\n")).split("\n") if l.strip()]


problems, changes = [], []
for line in git("diff", "--name-status", f"{base}..{branch}").decode("utf-8").splitlines():
    status, path = line.split("\t", 1)
    ext = path.lower().rsplit(".", 1)[-1] if "." in path else ""
    if ext == "html" and status == "M":
        old, new = git("show", f"{base}:{path}"), git("show", f"{branch}:{path}")
        a, b = skeleton(old, allow_docs), skeleton(new, allow_docs)
        if a != b:
            first = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            problems.append(f"STRUCTURE CHANGED in {path} at element #{first} (baseline {len(a)} elements vs branch {len(b)})")
        d = [l for l in difflib.unified_diff(visible_lines(old), visible_lines(new), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        changes.append({"file": path, "status": status, "text_diff": d})
    elif ext == "pdf" and status in ("A", "M") and allow_docs:
        changes.append({"file": path, "status": status, "text_diff": []})
    elif status == "D" and allow_delete and ext == "html":
        changes.append({"file": path, "status": status, "text_diff": []})
    else:
        problems.append(f"NOT ALLOWED: {status} {path}")

if as_json:
    import json
    print(json.dumps({"pass": not problems, "problems": problems, "changes": changes}, indent=1))
else:
    print(f"[{repo}] {branch} vs {base}: {'PASS' if not problems else 'FAIL'}  ({len(changes)} file(s) changed)")
    for p in problems:
        print("  !!", p)
    for c in changes:
        print(f"  {c['status']} {c['file']}")
        for l in c["text_diff"][:12]:
            print("     ", l[:200])
sys.exit(1 if problems else 0)
