import os
import re
import time
import datetime
import subprocess
import requests
import sys
from xml.etree import ElementTree
from urllib.parse import urlparse

sys.stdout.reconfigure(line_buffering=True)
print("Step 5: Scrape OpenWrt wiki (incremental, last 2 years)")

OUT_DIR = "openwrt-wiki-docs"
DELAY   = 1.5   
CUTOFF  = datetime.datetime.utcnow() - datetime.timedelta(days=730)

INCLUDE_PREFIXES = [
    "/docs/techref/",
    "/docs/guide-developer/",
]

SKIP_PATTERNS = [
    "/toh/",
    "/inbox/",
    "/meta/",
    "/playground/",
    "changelog",
    "release_notes",
]

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (openwrt-llm-docs-bot/1.0; https://github.com)"
})

def get_existing_lastmod(fname):
    fpath = os.path.join(OUT_DIR, fname)
    if not os.path.isfile(fpath):
        return None
    try:
        with open(fpath, encoding="utf-8") as fh:
            for line in fh:
                m = re.search(r'\*\*Last modified:\*\*\s*(\d{4}-\d{2}-\d{2})', line)
                if m:
                    return datetime.datetime.strptime(m.group(1), "%Y-%m-%d")
                if line.startswith("---"):
                    break
    except Exception:
        pass
    return None

def get_existing_title(fname):
    fpath = os.path.join(OUT_DIR, fname)
    try:
        with open(fpath, encoding="utf-8") as fh:
            first = fh.readline().strip()
            if first.startswith("# "):
                return first[2:]
    except Exception:
        pass
    return fname

print("Fetching https://openwrt.org/sitemap.xml ...")
try:
    resp = session.get("https://openwrt.org/sitemap.xml", timeout=30)
    resp.raise_for_status()
except Exception as e:
    print(f"WARNING: Could not fetch sitemap: {e}")
    print("Skipping wiki documentation generation.")
    sys.exit(0)

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
try:
    sitemap_root = ElementTree.fromstring(resp.content)
except Exception as e:
    print(f"WARNING: Could not parse sitemap XML: {e}")
    print("Skipping wiki documentation generation.")
    sys.exit(0)

candidates = []
total_in_sitemap = 0

for url_el in sitemap_root.findall("sm:url", NS):
    total_in_sitemap += 1
    loc_el = url_el.find("sm:loc",     NS)
    mod_el = url_el.find("sm:lastmod", NS)
    if loc_el is None:
        continue

    url  = loc_el.text.strip()
    path = urlparse(url).path

    if not any(path.startswith(p) for p in INCLUDE_PREFIXES):
        continue
    if any(pat in path for pat in SKIP_PATTERNS):
        continue

    last_mod = None
    if mod_el is not None and mod_el.text:
        try:
            last_mod = datetime.datetime.strptime(mod_el.text.strip()[:10], "%Y-%m-%d")
        except ValueError:
            pass

    if last_mod is not None and last_mod < CUTOFF:
        continue

    candidates.append((url, path, last_mod))

print(f"Sitemap: {total_in_sitemap} total pages")
print(f"After scope/age filter: {len(candidates)} candidates")

def path_to_filename(url_path):
    parts = url_path.strip("/").split("/")
    if parts and parts[0] == "docs":
        parts = parts[1:]
    if parts and parts[-1] == "start":
        parts = parts[:-1]
    slug = "-".join(p for p in parts if p)
    slug = re.sub(r"[^a-z0-9-]", "-", slug.lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return f"openwrt-{slug}.md" if slug else "openwrt-misc.md"

toc_entries = []
saved = 0
skipped_unchanged = 0
failed = 0

for url, path, last_mod in candidates:
    fname = path_to_filename(path)
    existing_mod = get_existing_lastmod(fname)
    if existing_mod and last_mod and existing_mod >= last_mod:
        title = get_existing_title(fname)
        toc_entries.append((fname, title, url, last_mod.strftime("%Y-%m-%d")))
        skipped_unchanged += 1
        continue

    time.sleep(DELAY)
    raw_url = url + "?do=export_raw"
    try:
        r = session.get(raw_url, timeout=20)
        r.raise_for_status()
        raw_content = r.text
    except Exception as e:
        print(f"  FAIL ({e}): {path}")
        failed += 1
        continue

    if not raw_content.strip():
        continue

    try:
        result = subprocess.run(
            ["pandoc", "-f", "dokuwiki", "-t", "gfm", "--wrap=none"],
            input=raw_content, capture_output=True, text=True, timeout=30
        )
        md = result.stdout
    except Exception as e:
        print(f"  PANDOC FAIL ({e}): {path}")
        failed += 1
        continue

    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    if len(md) < 200:
        continue

    date_str  = last_mod.strftime("%Y-%m-%d") if last_mod else "unknown"
    fetch_ts  = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    title_m   = re.search(r"^#+ (.+)$", md, re.MULTILINE)
    title     = title_m.group(1).strip() if title_m else path.split("/")[-1]

    with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"> **Source:** {url}\n")
        f.write(f"> **Last modified:** {date_str}\n")
        f.write(f"> **Fetched:** {fetch_ts}\n\n")
        f.write("---\n\n")
        f.write(re.sub(r"^#+ .+\n\n?", "", md, count=1))

    toc_entries.append((fname, title, url, date_str))
    saved += 1
    print(f"  OK [{date_str}] {fname} — {title[:55]}")

ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
with open(os.path.join(OUT_DIR, "llms.txt"), "w", encoding="utf-8") as f:
    f.write("# OpenWrt Wiki Developer Documentation Index\n")
    f.write("# Source: https://openwrt.org/docs/\n")
    f.write(f"# Generated: {ts}\n")
    f.write("# Scope: /docs/techref/ + /docs/guide-developer/ — last 2 years\n")
    f.write("# Incremental: unchanged pages are preserved from previous run.\n")
    f.write("#\n## Files in this directory\n\n")
    for fname, title, url, date in sorted(toc_entries):
        f.write(f"- [{fname}](/openwrt-wiki-docs/{fname}): {title} (modified: {date}) — {url}\n")

print(f"\nStep 5 complete: {saved} fetched, {skipped_unchanged} unchanged/cached, {failed} failed.")
