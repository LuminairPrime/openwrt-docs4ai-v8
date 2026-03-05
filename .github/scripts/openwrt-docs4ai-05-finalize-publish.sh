#!/bin/bash
set -euo pipefail
set -x
trap 'echo "ERROR in $0 at line $LINENO: $BASH_COMMAND" >&2' ERR

TS=$(date -u +"%Y-%m-%d %H:%M UTC")

echo "Step 11a: Assemble ucode complete reference"
{
  echo "# ucode Complete API Reference"
  echo ""
  echo "> **Source:** https://github.com/jow-/ucode (commit: \`${UCODE_COMMIT:-unknown}\`)"
  echo "> **Live docs:** https://ucode.mein.io/"
  echo "> **Generated:** $TS"
  echo "> **Standalone use:** This file is self-contained. TOC links use"
  echo "> in-page anchors. Cross-reference links point to the modular"
  echo "> ucode-docs/ files; the linked content is also embedded in this file."
  echo ""
  echo "ucode is a tiny ECMAScript-like scripting language for OpenWrt system"
  echo "scripting. Provides bindings for ubus, uci, uloop, netlink, and other"
  echo "OpenWrt APIs. Synchronous, procedural, no OOP standard library."
  echo ""
  echo "---"
  echo ""
  echo "## Table of Contents"
  echo ""
  for f in ucode-docs/ucode-tutorial-*.md; do
    [ -f "$f" ] || continue
    title=$(grep -m1 "^#" "$f" | sed 's/^#* *//')
    bname=$(basename "$f" .md)
    echo "- [$title](#$bname)"
  done
  for f in ucode-docs/ucode-module-*.md; do
    [ -f "$f" ] || continue
    title=$(grep -m1 "^#" "$f" | sed 's/^#* *//')
    bname=$(basename "$f" .md)
    echo "- [$title](#$bname)"
  done
  echo ""
  echo "---"
  echo ""
  for f in ucode-docs/ucode-tutorial-*.md ucode-docs/ucode-module-*.md; do
    [ -f "$f" ] || continue
    bname=$(basename "$f" .md)
    echo "<a id=\"$bname\"></a>"
    cat "$f"
    printf "\n\n---\n\n"
  done
} > ucode-complete-reference.md
echo "ucode-complete-reference.md: $(wc -l < ucode-complete-reference.md) lines"

echo "Step 11b: Assemble LuCI JS API complete reference"
{
  echo "# LuCI JS API Complete Reference"
  echo ""
  echo "> **Source:** https://github.com/openwrt/luci (commit: \`${LUCI_COMMIT:-unknown}\`)"
  echo "> **Live docs:** https://openwrt.github.io/luci/jsapi/"
  echo "> **Generated:** $TS"
  echo "> **Standalone use:** This file is self-contained. All API classes"
  echo "> are embedded below. TOC links use in-page anchors."
  echo ""
  echo "LuCI is the OpenWrt web configuration interface. This document covers"
  echo "its complete client-side JavaScript API."
  echo ""
  echo "---"
  echo ""
  echo "## Table of Contents"
  echo ""
  for f in luci-docs/luci-api-*.md; do
    [ -f "$f" ] || continue
    title=$(grep -m1 "^#" "$f" | sed 's/^#* *//')
    bname=$(basename "$f" .md)
    echo "- [$title](#$bname)"
  done
  echo ""
  echo "---"
  echo ""
  for f in luci-docs/luci-api-*.md; do
    [ -f "$f" ] || continue
    bname=$(basename "$f" .md)
    echo "<a id=\"$bname\"></a>"
    cat "$f"
    printf "\n\n---\n\n"
  done
} > luci-jsapi-complete-reference.md
echo "luci-jsapi-complete-reference.md: $(wc -l < luci-jsapi-complete-reference.md) lines"

if [ "${SKIP_WIKI:-false}" != "true" ]; then
  echo "Step 11c: Assemble wiki complete reference"
  {
    echo "# OpenWrt Developer Documentation — Wiki Reference"
    echo ""
    echo "> **Source:** https://openwrt.org/docs/"
    echo "> **Scope:** /docs/techref/ and /docs/guide-developer/ — pages modified within the last 2 years"
    echo "> **Generated:** $TS"
    echo "> **Standalone use:** This file is self-contained. All wiki pages are"
    echo "> embedded below with their original metadata headers."
    echo ""
    echo "---"
    echo ""
    echo "## Table of Contents"
    echo ""
    for f in openwrt-wiki-docs/*.md; do
      [ -f "$f" ] || continue
      title=$(grep -m1 "^#" "$f" | sed 's/^#* *//')
      bname=$(basename "$f" .md)
      echo "- [$title](#$bname)"
    done
    echo ""
    echo "---"
    echo ""
    for f in openwrt-wiki-docs/*.md; do
      [ -f "$f" ] || continue
      bname=$(basename "$f" .md)
      echo "<a id=\"$bname\"></a>"
      cat "$f"
      printf "\n\n---\n\n"
    done
  } > openwrt-wiki-complete-reference.md
  echo "openwrt-wiki-complete-reference.md: $(wc -l < openwrt-wiki-complete-reference.md) lines"
else
  echo "Skipped wiki complete reference (SKIP_WIKI=true)"
fi

if [ "${SKIP_BUILDROOT:-false}" != "true" ]; then
  echo "Step 11d: Assemble buildroot complete reference"
  {
    echo "# OpenWrt Buildroot Complete Reference"
    echo ""
    echo "> **Source:** https://github.com/openwrt/openwrt (commit: \`${OPENWRT_COMMIT:-unknown}\`)"
    echo "> **Generated:** $TS"
    echo "> **Standalone use:** This file is self-contained. All package category"
    echo "> documentation and build system include files are embedded below."
    echo ""
    echo "Package metadata, descriptions, and README content extracted from the OpenWrt buildroot."
    echo ""
    echo "---"
    echo ""
    echo "## Table of Contents"
    echo ""
    for f in openwrt-buildroot-docs/*.md; do
      [ -f "$f" ] || continue
      title=$(grep -m1 "^#" "$f" | sed 's/^#* *//')
      bname=$(basename "$f" .md)
      echo "- [$title](#$bname)"
    done
    echo ""
    echo "---"
    echo ""
    for f in openwrt-buildroot-docs/*.md; do
      [ -f "$f" ] || continue
      bname=$(basename "$f" .md)
      echo "<a id=\"$bname\"></a>"
      cat "$f"
      printf "\n\n---\n\n"
    done
  } > openwrt-buildroot-complete-reference.md
  echo "openwrt-buildroot-complete-reference.md: $(wc -l < openwrt-buildroot-complete-reference.md) lines"
else
  echo "Skipped buildroot complete reference (SKIP_BUILDROOT=true)"
fi

echo "Step 11e: Assemble examples complete reference"
LUCI_APPS_URL="https://github.com/openwrt/luci/tree/master/applications"
{
  echo "# OpenWrt LuCI Application Examples — Complete Reference"
  echo ""
  echo "> **Source:** $LUCI_APPS_URL"
  echo "> **LuCI commit:** \`${LUCI_COMMIT:-unknown}\`"
  echo "> **Generated:** $TS"
  echo "> **Standalone use:** This file is self-contained. All four curated apps"
  echo "> are embedded below with full source code — no other files needed."
  echo ""
  echo "Four curated full-stack LuCI applications demonstrating modern OpenWrt"
  echo "development patterns. All source files are raw, unmodified upstream code."
  echo ""
  echo "---"
  echo ""
  echo "## Table of Contents"
  echo ""
  echo "- [luci-app-example](#luci-app-example) — Hello world / baseline"
  echo "- [luci-app-commands](#luci-app-commands) — HTTP API / controller"
  echo "- [luci-app-ddns](#luci-app-ddns) — Standard configuration app"
  echo "- [luci-app-dockerman](#luci-app-dockerman) — Advanced / streaming"
  echo ""
  echo "---"
  echo ""

  for app in luci-app-example luci-app-commands luci-app-ddns luci-app-dockerman; do
    [ -d "openwrt-examples/$app" ] || continue

    echo "## $app"
    echo ""
    echo "> Source: $LUCI_APPS_URL/$app"
    echo ""

    while IFS= read -r -d '' f; do
      relpath="${f#openwrt-examples/}"
      ext="${f##*.}"
      if [ "$ext" = "uc" ]; then
        lang=""
        ftype="ucode backend"
      else
        lang="javascript"
        ftype="JavaScript frontend"
      fi
      echo "### \`$relpath\` ($ftype)"
      echo ""
      printf '```%s\n' "$lang"
      cat "$f"
      echo ""
      printf '```\n'
      echo ""
    done < <(find "openwrt-examples/$app" -type f \( -name "*.uc" -o -name "*.js" \) -print0 | sort -z)

    printf "\n---\n\n"
  done
} > openwrt-examples-complete-reference.md
echo "openwrt-examples-complete-reference.md: $(wc -l < openwrt-examples-complete-reference.md) lines"

echo "Step 11f: Promote static-docs/ to repository root"
if [ -d "static-docs" ] && [ "$(ls -A static-docs/*.md 2>/dev/null)" ]; then
  echo "Promoting static-docs/ to root..."
  for f in static-docs/*.md; do
    [ -f "$f" ] || continue
    cp "$f" "./$(basename "$f")"
    echo "  Promoted: $(basename "$f")"
  done
else
  echo "Note: static-docs/ is empty or absent."
fi

echo "Step 12a: Generate CHANGES.md (diff vs. previous run)"
python3 << 'PYEOF'
import os
import subprocess
import datetime
import sys

sys.stdout.reconfigure(line_buffering=True)
TS = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

DIFF_TARGETS = [
    "ucode-docs/llms.txt",
    "luci-docs/llms.txt",
    "openwrt-wiki-docs/llms.txt",
    "openwrt-buildroot-docs/llms.txt",
    "openwrt-examples/llms.txt",
    "llms.txt",
]

sections = []

for target in DIFF_TARGETS:
    if not os.path.isfile(target):
        continue
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD", "--", target],
            capture_output=True, text=True, timeout=10
        )
        diff_output = result.stdout.strip()
        if diff_output:
            sections.append(f"## Changes in `{target}`\n\n```diff\n{diff_output}\n```\n")
    except Exception as e:
        sections.append(f"## Changes in `{target}`\n\n*(diff unavailable: {e})*\n")

with open("CHANGES.md", "w", encoding="utf-8") as f:
    f.write(f"# Documentation Changes — {TS}\n\n")
    if sections:
        f.write("> Summary of changes detected in this run compared to the\n")
        f.write("> previous committed version. Shows added, removed, and\n")
        f.write("> modified entries in each documentation index.\n\n")
        f.write("---\n\n")
        for section in sections:
            f.write(section + "\n")
    else:
        f.write("> No changes detected — all outputs are identical to the\n")
        f.write("> previous run.\n")

print(f"Step 12a complete: CHANGES.md written ({len(sections)} sections with diffs).")
PYEOF

echo "Step 12b: Generate Root llms.txt"
{
  echo "# OpenWrt Developer Documentation for AI LLMs"
  echo ""
  echo "> **Source:** https://github.com/openwrt/openwrt"
  echo "> **Source:** https://github.com/openwrt/luci"
  echo "> **Source:** https://github.com/jow-/ucode"
  echo "> **Source:** https://openwrt.org/"
  echo "> **Generated:** $TS"
  echo ""
  echo "This repository provides modular, LLM-optimized OpenWrt developer documentation."
  echo "Use these reference files to establish technical context before generating code."
  echo ""
  echo "---"
  echo ""
  echo "## Complete Topic References (Concatenated)"
  echo "For deep dives, provide the relevant complete reference file to the LLM."
  echo "These files span thousands of lines and contain all related modules."
  echo ""
  echo "- [ucode-complete-reference.md](ucode-complete-reference.md): Full ucode language and API docs."
  echo "- [luci-jsapi-complete-reference.md](luci-jsapi-complete-reference.md): Full LuCI client-side JavaScript API."
  echo "- [openwrt-wiki-complete-reference.md](openwrt-wiki-complete-reference.md): Consolidated developer wiki."
  echo "- [openwrt-buildroot-complete-reference.md](openwrt-buildroot-complete-reference.md): Package descriptions and makefile references."
  echo "- [openwrt-examples-complete-reference.md](openwrt-examples-complete-reference.md): Curated LuCI app examples built with modern standards."
  echo ""
  echo "---"
  echo ""
  echo "## Modular Indices"
  echo "For targeted lookups, read the index below to find modular sub-files."
  echo "Modular files are located in folders (e.g., \`ucode-docs/ucode-module-fs.md\`)."
  echo ""
  echo "### ucode Language and Modules"
  [ -f ucode-docs/llms.txt ] && awk '/^[^#]/' ucode-docs/llms.txt || true
  echo ""
  echo "### LuCI JavaScript API"
  [ -f luci-docs/llms.txt ] && awk '/^[^#]/' luci-docs/llms.txt || true
  echo ""
  echo "### OpenWrt Buildroot Packages"
  [ -f openwrt-buildroot-docs/llms.txt ] && awk '/^[^#]/' openwrt-buildroot-docs/llms.txt || true
  echo ""
  echo "### Curated LuCI Examples"
  [ -f openwrt-examples/llms.txt ] && awk '/^[^#]/' openwrt-examples/llms.txt || true
  echo ""
  echo "### OpenWrt Developer Wiki"
  [ -f openwrt-wiki-docs/llms.txt ] && awk '/^[^#]/' openwrt-wiki-docs/llms.txt || true
} > llms.txt

echo "llms.txt: $(wc -l < llms.txt) lines"

echo "Step 13: Validate output (check for silent failures)"
WARN=0

check_file() {
  local file="$1"
  local min_lines="$2"
  local desc="$3"
  if [ -f "$file" ]; then
    lines=$(wc -l < "$file")
    if [ "$lines" -lt "$min_lines" ]; then
      echo "⚠️  WARNING: $file has only $lines lines (expected >= $min_lines)"
      WARN=$((WARN + 1))
    else
      printf "  ✓ %-55s %6s lines\n" "$file" "$lines"
    fi
  else
    echo "⚠️  WARNING: $file is MISSING — $desc"
    WARN=$((WARN + 1))
  fi
}

check_dir() {
  local dir="$1"
  local min_files="$2"
  local desc="$3"
  if [ -d "$dir" ]; then
    # Use find to avoid ls exit code 2 if nothing matches
    count=$(find "$dir" -maxdepth 1 -name "*.md" | wc -l)
    if [ "$count" -lt "$min_files" ]; then
      echo "⚠️  WARNING: $dir/ has only $count .md files (expected >= $min_files)"
      WARN=$((WARN + 1))
    else
      printf "  ✓ %-55s %3s .md files\n" "$dir/" "$count"
    fi
  else
    echo "⚠️  WARNING: $dir/ is MISSING — $desc"
    WARN=$((WARN + 1))
  fi
}

check_file "ucode-complete-reference.md"    200 "ucode documentation generation"
check_file "luci-jsapi-complete-reference.md" 200 "LuCI JS API documentation generation"
check_dir "ucode-docs"   3 "ucode module/tutorial generation"
check_dir "luci-docs"    3 "LuCI JS API generation"

if [ "${SKIP_WIKI:-false}" != "true" ]; then
  check_file "openwrt-wiki-complete-reference.md" 100 "wiki scraping"
  check_dir "openwrt-wiki-docs" 2 "wiki page conversion"
fi
if [ "${SKIP_BUILDROOT:-false}" != "true" ]; then
  check_file "openwrt-buildroot-complete-reference.md" 50 "buildroot extraction"
  check_dir "openwrt-buildroot-docs" 2 "buildroot package extraction"
fi

check_file "openwrt-examples-complete-reference.md" 50 "examples extraction"
check_file "llms.txt" 10 "root llms.txt generation"

if [ "$WARN" -gt 0 ]; then
  echo "⚠️  $WARN validation warning(s) detected. Review the output above."
else
  echo "✓ All validation checks passed."
fi

echo "Step 14 & 15: Clean artifacts and commit to repository"
rm -rf repo-ucode repo-luci repo-openwrt node_modules .venv || true
rm -f jsdoc-ucode.err jsdoc-luci.err jsdoc.err || true

if [ -d .git ]; then
  git config --local user.name "github-actions[bot]" || true
  git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com" || true
  git add --all . || true
  git commit -m "docs: auto-update LLM-optimized documentation" || echo "No changes to commit"
  git push || echo "WARNING: Failed to push to repository (transient error or concurrent update). Continuing workflow."
else
  echo "Not a git repository or no .git folder exist. Skipping commit."
fi
