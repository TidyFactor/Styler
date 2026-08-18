# Asset Tooling & Python Automation Utilities

`tidyfactor-styler` provides Python scripts under `scripts/` to automate color palette extraction, WCAG 2.1 AA contrast calculations, image web optimization (WebP/AVIF conversion), asset minification, and budget audits.

## Tooling Index

| Script Tool | Command / Purpose | Execution |
|---|---|---|
| `scripts/extract_palette.py` | Extract brand colors + WCAG AA contrast ratio | `python scripts/extract_palette.py <image> --json brand.json --css tokens.css` |
| `scripts/optimize_images.py` | WebP/AVIF conversion, resizing & compression | `python scripts/optimize_images.py assets/ --quality 85` |
| `scripts/inspect_images.py` | Audit image sizes & dimensions against budgets | `python scripts/inspect_images.py assets/` |
| `scripts/minify_assets.py` | Minify CSS/JS without heavy build tools | `python scripts/minify_assets.py design-system/` |
| `scripts/remove_backgrounds.py` | Cutout image background removal helper | `python scripts/remove_backgrounds.py input.png output.png` |

## 1. Palette Extraction & Contrast Audit (`extract_palette.py`)

Extracts dominant colors from a reference image, logo, or screenshot, computes relative luminance, and verifies WCAG AA contrast (≥ 4.5:1 for body copy).

```bash
python scripts/extract_palette.py reference_shot.png --json brand.json --css design-system/tokens.css
```

## 2. Image Optimization & Budget Enforcement (`optimize_images.py`)

Converts PNG/JPG images to WebP/AVIF, strips metadata, enforces max dimensions (e.g. 1920px max width), and verifies the LCP image stays under 400KB.

```bash
python scripts/optimize_images.py public/images/ --quality 85
```
