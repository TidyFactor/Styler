# Stack: PHP (Flight / Medoo / Plates — TidyFactor PHP tracks)

## Detect
`composer.json` requiring `mikecao/flight` and/or `catfan/medoo`, `views/` or `templates/` directory of `.php` partials rendered via Plates, PocketOffice's `module.json` / `modules/` folder pattern, or Webletz's `website.json` Section/Component pattern.

## Defer to the owning skill first
This stack is governed by other TidyFactor skills with locked architecture — **read the matching one before writing anything**:
- `tidyfactor-php-micro` — small sites with the fixed 3-screen Admin Panel.
- `tidyfactor-php-kernel` — the modular-monolith Kernel/Module architecture.
- `pocketoffice-module-builder` — PocketOffice modules specifically (flat-file JSON storage, `AIService.php`, bilingual EN/AR RTL).
- `webletz-core-architecture` — Webletz's Section/Component split and `website.json` Website Document.

This skill's job is the **design decision** (layout, type, motion, direction); the file location, routing, and data-access pattern always follow whichever of the above skills owns the project. Never invent a competing file structure.

## Conventions to match
- **Templates**: Plates partials (`.php` files in `views/`), passed data via the controller — no inline `<style>`/`<script>` mixed into template logic beyond what the project already does.
- **Styling**: check the project's existing CSS approach (native CSS variables per TidyFactor convention, or Tailwind if already wired in) — match it.
- **Interactivity**: Alpine.js for component-level state (dropdowns, tabs, toggles) is the TidyFactor-track default; HTMX for partial-page updates if the project already uses it. Don't introduce a JS framework (React/Vue) into a Flight/Medoo project without explicit confirmation — that's a stack change, not a styling task.

## Motion
CSS transitions/`@keyframes`, or Alpine's built-in `x-transition` for state-driven motion (menu open/close, modal in/out) — matches what these projects already ship with.

## Arabic/RTL
Follow the owning skill's bilingual pattern exactly (PocketOffice's `$_GET['lang']`/session/cookie override chain, or Webletz's bilingual content editing model) — don't add a second i18n mechanism. That governs which language loads; CSS correctness inside the Plates templates still follows `memory/rtl-css-engineering.md` (logical properties, per-component checklist) rather than physical left/right values.
