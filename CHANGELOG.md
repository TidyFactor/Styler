# CHANGELOG — TidyFactor Styler

All notable changes to `tidyfactor-styler` will be documented in this file.

The format is based on [Keep a CHANGELOG](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
