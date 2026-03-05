#!/bin/bash
set -euo pipefail
set -x
trap 'echo "ERROR in $0 at line $LINENO: $BASH_COMMAND" >&2' ERR

if [ "${SKIP_BUILDROOT:-false}" == "true" ]; then
  echo "Skipping package metadata extraction (SKIP_BUILDROOT=true)"
  exit 0
fi

echo "Step 2d: Extract OpenWrt core package documentation"
python3 << 'PYEOF'
import os
import re
import glob
import datetime
import sys

# Flush output immediately
sys.stdout.reconfigure(line_buffering=True)

REPO     = "repo-openwrt"
OUT_DIR  = "openwrt-buildroot-docs"
os.makedirs(OUT_DIR, exist_ok=True)
TS       = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
COMMIT   = os.environ.get("OPENWRT_COMMIT", "unknown")
REPO_URL = "https://github.com/openwrt/openwrt"

if not os.path.isdir(REPO):
    print("Buildroot repo not found (step skipped or clone failed).")
    sys.exit(0)

def extract_makefile_meta(path):
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return {}
    fields = {}
    for key in ["PKG_NAME", "PKG_VERSION", "PKG_SOURCE_URL",
                "PKG_MAINTAINER", "PKG_LICENSE"]:
        m = re.search(
            rf'^{key}\s*[?:+]?=\s*(.+?)(?=\n[A-Z_]|\Z)',
            text, re.MULTILINE | re.DOTALL
        )
        if m:
            val = re.sub(r"\s+", " ", m.group(1).replace("\\\n", " ")).strip()
            if val and not val.startswith("$("):
                fields[key] = val[:200]

    m = re.search(
        r'^PKG_DESCRIPTION\s*[?:+]?=\s*(.+?)(?=\n[A-Z]|\Z)',
        text, re.MULTILINE | re.DOTALL
    )
    if m:
        fields["DESCRIPTION"] = re.sub(
            r"\s+", " ", m.group(1).replace("\\\n", " ")
        ).strip()[:500]

    block_m = re.search(
        r'define Package/[^\n]+\n(.*?)^endef',
        text, re.MULTILINE | re.DOTALL
    )
    if block_m:
        block = block_m.group(1)
        d = re.search(
            r'DESCRIPTION\s*:?=\s*(.+?)(?=\n\s*[A-Z]|\Z)', block, re.DOTALL
        )
        if d:
            desc = re.sub(r"\s+", " ", d.group(1).replace("\\\n", " ")).strip()
            if desc:
                fields.setdefault("DESCRIPTION", desc[:500])
    return fields

def extract_readme(pkg_dir):
    for name in ["README.md", "README", "README.txt"]:
        p = os.path.join(pkg_dir, name)
        if os.path.isfile(p):
            try:
                content = open(p, encoding="utf-8", errors="replace").read().strip()
                if len(content) > 50:
                    return content
            except Exception:
                pass
    return None

toc_lines  = []
total_pkgs = 0

for cat_path in sorted(glob.glob(f"{REPO}/package/*")):
    if not os.path.isdir(cat_path):
        continue
    category = os.path.basename(cat_path)
    entries  = []

    for pkg_path in sorted(glob.glob(f"{cat_path}/*")):
        if not os.path.isdir(pkg_path):
            continue
        pkg_name = os.path.basename(pkg_path)
        meta     = extract_makefile_meta(os.path.join(pkg_path, "Makefile"))
        readme   = extract_readme(pkg_path)
        if not meta and not readme:
            continue
        entries.append({"name": pkg_name, "meta": meta, "readme": readme})

    if not entries:
        continue

    total_pkgs += len(entries)
    cat_src_url = f"{REPO_URL}/tree/master/package/{category}"
    outfile     = os.path.join(OUT_DIR, f"openwrt-buildroot-{category}.md")

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(f"# OpenWrt Buildroot: `{category}` packages\n\n")
        f.write(f"> **Source:** {cat_src_url}\n")
        f.write(f"> **Generated:** {TS} from commit `{COMMIT}`\n\n---\n\n")

        for e in entries:
            m = e["meta"]
            f.write(f"## `{e['name']}`\n\n")
            if m.get("DESCRIPTION"):
                f.write(f"{m['DESCRIPTION']}\n\n")
            rows = []
            if m.get("PKG_VERSION"):    rows.append(f"| Version | {m['PKG_VERSION']} |")
            if m.get("PKG_LICENSE"):    rows.append(f"| License | {m['PKG_LICENSE']} |")
            if m.get("PKG_MAINTAINER"): rows.append(f"| Maintainer | {m['PKG_MAINTAINER']} |")
            if m.get("PKG_SOURCE_URL"): rows.append(f"| Source URL | {m['PKG_SOURCE_URL'][:120]} |")
            if rows:
                f.write("| Field | Value |\n|---|---|\n" + "\n".join(rows) + "\n\n")
            if e["readme"]:
                content   = e["readme"]
                truncated = len(content) > 2000
                f.write("**README:**\n\n")
                f.write(content[:2000])
                if truncated:
                    pkg_url = f"{REPO_URL}/tree/master/package/{category}/{e['name']}"
                    f.write(f"\n\n> *(README truncated — [view full file]({pkg_url}))*")
                f.write("\n\n")
            pkg_url = f"{REPO_URL}/tree/master/package/{category}/{e['name']}"
            f.write(f"> Source: {pkg_url}\n\n---\n\n")

    toc_lines.append(
        f"- [openwrt-buildroot-{category}.md]"
        f"(/openwrt-buildroot-docs/openwrt-buildroot-{category}.md): "
        f"OpenWrt buildroot `{category}` — {len(entries)} packages"
    )
    print(f"  {category}: {len(entries)} packages")

mk_entries = []
for mk_file in sorted(glob.glob(f"{REPO}/include/*.mk")):
    try:
        text = open(mk_file, encoding="utf-8", errors="replace").read()
    except Exception:
        continue
    fname_mk = os.path.basename(mk_file)
    comments = []
    for line in text.splitlines()[:100]:
        if line.startswith("#"):
            cleaned = line.lstrip("# ").strip()
            if cleaned:
                comments.append(cleaned)
        elif comments:
            break
    if len(comments) >= 2:
        mk_entries.append((fname_mk, "\n".join(comments)))

if mk_entries:
    outfile = os.path.join(OUT_DIR, "openwrt-buildroot-include-mk.md")
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("# OpenWrt Buildroot: Build System Include Files\n\n")
        f.write(f"> **Source:** {REPO_URL}/tree/master/include\n")
        f.write(f"> **Generated:** {TS} from commit `{COMMIT}`\n\n")
        f.write("Core build system Makefile fragments.\n\n---\n\n")
        for fname_mk, doc in mk_entries:
            f.write(f"## `{fname_mk}`\n\n```\n{doc}\n```\n\n")
            f.write(f"> Source: {REPO_URL}/blob/master/include/{fname_mk}\n\n---\n\n")
    toc_lines.append(
        f"- [openwrt-buildroot-include-mk.md]"
        f"(/openwrt-buildroot-docs/openwrt-buildroot-include-mk.md): "
        f"Build system .mk files — {len(mk_entries)} documented"
    )

with open(os.path.join(OUT_DIR, "llms.txt"), "w", encoding="utf-8") as f:
    f.write("# OpenWrt Buildroot Documentation Index\n")
    f.write(f"# Source: {REPO_URL} (commit: {COMMIT})\n")
    f.write(f"# Generated: {TS}\n#\n")
    f.write("# Package metadata and README files from the OpenWrt buildroot.\n#\n")
    f.write("## Files in this directory\n\n")
    for line in toc_lines:
        f.write(line + "\n")

print(f"\nStep 2d complete: {total_pkgs} packages across {len(toc_lines)} outputs.")
PYEOF
