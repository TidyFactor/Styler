# Stack: React / Next.js

## Detect
`package.json` with `react`/`next` dependency, `.jsx`/`.tsx` files, `app/` or `pages/` directory (Next.js router).

## Conventions to match, not invent
- **Styling**: check what the project already uses before choosing — Tailwind utility classes (most common in Kootaab-style projects), CSS Modules (`Component.module.css`), or styled-components. Never introduce a second styling approach into a project that already picked one.
- **Component files**: PascalCase filename matching the exported component (`PricingCard.tsx`), colocated with its styles if CSS Modules, functional components with hooks — no class components in new/redesigned code unless the codebase is entirely class-based already.
- **Routing**: Next.js App Router (`app/<route>/page.tsx`) is the default for new pages in a modern (13+) Next project; Pages Router (`pages/<route>.tsx`) only if the project is already on it — check `next.config` / existing folder before assuming.
- **Props/variants**: use a `variant`/`size` prop pattern (e.g. via `class-variance-authority` if already present, or a simple prop-to-class map) for component modifiers — matches the "modifier, not new component" rule in `component-anatomy.md`.

## Motion
Framer Motion (`framer-motion`) if already a dependency — `motion.div` with `initial`/`animate`/`whileInView` for staged entrances/scroll-reveals. If not present, plain CSS transitions/`@keyframes` rather than adding a new animation dependency without confirming with the user first.

## Arabic/RTL
Set `dir="rtl"` at the layout/root level for Arabic locales; Tailwind's logical properties (`ps-4`/`pe-4` instead of `pl-4`/`pr-4`) if the project's Tailwind version supports them, so spacing mirrors automatically. This covers the stack mechanism only — run the full `memory/rtl-css-engineering.md` per-component checklist (icons, modals, dropdowns, animations) before calling any Arabic component/page done; Tailwind's logical utilities handle spacing, not icon direction or animation direction.

## When the target is Kootaab or another Next+Supabase project
Confirm the project's existing data-fetching pattern (Server Components vs. client-side Supabase calls) before adding a new component that needs data — match it, don't introduce a third pattern.
