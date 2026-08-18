#!/usr/bin/env python3
"""
Extended Build Integrity & Quality Test Suite
Checks files, broken local links, duplicate IDs, accessibility (alt tags, ARIA attributes),
and external CDNs to ensure production-grade deployment quality.

Exit Codes:
    0 = Success
    1 = Test Failures Found
"""

import re
import sys
from pathlib import Path

# Project root is the parent directory of this script
PROJECT_ROOT = Path(__file__).resolve().parent.parent


class TestSuite:
    def __init__(self):
        self.failures = []
        self.warnings = []

    def log_failure(self, message):
        self.failures.append(message)

    def log_warning(self, message):
        self.warnings.append(message)

    def run_tests(self):
        print("="*60)
        print("         RUNNING EXTENDED BUILD INTEGRITY TESTS")
        print("="*60)

        self.test_production_files_exist()
        self.test_index_html_links()
        self.test_css_urls()
        self.test_duplicate_ids()
        self.test_accessibility()
        self.test_external_cdn_dependencies()

        print("\n" + "="*60)
        print("TEST RESULTS SUMMARY")
        print("="*60)
        
        if self.failures:
            print(f"\n[FAIL] {len(self.failures)} TEST FAILURE(S) FOUND:")
            for fail in self.failures:
                print(f"  - [FAIL] {fail}")
        else:
            print("\n[SUCCESS] ALL INTEGRITY AND ACCESSIBILITY TESTS PASSED SUCCESSFULLY!")

        if self.warnings:
            print(f"\n[WARN] {len(self.warnings)} WARNING(S) ENCOUNTERED:")
            for warn in self.warnings:
                print(f"  - [WARN] {warn}")

        print("="*60)
        return len(self.failures) == 0

    # 1. Check generated minified CSS and JS exist
    def test_production_files_exist(self):
        print("\n[TEST] Verifying production minified files exist...")
        required_files = [
            "assets/css/style.min.css",
            "assets/js/bundle.min.js"
        ]
        
        for rel_path in required_files:
            file_path = PROJECT_ROOT / rel_path
            if not file_path.exists():
                self.log_failure(f"Production file is missing: {rel_path}")
            elif file_path.stat().st_size == 0:
                self.log_failure(f"Production file is empty: {rel_path}")
            else:
                print(f"  [OK] {rel_path} is present ({file_path.stat().st_size} bytes)")

    # 2. Check broken local links in index.html
    def test_index_html_links(self):
        print("\n[TEST] Scanning index.html for broken local asset links...")
        index_path = PROJECT_ROOT / "index.html"
        if not index_path.exists():
            self.log_failure("index.html does not exist in project root!")
            return

        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Regex patterns to find local files (excluding external http/https/double slash)
        patterns = {
            "stylesheets": r'<link[^>]*href=["\'](?!https?:\/\/|\/\/)([^"\']+)["\']',
            "scripts": r'<script[^>]*src=["\'](?!https?:\/\/|\/\/)([^"\']+)["\']',
            "images": r'<img[^>]*src=["\'](?!https?:\/\/|\/\/)([^"\']+)["\']',
            "video_sources": r'<source[^>]*src=["\'](?!https?:\/\/|\/\/)([^"\']+)["\']',
            "video_posters": r'<video[^>]*poster=["\'](?!https?:\/\/|\/\/)([^"\']+)["\']'
        }

        for category, regex in patterns.items():
            matches = re.findall(regex, html)
            print(f"  Checking {len(matches)} local {category} references...")
            for match in matches:
                # Remove version query string if present (e.g. ?v=2.1.3)
                clean_path = match.split("?")[0]
                
                # Exclude mailto, tel, or hash links
                if clean_path.startswith(("#", "mailto:", "tel:", "javascript:")) or not clean_path.strip():
                    continue

                full_path = PROJECT_ROOT / clean_path
                if not full_path.exists():
                    self.log_failure(f"Broken {category} link in index.html: '{clean_path}' does not exist on disk.")

    # 3. Check assets referenced in CSS via url()
    def test_css_urls(self):
        print("\n[TEST] Scanning style.css for broken url() links...")
        css_path = PROJECT_ROOT / "assets/css/style.css"
        if not css_path.exists():
            self.log_failure("assets/css/style.css is missing!")
            return

        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()

        # Find all url(...) patterns
        urls = re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', css)
        css_dir = css_path.parent
        print(f"  Checking {len(urls)} url() links inside CSS...")

        for url in urls:
            # Skip external fonts, data URIs, or anchor links
            if url.startswith(("http://", "https://", "//", "data:")) or not url.strip():
                continue

            # CSS urls are relative to the CSS file itself
            resolved_path = (css_dir / url.split("?")[0]).resolve()
            if not resolved_path.exists():
                self.log_failure(f"Broken link in style.css url(): '{url}' (resolved to '{resolved_path.relative_to(PROJECT_ROOT)}') does not exist.")

    # 4. Check for duplicate element IDs in index.html
    def test_duplicate_ids(self):
        print("\n[TEST] Auditing index.html for duplicate element IDs...")
        index_path = PROJECT_ROOT / "index.html"
        if not index_path.exists():
            return

        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        ids = re.findall(r'id=["\']([^"\']+)["\']', html)
        seen_ids = {}
        for elem_id in ids:
            seen_ids[elem_id] = seen_ids.get(elem_id, 0) + 1

        duplicates = {k: v for k, v in seen_ids.items() if v > 1}
        
        if duplicates:
            for k, v in duplicates.items():
                self.log_failure(f"Duplicate element ID found: '#{k}' appears {v} times in HTML.")
        else:
            print(f"  [OK] Checked {len(ids)} element IDs. No duplicates found.")

    # 5. Accessibility Audit (alt attributes, ARIA roles, Heading levels)
    def test_accessibility(self):
        print("\n[TEST] Auditing accessibility (alt tags, ARIA attributes, headings)...")
        index_path = PROJECT_ROOT / "index.html"
        if not index_path.exists():
            return

        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        # 5.1 Check img alt attributes
        images = re.findall(r'<img([^>]*src=["\']([^"\']+)["\']([^>]*))>', html)
        print(f"  Auditing {len(images)} images for screen reader alt tags...")
        for img_tag, src, _ in images:
            if "alt=" not in img_tag:
                self.log_failure(f"Image tag is missing required 'alt' attribute: src='{src}'")

        # 5.2 Check single h1 tag outline
        h1s = re.findall(r'<h1[^>]*>.*?</h1>', html, re.DOTALL)
        if len(h1s) != 1:
            self.log_failure(f"SEO/Outline mismatch: index.html must have exactly one <h1> tag (found {len(h1s)}).")
        else:
            print("  [OK] Document contains exactly one <h1> tag.")

        # 5.3 Verify critical interactive element accessibility properties
        # Hamburger checks
        hamburger = re.search(r'<button[^>]*id=["\']hamburger["\'][^>]*>', html)
        if hamburger:
            tag = hamburger.group(0)
            if "aria-expanded=" not in tag or "aria-controls=" not in tag or "aria-label=" not in tag:
                self.log_failure("Interactive Hamburger menu button is missing vital accessibility attributes (aria-expanded, aria-controls, or aria-label).")
            else:
                print("  [OK] Hamburger menu accessibility attributes are correct.")
        
        # Interactive dots check
        dots = re.findall(r'<div[^>]*class=["\']process__dot["\'][^>]*>', html)
        for i, dot_tag in enumerate(dots):
            if 'role="button"' not in dot_tag or 'tabindex="0"' not in dot_tag or 'aria-label=' not in dot_tag:
                self.log_failure(f"Process step indicator dot {i+1} is missing vital accessibility attributes (role=\"button\", tabindex=\"0\", or aria-label).")

    # 6. Audit for unauthorized external CDN scripts
    def test_external_cdn_dependencies(self):
        print("\n[TEST] Auditing for external CDN script dependencies...")
        index_path = PROJECT_ROOT / "index.html"
        if not index_path.exists():
            return

        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Search for scripts with external http/https/double-slash sources
        cdn_scripts = re.findall(r'<script[^>]*src=["\'](https?:\/\/|\/\/)([^"\']+)["\']', html)
        
        # Check if any external CDN JS scripts exist
        if cdn_scripts:
            for protocol, url in cdn_scripts:
                # We flag external CDN JS scripts as failures because local versions are required
                self.log_failure(f"External script CDN dependency detected: '{protocol}{url}'. Only local assets are allowed.")
        else:
            print("  [OK] No external CDN JavaScript script tags detected. Fully self-contained local stack.")


if __name__ == "__main__":
    suite = TestSuite()
    success = suite.run_tests()
    sys.exit(0 if success else 1)
