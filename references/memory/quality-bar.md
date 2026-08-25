# Quality Bar — Reference for every command, checked before calling anything finished

## Layout — viewport overflow & One-Page Fold View
- **Zero Scroll on Single-View Panels & Hero Stages**: A standalone single-page view, mission control dashboard, or dedicated section fold MUST NOT require vertical scrolling on standard desktop viewports (1080p, 1440p, standard laptop resolutions). On narrow/mobile viewports (<768px), graceful linear vertical stacking is expected.
- **High-Density Scaling & Viewport Enclosure**: Use compact headers/footers, fluid vertical padding (`py-2` to `py-3.5`), multi-column side-by-side metric grids (e.g. 3-column horizontal gauges instead of stacked vertical rows), and space-efficient typography so the entire core UI fits above the fold.
- **Dynamic Feeds Internal Scroll**: For single-page dashboards containing dynamic tables or log feeds, the outer container must remain fixed (`h-[100dvh] overflow-hidden`) with internal scroll assigned strictly to the feed container (`flex-1 min-h-0 overflow-y-auto`).
- A Hero, Intro, or CTA section's rendered height must not exceed 100vh without content that actually justifies it (long lists, data tables, galleries) — forcing scroll *inside* a section to see its own content is a defect.
- Spacing (`padding`, `margin`, `gap`) uses fluid values (`clamp(min, preferred-vw/vh, max)`), not hardcoded fixed px, for anything that scales with viewport.
- Heading/display type uses `clamp(min, preferred-vw, max)`, tested against how many lines the actual copy wraps to — not a fixed `font-size` assumed to fit.
- Hero/CTA sections center content via `display:flex; flex-direction:column; justify-content:center;` inside a `min-height:100vh; max-height:100vh;` container — not manual top/bottom padding guesses.
- Section height/typography is checked in every language the page ships in. Arabic copy commonly wraps to a different line count than the English equivalent at the same width.
- Background images/media use `background-size: cover` / `object-fit: cover` — never let an asset's intrinsic size dictate section height.

## Performance & production readiness (Performance Budgets)
- **Component CSS/JS Payload**: New component CSS/JS delta must stay ≤ 10KB. Never import an entire icon library (e.g. FontAwesome / full Lucide bundle) for a few icons; use isolated inline SVGs or existing project icon tokens.
- **Font Weight Budget**: Maximum 3 font families site-wide, and ≤ 4 font weights total (e.g. 400, 500, 600, 700). Self-host critical fonts with `font-display: swap`.
- **Images & Media**: WebP/AVIF format required. Hero image size budget ≤ 400KB. Explicit `width`/`height` or `aspect-ratio` to enforce 0 Cumulative Layout Shift (CLS). `loading="eager"` on LCP hero images; `loading="lazy"` on everything below the fold.
- **SEO & Semantic Baseline**: Exactly one `<h1>` per page, logical heading hierarchy (`h1` -> `h2` -> `h3`), meaningful `alt` text on content images (empty `alt=""` for decorative).
- **Asset Hygiene**: Zero unused CSS/JS introduced. Reuse existing codebase utility classes and variables rather than adding single-use custom styles.

## Contrast & accessibility
- Text-on-background contrast meets WCAG AA at minimum for body text; glassmorphism/overlay panels are checked individually, not assumed safe because the design direction calls for translucency.
- Every interactive element has a visible `focus-visible` state — not just hover.

## Visual Consistency Contract & Anti-Drift Rules
- **Zero Visual Drift**: Spacing, border-radius, and color values must strictly reuse existing project tokens/variables (`var(--brand-primary)`, `var(--radius-brand)`). Never introduce one-off magic numbers (`mt-[13px]`, `rounded-[17px]`) for a single component.
- **Border Radius Hierarchy Scale**: Maintain strict radius hierarchy across elements:
  - Pills / Badges / Avatars: `rounded-full` (9999px)
  - Interactive Buttons / Inputs: `rounded-lg` (8px) or `rounded-xl` (12px)
  - Surface Cards / Modals: `rounded-xl` (12px) or `rounded-2xl` (16px) — never exceed 16px on content cards.
- **No Orphaned CSS / Duplicate Utility Classes**: Match existing project styling patterns (Tailwind classes if Tailwind is present; existing CSS classes if not).

## The 16 AI Anti-Pattern Tells Checklist
Reject and revise any generated code that exhibits any of the following 16 AI anti-pattern tells:

1. **Ambient Animation Overload**: Everything moving simultaneously without an orchestrated focus moment.
2. **Generic Stock Hero**: Stock image + generic headline with zero distinguishing design decisions.
3. **Excessive Gradient / Glow Abuse**: Overusing radial ambient glows or bright gradients to mask weak layout decisions.
4. **Uniform Border-Radius & Shadow**: Applying identical `rounded-2xl shadow-lg` to every single element regardless of hierarchy.
5. **Light Gray Low-Contrast Copy**: Using faint gray text (`#94a3b8`) that violates WCAG 2.1 AA (minimum 4.5:1 ratio).
6. **Warm Cream / Sand Backgrounds**: Defaulting to `#fdf6e2`, paper, or parchment textures outside explicit editorial directions.
7. **Decorative Side-Stripe Borders**: Adding arbitrary 4px colored left-borders on content cards.
8. **Gradient Text Overuse**: Applying `background-clip: text` to standard body or section headings.
9. **Blueprint Grid Lines**: Overlaying decorative blueprint grid lines across section backgrounds without purpose.
10. **Uppercase Eyebrow Saturation**: Adding small, tracked-out uppercase eyebrow text above every single section title.
11. **Section Height Overfill**: Forcing `100vh` height on a section with insufficient content, causing scroll inside sections.
12. **Interchangeable Component Design**: Designing a component that looks identical whether used in SaaS, e-commerce, or editorial.
13. **Unbound Hero Top Padding**: Over-padding hero containers (`pt-48`) causing content to drop below the fold.
14. **Multi-Line CTA Buttons**: Wrapping CTA button text onto 2 lines instead of forcing a crisp single line.
15. **Un-Isolated Microcopy**: Using English microcopy conventions inside Arabic RTL layouts without bidi isolation.
16. **Missing Interactive State Matrix**: Shipping default/hover states while omitting `focus-visible`, `active`, `disabled`, or `loading`.

## Pre-Emit Self-Critique System (7 Axes)
Before outputting code, score the design from 1 to 5 on 7 axes. Any score < 3 triggers an immediate internal revision pass. Stamp the output header with the result:
`/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`

1. **Philosophy (`P`)**: Aligned with the project's actual identity and brand voice — not a generic template.
2. **Hierarchy (`H`)**: Clear visual priority; exactly one primary action per viewport; logical contrast in type and color.
3. **Execution (`E`)**: Clean, production-grade markup; proper responsive wrapping; fluid values (`clamp()`).
4. **Specificity (`S`)**: Designed specifically for the target domain (SaaS vs. Editorial vs. Utility) with zero interchangeable generic parts.
5. **Restraint (`R`)**: Controlled animations, minimal decoration, and purposeful whitespace — avoiding visual clutter.
6. **Variety (`V`)**: Dynamic visual pacing across sections; avoiding repetitive uniform card stacks.
7. **Decision Alignment (`D`)**: 100% faithful to the confirmed choices in `.tidyfactor/design-brief.md` or explicit prompt override.

## Pre-delivery Check
Before calling any `component`, `section`, `page`, or `redesign` output finished: measure actual rendered height against viewport at mobile and desktop widths, in every shipped language, and confirm against this file's checklist — not just "it looks fine." For `page`/`redesign` specifically, also confirm the Performance & production-readiness items above — a prototype-quality page that merely looks right is not the deliverable this skill exists to produce.
