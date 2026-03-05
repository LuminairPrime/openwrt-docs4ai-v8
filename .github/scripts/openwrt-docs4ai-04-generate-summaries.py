import os
import time
import glob
import requests
import sys

# Flush output immediately
sys.stdout.reconfigure(line_buffering=True)

print("Step 10: AI module summaries via GitHub Models (openai/gpt-4o-mini)")

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("LOCAL_DEV_TOKEN")
if not TOKEN:
    print("WARNING: No API token. Skipping AI summarization.")
    sys.exit(0)

ENDPOINT  = "https://models.github.ai/inference/chat/completions"
MODEL     = "openai/gpt-4o-mini"
MAX_FILES = 40
DELAY     = 1.5

SYSTEM_PROMPT = (
    "You are a technical documentation assistant. "
    "Given an API module reference, write a 2-3 sentence plain-English "
    "summary of what this module does and when a developer would use it. "
    "Be concrete and specific. "
    "Output ONLY the summary text — no headers, no bullets, no markdown. "
    "Maximum 60 words."
)

def summarize(content):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": content[:4000]},
        ],
        "max_tokens": 120,
        "temperature": 0.3,
    }
    try:
        r = requests.post(ENDPOINT, headers=headers, json=body, timeout=30)
        if r.status_code == 429:
            print("  HTTP 429 — rate limit reached. Stopping AI step.")
            return None
        r.raise_for_status()
        resp_json = r.json()
        choices = resp_json.get("choices") or []
        if not choices:
            print("  API returned empty choices — skipping this file")
            return "SKIP"
        message = choices[0].get("message", {})
        text    = message.get("content", "")
        return text.strip() if text.strip() else "SKIP"
    except Exception as e:
        print(f"  API error ({e}) — skipping this file")
        return "SKIP"

def inject_summary(fpath, summary):
    try:
        content = open(fpath, encoding="utf-8").read()
    except Exception:
        return
    if "**Summary:**" in content:
        return
    block = f"\n**Summary:** {summary}\n"
    pos = content.find("\n\n---\n\n")
    if pos != -1:
        content = content[:pos] + block + content[pos:]
    else:
        pos = content.find("\n\n")
        if pos != -1:
            content = content[:pos + 2] + block + content[pos + 2:]
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

ucode_files = sorted(glob.glob("ucode-docs/ucode-module-*.md"))
luci_files  = sorted(glob.glob("luci-docs/luci-api-*.md"))
queue       = ucode_files + luci_files

print(f"Queue: {len(ucode_files)} ucode + {len(luci_files)} luci = {len(queue)} total")
print(f"Hard cap: {MAX_FILES} files (free tier daily budget)")

processed = 0
skipped   = 0

for fpath in queue:
    if processed >= MAX_FILES:
        print(f"Reached {MAX_FILES}-file cap. Stopping.")
        break

    try:
        content = open(fpath, encoding="utf-8").read()
    except Exception:
        continue

    if "**Summary:**" in content:
        skipped += 1
        continue

    result = summarize(content)
    if result is None:
        break
    if result == "SKIP":
        continue

    inject_summary(fpath, result)
    processed += 1
    print(f"  [{processed}/{MAX_FILES}] {os.path.basename(fpath)}")
    time.sleep(DELAY)

print(f"\nStep 10 complete: {processed} summarized, {skipped} already done.")
