# Command: `page` — Build a New Production Page

## When to use
- A brand-new page/route/view is needed inside an existing, already-shipping codebase (e.g. add a pricing page to an existing Next.js app, add a new WordPress template, add a new route to a TidyFactor PHP project).
- Not for a page that doesn't exist yet in a project that doesn't exist yet — that's project scaffolding, handled by the matching `tidyfactor-*` track skill, not this one.

## Dispatch steps
1. Load `references/workflows/page-create.md`.
2. Load `references/memory/component-anatomy.md` — a page is organisms arranged into a specific layout; reuse the project's existing components first. Load `references/memory/decision-points.md` to resolve any unresolved decision points (D1-D5, checking `.tidyfactor/design-brief.md` first).
3. Load `references/memory/layout-archetypes.md` and `references/memory/nav-footer-catalog.md` to select page macrostructure.
4. If `brand.json` exists at project root, load `references/memory/brand-tokens.md` to ingest colors and typography.
5. Detect the target stack, load the matching `references/memory/stacks/*.md` file.
6. If the target stack is a TidyFactor production track (PHP Micro/Kernel, Webletz, tidyfactor-html), read that skill's own SKILL.md constraints before writing the page — its file/routing/module contract wins over any generic assumption here.
7. If the page is Arabic/bilingual, also load `references/memory/typography-arabic.md` and `references/memory/rtl-css-engineering.md` — an Arabic-first design pass, not an English page mirrored afterward.

## Do not load
`component.md` / `section.md` workflows directly — building a page composes existing or newly-defined components/sections, but the outcome and validation checklist are page-level, not component-level.
