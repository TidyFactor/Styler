# RTL CSS Engineering — Reference for `rtl`

Building a real RTL system, not sprinkling `direction: rtl` and hoping. The target: **direction-agnostic components** — written once, correct in both directions automatically — not separate LTR and separate RTL stylesheets maintained in parallel forever.

## The core shift: physical → logical properties
Physical properties (`left`, `right`, `margin-left`, `padding-right`, `top-left` radius) hardcode a direction. Logical properties describe position relative to text flow, and flip automatically when `direction` changes:

| Physical (avoid) | Logical (use) |
|---|---|
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` |
| `padding-left` / `padding-right` | `padding-inline-start` / `padding-inline-end` |
| `left` / `right` (positioning) | `inset-inline-start` / `inset-inline-end` |
| `top` / `bottom` | `inset-block-start` / `inset-block-end` |
| `border-left` / `border-right` | `border-inline-start` / `border-inline-end` |
| `border-top-left-radius` | `border-start-start-radius` |
| `text-align: left` | `text-align: start` |
| `float: left` / `float: right` | avoid float for layout entirely — see Flexbox/Grid below |
| `width` shorthand margins (`margin: 0 10px 0 0`) | write each side explicitly with logical properties — shorthand physical margins are the most common silent RTL bug |

Any new component/section/page written by this skill uses logical properties by default — not as an RTL-specific pass applied afterward. Retrofitting physical→logical on redesign of an existing LTR-only codebase is itself a legitimate, scoped task (see `component-redesign.md`/`section-redesign.md`, applied here).

## `direction` and `unicode-bidi`
- `direction: rtl` on the root (`<html dir="rtl">` is preferable to CSS-only — it also fixes native browser behavior like scrollbar side and form control alignment that CSS `direction` alone doesn't).
- `unicode-bidi: isolate` (or `plaintext`) on any element whose content's actual direction may differ from its container — critical for a Latin brand name, a URL, or a numeral run embedded inside Arabic RTL flow, preventing the bidi algorithm from reordering surrounding punctuation incorrectly.
- A dedicated `dir="ltr"` span (not just CSS) is more reliable than `unicode-bidi` alone for genuinely mixed content like `"السعر: 120 EGP فقط"` — wrap the Latin/numeral fragment.

## Flexbox and Grid — RTL is close to free here
- Flexbox: `flex-direction: row` already reverses visually under `dir="rtl"` automatically — don't hardcode `row-reverse` to "fix" RTL, that breaks it back to LTR-looking order. Only use `row-reverse` for a genuine reversed sequence independent of language direction.
- Grid: `grid-template-columns` order follows `direction` automatically for logical placement; explicit `grid-column: 1 / 2` numeric placement does not auto-flip — prefer named grid areas or `dir`-aware placement over hardcoded column numbers where the visual order must mirror.

## Per-component RTL checklist
Re-verify each of these individually when a component/section/page ships Arabic — a global mirror does not correctly handle all of them:
- **Modals/Drawers**: a drawer that slides from the physical "right" in LTR must slide from the *logical end* in RTL (visually the left) — animate `inset-inline-end`, not `right`.
- **Tables**: header alignment follows `text-align: start`; a numeric/data column that's conventionally right-aligned in LTR usually stays *numeral-aligned to the same visual side project-wide* — decide once and apply consistently, don't let each table auto-flip independently.
- **Forms**: label position, input `text-align: start`, validation icon position (inline-end, not hardcoded right), required-field asterisk position.
- **Navigation**: menu items follow logical order; a mega-menu dropdown's open-direction (does it grow toward inline-start or inline-end from its trigger) needs explicit checking, not assumed.
- **Data visualization**: chart axis direction, legend position, and tooltip anchor side don't automatically mirror via CSS `direction` (most charting libraries lay out in a fixed coordinate system) — verify per library; Arabic-Indic vs Western numerals on axis labels is a separate decision (see `typography-arabic.md`).
- **Icons**: directional icons (back/next arrow, chevron, undo/redo, play/skip) must mirror; non-directional icons (search, settings gear, trash) must NOT be mirrored — mirroring a search-icon magnifying glass looks visibly wrong. Audit icon-by-icon, don't apply a blanket `transform: scaleX(-1)` to an entire icon set.
- **Animations**: any motion with directional meaning (slide-in-from-side, progress bar fill direction) follows logical direction, not a hardcoded translateX sign — see `motion-principles.md` for the motion decision itself, this file governs its RTL correctness.

## Mixed-direction content (bidi)
Arabic body text containing an English brand name, a URL, a hashtag, or a numeral run is normal, not an edge case — plan for it from the start:
- Numerals inside Arabic text do not reverse (`120` stays `120`, never `021`) — the bidi algorithm handles this correctly by default; the risk is CSS/JS that manually reverses strings, which breaks numerals.
- A predominantly-Latin technical term embedded in Arabic UI copy (e.g., a product/feature name kept in English by brand convention) should be wrapped for isolation per the `unicode-bidi`/`dir="ltr"` guidance above, especially near Arabic punctuation, to prevent punctuation reordering artifacts.

## Validation
Before calling any Arabic/bilingual output finished: toggle `dir` and re-check the per-component checklist above item by item in the actual target stack's rendering — not just confirmed visually "looks mirrored," which misses icon-direction and animation-direction mistakes specifically.
