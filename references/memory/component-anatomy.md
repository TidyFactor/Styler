# Component Anatomy — Reference for `component`/`section`/`page`
<!-- last-verified: 2026-08-30 -->

## Atomic hierarchy (Atomic Design, adapted)
- **Atoms** — button, input, label, icon, badge. Smallest named unit, never composed of other named components.
- **Molecules** — a form field (label + input + error text), a stat (label + value + trend), a nav item (icon + label + active state).
- **Organisms** — a card, a data table, a navbar, a pricing tile, a modal. Composed from atoms/molecules, still one reusable named unit.
- **Templates** (`page`/`redesign` output) — organisms arranged into an actual page layout. The one level allowed to be page-specific — it's arrangement, not new styling.

A new visual need almost always belongs at the atom/molecule/organism level, added once to the project's existing component library — not invented fresh at the template level.
 
---

## Navigation & Header Styling Invariants (Strict Quality Bar)
1. **Zero Emoji Invariant**: Emojis are strictly banned from navigation menus, headers, and buttons. Use lightweight inline SVGs (`currentColor`, 1.5–2px stroke).
2. **Single-Line Menu (`white-space: nowrap`)**: Navigation links must never wrap to multiple lines on desktop. Labels should be concise (1–2 words) or use stacked title + sub-descriptor.
3. **Mobile-First Drawer Maintenance**: Seamlessly fold into an accessible drawer or bottom sheet on mobile screens with $\ge 44\times 44\text{px}$ touch targets and locked body scroll.
4. **Submenu & Mega Menu Fallback**: When links exceed 5–6 items, escalate cleanly to structured submenus or a mega menu rather than crowding the header bar.
5. **Action Controls Cap (Max 3)**: Limit header actions to 3 cohesive controls (e.g. Primary CTA + Lang Toggle + Theme Toggle).

---

## The 8-State Interactive Component Matrix

Every interactive component (button, card, input, dropdown, tab, modal trigger) must define explicit styles for all applicable states — never relying on browser default fallbacks:

| State | Trigger / Condition | Visual & A11y Requirement |
|---|---|---|
| **1. Default** | Resting state | Base tokens (color, border, radius, shadow) |
| **2. Hover** | Mouse cursor over element | Smooth transition (150–250ms), contrast shift, elevation/border change |
| **3. Focus-Visible** | Keyboard navigation (`Tab`) | Visible outline / ring (WCAG AA ≥ 3:1 contrast), `outline-offset` |
| **4. Active / Pressed** | Mouse down / Clicked | Pressed scale (`scale(0.98)`), inset shadow, active token |
| **5. Disabled** | `disabled` attribute / `aria-disabled` | Reduced opacity (`opacity-50`), `pointer-events-none`, clear disabled visual |
| **6. Loading** | Asynchronous action in progress | Spinner / Skeleton pulse, text hidden or replaced, `aria-busy="true"` |
| **7. Empty** | No data / results present | Friendly empty state vector/microcopy, actionable reset CTA |
| **8. Error / Success** | Validation feedback | High contrast error/success tokens, inline message with icon + `aria-invalid` |

## Naming discipline
One canonical name per real pattern. A "featured pricing card" and a "testimonial card" sharing 90% of their structure should be one component with modifiers, not two components that quietly diverge over time.

## When something looks like it needs a new component but doesn't
If the only difference from an existing component is a token value (a different accent color, a different size), that's a modifier/variant, not a new component. New components are for genuinely different structure/behavior.

## Reuse-before-create is mandatory
Before designing anything new for a `component`, `section`, or `page` task, inventory what the target project already has. Production work compounds inconsistency fast if every task quietly adds a near-duplicate component instead of extending the existing one.

---

## Master Component Pattern Registry (Production Quick-Reference)
For operational tables, token selectors, and anti-cliché variants across all 7 core component families, consult:
- [`component-matrix-registry.md`](file:///c:/wamp64/www/TidyFactor/Skills/Skills-LAB/tidyfactor-styler/references/memory/component-matrix-registry.md)

*Architectural Single Source of Truth (SSOT)*: Full token schemas, deep SVG detailing, and design foundations are maintained authoritatively in `tidyfactor-design/references/memory/` (`21-` through `27-`).


