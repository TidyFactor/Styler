# Command: `assets` — Asset Optimization & Image Hygiene

## When to use
- Batch optimizing images (converting PNG/JPG to WebP/AVIF, stripping metadata, enforcing max dimensions).
- Auditing asset budgets (component CSS/JS delta ≤ 10KB, LCP hero image ≤ 400KB, font weights).

## Dispatch steps
1. Load `references/memory/asset-tooling.md` and `references/memory/quality-bar.md`.
2. Run image inspection and web optimization tools:
   ```bash
   python scripts/inspect_images.py assets/
   python scripts/optimize_images.py assets/ --quality 85
   ```
3. Enforce zero unused icon libraries and verify 0 Cumulative Layout Shift (CLS) via explicit `width`/`height` or `aspect-ratio` attributes.
