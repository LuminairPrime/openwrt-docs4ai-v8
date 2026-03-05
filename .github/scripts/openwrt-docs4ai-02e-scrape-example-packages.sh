#!/bin/bash
set -euo pipefail
set -x
trap 'echo "ERROR in $0 at line $LINENO: $BASH_COMMAND" >&2' ERR

if [ "${SKIP_BUILDROOT:-false}" == "true" ]; then
  echo "Skipping example extraction (SKIP_BUILDROOT=true)"
  exit 0
fi

echo "Step 2e: Extract curated LuCI application examples"
SRC="repo-luci/applications"
OUT="openwrt-examples"
mkdir -p "$OUT"
TS=$(date -u +"%Y-%m-%d %H:%M UTC")
LUCI_URL="https://github.com/openwrt/luci/tree/master/applications"
LUCI_COMMIT="${LUCI_COMMIT:-unknown}"

cat > "$OUT/llms.txt" << LLMS_EOF
# OpenWrt Curated LuCI Application Examples
# Source: $LUCI_URL
# Generated: $TS from LuCI commit $LUCI_COMMIT
#
# Four apps selected for distinct pedagogical value. Together they cover the
# full range of modern LuCI development patterns. All files are raw upstream
# source code — unmodified, suitable for direct use as coding templates.
#
# Standalone use: this llms.txt plus the app subdirectories are self-contained.
# The file tree below each app shows the structure before reading any source.
#
# Recommended reading order:
#   1. luci-app-example    — baseline structure and ucode<->JS bridge
#   2. luci-app-commands   — HTTP endpoints and controller pattern
#   3. luci-app-ddns       — config management and service state
#   4. luci-app-dockerman  — advanced sockets, streaming, multi-file
#
## Application Files

LLMS_EOF

for app in luci-app-example luci-app-commands luci-app-ddns luci-app-dockerman; do
  APP_DIR="$SRC/$app"

  if [ ! -d "$APP_DIR" ]; then
    echo "  WARNING: $app not found at $APP_DIR — skipping"
    printf "\n## %s\n# NOTE: Not found in upstream repo at generation time.\n\n" \
      "$app" >> "$OUT/llms.txt"
    continue
  fi

  echo "Extracting $app..."
  mkdir -p "$OUT/$app"

  cd "$SRC"
  find "$app" -type f \( -name "*.uc" -o -name "*.js" \) \
    -exec cp --parents {} "../../$OUT/" \;
  cd ../..

  uc_count=$(find "$OUT/$app" -name "*.uc" 2>/dev/null | wc -l)
  js_count=$(find "$OUT/$app" -name "*.js" 2>/dev/null | wc -l)

  case "$app" in
    luci-app-example)
      desc="Hello world / baseline — minimum viable app; ucode<->JS bridge, ACL, UCI form, rpcd scaffolding"
      ;;
    luci-app-commands)
      desc="HTTP API / controller — custom endpoints in ucode/controller/, URL parsing, secure popen execution"
      ;;
    luci-app-ddns)
      desc="Standard config app — service state (init_enabled), rpcd microbus, deep UCI read/write"
      ;;
    luci-app-dockerman)
      desc="Advanced / streaming — UNIX socket communication, HTTP streaming, large JSON, multi-file ucode"
      ;;
  esac

  {
    printf "\n## %s\n" "$app"
    printf "# Pattern: %s\n" "$desc"
    printf "# Source: %s/%s\n" "$LUCI_URL" "$app"
    printf "# Files: %s .uc (ucode backend), %s .js (JavaScript frontend)\n" \
      "$uc_count" "$js_count"
    printf "#\n"

    printf "# File tree:\n"
    find "$OUT/$app" -type f \( -name "*.uc" -o -name "*.js" \) | sort | \
    while read -r f; do
      rel="${f#$OUT/$app/}"
      ext="${f##*.}"
      [ "$ext" = "uc" ] && ftype="[ucode]" || ftype="[js]   "
      printf "#   %s  %s\n" "$ftype" "$rel"
    done
    printf "#\n"
  } >> "$OUT/llms.txt"

  while IFS= read -r -d '' f; do
    rel="${f#$OUT/}"
    ext="${f##*.}"
    [ "$ext" = "uc" ] && ftype="ucode backend" || ftype="JavaScript frontend"
    echo "- [$rel](/$rel): $app — $ftype" >> "$OUT/llms.txt"
  done < <(find "$OUT/$app" -type f \( -name "*.uc" -o -name "*.js" \) -print0 | sort -z)

  echo "" >> "$OUT/llms.txt"
  echo "  $app: $uc_count .uc, $js_count .js"
done

echo "Step 2e complete."
