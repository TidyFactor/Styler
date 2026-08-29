# Contributing to TidyFactor Styler

Thank you for your interest in contributing to **TidyFactor Styler** (`@alwkala/tidyfactor-styler`)!

This repository follows strict **TidyFactor Skill Methodology** guidelines to ensure deterministic workflows, anti-slop design execution, and cross-platform compatibility across AI Coding Agents (*Google Antigravity, Claude Code, Cursor, Codex, Windsurf*).

---

## 🛠️ Development & Validation Workflow

1. **Clone & Setup**:
   ```bash
   git clone https://github.com/TidyFactor/Styler.git
   cd Styler
   ```

2. **Validate Skill Integrity**:
   Every change must satisfy the structural rules and YAML/frontmatter compliance:
   ```bash
   npm run validate
   # or: python tools/validate_skill.py
   ```

3. **Build Packages & Bundles**:
   ```bash
   npm run build
   # or: node tools/build-skill.js
   ```

---

## 🌿 Branching & Pull Requests

1. **Branch Naming**:
   - `feature/<short-name>`: New framework integrations, presets, or workflows.
   - `fix/<short-name>`: Bug fixes or validation corrections.
   - `docs/<short-name>`: Documentation, guides, or Arabic localization updates.

2. **Commit Hygiene & SemVer**:
   - Updates must synchronize version references across `.tidyfactor`, `package.json`, `brand.json`, `README.md`, and `CHANGELOG.md`.
   - Never commit ad-hoc changes without passing `npm run validate`.

3. **Submitting a Pull Request**:
   - Fill out the PR template completely.
   - Link all relevant issues.
   - Confirm automated integrity validation passes.
