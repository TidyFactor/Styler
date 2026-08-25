# Command: `section` — Create or Redesign a Page Section

## When to use
- The user points at one bounded region of a page (a hero, a pricing block, a testimonials strip, a footer) and wants it created or restyled — not a single component in isolation, not the whole page.
- Common trigger: a screenshot or file with one section circled/described, plus "fix this section" / "this looks off" / "redesign the hero".

## Dispatch steps
1. Determine which outcome this is:
   - The section **already exists** on the target page → load `references/workflows/section-redesign.md`.
   - The section is **being added new** → load `references/workflows/section-create.md`.
   - Unclear which → check the page's current sections before assuming; if still unclear, ask.
2. Load `references/memory/component-anatomy.md` — a section is usually several organisms arranged together; reuse/extend existing components before inventing new ones. Load `references/memory/decision-points.md` to resolve any unresolved decision points (checking `.tidyfactor/design-brief.md` first).
3. If `brand.json` exists at project root, load `references/memory/brand-tokens.md` to ingest colors and typography.
4. Load `references/memory/layout-archetypes.md` (and `references/memory/nav-footer-catalog.md` if header/footer) to select section macrostructure.
5. Detect the target stack, load the matching `references/memory/stacks/*.md` file.
6. If the section carries Arabic/bilingual text, also load `references/memory/typography-arabic.md` and `references/memory/rtl-css-engineering.md`.
7. If the section needs entrance/scroll motion, also load `references/memory/motion-principles.md`.

## Do not load
`page-create.md` / `page-redesign.md` — a section redesign never touches nav, footer, or other sections on the page. If the user's actual complaint spans the whole page (e.g. "the whole page feels inconsistent"), that's `redesign`, not `section`.
