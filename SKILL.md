---
name: tidyfactor-styler
description: "Production framework styler and surgical RTL UI polish engine with Contextual Decision Layer (CDL). Operates directly inside existing codebases across React/Next.js, PHP, WordPress, and Vanilla HTML/CSS/JS. Trigger on commands 'brief', 'component', 'section', 'page', 'redesign', 'typography', 'palette', 'layout', 'rtl', 'motion', 'styles', or requests for UI polishing and RTL refactoring."
---
# TidyFactor Styler (Production Design — Any Stack)

A command dispatcher for production-stage visual/interaction design work performed **inside a real, already-existing codebase**. Unlike `tidyfactor-design` (which builds a standalone, zero-build clickable prototype under its own locked `design-system/` folder), this skill never invents its own architecture — it reads the target stack's existing conventions and produces output that belongs there.

## What this is, precisely

The deliverable is always one of: a new component, a new section, a new page, or a redesign of an existing component/section/page — written in the target codebase's actual language and conventions (JSX+Tailwind for a Next.js app, a Plates partial for a TidyFactor PHP Micro project, a WordPress block/template/page-builder structure, or plain HTML/CSS/JS for a static site). The design judgment (typography, motion, design-style direction, and — as this skill's deepest specialization — Arabic/RTL correctness) is stack-agnostic and shared across all of it.

**Arabic/RTL Execution Requirement.** Any component, section, or page carrying Arabic content must implement `memory/rtl-css-engineering.md` and `memory/typography-arabic.md` — enforcing direction-agnostic logical properties CSS, letterform-aware font sizing, and Arabic-native layout structure.

**When this is the right tool vs. others:**
- Exploring a direction fast, before real content/data exists, as a standalone clickable demo → `tidyfactor-design`.
- Scaffolding a brand-new project's folder structure and stack from zero → the matching track skill (`tidyfactor-html`, `tidyfactor-next`, `tidyfactor-php`).
- Documenting codebase architecture, API specifications, or generating a Docsify site → `tidyfactor-doc`.
- Building, auditing, or refactoring skills according to master governance rules → `tidyfactor-skill-architect`.
- Styling, restyling, or adding to something that **already exists and already ships** → this skill.

## Commands

| User intent | Command | What it loads |
|---|---|---|
| "Establish design brief / project baseline" | `references/commands/brief.md` | `workflows/brief.md` + `memory/decision-points.md` |
| "Redesign/create this component" | `references/commands/component.md` | `workflows/component-create.md` **or** `workflows/component-redesign.md` + `memory/component-anatomy.md` + `memory/decision-points.md` + matching `memory/stacks/*.md` |
| "Redesign/restyle this section" | `references/commands/section.md` | `workflows/section-create.md` **or** `workflows/section-redesign.md` + `memory/layout-archetypes.md` + `memory/nav-footer-catalog.md` + `memory/decision-points.md` + matching `memory/stacks/*.md` |
| "Build a new production page" | `references/commands/page.md` | `workflows/page-create.md` + `memory/layout-archetypes.md` + `memory/nav-footer-catalog.md` + `memory/decision-points.md` + matching `memory/stacks/*.md` |
| "Redesign this existing page" | `references/commands/redesign.md` | `workflows/page-redesign.md` + `memory/layout-archetypes.md` + `memory/nav-footer-catalog.md` + `memory/quality-bar.md` + matching `memory/stacks/*.md` |
| "Select layout archetype / macrostructure" | `references/commands/layout.md` | `memory/layout-archetypes.md` + matching `memory/stacks/*.md` |
| "Select navigation (N1–N9) & footer (Ft1–Ft8)" | `references/commands/nav-footer.md` | `memory/nav-footer-catalog.md` + `memory/typography-arabic.md` + `memory/rtl-css-engineering.md` |
| "Pick/pair typography, incl. Arabic" | `references/commands/typography.md` | `memory/typography-arabic.md` |
| "Extract color palette & WCAG AA contrast" | `references/commands/palette.md` | `memory/brand-tokens.md` + `memory/asset-tooling.md` |
| "Asset hygiene & image optimization" | `references/commands/assets.md` | `memory/asset-tooling.md` + `memory/quality-bar.md` |
| "Fix/build RTL correctness" | `references/commands/rtl.md` | `workflows/rtl-audit-fix.md` + `memory/rtl-css-engineering.md` |
| "Add/review motion and interaction" | `references/commands/motion.md` | `memory/motion-principles.md` |
| "Choose a design direction / style movement" | `references/commands/styles.md` | `memory/design-styles.md` |

Read only the command file that matches the request. A command loads its workflow (if it has one) and its listed memory files — nothing else, until the workflow itself calls for more. `component`, `section`, `page`, and `redesign` additionally load `memory/rtl-css-engineering.md` and `memory/typography-arabic.md` whenever the target carries Arabic/bilingual content.

## Non-negotiable constraints (every command)

1. **Detect before designing.** Before producing any output, identify the target stack (React/Next.js, PHP Flight/Medoo, WordPress, or plain HTML/CSS/JS) from the files the user shows or names. If it's ambiguous, ask — never guess and silently pick one.
2. **Conform, don't compete.** Match the existing codebase's naming, file layout, and styling approach (Tailwind classes if the project uses Tailwind, the project's existing CSS methodology if not, the project's existing component patterns). Never introduce a second, parallel styling system into a codebase that already has one.
3. **If the target stack is a TidyFactor production track** (PHP Micro, PHP Kernel, Webletz Core, tidyfactor-html) **its locked architecture wins.** This skill supplies the design decision (layout, type, motion, color); it never overrides that skill's file/module contract. Read that skill's own SKILL.md constraints before writing into its codebase.
4. **Component and section redesigns are scoped.** A component redesign touches only that component's definition and its own usages — never neighboring components. A section redesign touches only that section's markup/styles — never global nav, footer, or unrelated sections. Scope creep is a failure, not thoroughness.
5. **Arabic / RTL First-Class Integration.** If the content is Arabic or bilingual, typography and layout decisions must be configured for Arabic at launch (`typography-arabic.md`) using logical-properties CSS (`rtl-css-engineering.md`), applying the per-component checklist for icons, modals, tables, and animations.
6. **Brand Single Source of Truth.** If `brand.json` is present at the project root, read `memory/brand-tokens.md` and map tokens directly into CSS variables or Tailwind theme configs.
7. **Every deliverable passes `memory/quality-bar.md` before being called finished.**

Compatible with Antigravity, Claude Code, OpenAI Codex, and OpenCode.