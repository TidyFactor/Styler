# Workflow: Section Create — One Outcome

Outcome: one new bounded page section (hero, pricing block, testimonials, etc.), added to a page, without touching anything outside its boundary.

## Steps

0. **Step 0 One-Line Design Read & Decision Points Resolution**: Declare the section's core design intent in a single sentence. Configure the 3-Dial System (`designVariance`, `motionIntensity`, `visualDensity`). Resolve decision points per `memory/decision-points.md` (check `.tidyfactor/design-brief.md` first).
1. **Confirm where it's being inserted** — the exact position in the page's real markup/component tree, and what sections it sits between.
2. **Inventory existing components available to it.** A section is composed of organisms/molecules that likely already exist elsewhere in the project (cards, buttons, forms) — reuse and extend them via `memory/component-anatomy.md`'s discipline before creating new ones.
3. **Apply the project's established design direction** (from `styles`, or confirm one exists before proceeding on a highly visible section).
4. **Handle layout at the viewport level, not just desktop.** Section height/spacing must hold up at mobile and desktop widths without forcing scroll inside the section itself — use fluid spacing, not fixed px.
5. **Apply motion if in scope** per `memory/motion-principles.md`, matching the direction's intensity.
6. **Run Pre-Emit Self-Critique (1-5 Scoring on 7 Axes)**: Score the proposed section on Philosophy (P), Hierarchy (H), Execution (E), Specificity (S), Restraint (R), Variety (V), and Decision Alignment (D). Any score < 3 triggers an immediate revision pass. Stamp the output header/comment: `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`.
7. **Enforce Mechanical Pre-Flight Checks**: Verify eyebrow cap (`ceil(sectionCount / 3)`), hero top padding cap (`pt-24`), single-line CTAs, optical alignment, and zero AI anti-patterns or interchangeable UI components.
8. **Write the output in the target stack's own idiom.**
9. **Confirm nothing outside the new section's boundary changed** as a side effect of inserting it (spacing on neighboring sections, nav/footer untouched).

## Validation checklist
- [ ] Step 0 Design Read & Decision Points resolved per `memory/decision-points.md`
- [ ] Insertion point confirmed in the real markup before building
- [ ] Existing components reused where they already cover the need; new components added only for genuinely new structure
- [ ] Section height/spacing checked at mobile and desktop widths — no unjustified viewport overflow
- [ ] Motion (if any) matches the established direction's intensity
- [ ] Pre-Emit Self-Critique (7 Axes P/H/E/S/R/V/D) executed and stamped (`/* Pre-emit critique: ... */`)
- [ ] Mechanical pre-flight checks verified (eyebrow cap, hero top padding cap `pt-24`, single-line CTAs, optical alignment)
- [ ] Output matches the target stack's existing conventions
- [ ] If Arabic/bilingual, `typography-arabic.md` applied from the start
- [ ] Nothing outside the new section's boundary was touched
- [ ] Passes `memory/quality-bar.md`

