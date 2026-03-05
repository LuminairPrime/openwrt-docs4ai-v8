import os
import subprocess
import glob
import datetime
import sys
import re

# Flush output immediately
sys.stdout.reconfigure(line_buffering=True)

TS = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
IS_WINDOWS = os.name == "nt"

# LuCI processing
print("Step 2c: Generate LuCI JS API documentation (JSDoc)")
repo_luci = "repo-luci"
if not os.path.exists(repo_luci):
    print(f"Directory {repo_luci} not found, skipping.")
else:
    luci_commit = os.environ.get("LUCI_COMMIT", "unknown")
    out_dir = "luci-docs"
    os.makedirs(out_dir, exist_ok=True)
    repo_url = "https://github.com/openwrt/luci"
    live_base = "https://openwrt.github.io/luci/jsapi"
    
    with open(f"{out_dir}/llms.txt", "w", encoding="utf-8") as f:
        f.write(f"# LuCI JS API Documentation Index\n# Source: {repo_url} (commit: {luci_commit})\n")
        f.write(f"# Live docs: {live_base}/\n# Generated: {TS}\n#\n")
        f.write("# LuCI is the OpenWrt web configuration interface.\n")
        f.write("# This index covers its complete client-side JavaScript API.\n#\n")
        f.write("# Standalone use: each .md file in this folder is self-contained with full\n")
        f.write("# metadata headers. This llms.txt provides the navigational index.\n#\n## Files in this directory\n\n")
        
    print("Processing LuCI JS API source files (without upstream config)...")
    target_dir = f"{repo_luci}/modules/luci-base/htdocs/luci-static/resources"
    
    file_count = 0
    skip_count = 0
    
    luci_srcs = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".js"):
                luci_srcs.append(os.path.join(root, file))
        luci_srcs.sort()

    for src in luci_srcs:
        filename = os.path.basename(src)
        mod = os.path.splitext(filename)[0]
        relpath = os.path.relpath(src, repo_luci).replace("\\", "/")
        
        cmd = ["jsdoc2md", "--heading-depth", "2", "--global-index-format", "none", src]
        res = subprocess.run(cmd, capture_output=True, text=True, shell=IS_WINDOWS, encoding="utf-8")
        stdout = res.stdout or ""
        stderr = res.stderr or ""
        if stderr:
            with open("jsdoc-luci.err", "a", encoding="utf-8") as err_f:
                err_f.write(f"Stderr for {mod}:\n{stderr}\n")
                
        output = stdout.strip()
        word_count = len(output.split())
        
        if not output or word_count < 15:
            skip_count += 1
            continue
            
        live_url = f"{live_base}/LuCI.html" if mod == "luci" else f"{live_base}/LuCI.{mod}.html"
        outfile = f"{out_dir}/luci-api-{mod}.md"
        member_count = output.count("##")
        
        with open(outfile, "w", encoding="utf-8") as fw:
            fw.write(f"# LuCI API: `{mod}`\n\n")
            fw.write(f"> **Source:** [`{relpath}`]({repo_url}/blob/master/{relpath})\n")
            fw.write(f"> **Live docs:** {live_url}\n")
            fw.write(f"> **Generated:** {TS} from commit `{luci_commit}`\n\n---\n\n")
            fw.write(output)
            
        with open(f"{out_dir}/llms.txt", "a", encoding="utf-8") as f:
            f.write(f"- [luci-api-{mod}.md](/luci-docs/luci-api-{mod}.md): LuCI `{mod}` JS API — {member_count} documented members\n")
            
        file_count += 1

    if file_count == 0 and len(luci_srcs) > 0:
        print("WARNING: 0 LuCI files generated in single-file mode. Running whole-directory fallback.")
        cmd = ["jsdoc2md", "--heading-depth", "2", "--global-index-format", "none", f"{target_dir}/**/*.js"]
        res = subprocess.run(" ".join(cmd), shell=True, capture_output=True, text=True)
        output = res.stdout.strip()
        if output:
            with open(f"{out_dir}/luci-api-all.md", "w", encoding="utf-8") as fw:
                fw.write(f"# LuCI API: All\n\n{output}")
            with open(f"{out_dir}/llms.txt", "a", encoding="utf-8") as f:
                f.write(f"- [luci-api-all.md](/luci-docs/luci-api-all.md): LuCI complete API\n")

    if os.path.exists("jsdoc-luci.err"):
        print("\n=== jsdoc warnings/errors (LuCI) ===")
        with open("jsdoc-luci.err", "r", encoding="utf-8") as err_f:
            print(err_f.read())
        print("=== end jsdoc warnings ===")
        os.remove("jsdoc-luci.err")
        
    print(f"Step 2c complete: {file_count} files generated, {skip_count} skipped.")
