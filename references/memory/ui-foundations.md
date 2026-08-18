# UI Design Foundations — Reference for `component`/`section`/`page`/`redesign`

The layer beneath every decision this skill makes, in any language or stack. `component-anatomy.md` covers atomic structure and state; this file covers layout/system-level judgment.

## Visual hierarchy
Every screen has exactly one primary action per view — everything else is visually subordinate to it (size, weight, color saturation, position). A page with three equally-weighted CTAs has no hierarchy, not three opportunities. Hierarchy is built through contrast in size, weight, color, and whitespace around an element — not through adding more elements.

## Grid systems
A 12-column grid (or the project's existing column count — don't introduce a second grid system into a project that has one) with a defined max container width and consistent gutter. Content should snap to the grid's column boundaries; ad-hoc pixel widths that don't align to any column are a tell of an ungoverned layout.

## Spacing systems (the token layer under "no magic numbers")
A spacing scale built on one base unit (commonly 4px or 8px) — `4, 8, 12, 16, 24, 32, 48, 64...` — not arbitrary values like `13px`/`22px` chosen per-element. Every margin/padding/gap in new or redesigned work should resolve to a step on this scale, sourced from the project's actual token/variable system (CSS custom properties, Tailwind's spacing scale, a `tokens.css` file) — never introduced as a fresh literal value.

## Responsive design
Design mobile-first when starting fresh (base styles for the smallest breakpoint, enhance upward), but when redesigning an existing desktop-first codebase, follow its existing breakpoint convention rather than inverting the whole system. Breakpoints are a small fixed set (commonly ~3-5) matched to the project's existing ones — don't invent a new breakpoint for one component's specific need without checking if an existing one already covers it.

## Component-based design
See `component-anatomy.md` for the atomic hierarchy and reuse-before-create discipline — this is the operating principle behind every `component`/`section`/`page` outcome this skill produces.

## Forms
Label always visible (not placeholder-as-label — placeholder text disappearing on focus loses context, especially costly for longer Arabic labels). Inline validation appears near the field it concerns, not only in a summary at the top. Required-field marking is consistent site-wide (asterisk position — see `rtl-css-engineering.md` for its logical placement in RTL). Multi-step forms show progress state, not just a bare "next" button.

## Tables
Distinguish data tables (dense, sortable, numeric-aligned) from card-based "table-like" layouts used for browsing — don't force dense tabular data into a card grid or vice versa. Sticky header on scroll for long tables. Row-level actions get a consistent, predictable position (see `rtl-css-engineering.md` for its side in RTL) rather than varying by row content length.

## Dashboards
Lead with the metric the user checks most often, not an alphabetically/creation-ordered widget grid. Group related metrics visually (proximity = relatedness) rather than a uniform grid of disconnected cards. Empty/zero-data states for widgets are designed intentionally, not left as a blank card — a new dashboard user seeing nothing but empty boxes reads as broken, not "no data yet."

## Accessibility (layout-level; see `quality-bar.md` for contrast/focus specifics)
Touch targets at minimum ~44x44px for anything tappable. Logical tab order matches visual order (a CSS-only reorder that doesn't match DOM order breaks keyboard navigation) — this interacts directly with RTL: confirm tab order still makes sense after a logical-properties-driven mirror, don't assume it inherits correctly.

## Design systems (the governing idea, not a specific deliverable)
Every visual decision (color, spacing, radius, type size) should trace back to a token, not a one-off value chosen for a single instance. When a genuinely new value is needed repeatedly, it becomes a new token added to the project's system — not a precedent for scattering ad-hoc values everywhere.
