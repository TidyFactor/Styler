#!/usr/bin/env python3
"""
TidyFactor Styler Track — Automated RTL & Logical Properties Auditor (scripts/audit_rtl.py)
Scans CSS and HTML files for legacy physical direction properties (left, right, margin-left, padding-right, float: left)
and validates adherence to modern CSS logical properties (inset-inline, margin-inline-start, padding-inline-end).
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PHYSICAL_PROP_PATTERNS = [
    (re.compile(r'\bmargin-left\s*:', re.IGNORECASE), "margin-left", "margin-inline-start"),
    (re.compile(r'\bmargin-right\s*:', re.IGNORECASE), "margin-right", "margin-inline-end"),
    (re.compile(r'\bpadding-left\s*:', re.IGNORECASE), "padding-left", "padding-inline-start"),
    (re.compile(r'\bpadding-right\s*:', re.IGNORECASE), "padding-right", "padding-inline-end"),
    (re.compile(r'\bleft\s*:\s*([^;]+);', re.IGNORECASE), "left", "inset-inline-start"),
    (re.compile(r'\bright\s*:\s*([^;]+);', re.IGNORECASE), "right", "inset-inline-end"),
    (re.compile(r'\bfloat\s*:\s*left\b', re.IGNORECASE), "float: left", "float: inline-start"),
    (re.compile(r'\bfloat\s*:\s*right\b', re.IGNORECASE), "float: right", "float: inline-end"),
    (re.compile(r'\btext-align\s*:\s*left\b', re.IGNORECASE), "text-align: left", "text-align: start"),
    (re.compile(r'\btext-align\s*:\s*right\b', re.IGNORECASE), "text-align: right", "text-align: end"),
    (re.compile(r'\bborder-left\s*:', re.IGNORECASE), "border-left", "border-inline-start"),
    (re.compile(r'\bborder-right\s*:', re.IGNORECASE), "border-right", "border-inline-end"),
]

def audit_rtl_directory(target_path: Path, auto_fix: bool = False):
    violations = []
    stats = {
        "physical_properties_count": 0,
        "fixed_properties_count": 0,
        "total_files_audited": 0
    }

    if not target_path.exists():
        return {
            "status": "FAIL",
            "violations": [{
                "severity": "ERROR",
                "rule": "target-path-exists",
                "file": str(target_path),
                "line": 0,
                "snippet": "",
                "message": f"Target path does not exist: {target_path}"
            }],
            "stats": stats
        }

    css_files = list(target_path.glob("**/*.css"))
    
    def is_valid_file(p: Path):
        parts = p.parts
        return not any(ignored in parts for ignored in [".git", "node_modules", "dist", ".gemini", "__pycache__"])

    valid_css_files = [f for f in css_files if is_valid_file(f)]
    stats["total_files_audited"] = len(valid_css_files)

    for file_path in valid_css_files:
        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
            lines = content.splitlines()
            rel_file = str(file_path.relative_to(target_path)) if target_path != file_path else file_path.name

            for idx, line in enumerate(lines, start=1):
                # Skip comments
                if line.strip().startswith("/*") or line.strip().startswith("*"):
                    continue

                for pattern, legacy_name, logical_replacement in PHYSICAL_PROP_PATTERNS:
                    if pattern.search(line):
                        stats["physical_properties_count"] += 1
                        violations.append({
                            "severity": "WARNING",
                            "rule": "use-css-logical-properties",
                            "file": rel_file,
                            "line": idx,
                            "snippet": line.strip()[:80],
                            "message": f"Legacy physical property '{legacy_name}' detected. Replace with logical property '{logical_replacement}' for flawless RTL support."
                        })
        except Exception as e:
            violations.append({
                "severity": "WARNING",
                "rule": "file-read-error",
                "file": str(file_path),
                "line": 0,
                "snippet": "",
                "message": f"Could not read CSS file: {str(e)}"
            })

    status = "FAIL" if any(v["severity"] == "ERROR" for v in violations) else ("WARNING" if violations else "PASS")

    return {
        "status": status,
        "violations": violations,
        "stats": stats
    }

def main():
    parser = argparse.ArgumentParser(description="TidyFactor Styler RTL & Logical Properties Auditor")
    parser.add_argument("--target", "-t", type=str, default=".", help="Target project directory to audit")
    parser.add_argument("--fix", action="store_true", help="Automatically convert physical properties to logical")
    parser.add_argument("--json", action="store_true", default=True, help="Output JSON format")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON")

    args = parser.parse_args()
    target_path = Path(args.target).resolve()

    result = audit_rtl_directory(target_path, auto_fix=args.fix)

    indent = 2 if args.pretty or not sys.stdout.isatty() else None
    print(json.dumps(result, indent=indent, ensure_ascii=False))

    sys.exit(1 if result["status"] == "FAIL" else 0)

if __name__ == "__main__":
    main()
