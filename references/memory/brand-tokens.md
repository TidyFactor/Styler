# Brand Tokens — `brand.json` Single Source of Truth

When a project contains a `brand.json` file at its root, it serves as the single source of truth for colors, typography, identity, voice, and visual tokens. `tidyfactor-styler` respects existing `brand.json` definitions over ad-hoc component styles.

## 1. Token Ingestion Matrix

| `brand.json` Property | CSS Custom Property Target | Tailwind Config Alias | Stack Ingestion |
|---|---|---|---|
| `colors.primary` | `--brand-primary` | `colors.primary` | Global CSS / Tailwind theme |
| `colors.secondary` | `--brand-secondary` | `colors.secondary` | Global CSS / Tailwind theme |
| `colors.accent` | `--brand-accent` | `colors.accent` | Global CSS / Tailwind theme |
| `colors.background` | `--brand-bg` | `colors.bg` | Layout container defaults |
| `colors.surface` | `--brand-surface` | `colors.surface` | Card / Modal surfaces |
| `typography.fontFamily.arabic.heading` | `--font-ar-heading` | `font.arHeading` | Heading components |
| `typography.fontFamily.arabic.body` | `--font-ar-body` | `font.arBody` | Body / Paragraph components |
| `typography.fontFamily.latin.heading` | `--font-en-heading` | `font.enHeading` | Latin heading components |
| `typography.fontFamily.latin.body` | `--font-en-body` | `font.enBody` | Latin body components |
| `shape.borderRadius` | `--radius-brand` | `borderRadius.brand` | Button & Card corners |

## 2. Ingestion Rules across Stacks

1. **React / Next.js**:
   - Check `tailwind.config.js` or `app/globals.css`. Map `brand.json` values to CSS variables (`var(--brand-primary)`) or Tailwind theme extensions (`bg-primary`).
2. **PHP (Flight / Medoo / TidyFactor Track)**:
   - Map tokens directly to CSS variables inside the global layout stylesheet (e.g. `public/css/brand.css` or `assets/css/style.css`).
3. **WordPress (Elementor / Gutenberg / Classic)**:
   - Register tokens in `theme.json` (`settings.color.palette`, `settings.typography.fontFamilies`) or theme root CSS custom properties.
4. **Plain HTML/CSS/JS**:
   - Declare at `:root` level in primary CSS file.

## 3. Fallback Hierarchy

```
Existing brand.json -> Existing Project CSS/Tailwind -> Default TidyFactor Tokens
```

If `brand.json` is missing, inspect existing CSS/Tailwind configs first. Never invent a second parallel color or typography variable if one already exists in the codebase.
