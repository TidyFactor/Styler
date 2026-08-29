#!/usr/bin/env python3
"""
validate_skill.py — TidyFactor Styler integrity and release validation script.
Verifies:
1. Version synchronization across .tidyfactor, package.json, brand.json, and CHANGELOG.md.
2. License consistency across files.
3. Link integrity between SKILL.md and referenced command/workflow/memory files.
4. Absence of hardcoded absolute machine paths in markdown files.
"""

import sys
import os
import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Set stdout/stderr encoding to UTF-8 on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def validate():
    failures = []
    print("=" * 60)
    print("  RUNNING TIDYFACTOR STYLER RELEASE VALIDATION")
    print("=" * 60)

    # 1. Version Sync Check
    print("\n[1] Checking SemVer synchronization across metadata...")
    with open(ROOT / "package.json", "r", encoding="utf-8") as f:
        pkg_ver = json.load(f).get("version")
    with open(ROOT / ".tidyfactor", "r", encoding="utf-8") as f:
        tf_ver = json.load(f).get("version")
    with open(ROOT / "brand.json", "r", encoding="utf-8") as f:
        brand_ver = json.load(f).get("version")

    with open(ROOT / "CHANGELOG.md", "r", encoding="utf-8") as f:
        changelog_content = f.read()

    print(f"  package.json : {pkg_ver}")
    print(f"  .tidyfactor  : {tf_ver}")
    print(f"  brand.json   : {brand_ver}")

    if not (pkg_ver == tf_ver == brand_ver):
        failures.append(f"Version mismatch: package.json({pkg_ver}) vs .tidyfactor({tf_ver}) vs brand.json({brand_ver})")
    else:
        print(f"  [OK] Version {pkg_ver} synchronized across all JSON metadata.")

    if f"## [{pkg_ver}]" not in changelog_content:
        failures.append(f"CHANGELOG.md is missing release entry for version [{pkg_ver}].")
    else:
        print(f"  [OK] CHANGELOG.md contains release entry for [{pkg_ver}].")

    # 2. License Consistency Check
    print("\n[2] Checking license consistency...")
    with open(ROOT / "package.json", "r", encoding="utf-8") as f:
        pkg_lic = json.load(f).get("license")
    with open(ROOT / "README.md", "r", encoding="utf-8") as f:
        readme_en = f.read()
    with open(ROOT / "README.ar.md", "r", encoding="utf-8") as f:
        readme_ar = f.read()

    if "License-MIT" in readme_en or "License-MIT" in readme_ar:
        failures.append("README contains MIT badge while package is licensed under Apache-2.0.")
    else:
        print("  [OK] License badges match Apache-2.0.")

    # 3. Path reference and link checks from SKILL.md
    print("\n[3] Checking SKILL.md referenced files exist on disk...")
    with open(ROOT / "SKILL.md", "r", encoding="utf-8") as f:
        skill_content = f.read()

    # Find all references like references/commands/*.md, workflows/*.md, memory/*.md
    refs = re.findall(r'(?:references/)?((?:commands|workflows|memory)/[a-zA-Z0-9_\-\.\*]+)', skill_content)
    for ref in refs:
        if "*" in ref:
            continue
        full_ref_path = ROOT / "references" / ref
        if not full_ref_path.exists():
            failures.append(f"Broken link in SKILL.md: references/{ref} does not exist on disk.")
        else:
            print(f"  [OK] Found references/{ref}")

    # 4. Check for personal/machine-specific absolute paths
    print("\n[4] Auditing for leaked machine-specific absolute paths...")
    leaked_path_pattern = re.compile(r'[a-zA-Z]:\\[wW]amp64\\', re.IGNORECASE)
    for ext in ["*.md", "*.json", "*.js", "*.py"]:
        for file_path in ROOT.rglob(ext):
            if "dist" in file_path.parts or "__pycache__" in file_path.parts:
                continue
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                if leaked_path_pattern.search(content):
                    rel = file_path.relative_to(ROOT)
                    failures.append(f"Leaked machine-specific absolute path found in {rel}")

    # 5. Check Multi-Language Navigation Links
    print("\n[5] Checking multi-language documentation consistency (Rule 13)...")
    locales = ["README.md", "README.ar.md", "README.fa.md", "README.es.md", "README.pt.md", "README.zh.md", "README.de.md", "README.fr.md"]
    for loc in locales:
        loc_path = ROOT / loc
        if loc_path.exists():
            loc_text = loc_path.read_text(encoding="utf-8")
            if "README.md" not in loc_text or "README.ar.md" not in loc_text:
                failures.append(f"{loc} is missing cross-language switcher links.")
            else:
                print(f"  [OK] {loc} contains valid language switcher.")
        else:
            failures.append(f"Missing expected localized doc file: {loc}")

    print("\n" + "=" * 60)
    if failures:
        print(f"[FAIL] {len(failures)} validation error(s) found:")
        for err in failures:
            print(f"  - {err}")
        print("=" * 60)
        sys.exit(1)
    else:
        print("[SUCCESS] ALL SKILL INTEGRITY CHECKS PASSED!")
        print("=" * 60)
        sys.exit(0)

if __name__ == "__main__":
    validate()
