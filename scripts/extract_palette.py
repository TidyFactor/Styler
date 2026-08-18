#!/usr/bin/env python3
"""
extract_palette.py — Design System Palette & Color Extraction Tool
Extracts dominant brand colors, background tones, text colors, and WCAG contrast scores
from reference screenshots, logos, or hero images to generate brand.json and tokens.css.

Dependencies:
    pip install pillow

Usage:
    python scripts/extract_palette.py assets/logo.png --json brand.json
    python scripts/extract_palette.py reference_shot.png --css design-system/tokens.css
"""

import os
import sys
import json
import argparse
from PIL import Image

def get_rgb_luminance(rgb):
    """Calculates relative luminance according to WCAG 2.1 specifications."""
    r, g, b = [x / 255.0 for x in rgb]
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(rgb1, rgb2):
    """Calculates WCAG contrast ratio between two RGB colors (1 to 21)."""
    l1 = get_rgb_luminance(rgb1)
    l2 = get_rgb_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def rgb_to_hex(rgb):
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"

def extract_dominant_colors(image_path, num_colors=5):
    if not os.path.exists(image_path):
        print(f"ERROR: File not found: {image_path}", file=sys.stderr)
        return None
    
    img = Image.open(image_path).convert("RGB")
    img.thumbnail((200, 200), Image.Resampling.LANCZOS)
    
    # Quantize image to extract primary color palette
    quantized = img.quantize(colors=num_colors, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()[:num_colors * 3]
    
    colors = []
    for i in range(0, len(palette), 3):
        rgb = tuple(palette[i:i+3])
        colors.append(rgb)
    
    return colors

def main():
    parser = argparse.ArgumentParser(description="Extract brand color palettes and WCAG contrast metrics.")
    parser.add_argument("input", help="Path to input image (logo, screenshot, brand photo)")
    parser.add_argument("--json", "-j", help="Output path for brand.json update")
    parser.add_argument("--css", "-c", help="Output path for tokens.css variables")
    
    args = parser.parse_args()
    
    colors = extract_dominant_colors(args.input)
    if not colors:
        sys.exit(1)
        
    hex_colors = [rgb_to_hex(c) for c in colors]
    
    primary = hex_colors[0]
    secondary = hex_colors[1] if len(hex_colors) > 1 else "#06B6D4"
    accent = hex_colors[2] if len(hex_colors) > 2 else "#F59E0B"
    dark_bg = "#0F172A"
    light_bg = "#F8FAFC"
    
    cr_on_dark = contrast_ratio(colors[0], (15, 23, 42))
    cr_on_light = contrast_ratio(colors[0], (248, 250, 252))
    
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass
    print(f"[OK] Extracted Palette from {args.input}:")
    print(f"  Primary:   {primary} (WCAG Contrast vs Dark: {cr_on_dark:.2f}:1, Light: {cr_on_light:.2f}:1)")
    print(f"  Secondary: {secondary}")
    print(f"  Accent:    {accent}")
    
    if args.json:
        brand_data = {}
        if os.path.exists(args.json):
            try:
                with open(args.json, "r", encoding="utf-8") as f:
                    brand_data = json.load(f)
            except Exception:
                brand_data = {}

        if "colors" not in brand_data or not isinstance(brand_data["colors"], dict):
            brand_data["colors"] = {}

        # Handle brand.json v2 dual-mode schema if present
        if "light" in brand_data["colors"] and isinstance(brand_data["colors"]["light"], dict):
            brand_data["colors"]["light"]["primary"] = primary
            brand_data["colors"]["light"]["secondary"] = secondary
            brand_data["colors"]["light"]["accent"] = accent
            if "dark" in brand_data["colors"] and isinstance(brand_data["colors"]["dark"], dict):
                brand_data["colors"]["dark"]["secondary"] = secondary
                brand_data["colors"]["dark"]["accent"] = accent
        else:
            # Fallback for flat structure
            brand_data["colors"]["primary"] = primary
            brand_data["colors"]["secondary"] = secondary
            brand_data["colors"]["accent"] = accent
            brand_data["colors"]["neutralDark"] = dark_bg
            brand_data["colors"]["neutralLight"] = light_bg

        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(brand_data, f, indent=2)
        print(f"✓ Palette updated in: {args.json}")
        
    if args.css:
        css_vars = f"""/* Auto-generated Design Tokens from {args.input} */
:root {{
  --color-primary: {primary};
  --color-secondary: {secondary};
  --color-accent: {accent};
  --color-dark: {dark_bg};
  --color-light: {light_bg};
}}
"""
        with open(args.css, "a", encoding="utf-8") as f:
            f.write(css_vars)
        print(f"✓ CSS Variables appended to: {args.css}")

if __name__ == "__main__":
    main()
