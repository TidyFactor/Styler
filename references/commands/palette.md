# Command: `palette` — Extract Color Palette & WCAG AA Contrast Scores

## When to use
- Extracting primary, secondary, accent, and background colors from a reference screenshot, logo, or brand asset.
- Calculating WCAG 2.1 AA contrast scores (≥ 4.5:1 ratio) to generate or update `brand.json` and CSS custom properties.

## Dispatch steps
1. Load `references/memory/brand-tokens.md` and `references/memory/asset-tooling.md`.
2. Run the automated palette extraction tool:
   ```bash
   python scripts/extract_palette.py <image-path> --json brand.json --css design-system/tokens.css
   ```
3. Verify that contrast ratios for body copy meet WCAG AA standards (≥ 4.5:1). Update CSS variables or Tailwind theme configs accordingly.
