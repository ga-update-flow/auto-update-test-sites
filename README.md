# Auto-Update Test Sites (hub)

This private repo is the team's single entry point for the **test sites** used to exercise the
opportunity auto-update flow. The sites themselves are exact static mirrors of three real funder
websites. Each lives in its own repo (GitHub Pages caps a site at 1 GB, so they can't share one).
We change the copies on purpose (dates, documents, links, text) and check that the flow detects
and reports exactly those changes.

## Sites

| Level  | Original                       | Repo                         | Live URL (GitHub Pages) |
|--------|--------------------------------|------------------------------|-------------------------|
| Easy   | https://www.bcm.org/           | `test-site-easy-bcm`         | https://javedibrahim200.github.io/test-site-easy-bcm/ |
| Medium | https://muskegonfoundation.org | `test-site-medium-muskegon`  | https://javedibrahim200.github.io/test-site-medium-muskegon/ |
| Hard   | https://cffoxvalley.org/       | `test-site-hard-cffoxvalley` | https://javedibrahim200.github.io/test-site-hard-cffoxvalley/ |

Mirror stats (all pages in each site's sitemap are included):

| Site   | Sitemap pages | Files | Notes |
|--------|---------------|-------|-------|
| Easy   | 153           | ~830  | ~150 MB |
| Medium | 1,214         | ~7,200| 95 URLs were already dead on the live site |
| Hard   | 1,965         | ~5,500| ~1 GB, right at the GitHub Pages 1 GB cap; contains two files over 25 MB (a 32 MB audio file and a 29.9 MB report PDF) |

All internal links are relative, so each site works from any URL or sub-path.
`_manifest.json` in each site repo maps every mirrored file to its original URL and lists URLs that
were already dead (404) on the live site when copied. Those dead links are real and intentionally left in.

## Versions

Every site repo follows the same rules:

- Tag `baseline-v1`: the untouched copy. The shared starting point for every test.
- `main`: what GitHub Pages serves, i.e. the **currently active scenario**. Pages publishes one branch
  only, so a site shows one scenario at a time.
- `test/<case>` branches: prepare one test case, open a pull request, and merge it to `main` to activate it.
  Tag the merge `case/<case>` so the scenario can be returned to later.
- To reset: `git checkout baseline-v1 -- .` then commit (or reset `main` to the tag).

`.gitattributes` sets `-text`, so git never changes file bytes. Content hashes are identical on every
machine and OS. Don't override this.

## Workflow for a new test case (example: easy site)

```bash
git clone https://github.com/javedibrahim200/test-site-easy-bcm.git
cd test-site-easy-bcm
git checkout -b test/deadline-moved
# edit files: a date, swap a PDF, change a paragraph ...
git add -A && git commit -m "bcm: move application deadline to 2026-12-01"
git push -u origin test/deadline-moved   # open a PR; merge to main to activate
```

The answer key for a case is the diff against the baseline. It is exactly what the update flow
should report:

```bash
git diff baseline-v1..test/deadline-moved
```

Put the expected result (field, old value, new value) in the pull request description.

## Viewing a site locally

```bash
cd test-site-easy-bcm
py -m http.server 8000      # or: python3 -m http.server 8000
# open http://localhost:8000/
```

## Enabling GitHub Pages (once per site repo)

Repo Settings, then Pages, Source: *Deploy from a branch*, Branch: `main`, folder `/ (root)`.
The `.nojekyll` file in each repo is required: without it Pages drops folders starting with `_`
(for example `_ext`, which holds third-party assets).

## Things to know

- **The site repos are public** (free GitHub only serves Pages from public repos), and the published
  URLs are public. These are copies of third-party sites for internal testing only. Project Pages
  can't set `X-Robots-Tag` and the `robots.txt` isn't at the host root, so search engines may index them.
  If that matters, add a `noindex` meta tag to the pages (it changes the copied HTML, so decide as a team).
- Calendar archive pages (per-day and per-month event views) were skipped on purpose: they are endless.
  Individual event pages are included.
- Pages deploys can take a minute or two after a push.

## Tools (`tools/`)

- `mirror.py <start_url> <out_dir>` re-crawls a site. `SITEMAP=1` seeds from the sitemap; `SUPPLEMENT=1`
  fetches only what an existing mirror is missing; `WORKERS=n` sets parallel downloads (use 2-3 for
  sites that rate-limit).
- `check_sitemap.py <site_url> <mirror_dir>` lists sitemap pages missing from a mirror.
