# Command: `redesign` — Redesign an Existing Production Page

## When to use
- A page that already exists and already ships needs a visual/interaction overhaul end-to-end — not one section, not one component, the whole page.
- Common trigger: "redesign our homepage", "this whole page feels dated", "bring this page up to our new design direction".

## Dispatch steps
1. Load `references/workflows/page-redesign.md`.
2. Load `references/memory/quality-bar.md` — a full-page redesign is judged against the whole checklist, not spot-checked. Load `references/memory/decision-points.md` to resolve any unresolved decision points (checking `.tidyfactor/design-brief.md` first; preserve existing baseline silently unless explicit overhaul requested).
3. Load `references/memory/layout-archetypes.md` and `references/memory/nav-footer-catalog.md` to establish macrostructure flow.
4. If `brand.json` exists at project root, load `references/memory/brand-tokens.md` to ingest colors and typography.
5. Detect the target stack, load the matching `references/memory/stacks/*.md` file.
6. If the target stack is a TidyFactor production track, read that skill's own constraints first — a redesign must stay inside its locked architecture, not fight it.
7. If the page is Arabic/bilingual, also load `references/memory/typography-arabic.md` and `references/memory/rtl-css-engineering.md` — re-run the per-component RTL checklist across every section, not just the ones that visibly prompted the redesign.
9. If motion/interaction is in scope, also load `references/memory/motion-principles.md`.

## Do not load
`component.md` / `section.md` — if the actual ask is narrower ("just the hero needs work"), redirect to `section` instead; don't run a full-page redesign workflow on a partial ask.
