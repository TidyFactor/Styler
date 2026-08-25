# Memory: Decision Points & Elicitation Protocol

Thin arbitration protocol for resolving high-impact design ambiguities BEFORE code generation. References existing memory catalogs as Single Source of Truth (SSOT).

<!-- TODO: audit-trigger definition, D2/D4 redesign parity refinement in Step 4 workflow hooks -->

---

## 1. Governance & Execution Rules

1. **Direct Invocation Invariant:** Skip conditions apply ONLY when decision points trigger implicitly inside composite workflows (`page`, `redesign`, `section`). When a user explicitly invokes a dedicated decision command (`/styles`, `/typography`, `/layout`, `/motion`), **ALWAYS present the options catalog from that command's SSOT memory file. Never skip an explicitly invoked command.**
2. **Redesign Zero-Regression Invariant:** In `*-redesign` workflows (`page-redesign`, `section-redesign`, `component-redesign`), the default is to **preserve the existing design direction, typography, and layout structure silently**. Do NOT trigger D1, D2, D3, or D4 in redesigns unless:
   - The user prompt explicitly requests a visual, typographic, motion, or structural overhaul (e.g. *"change the style completely"*, *"switch to luxury serif"*, *"re-architect layout"*).
   - Component audit detects severe visual or architectural fragmentation across the target element.
3. **Single-Round Batching & Priority Overflow:**
   - Maximum **3 questions** in a single round. Never ask sequential piecemeal questions.
   - **Priority Hierarchy:** `D1 (Style Movement) > D3 (Layout Archetype) > D2 (Typography Pairing) > D4 (Motion Approach) > D5 (UI Density)`.
   - **Overflow Protocol:** If $\ge 4$ decision points trigger simultaneously:
     - Batch the **top 3 priority decisions** into the single interactive question round.
     - Automatically resolve remaining lower-priority decisions to **safe conservative defaults** (e.g. Balanced density, Restrained Micro motion).
     - Explicitly state in the terminal output: `"[Auto-resolved D4/D5 to conservative defaults; override anytime]"`.
4. **Cache-First vs. Scoped One-Time Override:**
   - Always check `.tidyfactor/design-brief.md` first.
   - **One-Time Prompt Override:** Explicit instructions in the user prompt (e.g. *"Redesign this hero in Swiss style"*) override the cached brief for this single execution ONLY. Do not overwrite `.tidyfactor/design-brief.md` unless explicitly commanded (*"make this the project default"* or via `/brief`).
5. **Terminal Hard-Stop Contract:** When presenting a decision round, output the exact Markdown format in §3 and **HALT EXECUTION IMMEDIATELY**. Do not generate code, do not assume answers.

---

## 2. Decision Points Catalog (D1–D5)

### D1: Design Movement & Visual Direction
- **Trigger:** `page`, `section` (and `redesign` only if explicit overhaul requested).
- **Source of Truth (SSOT):** `memory/design-styles.md`
- **Implicit Skip Conditions (Skip if ANY is true):**
  - Prompt contains explicit style instruction (e.g. *"in Neo-Brutalist style"*).
  - `brand.json` contains a valid `designMovement` or `style`.
  - `.tidyfactor/design-brief.md` has `D1` recorded.
  - Existing codebase exhibits a dominant style signature across 3+ existing components.
- **Resolution Behavior (if NOT skipped):**
  - Read `memory/design-styles.md`.
  - Select the **top 2–3 candidate styles** best matching the detected project type (e.g. Modern SaaS, Luxury Editorial, Swiss Utility).
  - Present with one recommended default and rationale.

---

### D2: Arabic & Latin Typography Pairing
- **Trigger:** Content carries Arabic or bilingual text across `page`, `section`, `component` (and `*-redesign` only if typography change requested).
- **Source of Truth (SSOT):** `memory/typography-arabic.md`
- **Implicit Skip Conditions (Skip if ANY is true):**
  - Workflow is a standard `*-redesign` preserving existing font stack.
  - Prompt specifies explicit font families.
  - Font families are locked in project CSS / Tailwind config.
  - `brand.json` defines `typography.primary` / `typography.arabic`.
  - `.tidyfactor/design-brief.md` has `D2` recorded.
  - Target output is English-only and uses standard project font tokens.
- **Resolution Behavior (if NOT skipped):**
  - Read `memory/typography-arabic.md`.
  - Select the **top 2–3 pairings** matching content category.
  - Present with one recommended default and rationale.

---

### D3: Layout Archetype & Macrostructure
- **Trigger:** Full-page assembly under `page` (and `page-redesign` only if structural overhaul requested).
- **Source of Truth (SSOT):** `memory/layout-archetypes.md`
- **Implicit Skip Conditions (Skip if ANY is true):**
  - Command targets an isolated sub-element (`component` or single `section`).
  - Prompt specifies explicit layout structure (e.g. *"bento grid"*).
  - Workflow is standard `*-redesign` preserving existing macro-grid.
  - `.tidyfactor/design-brief.md` has `D3` recorded.
- **Resolution Behavior (if NOT skipped):**
  - Read `memory/layout-archetypes.md`.
  - Select the **top 2–3 archetypes** fitting the viewport goal.
  - Present with one recommended default.

---

### D4: Motion & Interaction Intensity
- **Trigger:** Motion integration under `page`, `section`, `component` when framework supports JS/CSS animations (and `*-redesign` only if motion change requested).
- **Source of Truth (SSOT):** `memory/motion-principles.md`
- **Implicit Skip Conditions (Skip if ANY is true):**
  - Workflow is a standard `*-redesign` preserving existing interaction pacing.
  - Stack is pure static HTML/CSS with no JS motion library installed.
  - Motion tier is locked in project CSS / `brand.json`.
  - `.tidyfactor/design-brief.md` has `D4` recorded.
- **Resolution Behavior (if NOT skipped):**
  - Read `memory/motion-principles.md`.
  - Present the 2 applicable motion tiers (e.g. Restrained Micro vs Narrative Scroll Reveal).

---

### D5: UI Density & Spacing Scale (Self-Contained)
- **Trigger:** Scaffolding dashboards, data tables, or dense application views under `page`, `section`.
- **Source of Truth (SSOT):** Self-contained in this catalog.
- **Implicit Skip Conditions (Skip if ANY is true):**
  - Target is a standard marketing landing page (defaults to standard marketing rhythm).
  - Spacing scale is already locked in `.tidyfactor/design-brief.md` or existing design tokens.
- **Options:**
  1. `Compact (Data-Dense)` — 8px/12px padding, 13px base text, tight table rows (Dashboards/Fintech/Admin).
  2. `Balanced (Standard SaaS)` — 16px/24px padding, 15px base text, 16px radius (Default B2B SaaS).
  3. `Expansive (Editorial/Luxury)` — 32px/48px padding, 17px base text, wide whitespace (Marketing, Publications).

---

## 3. Terminal Presentation Protocol (Cross-Agent Standard)

When 1–3 decision points trigger, output ONLY the following structured block and **HALT**:

```markdown
🔍 **TidyFactor Styler — Design Decisions Required**

Context Detected:
- Stack: [e.g. Next.js 16 + Tailwind v4]
- Scope: [e.g. Full-Page Creation / Arabic RTL]

Please confirm the following decisions before code generation:

### 1. Design Direction [D1]
- ⭐ **1. [Recommended] Luxury Editorial** — Best for content-led Arabic platforms with high typographic prestige.
- **2. Modern SaaS** — Clean card hierarchy, high conversion focus.
- **3. Swiss Utility** — Minimalist grid, high data density.

### 2. Layout Archetype [D3]
- ⭐ **1. [Recommended] Bento / Modular Grid** — Modern asymmetric feature showcase.
- **2. Stacked Linear** — Classic sequential conversion narrative.

---
👉 **Reply with your choices (e.g. `1, 1` or `Modern SaaS + Linear`) or provide your custom direction. Code generation will NOT proceed until you reply.**
```

---

## 4. Pre-Emit Critique Expansion (7th Axis: D)

Stamp output header with **7 Axes (P/H/E/S/R/V/D)**:
`/* Pre-emit critique: P5 H5 E4 S5 R5 V4 D5 */`

- **Axis 7: Decision Alignment (`D`)**:
  - `D5`: 100% compliant with the confirmed choices in `.tidyfactor/design-brief.md` or prompt override.
  - `D3`: Followed primary direction but drifted in secondary sections.
  - `D1`: Reverted to generic unconfirmed defaults (Immediate failure — re-generate).
