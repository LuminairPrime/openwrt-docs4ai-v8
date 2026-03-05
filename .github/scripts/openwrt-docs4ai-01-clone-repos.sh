#!/bin/bash
set -euo pipefail
set -x
trap 'echo "ERROR in $0 at line $LINENO: $BASH_COMMAND" >&2' ERR

echo "Step 0: Setup and Cleanup"
for d in ucode-docs luci-docs openwrt-wiki-docs openwrt-buildroot-docs openwrt-examples; do
    mkdir -p "$d"
    rm -f "$d"/*.md "$d"/llms.txt
done
rm -f ucode-complete-reference.md luci-jsapi-complete-reference.md
rm -f openwrt-wiki-complete-reference.md openwrt-buildroot-complete-reference.md
rm -f openwrt-examples-complete-reference.md llms.txt CHANGES.md

echo "Step 2: Clone upstream repositories"

git clone --depth=1 https://github.com/jow-/ucode.git repo-ucode \
  || { echo "ERROR: Failed to clone ucode repo"; exit 1; }
UCODE_COMMIT=$(git -C repo-ucode rev-parse --short HEAD)
echo "UCODE_COMMIT=$UCODE_COMMIT" >> "${GITHUB_ENV:-/dev/null}"
echo "Cloned ucode @ $UCODE_COMMIT"

git clone --depth=1 https://github.com/openwrt/luci.git repo-luci \
  || { echo "ERROR: Failed to clone luci repo"; exit 1; }
LUCI_COMMIT=$(git -C repo-luci rev-parse --short HEAD)
echo "LUCI_COMMIT=$LUCI_COMMIT" >> "${GITHUB_ENV:-/dev/null}"
echo "Cloned luci @ $LUCI_COMMIT"

if [ "${SKIP_BUILDROOT:-false}" != "true" ]; then
  git clone --depth=1 --filter=blob:none --sparse \
    https://github.com/openwrt/openwrt.git repo-openwrt \
    || { echo "ERROR: Failed to clone openwrt repo"; exit 1; }

  cd repo-openwrt
  git sparse-checkout set \
    package/network package/kernel package/utils package/system \
    package/libs package/firmware package/boot package/multimedia \
    include scripts
  cd ..
  OPENWRT_COMMIT=$(git -C repo-openwrt rev-parse --short HEAD)
  echo "OPENWRT_COMMIT=$OPENWRT_COMMIT" >> "${GITHUB_ENV:-/dev/null}"
  echo "Cloned openwrt @ $OPENWRT_COMMIT (sparse)"
else
  echo "Skipping openwrt buildroot clone (SKIP_BUILDROOT=true)"
fi
