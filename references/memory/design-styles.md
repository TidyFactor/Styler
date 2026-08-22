# Design Styles & Movements — Reference for `styles`

A working palette of directions, not an art-history survey. Each entry: what it looks like, when it fits, what to avoid. Stack-agnostic — the direction is a design decision; each `memory/stacks/*.md` file covers how to actually express it in that stack's idiom.

## Swiss / International Typographic Style
Grid-driven, sans-serif, objective, generous negative space, asymmetric but rigorously aligned layouts. Fits: institutional, editorial, technical/precision brands. Avoid: applying the grid so rigidly the content feels bureaucratic.

## Bauhaus
Geometric shapes as structural elements, primary-plus-black palettes, function-follows-form typography. Fits: education, design tools, craft/foundational-thinking brands. Avoid: circles+triangles as decoration with no structural logic.

## Brutalism (web)
Raw, deliberately "undesigned" HTML elements, harsh contrast, visible grid lines, monospace accents. Fits: developer tools, portfolios, anti-polish brands. Avoid: mistaking actual unstyled defaults for the aesthetic — it's a considered choice.

## Neo-Brutalism
Hard black drop shadows (`shadow-[4px_4px_0px_#000]`), thick borders (`border-2 border-black`), tactile push buttons with active offset (`active:translate-x-0.5 active:translate-y-0.5 active:shadow-none`), saturated pastel/neon stickers (`#FFE600`, `#00F0FF`, `#00FF66`, `#FF4D6D`), and bold Arabic/Latin typography (Cairo 900 + Space Grotesk + Fira Code). Fits: mission control dashboards, developer platforms, bold modern SaaS, Web NOC telemetry.
- **Dark Mode Contrast Guardrail (WCAG AA)**: Colored accent sticker cards (`bg-neo-yellow`, `bg-neo-green`, `bg-neo-cyan`, `bg-neo-coral`) must retain explicit `text-black font-black` and MUST NOT be overridden by global dark card background rules (`html.dark .neo-card`). Use explicit specificity (`!bg-neo-yellow !text-black`) or `:not([class*="bg-neo-"])` selectors so colored cards remain high-contrast (21:1) in both modes.

## Editorial / Broadsheet
Hairline rules, dense multi-column text, serif display, byline/dateline conventions from print journalism. Fits: publications, long-form, thought-leadership. Avoid: applying this density to a page with nothing to say at that density.

## Minimalism
Extreme restraint, one accent color maximum, huge whitespace, type doing almost all the work. Fits: luxury, premium single-product brands. Avoid: restraint as a substitute for a real decision — every remaining element must be precisely placed.

## Glassmorphism
Frosted-glass translucent panels, soft shadows, layered depth over a blurred background. Fits: modern consumer apps, dashboards wanting a soft/premium tech feel. Avoid: overusing blur to the point of readability loss; test contrast on every panel.

## Material-influenced
Elevation via shadow, clear touch targets, motion as spatial logic (things move the way physical objects would). Fits: cross-platform app UI, utilitarian dashboards. Avoid: importing Material's specific component shapes wholesale when the brand wants its own identity — take the principles, not the skin.

## Modern SaaS (Vercel/Linear-influenced)
Near-black or pure-white grounds, one saturated accent, monospace for data/code, tight type scale, subtle gradient accents, generous but efficient spacing. Fits: developer tools, B2B SaaS, technical dashboards, most of Kootaab/ePlusWeb-style product surfaces. Avoid: defaulting here just because the brief is "a SaaS product" — this look is common enough now to read as generic if the brand has no other point of view.

## Luxury / Editorial-Premium
Restrained palette (often near-monochrome plus one metallic or jewel accent), serif or high-contrast display type for headlines, large uncluttered imagery, slow/subtle motion. Fits: skincare/beauty, hospitality, high-end consulting/mentoring brands, premium Arabic-market positioning. Avoid: cluttering it with more than one hero message per screen; this direction fails fastest under crowding. Pairs with the premium Arabic display faces in `typography-arabic.md`.

## Calibration: defaults to avoid unless the brief asks for them
Warm-cream + terracotta-serif, near-black + single acid-green/vermilion accent, and broadsheet-hairline-columns applied regardless of subject are the three most common AI-design tells right now. Choosing one deliberately because it fits the brief is fine; landing on one by default is the failure mode `styles` exists to prevent.

## Choosing a direction
Match the brief's actual positioning and audience — don't default to Modern SaaS because it's the safest choice. State the chosen direction explicitly (in the project or to the user) before typography, motion, or any component decision runs, so downstream decisions stay consistent with it.
