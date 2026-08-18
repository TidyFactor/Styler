# 1. Layout Archetypes — Surface Blueprints for Production Codebases

When creating or redesigning pages and sections inside an existing codebase, select one of the 8 macrostructure layout archetypes to govern visual rhythm, container hierarchy, and surface grid structure.

## Layout Archetypes Summary

| Layout Archetype | Codename | Hero / Intro Structure | Section Rhythm | Best For |
|---|---|---|---|---|
| **1. Film** | `fullbleed` | Cutout media + aura background | Fullbleed Hero → Story Sequence → Feature Grid → Testimonial → CTA | Brand stories, physical luxury products, flagships |
| **2. Story** | `editorial` | Split-screen media & typography | Split Hero → Multi-column Feature Grid → Origin Story → Specs → CTA | Editorial products, spec-heavy platforms, founder stories |
| **3. Space** | `spatial` | Wide architectural view | Spatial Hero → Grid Showcase → Location/Details → Features → CTA | Hospitality, real estate, architecture, events |
| **4. App** | `interface` | Device mockup / UI stage | App Mockup Hero → Workflow Steps → Interactive Proof → Grid → CTA | SaaS, web & mobile applications, dashboards |
| **5. Creator** | `minimal` | Centered portrait / statement | Minimal Hero → Statement Block → Work Gallery → Biography → CTA | Personal brands, digital creators, agencies |
| **6. Product** | `product` | Product focus + Price + CTA | Hero Product → Spec Sheet → Reviews Grid → FAQ → Purchase CTA | E-commerce single-product, high-conversion landing |
| **7. Store** | `store` | Banner + Category Navigation | Store Banner → Category Nav → Filter Grid → Catalog Cards → Footer | Multi-product catalog, e-commerce stores |
| **8. Auto** | `auto` | Stage vehicle / HUD gauge | Hero Stage → Spec Slider → Tech Breakdown → Gallery → CTA | Automotive, high-tech hardware, robotics |

## Framework Implementation Guidelines

1. **React / Next.js**:
   - Implement layouts using CSS Grid (`grid grid-cols-12 gap-6`) or Flexbox. Wrap sections in `<section className="relative w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">`.
2. **PHP (Flight / Medoo / TidyFactor Track)**:
   - Use semantic HTML5 layout containers (`<main>`, `<article>`, `<section class="container mx-auto">`).
3. **WordPress (Elementor / Gutenberg / Classic)**:
   - Map archetypes to Gutenberg section blocks or Elementor containers (`.e-container`).
4. **Plain HTML/CSS/JS**:
   - Use CSS custom properties for section spacing (`padding-block: clamp(4rem, 8vh, 8rem)`).
