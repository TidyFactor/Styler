# Motion Principles — Reference for `motion`

Adapted from classic animation principles, applied to UI motion. Stack-agnostic — the target stack's own mechanism (see `memory/stacks/*.md`) is how these get implemented.

## Staging
One focal change communicated at a time. Five cards revealing simultaneously reads as noise; the same five staggered by ~60-80ms each reads as a considered sequence.

## Anticipation
A small pre-state before a bigger change helps the eye track it (a button's subtle scale-down before a transition, a skeleton before content pops in) — used sparingly, not on every interaction.

## Ease-out for entrances, ease-in for exits
Things entering should decelerate into place; things leaving should accelerate away. Using the same easing for both reads as mechanical.

## Follow-through / slight overshoot
A very small overshoot-and-settle on entrance reads as more alive than a purely linear arrival — subtle only; easy to overdo into "bouncy" and undermine a restrained direction like Minimalism or Swiss.

## Secondary motion
A primary element moving can carry a small, delayed secondary motion (a shadow settling a beat later, an accent trailing slightly) — this is what separates orchestrated motion from everything moving in lockstep.

## Restraint is a choice, driven by direction
An orchestrated single moment usually lands harder than scattered effects everywhere; excess ambient animation is one of the strongest tells of AI-generated design. Motion intensity follows the chosen `design-styles.md` direction — Minimalism and Swiss want very little; Modern SaaS and Glassmorphism can carry more; Luxury/Editorial-Premium wants slow, deliberate motion, never snappy/playful easing.

## Stack-Native Implementation Mechanisms

Match the target stack's established motion pattern — never introduce a redundant animation library into a project:

| Target Stack | Primary Motion Mechanism | Lightweight Alternative | A11y Fallback (`prefers-reduced-motion`) |
|---|---|---|---|
| **React / Next.js** | Framer Motion (`framer-motion`) | Tailwind `transition-*` / CSS modules | `useReducedMotion()` hook / CSS media query |
| **PHP (Flight / TidyFactor)** | Alpine.js `x-transition` | Native CSS keyframes / CSS transitions | `@media (prefers-reduced-motion: reduce)` |
| **WordPress** | Interactivity API / Native CSS | GSAP (if already enqueued by theme) | `@media (prefers-reduced-motion: reduce)` |
| **Plain HTML/CSS/JS** | Native CSS Animations + Web Animations API | GSAP 3.12 (if CDN present) | `@media (prefers-reduced-motion: reduce)` |

## `prefers-reduced-motion` Mandatory Pattern
Every custom animation or transition must include a reduced-motion fallback:

```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## Performance — production-specific
Animate only `transform` and `opacity` wherever possible — these run on the compositor without triggering layout/paint. Animating `width`, `height`, `top`/`left`, or `box-shadow` spread causes layout thrashing. Use `transform: scale()` or `transform: translate3d()` instead.

## Always required
- `prefers-reduced-motion` compliance on every animated interaction across all stacks.
- Never introduce a second animation library/mechanism into a codebase that already has one — extend what's there.
