# CHANGELOG — TidyFactor Styler

All notable changes to `tidyfactor-styler` will be documented in this file.

The format is based on [Keep a CHANGELOG](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-08-29

### Added - Global Multi-Tier & Multi-Language Documentation Architecture
- **Rule 13 Implementation**: Two-tier documentation separation between Canonical Technical Documentation (`README.md` SSOT) and First-Class Market Localizations.
- **Universal Multi-Language Switcher**: Standardized 8-language switcher navigation bar across all documentation files (`EN`, `AR`, `FA`, `ES`, `PT`, `ZH`, `DE`, `FR`).
- **First-Class Localized Developer Adoption Guides**:
  - `README.es.md` (Spanish 🇪🇸): LATAM & Spain quickstart, commands, and component workflows.
  - `README.pt.md` (Portuguese 🇧🇷): Brazil developer onboarding and practical styling recipes.
  - `README.fa.md` (Persian 🇮🇷): Native RTL Persian guide for AI agents and UI engineering.
  - `README.zh.md` (Simplified Chinese 🇨🇳): Asian web developer framework styling guide.
  - `README.de.md` (German 🇩🇪): DACH enterprise design governance and precision UI polish.
  - `README.fr.md` (French 🇫🇷): Francophone agency workflow automation and UI redesign.
- **Packaging & Validation Upgrades**:
  - Registered all localized READMEs in `package.json["files"]`.
  - Updated `tools/build-skill.js` to automatically bundle all localized documentation.
  - Added automated multi-language cross-link verification to `tools/validate_skill.py`.

---

## [1.1.1] - 2026-08-25

### Fixed
- **CLI Executable & NPX Packaging**: Added `"bin"` mapping (`tidyfactor-styler`, `add-skill`, `add-styler-skill`) and included `"bin"` in the `"files"` whitelist of `package.json`, fixing the `npx @alwkala/tidyfactor-styler add-skill` execution failure (`npm error could not determine executable to run`).

---

## [1.1.0] - 2026-08-25

### Added
- **Contextual Decision Layer (CDL)**: Added `references/memory/decision-points.md` defining a thin arbitration protocol for resolving design ambiguities (D1–D5) before code generation.
- **Design Brief Command (`/brief`)**: Added `references/commands/brief.md` and `references/workflows/brief.md` for pre-flight design discovery and caching baseline decisions in `.tidyfactor/design-brief.md`.
- **Single-Round Batching & Priority Overflow**: Codified strict batching (max 3 questions per round) with priority hierarchy (`D1 > D3 > D2 > D4 > D5`) and auto-conservative defaults.
- **Direct Invocation & Zero-Regression Invariants**: Guaranteed that explicit command calls (`/styles`, `/typography`) never skip, while redesign workflows silently preserve existing baselines.
- **7-Axis Pre-Emit Self-Critique (`P/H/E/S/R/V/D`)**: Expanded pre-emit critique with Axis 7 (`D` - Decision Alignment) in `quality-bar.md` and across all 7 workflows.

---

## [1.0.1] - 2026-08-23

### Fixed
- **License Badge Consistency**: Corrected badge in `README.md` and `README.ar.md` to `Apache-2.0`, resolving legal conflict with `package.json`, `brand.json`, and `LICENSE`.
- **Portability in AGENTS.md**: Removed machine-specific Windows absolute path; replaced with relative repository root reference (`tidyfactor-styler/`).
- **Packaging Exclusions**: Updated `tools/build-skill.js` to strictly filter out `__pycache__`, `*.pyc`, `.DS_Store`, and temporary build artifacts from staged distributions.
- **Git Hygiene**: Added `.gitignore` and comprehensive `.gitattributes` to enforce uniform LF line endings and ignore bytecode/build caches.

### Added
- **One-Page Fold View Quality Guardrail**: Codified `Zero Scroll on Single-View Panels & Hero Stages` and high-density viewport enclosure inside `quality-bar.md`.
- **Neo-Brutalism Design Movement & Dark Mode Contrast Rule**: Codified tactile push buttons, saturated stickers, and WCAG AA dark-mode specificity guardrails inside `design-styles.md`.
- **Pre-Release Integrity Validator**: Added `tools/validate_skill.py` checking version synchronization across `.tidyfactor`, `package.json`, `brand.json`, and verifying command/memory links.

---

## [1.0.0] - 2026-08-22

### Added
- **Production Framework Styler Engine**: Component, section, and page redesign across React/Next.js, PHP, WordPress, and Vanilla HTML/CSS.
- **Direction-Agnostic Layout**: Logical CSS properties (`margin-inline`, `padding-inline`, `inset-inline-start`) with complete Arabic RTL support.
- **Letterform-Aware Typography**: Curated luxury Arabic & Latin typography mood pairings (Alexandria, Tajawal, Cairo, Outfit, Inter).
- **Anti-Slop Mechanical Quality Control**: 3-Dial variance tuning and pre-emit self-critique (6 axes: P, H, E, S, R, V).
- **Tooling & Distribution**: NPM binary runner, automated `.skill` builder, and cross-agent sync.
