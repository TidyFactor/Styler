# Command: `nav-footer` — Select Navigation & Footer Archetypes

## When to use
- Creating or redesigning navigation bars (N1–N9) or footers (Ft1–Ft8) inside a production codebase.
- Auto-loaded by `section` or `redesign` when targeting header/footer regions.

## Dispatch steps
1. Load `references/memory/nav-footer-catalog.md`.
2. Match the brand archetype and content needs to a navigation pattern (N1–N9) or footer pattern (Ft1–Ft8).
3. If the layout is Arabic or bilingual, ensure `typography-arabic.md` and `rtl-css-engineering.md` rules are loaded — navigation and footer elements require direction-agnostic logical properties and explicit bidi isolation.

## No dedicated workflow file
This command selects the archetype structure. Hand off to `section-create.md` or `section-redesign.md` to execute the code.
