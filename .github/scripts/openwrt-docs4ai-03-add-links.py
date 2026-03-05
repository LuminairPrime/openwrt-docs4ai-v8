import os
import re
import glob

print("Step 8: Cross-reference injection (code-like symbols only)")

all_md = (
    sorted(glob.glob("ucode-docs/*.md")) +
    sorted(glob.glob("luci-docs/*.md")) +
    sorted(glob.glob("openwrt-wiki-docs/*.md")) +
    sorted(glob.glob("openwrt-buildroot-docs/*.md"))
)

print(f"Building symbol index from {len(all_md)} markdown files...")

COMMON_WORDS = {
    "name", "type", "value", "event", "data", "code", "info", "list",
    "item", "node", "text", "form", "page", "time", "date", "user",
    "host", "port", "path", "file", "mode", "status", "error", "result",
    "state", "flags", "index", "count", "length", "size", "version",
    "base", "init", "load", "open", "read", "write", "close", "send",
    "recv", "bind", "call", "stop", "start", "reset", "clear", "check",
    "parse", "fetch", "apply", "remove", "create", "update", "delete",
    "source", "target", "output", "input", "params", "options", "config",
    "return", "object", "string", "number", "boolean", "array", "table",
    "class", "method", "property", "function", "callback", "promise",
}

def is_code_symbol(name):
    if name.lower() in COMMON_WORDS:
        return False
    if len(name) < 5:
        return False
    if re.match(r'^[a-z][a-zA-Z0-9]+$', name) and any(c.isupper() for c in name):
        return True
    if "." in name and len(name) >= 6:
        return True
    if "_" in name and len(name) >= 7:
        return True
    if re.match(r'^[A-Z]{3,6}$', name):
        return True
    return False

symbol_index = {}

for fpath in all_md:
    root_url = "/" + fpath.replace(os.sep, "/")
    try:
        content = open(fpath, encoding="utf-8").read()
    except Exception:
        continue

    for m in re.finditer(
        r'^#{2,4}\s+[`"]?([A-Za-z][A-Za-z0-9_.]+(?:\(\))?)[`"]?',
        content, re.MULTILINE
    ):
        symbol = m.group(1).rstrip("()")
        if not is_code_symbol(symbol):
            continue

        if symbol not in symbol_index:
            symbol_index[symbol] = root_url
        else:
            current      = symbol_index[symbol]
            this_is_api  = "ucode-docs" in fpath or "luci-docs" in fpath
            curr_is_wiki = "wiki" in current or "buildroot" in current
            curr_is_api  = "ucode-docs" in current or "luci-docs" in current
            if this_is_api and curr_is_wiki:
                symbol_index[symbol] = root_url
            elif this_is_api and curr_is_api:
                print(
                    f"Warning: API symbol collision '{symbol}': "
                    f"{current} vs {root_url} (keeping first)"
                )

print(f"Symbol index: {len(symbol_index)} code-like symbols")

total_injected = 0
files_modified = 0

for fpath in all_md:
    this_root_url = "/" + fpath.replace(os.sep, "/")
    try:
        original = open(fpath, encoding="utf-8").read()
    except Exception:
        continue

    protected = set()
    for fence in re.finditer(r'```.*?```|~~~.*?~~~', original, re.DOTALL):
        protected.update(range(fence.start(), fence.end()))
    for code in re.finditer(r'`[^`\n]+`', original):
        protected.update(range(code.start(), code.end()))
    for link in re.finditer(r'\[[^\]]+\]\([^)]+\)', original):
        protected.update(range(link.start(), link.end()))

    spans = []

    def overlaps_existing(s, e):
        for es, ee, _ in spans:
            if not (e <= es or s >= ee):
                return True
        return False

    for symbol, target_url in sorted(symbol_index.items(), key=lambda x: -len(x[0])):
        if target_url == this_root_url:
            continue
        pat = re.compile(rf'\b{re.escape(symbol)}\b(?!\()')
        for m in pat.finditer(original):
            s, e = m.start(), m.end()
            if any(i in protected for i in range(s, e)):
                continue
            if overlaps_existing(s, e):
                continue
            spans.append((s, e, f"[{symbol}]({target_url})"))

    if not spans:
        continue

    spans.sort(key=lambda x: x[0])
    out  = []
    last = 0
    for s, e, rep in spans:
        out.append(original[last:s])
        out.append(rep)
        last = e
    out.append(original[last:])
    modified = "".join(out)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(modified)
    files_modified += 1
    total_injected += len(spans)

print(
    f"Step 8 complete: {total_injected} cross-references "
    f"injected across {files_modified} files."
)

print("\nStep 9: Deprecation checker")

deprecated = {}

for fpath in sorted(glob.glob("ucode-docs/*.md") + glob.glob("luci-docs/*.md")):
    root_url = "/" + fpath.replace(os.sep, "/")
    try:
        content = open(fpath, encoding="utf-8").read()
    except Exception:
        continue
    for m in re.finditer(
        r'^(#{2,4})\s+[`"]?([A-Za-z][A-Za-z0-9_.]+)[`"]?',
        content, re.MULTILINE
    ):
        symbol = m.group(2).rstrip("()")
        window = content[m.end():m.end() + 1500]
        if re.search(r'\*\*Deprecated\*\*', window, re.IGNORECASE):
            deprecated[symbol] = root_url
            print(f"  Deprecated: {symbol} (in {os.path.basename(fpath)})")

if not deprecated:
    print("No deprecated symbols found in API docs.")
else:
    print(f"Found {len(deprecated)} deprecated symbols.")

injected = 0
for fpath in sorted(glob.glob("openwrt-wiki-docs/*.md")):
    try:
        content = open(fpath, encoding="utf-8").read()
    except Exception:
        continue

    warnings = [
        (sym, url) for sym, url in deprecated.items()
        if re.search(rf'\b{re.escape(sym)}\b', content)
    ]
    if not warnings:
        continue

    callout = ["> [!WARNING]"]
    for sym, url in warnings:
        callout.append(
            f"> This page references `{sym}`, which is marked as "
            f"**deprecated** in the official API documentation. "
            f"See [{sym}]({url}) for the current approach."
        )
    callout_text = "\n".join(callout) + "\n\n"

    pos = content.find("\n\n---\n\n")
    if pos != -1:
        pos += len("\n\n---\n\n")
        content = content[:pos] + callout_text + content[pos:]
    else:
        pos = content.find("\n\n")
        if pos != -1:
            content = content[:pos + 2] + callout_text + content[pos + 2:]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    injected += 1
    print(f"  Warning injected: {os.path.basename(fpath)}")

print(f"Step 9 complete: {injected} wiki pages received deprecation warnings.")
