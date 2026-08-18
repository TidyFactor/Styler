#!/usr/bin/env python3
"""
Main Production Build Orchestrator
Runs all production build steps in sequence:
  1. Bundles and minifies JS and CSS assets.
  2. Scans and optimizes all images in assets/image/.
  3. Executes the build test suite. Aborts the build on failure.
  4. Performs cache-busting on index.html, updating asset query strings (?v=) with a timestamp.
  5. Packages the clean production-ready files into release/deploy.zip.

Usage:
    python scripts/build.py
"""

import os
import re
import sys
import time
import zipfile
import subprocess
from pathlib import Path

# Paths relative to this script (inside scripts/)
SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent


def run_command(command_args, description):
    print(f"\n>>> Running: {description}...")
    try:
        # Run sub-script and redirect output to stdout
        result = subprocess.run(
            [sys.executable] + command_args, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True,
            check=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] {description} failed.")
        print(e.stdout)
        print(e.stderr)
        return False
    except Exception as e:
        print(f"  [ERROR] Failed to run command: {e}")
        return False


def update_cache_busting_versions():
    print("\n>>> Running: index.html Cache-Busting Version Updates...")
    index_path = PROJECT_ROOT / "index.html"
    if not index_path.exists():
        print("  [ERROR] index.html not found, skipping version updates.")
        return

    # Use current datetime stamp as unique version query string
    version_stamp = time.strftime("%Y%m%d%H%M%S")
    print(f"  Target version code: {version_stamp}")

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex matches to replace query strings in href and src attributes
    new_content = re.sub(
        r'(href=["\']assets/css/style\.min\.css)\?v=[^"\'\s]*([\x22\x27])',
        r'\1?v=' + version_stamp + r'\2',
        content
    )
    
    new_content = re.sub(
        r'(src=["\']assets/js/bundle\.min\.js)\?v=[^"\'\s]*([\x22\x27])',
        r'\1?v=' + version_stamp + r'\2',
        new_content
    )

    if content != new_content:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  [SUCCESS] index.html asset references updated with version code '?v={version_stamp}'.")
    else:
        print("  [INFO] No version references updated in index.html.")


def package_release():
    print("\n>>> Running: Packaging Clean Production Release...")
    release_dir = PROJECT_ROOT / "release"
    release_dir.mkdir(exist_ok=True)
    
    zip_path = release_dir / "deploy.zip"
    if zip_path.exists():
        try:
            zip_path.unlink()
        except Exception as e:
            print(f"  [ERROR] Could not delete old release package: {e}")
            sys.exit(1)

    print(f"  Creating ZIP archive: {zip_path.relative_to(PROJECT_ROOT)}")
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 1. Add index.html
            index_path = PROJECT_ROOT / "index.html"
            if index_path.exists():
                zipf.write(index_path, "index.html")
                print("  + index.html")
                
            # 2. Recurse assets/
            assets_dir = PROJECT_ROOT / "assets"
            added_count = 0
            for root, _, files in os.walk(assets_dir):
                for file in files:
                    file_path = Path(root) / file
                    
                    # Compute relative path string
                    rel_path = file_path.relative_to(PROJECT_ROOT)
                    rel_path_str = rel_path.as_posix()
                    
                    # Skip backups and system dotfiles
                    if "_backup" in file_path.name or file_path.name.startswith("."):
                        continue
                    
                    # Clean production exclusions:
                    # - Under assets/css/: skip style.css (keep style.min.css)
                    if rel_path_str.startswith("assets/css/"):
                        if file_path.name == "style.css":
                            continue
                            
                    # - Under assets/js/: skip main.js and unneeded library folders (keep only bundle.min.js)
                    if rel_path_str.startswith("assets/js/"):
                        if file_path.name != "bundle.min.js":
                            continue
                    
                    zipf.write(file_path, rel_path)
                    added_count += 1
            print(f"  + assets/ ({added_count} files included, unminified files and libraries excluded)")
            
        print(f"  [SUCCESS] Created release package successfully: release/deploy.zip")
    except Exception as e:
        print(f"  [ERROR] Failed to compile ZIP archive: {e}")
        sys.exit(1)


def main():
    start_time = time.time()
    
    print("="*60)
    print("      NOOR AL-ISLAM LANDING PAGE — PRODUCTION BUILDER")
    print("="*60)

    # 1. Run Minifier & Bundler
    assets_success = run_command(
        [str(SCRIPTS_DIR / "minify_assets.py")], 
        "Minifying and Bundling CSS & JS Assets"
    )
    if not assets_success:
        print("Build aborted due to JS/CSS bundling errors.")
        sys.exit(1)

    # 2. Run Image Optimizer
    images_success = run_command(
        [str(SCRIPTS_DIR / "optimize_images.py"), "assets/image"],
        "Optimizing Project Images"
    )
    if not images_success:
        print("  [WARNING] Image optimization script reported warnings/errors. Continuing build...")

    # 3. Run Build Integrity Tests
    tests_success = run_command(
        [str(SCRIPTS_DIR / "test_build.py")],
        "Executing Automated Test Suite"
    )
    if not tests_success:
        print("\n[FAIL] BUILD ABORTED: The automated test suite reported failures.")
        print("Please resolve the failures listed above before deploying.")
        sys.exit(1)

    # 4. Cache Busting Version Updater
    update_cache_busting_versions()

    # 5. Package ZIP Release
    package_release()

    end_time = time.time()
    elapsed = end_time - start_time
    
    print("\n" + "="*60)
    print(f"[SUCCESS] PRODUCTION BUILD & PACKAGING COMPLETED IN {elapsed:.2f}s!")
    print("="*60)


if __name__ == "__main__":
    main()
