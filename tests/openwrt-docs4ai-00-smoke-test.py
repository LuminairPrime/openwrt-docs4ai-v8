import os
import sys
import shutil
import tempfile
import subprocess
import glob
import datetime
from datetime import timezone
import argparse

def main():
    parser = argparse.ArgumentParser(description="Smoke test runner for openwrt-docs4ai pipeline")
    parser.add_argument("--run-ai", action="store_true", help="Run AI summarization step. By default this is skipped to save quota.")
    parser.add_argument("--keep-temp", action="store_true", help="Keep the temporary execution folder for debugging")
    args = parser.parse_args()

    # Paths setup
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scripts_source = os.path.join(repo_root, ".github", "scripts")
    log_file_path = os.path.join(repo_root, "tests", "openwrt-docs4ai-00-smoke-test-log.txt")
    terminal_output_path = os.path.join(repo_root, "tests", "openwrt-docs4ai-00-smoke-test-terminal-output-recent.txt")

    if not os.path.isdir(scripts_source):
        print(f"ERROR: Cannot find scripts folder at {scripts_source}")
        sys.exit(1)

    print(f"Starting test runner...")
    print(f"Log will be appended to: {log_file_path}")

    # The scripts array to test in order
    steps_to_test = [
        ("01 Clone Repos", "bash", "openwrt-docs4ai-01-clone-repos.sh"),
        ("02a Scrape Wiki", "python", "openwrt-docs4ai-02a-scrape-wiki.py"),
        ("02b Scrape ucode", "python", "openwrt-docs4ai-02b-scrape-ucode.py"),
        ("02c Scrape jsdoc", "python", "openwrt-docs4ai-02c-scrape-jsdoc.py"),
        ("02d Core Packages", "bash", "openwrt-docs4ai-02d-scrape-core-packages.sh"),
        ("02e Example Packages", "bash", "openwrt-docs4ai-02e-scrape-example-packages.sh"),
        ("03 Add Links", "python", "openwrt-docs4ai-03-add-links.py"),
        ("04 AI Summaries", "python", "openwrt-docs4ai-04-generate-summaries.py", not args.run_ai),
        ("05 Finalize Publish", "bash", "openwrt-docs4ai-05-finalize-publish.sh")
    ]

    results = []
    ts_start_dt = datetime.datetime.now(timezone.utc)
    ts_start = ts_start_dt.strftime("%Y-%m-%d %H:%M:%S UTC")

    # We use tempfile.TemporaryDirectory to automatically clean up after the `with` block finishes
    # Using a local tmp directory in the project root as requested.
    local_tmp = os.path.join(repo_root, "tmp")
    os.makedirs(local_tmp, exist_ok=True)
    
    temp_context = tempfile.TemporaryDirectory(dir=local_tmp, prefix="openwrt-docs4ai-smoke-test-")
    temp_dir = temp_context.name if not args.keep_temp else tempfile.mkdtemp(dir=local_tmp, prefix="openwrt-docs4ai-smoke-test-")

    print(f"\nCreated isolated test sandbox at:\n {temp_dir}\n")

    # Capture all terminal output for the recent-output log
    terminal_log = []
    def log_term(msg):
        print(msg)
        terminal_log.append(msg)

    try:
        # 1. Setup Phase: Copy scripts into sandbox
        dest_scripts = os.path.join(temp_dir, ".github", "scripts")
        os.makedirs(dest_scripts, exist_ok=True)
        for expected_script in os.listdir(scripts_source):
            src_path = os.path.join(scripts_source, expected_script)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_scripts)

        # 2. Execution phase
        for step in steps_to_test:
            name = step[0]
            runner = step[1]
            script_file = step[2]
            skip = len(step) > 3 and step[3]

            if skip:
                print(f"[SKIP] {name}")
                results.append((name, "SKIPPED"))
                continue

            print(f"[RUN]  {name} ...")
            script_path = f".github/scripts/{script_file}"
            
            # Specifically inject SKIP_WIKI=true or similar if you want to speed up certain tests
            # But for a full smoke test, we let them run.
            env = os.environ.copy()
            # If skipping AI, we could also pass it effectively to the shell
            if skip:
                env["SKIP_AI"] = "true"

            try:
                # Run the command with cwd set to the safe temp_dir
                # Explicitly use encoding='utf-8' since OpenWrt data contains UTF-8 characters
                cmd = [runner, script_path] if runner != "bash" else ["bash", script_path]
                res = subprocess.run(cmd, cwd=temp_dir, env=env, text=True, capture_output=True, encoding="utf-8")
                
                # Append to terminal log
                terminal_log.append(f"--- STEP: {name} ---")
                terminal_log.append(f"COMMAND: {' '.join(cmd)}")
                terminal_log.append(f"STDOUT:\n{res.stdout}")
                terminal_log.append(f"STDERR:\n{res.stderr}")
                terminal_log.append(f"EXIT CODE: {res.returncode}\n")

                if res.returncode == 0:
                    log_term(f"  OK")
                    results.append((name, "PASS"))
                else:
                    log_term(f"  FAILED")
                    # No need to print stdout/stderr here anymore as it goes to the file
                    results.append((name, "FAIL"))
                    log_term(f"Halting test suite due to failure.")
                    break
            except Exception as e:
                log_term(f"  FAILED (Exception: {e})")
                results.append((name, f"FAIL-EX: {e}"))
                break

    finally:
        # 3. Teardown Phase
        if not args.keep_temp:
            import time
            print(f"\nCleaning up sandbox {temp_dir}...")
            # On Windows, sometimes file locks take a moment to release. 
            # We try to clean up, but if Windows Explorer is open to the folder, it will stay.
            try:
                temp_context.cleanup()
            except Exception as e:
                print(f"  WARNING: Could not fully delete {temp_dir}. It may be locked by another process (like Windows Explorer).")
                print(f"  Details: {e}")
        else:
            print(f"\nSkipping cleanup (flag --keep-temp). Sandbox preserved at: {temp_dir}")

    # 4. Write persistent log
    ts_end_dt = datetime.datetime.now(timezone.utc)
    ts_end = ts_end_dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, "a", encoding="utf-8") as lf:
        lf.write(f"=== Test Run [{ts_start} to {ts_end}] ===\n")
        for r in results:
            lf.write(f"{r[0]:<25}: {r[1]}\n")
        if any(r[1].startswith("FAIL") for r in results):
            lf.write("STATUS: FAILED\n\n")
        else:
            lf.write("STATUS: SUCCESS\n\n")
    
    # 5. Write terminal output log (Overwrites with most recent)
    with open(terminal_output_path, "w", encoding="utf-8") as tf:
        tf.write(f"=== FULL TERMINAL OUTPUT: {ts_start} ===\n\n")
        tf.write("\n".join(terminal_log))

    print(f"\nTest logging complete!")
    print(f" - Summary: {os.path.basename(log_file_path)}")
    print(f" - Details: {os.path.basename(terminal_output_path)}")

if __name__ == "__main__":
    main()
