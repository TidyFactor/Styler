# Stack: WordPress

## Detect
`wp-content/themes/` or `wp-content/plugins/` directory, `functions.php`, `style.css` with a WordPress theme header comment, or the user names a WordPress site/client directly. **Also check for a page builder before assuming classic/block theme conventions apply** — `wp-content/plugins/elementor/`, `wp-content/plugins/js_composer/` (WPBakery), or Divi's `et_` prefixed options are common on agency client sites and change the entire editing model below.

## If the site uses a page builder (Elementor / Divi / WPBakery)
The visible page is assembled from builder widgets/sections stored as serialized data (Elementor: `_elementor_data` post meta; Divi: shortcodes in post content), not plain template PHP. Redesign work here means:
- Editing through the builder's own section/column/widget structure — don't hand-write markup that bypasses it, the client's own editing access depends on the builder structure staying intact.
- Custom CSS goes in the builder's own custom-CSS field (per-element or theme-wide, whichever the project already uses) or the child theme's stylesheet — not scattered inline styles.
- Global colors/fonts: Elementor's Site Settings (Global Colors/Fonts) or Divi's Theme Customizer options are the project's actual token system here — read and reuse them rather than hardcoding new hex values, same discipline as `theme.json` on a block theme.
- Confirm which builder before touching anything — Elementor and Divi structures are not interchangeable, and editing one page's structure as if it were the other will visibly break it for the client's own future edits.

## Conventions to match (classic/block themes, no page builder)
- **Classic theme**: edit the actual template files (`front-page.php`, `page-*.php`, template parts in `template-parts/`) following the theme's existing template hierarchy — don't bypass it with a one-off custom page unless the theme already does that for similar cases.
- **Block theme (FSE)**: edit `theme.json` for tokens (colors, typography, spacing presets) and block templates/patterns in `templates/`/`parts/` — don't hardcode styles that `theme.json` should own.
- **Styling**: enqueue via `wp_enqueue_style`/`wp_enqueue_script` in `functions.php` — never inline `<style>`/`<script>` in a template file. If the theme uses a build step (webpack/vite for the theme's own assets), follow it rather than adding raw unbundled files.
- **Content editing surfaces**: if the client edits content via ACF fields or the block editor, a redesign must keep those fields/blocks functional — a visual redesign that breaks the client's own editing workflow isn't done.
- **Child themes**: if the project uses a child theme, edit the child theme, never the parent, even for a "just fix this one page" request.

## Motion
Plain CSS transitions/`@keyframes` in the theme's enqueued stylesheet, or the block editor's built-in animation attributes for Gutenberg-native blocks — avoid adding a JS animation library to a WordPress theme unless the project already has one loaded.

## Arabic/RTL
WordPress ships `is_rtl()` and auto-loads a `rtl.css` if present in the theme — use that mechanism (add/extend `rtl.css`) rather than inline RTL overrides scattered through the main stylesheet. A WPML/Polylang-managed multilingual site should have its language-switch mechanism respected, not duplicated. Write `rtl.css` itself using logical properties per `memory/rtl-css-engineering.md` rather than a parallel set of hardcoded left/right overrides — that's what turns `rtl.css` into a permanently-diverging second stylesheet instead of a thin, low-maintenance override layer.
