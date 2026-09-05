# Component Matrix Registry (Production Quick-Reference)
<!-- last-verified: 2026-09-05 -->

> **Single Source of Truth (SSOT) Notice**:
> The full token schemas, detailed architectural anatomy, and SVG detailing recipes for all core UI components reside authoritatively in **`tidyfactor-design/references/memory/`** (`21-eyebrow-kicker-matrix.md` through `27-list-indicator-matrix.md`).
> This registry serves as the **operational cheat sheet and styling index** for production implementation and quality auditing inside `tidyfactor-styler`.

---

## 1. Eyebrows & Kickers (16 Alternatives)
*SSOT: `tidyfactor-design/references/memory/21-eyebrow-kicker-matrix.md`*

| # | Variant | Family | Personality | Operational CSS Selector / Token |
|---|---------|--------|-------------|----------------------------------|
| 01 | Uppercase Kicker | Containerless | Luxury / Editorial | `.eyebrow-kicker` (tracking: 0.12em; uppercase) |
| 02 | Numbered Index | Containerless | Structured / Swiss | `.eyebrow-index` (counter / `01 —`) |
| 03 | Monospace Annotation | Containerless | Dev-native | `.eyebrow-mono` (`//` or `$`) |
| 04 | Slash Category Path | Containerless | Archival | `.eyebrow-slash` (`CAT / SUBCAT`) |
| 05 | Ghost Chip | Minimal Container | Refined / Quiet | `.chip-ghost` (1px subtle border) |
| 06 | Hard-Edge Tag | Minimal Container | Brutalist / Bold | `.tag-hard` (border-radius: 0) |
| 07 | Status Dot Indicator | Minimal Container | Live / Active | `.badge-status` (pulsing 8px dot) |
| 08 | Highlight Marker | Minimal Container | Warm / Human | `.marker-highlight` (linear-gradient underline) |
| 09 | Rule-Kicker Lockup | Structural | Classic Print | `.lockup-rule` (horizontal inline rule) |
| 10 | Inline Border Accent | Structural | Institutional | `.accent-border-start` (`border-inline-start: 3px`) |
| 11 | Icon Lockup | Structural | Functional | `.eyebrow-icon` (16px icon + text gap: 8px) |
| 12 | Vertical Rail Label | Structural | Avant-garde | `.rail-label` (writing-mode: vertical-rl) |
| 13 | Corner Ribbon | Expressive | Promotional | `.ribbon-corner` (clip-path / 45deg) |
| 14 | Rotating Stamp Seal | Expressive | Crafted / Heritage | `.stamp-seal` (circular text badge) |
| 15 | Marquee Strip | Expressive | Energetic | `.eyebrow-marquee` (infinite scroll ticker) |
| 16 | Hand-Drawn Accent | Expressive | Personal | `.accent-drawn` (SVG underline draw) |

---

## 2. Hero Motion Architecture (8 Choreographies)
*SSOT: `tidyfactor-design/references/memory/22-hero-section-matrix.md`*

| # | Variant | Motion Signature | SVG Technique | Personality |
|---|---------|-----------------|---------------|-------------|
| 01 | Kinetic Split-Type | Char stagger + rise | Scribble stroke-draw | Confident SaaS |
| 02 | Scribble Signature | Scrub line-drawing | `getTotalLength` + dashoffset | Editorial / Human |
| 03 | Text-Mask Scene | Parallax inside type | `<clipPath>` + `<image>` | Bold Agency |
| 04 | Organic Blob | Turbulence drift | `feTurbulence` + `feDisplacementMap` | Warm / Spatial |
| 05 | Aurora Grain | Drifting gradient mesh | Radial mesh + noise filter | Ambient Luxury |
| 06 | Orbit Field | Counter-rotation system | SVG groups (`+θ / -θ`) | Networked Tech |
| 07 | Blueprint Wireframe | Pinned scrub draw | Dashed strokes + measure tags | Dev-Tool / Infra |
| 08 | Pinned Horizontal | Scroll → X corridor | Panel dividers + rules | Product Showcase |

*Rule:* Every hero must combine exactly **1 entrance**, **1 scroll behavior**, and **1 ambient layer**.

---

## 3. Cards & Containers (16 Alternatives)
*SSOT: `tidyfactor-design/references/memory/23-card-architecture-matrix.md`*

| # | Variant | Family | Personality | CSS & Structural Architecture |
|---|---------|--------|-------------|-------------------------------|
| 01 | Double-Hairline Frame | A. Editorial | Archival | Concentric 1px hairlines with 4px gap (`::after`) |
| 02 | Passe-Partout Inset | A. Editorial | Museum | Mat board padding (24px) around recessed viewport |
| 03 | Museum Plaque Card | A. Editorial | Solid | Rigid plate with corner fixing pips/screws |
| 04 | Border-Fade Vignette | A. Editorial | Ethereal | CSS `mask-image: radial-gradient(...)` border fade |
| 05 | Low-Relief Debossed Stone | B. Tactile | Ancient | Dual inset shadow (`inset 2px 2px`, `inset -2px -2px`) |
| 06 | Beveled Chiseled Edge | B. Tactile | Industrial | 45° highlight border-top/start + shadow border-bottom/end |
| 07 | Frosted Obsidian Slab | B. Tactile | Sovereign Glass | `backdrop-filter: blur(28px) saturate(180%)` |
| 08 | Textured Papyrus Card | B. Tactile | Scholarly | Low-opacity (0.04) SVG `feTurbulence` grain overlay |
| 09 | Book-Spine Asymmetric | C. Architectural | Literary | Gutter spine (`writing-mode: vertical-rl`) + main content |
| 10 | Chamfered Notched Corner | C. Architectural | Cybernetic | `clip-path: polygon(...)` 45° corner cut |
| 11 | Cantilevered Accent Bar | C. Architectural | Modernist | Beam overhanging container by 8–12px |
| 12 | Layered Step-Elevation | C. Architectural | Dimensional | Background offset tier (`transform: translate(6px, 6px)`) |
| 13 | Crosshair Reticle HUD | D. Data-Dense | Telemetry | Corner `+` reticles at all 4 vertices |
| 14 | Status Telemetry Rail | D. Data-Dense | Operational | Top header rail with status LED + metric ticker |
| 15 | Terminal Window Box | D. Data-Dense | Authentic | macOS/Linux terminal bar with control pips |
| 16 | Expandable Drawer Card | D. Data-Dense | Interactive | Summary card with accessible `<div hidden>` tray |

---

## 4. Buttons & CTAs (16 Alternatives + 8 States)
*SSOT: `tidyfactor-design/references/memory/24-button-cta-matrix.md`*

| # | Variant | Family | Personality | Interaction Key |
|---|---------|--------|-------------|-----------------|
| 01 | Mechanical Depressable Key | Tactile | Physical | `box-shadow: 0 4px 0 ...` collapses to 0 on active |
| 02 | Hairline Ghost + Pip | Tactile | Minimalist | 1px border with colored indicator dot |
| 03 | Chamfered Action Block | Tactile | Industrial | 45° cut corners with directional arrow |
| 04 | Dual-Tone Split Button | Tactile | Operational | Primary action zone + dropdown chevron zone |
| 05 | Gliding Arrow Lockup | Editorial | Elegant | Embedded arrow translates 6px on hover |
| 06 | Underline Drawer | Editorial | Fine Print | 2px underline expands outward from center |
| 07 | Monospace Bracketed | Editorial | Dev-native | `[ ACTION // → ]` with terminal bracket styling |
| 08 | Circled Icon Anchor | Editorial | Modern | Floating circle vector + text link |
| 09 | Wax Seal Trigger | Authority | Sovereign | Circular seal stamp embedded on trailing side |
| 10 | Royal Cartouche Pill | Authority | Heritage | Gold border + micro emblem jewel |
| 11 | Embossed Low-Profile Tab | Authority | Institutional | Slight raised bevel + tactile depress |
| 12 | Monochrome Contrast Slab | Authority | Brutalist | Solid black/white invert on hover |
| 13 | Status Dot Live Trigger | Dynamic | Real-time | Pulsing green dot (1.8s loop) |
| 14 | Magnetic Glow Button | Dynamic | Immersive | Cursor-following ambient radial glow |
| 15 | Border-Beam Shimmer | Dynamic | High-Attention | Rotating hairline light streak along border |
| 16 | Split-Text Roll Over | Dynamic | Playful | Dual-text vertical roll on hover |

*Rule:* Every button must support the **8 states**: Default, Hover, Focus-Visible (≥ 3:1), Active/Pressed, Disabled, Loading (`aria-busy`), Cooldown, Error/Success.

---

## 5. Section Transitions & Dividers (Volume 03 — 12 Alternatives)
*SSOT: `tidyfactor-design/references/memory/25-divider-separator-matrix.md`*

| # | Variant | Family | Motion | SVG / CSS Technique | Perf Cost |
|---|---------|--------|--------|---------------------|-----------|
| 01 | Parametric Wave | Static Topology | None | Generated cubic wavePath token | ●○○ |
| 02 | Diagonal Cut | Static Topology | None | `preserveAspectRatio="none"` polygon | ●○○ |
| 03 | Corner Notch | Static Topology | None | CSS `clip-path: polygon(...)` | ●○○ |
| 04 | Scallop Perforation | Static Topology | None | CSS `radial-gradient` tiling (0.5px AA ring) | ●○○ |
| 05 | Morphing Wave | Scroll-Reactive | Scrub (0.6) | `attr: { d }` path interpolation (same cycles) | ●●○ |
| 06 | Draw-On Seam | Scroll-Reactive | Scrub (0.5) | Dashed stroke-draw + milestone nodes (prepDraw) | ●●○ |
| 07 | Rising Edge Wipe | Scroll-Reactive | Scrub (0.5) | `clip-path: inset()` radius collapses to 0 | ●●○ |
| 08 | Scaling Crest | Scroll-Reactive | Once | `scaleY` unfold from bottom baseline (expo.out) | ●○○ |
| 09 | Sticky Overlap Stack | Layer Overlap | Scrub | CSS `position: sticky;` + `.panel__inner` scale | ●●○ |
| 10 | Curtain Split Wipe | Layer Overlap | Pinned scrub | Dual 50.5% panels `xPercent: ±102` (LOUD) | ●●● |
| 11 | Color-Field Crossfade | Atmospheric | Toggle tween | `backgroundColor` morph on scroll thresholds | ●○○ |
| 12 | Rule + Index Divider | Editorial | Once | Hairline blooms outward from section number | ●○○ |

*Core Invariants:*
1. **Ownership Rule**: The seam belongs to the **incoming** section — filled with *its* background color (`fill="var(--bg)"`).
2. **Subpixel Hairline Fix**: Every SVG divider must enforce `display: block; margin-bottom: -1px;`.
3. **Energy Budget**: Max **one LOUD transition** per page (Curtain, Stack, Rising Edge). Everything else stays quiet.


---

## 6. Metrics & Stat Counters (12 Alternatives)
*SSOT: `tidyfactor-design/references/memory/26-metrics-stat-matrix.md`*

| # | Variant | Key Characteristic | Operational Rule |
|---|---------|--------------------|------------------|
| 01 | Superscript Precision Stat | Golden typographic ratio | Currency/unit superscripted to cap height (0.42em) |
| 02 | Circular Telemetry Arc | Radial SVG gauge | 240° open arc with `stroke-dasharray` |
| 03 | Split Target Benchmark Bar | Linear goal meter | Actual vs target comparative bar |
| 04 | Micro-Bento Stat Box | Compact status card | Metric + trend chip + live pulse dot |
| 05 | Calligraphic Heritage Monument | Monumental numerals | High-contrast serif / Eastern Arabic numerals |
| 06 | Monospace Telemetry Block | Terminal readout | `[098.4% OPTIMAL]` tabular format |
| 07 | Before / After Delta Pill | Comparative growth | Baseline vs result badge (`+34%`) |
| 08 | Trend Sparkline Lockup | Micro-chart pairing | Numerals directly above inline vector sparkline |
| 09 | Fractional Milestone Counter | Ratio display | `08 / 12` milestone ratio with progress fill |
| 10 | Pedigree Year Badge | Archival seal | `EST. 1984` gold-rimmed heritage badge |
| 11 | Radial Segmented Ring | HUD arc steps | Segmented 8-part stage indicator |
| 12 | Comparison Column Stat | Side-by-side delta | Traditional method vs optimized platform |

*Rule:* Always apply `font-variant-numeric: tabular-nums;` to prevent layout jittering during count-ups.

---

## 7. List Indicators & Trust Bullets (12 Alternatives)
*SSOT: `tidyfactor-design/references/memory/27-list-indicator-matrix.md`*

| # | Variant | Marker Shape | Best Use Case |
|---|---------|--------------|---------------|
| 01 | Diamond Lozenge | Geometric `◆` / `◇` | Luxury, jewelry, high-end editorial |
| 02 | Editorial Gliding Dash | Typographic `—›` | Long-form narratives, essays |
| 03 | Monospace Step Index | Tabular `01.`, `02.` | Tech documentation, step-by-step setup |
| 04 | Status Beacon Dot | Radiant colored dot | Operational SLAs, live feature flags |
| 05 | Key-Value Accent Bar | 3px `border-inline-start` | Enterprise feature lists, clean grids |
| 06 | Shield / Crest Insignia | 14px vector shield | Legal, medical, cybersecurity trust |
| 07 | Chevron Rail Pointer | Directional `›` | Roadmaps, progression items |
| 08 | Crosshair Plus Pip | Technical `+` | System specifications, hardware |
| 09 | Chamfered Check Box | 18px angular vector box | Modern SaaS checkout / pricing |
| 10 | Hyphen-Bullet Classic | Em-dash `—` | Academic bibliographies, notes |
| 11 | Dual-Tone Arrowhead | Overlapping vector arrows | Velocity, transformation metrics |
| 12 | Roman Sequence | Roman `I.`, `II.`, `III.` | Governance, contracts, protocol terms |

*Rule:* Always align markers with `align-items: baseline;` or `flex-start` (never `center` on multi-line text). Always flip directional arrows in RTL (`[dir="rtl"]`).
