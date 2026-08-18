# Stack: Plain HTML / CSS / JS (existing static sites)

## Detect
Flat `.html` files with linked `.css`/`.js`, no framework/build dependency in play, no `package.json` with a frontend framework — a site that already exists and ships as static files (as opposed to a brand-new static site being scaffolded, which is `tidyfactor-html`'s job, not this skill's).

## Conventions to match
- **Structure**: follow whatever the existing site already does — a shared `styles.css`/`design-system/` folder if it has one, or per-page styles if that's genuinely how it was built (don't impose a shared-system refactor as a side effect of a redesign task the user didn't ask for).
- **If the site already follows the `tidyfactor-html` track's shared design-system convention** (`design-system/tokens.css`, `base.css`, `components.css`), extend those files — don't add page-local CSS that would break that track's consistency guarantee.
- **JS**: vanilla JS modules if that's the existing pattern; don't introduce a framework dependency into a static site as part of a component/section redesign — that's a stack migration, a different, much bigger task the user would need to ask for explicitly.

## Motion
CSS transitions/`@keyframes` and `IntersectionObserver` for scroll-reveal — the standard no-dependency approach these sites already use.

## Arabic/RTL
`dir="rtl"` on `<html>` for Arabic pages/locale variant, mirrored per the site's existing bilingual pattern (separate localized pages vs. a single toggle) — match what's already there rather than picking a new pattern. Author the CSS itself with logical properties per `memory/rtl-css-engineering.md` so the same stylesheet serves both directions rather than a maintained-forever separate RTL file.
