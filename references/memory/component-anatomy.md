# Component Anatomy — Reference for `component`/`section`/`page`

## Atomic hierarchy (Atomic Design, adapted)
- **Atoms** — button, input, label, icon, badge. Smallest named unit, never composed of other named components.
- **Molecules** — a form field (label + input + error text), a stat (label + value + trend), a nav item (icon + label + active state).
- **Organisms** — a card, a data table, a navbar, a pricing tile, a modal. Composed from atoms/molecules, still one reusable named unit.
- **Templates** (`page`/`redesign` output) — organisms arranged into an actual page layout. The one level allowed to be page-specific — it's arrangement, not new styling.

A new visual need almost always belongs at the atom/molecule/organism level, added once to the project's existing component library — not invented fresh at the template level.

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
