#!/usr/bin/env python3
"""
Convenience launcher for tools/npm_publisher.py (works from any directory)
"""
import sys
import subprocess
from pathlib import Path

cur = Path(__file__).resolve().parent
script_path = cur / "tools" / "npm_publisher.py"
if not script_path.exists():
    script_path = cur.parent / "tools" / "npm_publisher.py"

args = [sys.executable, str(script_path)] + sys.argv[1:]
sys.exit(subprocess.call(args))
