# Workflow: RTL Audit & Fix — One Outcome

Outcome: an existing component/section/page's RTL support brought to full `rtl-css-engineering.md` correctness — not just visually mirrored, every item on the per-component checklist verified individually. Use this workflow when RTL correctness *is* the entire ask ("fix the RTL on this", "this looks wrong in Arabic", "convert this to a direction-agnostic component") — for RTL work happening as part of a broader component/section/page build, this checklist still applies but is folded into that workflow's own steps instead of run standalone.

## Steps

1. **Inventory physical CSS.** Search the target file(s) for `left`/`right`/`margin-left`/`padding-right`/`float: left|right`/hardcoded `top-left`-style radii and any other physical property — this is the concrete list of what needs converting to logical properties, not a guess.
2. **Convert to logical properties** per `rtl-css-engineering.md`'s mapping table. Confirm the target stack actually supports the logical utility/property being used (check the loaded `memory/stacks/*.md` file — e.g. Tailwind's logical spacing utilities require a version that supports them).
3. **Set direction correctly at the root**, not just via a CSS override on the piece being fixed — `dir="rtl"` (HTML attribute, not CSS-only) at the appropriate layout/root level for the target stack's convention.
4. **Walk the per-component checklist** in `rtl-css-engineering.md` individually for every interactive/directional element present: icons (directional vs. non-directional), modals/drawers (slide direction), dropdowns/menus (open direction), tables (alignment), forms (label/validation position), navigation, any motion with directional meaning. Do not skip an item because "it's probably fine" — verify each.
5. **Check bidi correctness** for any mixed Arabic+Latin+numeral content — wrap embedded Latin/numeral fragments for isolation, confirm numerals aren't being manually reversed anywhere in the code.
6. **Toggle direction and re-render** to confirm the fix in the actual target stack, not just reasoned about — a logical-property change that looks correct in theory can still fail if the stack's build step or a third-party component library doesn't support it.

## Validation checklist
- [ ] All physical CSS properties in scope converted to logical equivalents (not just the ones that were visibly broken)
- [ ] `dir="rtl"` set via the HTML attribute at the correct root, not CSS-only
- [ ] Every item on `rtl-css-engineering.md`'s per-component checklist explicitly checked, not assumed from a global mirror
- [ ] Icon-by-icon audit done — directional icons flipped, non-directional icons left alone
- [ ] Mixed Arabic/Latin/numeral content bidi-isolated where present
- [ ] Actually re-rendered in the target stack with `dir="rtl"` toggled, not verified by reasoning alone
- [ ] Passes `memory/quality-bar.md`
