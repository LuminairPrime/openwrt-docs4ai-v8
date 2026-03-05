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

# ucode processing
print("Step 2b: Generate ucode documentation (JSDoc)")
repo_ucode = "repo-ucode"
if not os.path.exists(repo_ucode):
    print(f"Directory {repo_ucode} not found, skipping.")
else:
    ucode_commit = os.environ.get("UCODE_COMMIT", "unknown")
    subprocess.run(["npm", "install", "--silent"], cwd=repo_ucode, shell=IS_WINDOWS)
    
    ucode_conf = None
    for conf in ["jsdoc/conf.json", "jsdoc.conf.json", ".jsdoc.json", ".jsdoc.conf.json"]:
        if os.path.isfile(os.path.join(repo_ucode, conf)):
            ucode_conf = os.path.join(repo_ucode, conf)
            print(f"Found jsdoc config: {ucode_conf}")
            break
    
    out_dir = "ucode-docs"
    os.makedirs(out_dir, exist_ok=True)
    repo_url = "https://github.com/jow-/ucode"

    with open(f"{out_dir}/llms.txt", "w", encoding="utf-8") as f:
        f.write(f"# ucode Documentation Index\n# Source: {repo_url} (commit: {ucode_commit})\n")
        f.write(f"# Live docs: https://ucode.mein.io/\n# Generated: {TS}\n#\n")
        f.write("# ucode is a tiny ECMAScript-like scripting language for OpenWrt.\n")
        f.write("# Provides bindings for ubus, uci, uloop, netlink, and other OpenWrt APIs.\n")
        f.write("# Syntax closely resembles ECMAScript; synchronous; no OOP standard library.\n#\n")
        f.write("# Standalone use: each .md file in this folder is self-contained with full\n")
        f.write("# metadata headers. This llms.txt provides the navigational index.\n#\n## Files in this directory\n\n")

    print("Processing tutorials...")
    for src in sorted(glob.glob(f"{repo_ucode}/docs/tutorial-*.md")):
        base = os.path.basename(src)
        dest = re.sub(r'tutorial-[0-9]*-', 'ucode-tutorial-', base)
        
        with open(src, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        
        title = "Tutorial"
        for line in lines:
            if line.startswith("#"):
                title = line.strip("# \n")
                break
        
        with open(f"{out_dir}/{dest}", "w", encoding="utf-8") as fw:
            fw.write(f"# {title}\n\n")
            fw.write(f"> **Source:** [`{src.replace(f'{repo_ucode}/', '')}`]({repo_url}/blob/master/{src.replace(f'{repo_ucode}/', '')})\n")
            fw.write(f"> **Live docs:** https://ucode.mein.io/{os.path.basename(src).replace('.md', '')}.html\n")
            fw.write(f"> **Generated:** {TS} from commit `{ucode_commit}`\n\n---\n\n")
            fw.writelines(lines[1:] if lines and lines[0].startswith("#") else lines)
            
        with open(f"{out_dir}/llms.txt", "a", encoding="utf-8") as f:
            f.write(f"- [{dest}](/ucode-docs/{dest}): ucode tutorial — {title}\n")
    
    print("Processing modules...")
    srcs = sorted(glob.glob(f"{repo_ucode}/lib/*.js") + glob.glob(f"{repo_ucode}/lib/*.c"))
    for src in srcs:
        mod = os.path.splitext(os.path.basename(src))[0]
        # Run from repo_ucode so jsdoc can find plugins and config relative to CWD
        cmd = ["jsdoc2md", "--heading-depth", "2", "--global-index-format", "none"]
        if ucode_conf:
            rel_conf = os.path.relpath(ucode_conf, repo_ucode)
            cmd.extend(["--configure", rel_conf])
        
        rel_src = os.path.relpath(src, repo_ucode)
        cmd.append(rel_src)
        
        res = subprocess.run(cmd, capture_output=True, text=True, shell=IS_WINDOWS, cwd=repo_ucode, encoding="utf-8")
        stdout = res.stdout or ""
        stderr = res.stderr or ""
        if stderr:
            with open("jsdoc-ucode.err", "a", encoding="utf-8") as err_f:
                err_f.write(f"Stderr for {mod}:\n{stderr}\n")
                
        output = stdout.strip()
        word_count = len(output.split())
        if not output or word_count < 15:
            continue
            
        outfile = f"{out_dir}/ucode-module-{mod}.md"
        member_count = output.count("##")
        
        with open(outfile, "w", encoding="utf-8") as fw:
            fw.write(f"# ucode module: `{mod}`\n\n")
            fw.write(f"> **Source:** [`{src.replace(f'{repo_ucode}/', '')}`]({repo_url}/blob/master/{src.replace(f'{repo_ucode}/', '')})\n")
            fw.write(f"> **Live docs:** https://ucode.mein.io/module-{mod}.html\n")
            fw.write(f"> **Generated:** {TS} from commit `{ucode_commit}`\n\n---\n\n")
            fw.write(output)
            
        with open(f"{out_dir}/llms.txt", "a", encoding="utf-8") as f:
            f.write(f"- [ucode-module-{mod}.md](/ucode-docs/ucode-module-{mod}.md): ucode `{mod}` module — {member_count} documented members\n")

    if os.path.exists("jsdoc-ucode.err"):
        print("\n=== jsdoc warnings/errors (ucode) ===")
        with open("jsdoc-ucode.err", "r", encoding="utf-8") as err_f:
            print(err_f.read())
        print("=== end jsdoc warnings ===")
        os.remove("jsdoc-ucode.err")
