#!/usr/bin/env python3
"""
Asset Bundler & Minifier Script
Combines and minifies CSS and JavaScript files relative to the project root.
"""

import re
from pathlib import Path

# Project root is the parent directory of this script's directory (i.e. scripts/ -> root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --- BUNDLE CONFIGURATION (Relative to PROJECT_ROOT) ---
CSS_BUNDLES = {
    "assets/css/style.min.css": [
        "assets/css/style.css"
    ]
}

JS_BUNDLES = {
    "assets/js/bundle.min.js": [
        "assets/js/gsap/3.12.5/gsap.min.js",
        "assets/js/gsap/3.12.5/ScrollTrigger.min.js",
        "assets/js/lenis@1.1.13/dist/lenis.min.js",
        "assets/js/main.js"
    ]
}


def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}T{suffix}"


def minify_css(css_content):
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove extra spaces around braces and symbols
    css = re.sub(r'\s*([\{\}:;,])\s*', r'\1', css)
    # Replace multiple spaces with a single space
    css = re.sub(r'\s+', ' ', css)
    # Remove unnecessary semicolons before closing braces
    css = re.sub(r';\}', '}', css)
    return css.strip()


def minify_js(js_content):
    # Save string literals to avoid corrupting comments inside quotes
    strings = []
    def save_str(match):
        strings.append(match.group(0))
        return f"__STR_PLACEHOLDER_{len(strings)-1}__"

    string_pattern = r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`(?:[^`\\]|\\.)*`)'
    js = re.sub(string_pattern, save_str, js_content)

    # Remove single-line comments // (protecting http:// style links)
    js = re.sub(r'(?<!:)\/\/.*$', '', js, flags=re.MULTILINE)
    # Remove multi-line comments /* ... */
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    # Remove multiple spaces/newlines around operator boundaries
    js = re.sub(r'\s*([=\+\-\*\/\:\?\{\}\(\)\[\]\,\;])\s*', r'\1', js)
    # Replace multiple whitespaces/newlines with single line-break or space
    js = re.sub(r'\n+', '\n', js)
    js = re.sub(r'[ \t]+', ' ', js)

    # Restore string literals
    for i, s in enumerate(strings):
        js = js.replace(f"__STR_PLACEHOLDER_{i}__", s)

    return js.strip()


def build_bundle(dest_path_rel, src_files_rel, file_type):
    dest_path = PROJECT_ROOT / dest_path_rel
    print(f"Building bundle -> {dest_path.relative_to(PROJECT_ROOT)}")
    combined_content = []
    total_src_size = 0

    for src_file in src_files_rel:
        src_path = PROJECT_ROOT / src_file
        if not src_path.exists():
            print(f"  [ERROR] Source file not found: {src_file}")
            continue

        size = src_path.stat().st_size
        total_src_size += size
        print(f"  + {src_path.name} ({get_size_format(size)})")

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        is_already_minified = src_path.name.endswith(".min.js") or src_path.name.endswith(".min.css")
        
        if is_already_minified:
            combined_content.append(content)
        else:
            if file_type == "css":
                minified = minify_css(content)
            elif file_type == "js":
                minified = minify_js(content)
            else:
                minified = content
            combined_content.append(minified)

    output_content = "\n".join(combined_content)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)

    final_size = dest_path.stat().st_size
    saved = total_src_size - final_size
    pct = (saved / total_src_size) * 100 if total_src_size > 0 else 0
    
    print(f"  [SUCCESS] Combined Size: {get_size_format(total_src_size)} -> {get_size_format(final_size)} (-{pct:.1f}%)")
    print(f"  Saved: {get_size_format(saved)}\n")


def main():
    print("="*50)
    print("Beginning Asset Bundler and Minifier (Scripts Folder)...")
    print("="*50 + "\n")

    for dest, sources in CSS_BUNDLES.items():
        build_bundle(dest, sources, "css")

    for dest, sources in JS_BUNDLES.items():
        build_bundle(dest, sources, "js")

    print("="*50)
    print("Bundling process completed successfully!")
    print("="*50)


if __name__ == "__main__":
    main()
