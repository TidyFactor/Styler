# Command: `component` — Create or Redesign a Single Component

## When to use
- The user points at one reusable UI piece (a button, card, nav item, form field, modal, pricing tile) and wants it created or restyled — not a whole section or page.
- The request mentions a component by name, or pastes/references the file that defines it.

## Dispatch steps
1. Determine which outcome this is:
   - The component **already exists** in the target project → load `references/workflows/component-redesign.md`.
   - The component **doesn't exist yet** → load `references/workflows/component-create.md`.
   - Unclear which → check the project's component library before assuming; if still unclear, ask.
2. Load `references/memory/component-anatomy.md` — atomic hierarchy, state matrix, naming discipline. Load `references/memory/decision-points.md` to resolve any unresolved decision points (checking `.tidyfactor/design-brief.md` first). If `brand.json` exists at project root, load `references/memory/brand-tokens.md` to ingest colors and typography tokens.
3. Detect the target stack from what the user has shown/named, then load the matching file:
   - React/Next.js → `references/memory/stacks/react-next.md`
   - PHP Flight/Medoo → `references/memory/stacks/php-flight-medoo.md`
   - WordPress → `references/memory/stacks/wordpress.md`
   - Plain HTML/CSS/JS → `references/memory/stacks/html-vanilla.md`
   - Ambiguous → ask which stack before proceeding.
4. If the component carries Arabic/bilingual text, also load `references/memory/typography-arabic.md` and `references/memory/rtl-css-engineering.md` — this component is not done until it passes both.

## Do not load
`page-create.md` / `page-redesign.md` / `section-create.md` / `section-redesign.md` — those are different outcomes. If mid-task the request grows into "actually restyle the whole section this lives in," stop and switch to the `section` command instead of quietly expanding scope.
