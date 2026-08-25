# Workflow: Existing Page Redesign — One Outcome

Outcome: one already-shipping page, overhauled end-to-end to a confirmed design direction, with every section and component on it brought to the same standard — not just the parts that were visibly bothering the user.

## Steps

0. **Step 0 One-Line Design Read & Decision Points Resolution**: Declare the page redesign's core design intent in a single sentence. Configure the 3-Dial System (`designVariance`, `motionIntensity`, `visualDensity`). Resolve decision points per `memory/decision-points.md` (check `.tidyfactor/design-brief.md` first; preserve existing direction silently unless explicit overhaul requested).
1. **Audit the page as it exists today** against `memory/quality-bar.md` before changing anything — know what's actually wrong, not just what prompted the request.
2. **Confirm the target design direction** (`styles`) from `.tidyfactor/design-brief.md` or prompt override — a full-page redesign without an agreed direction produces internally inconsistent output.
3. **Confirm the target stack's conventions** from `memory/stacks/*.md`, and if it's a TidyFactor production track, its own architecture constraints take precedence over any generic assumption here.
4. **Work section by section**, applying the `section-redesign` discipline to each region of the page, reusing/extending the project's existing component library rather than inventing a parallel one.
5. **Apply typography (incl. Arabic if relevant) and motion consistently across the whole page** — a redesign where the hero got the new direction and the footer didn't is unfinished.
6. **Run Pre-Emit Self-Critique (1-5 Scoring on 7 Axes)**: Score the proposed page redesign on Philosophy (P), Hierarchy (H), Execution (E), Specificity (S), Restraint (R), Variety (V), and Decision Alignment (D). Any score < 3 triggers an immediate revision pass. Stamp the output header/comment: `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`.
7. **Enforce Mechanical Pre-Flight Checks**: Verify eyebrow cap (`ceil(sectionCount / 3)`), hero top padding cap (`pt-24`), single-line CTAs, optical alignment, and zero AI anti-patterns or interchangeable UI components.
8. **Re-check every section at mobile and desktop widths together**, not just individually — a redesign can fix each section in isolation and still misalign in the full-page flow (spacing rhythm, color balance, motion pacing across sections).

## Validation checklist
- [ ] Step 0 Design Read & Decision Points resolved per `memory/decision-points.md`
- [ ] Pre-redesign audit against `quality-bar.md` was done and specific issues identified, not just "make it nicer"
- [ ] Design direction confirmed explicitly via brief, prompt, or preserved baseline
- [ ] Every section on the page reflects the same direction/typography/motion — no inconsistent leftover sections
- [ ] Existing component library reused/extended, not duplicated
- [ ] Pre-Emit Self-Critique (7 Axes P/H/E/S/R/V/D) executed and stamped (`/* Pre-emit critique: ... */`)
- [ ] Mechanical pre-flight checks verified (eyebrow cap, hero top padding cap `pt-24`, single-line CTAs, optical alignment)
- [ ] If a TidyFactor production track, its architecture constraints were respected throughout
- [ ] Full page re-checked at mobile and desktop widths as a whole, not just section-by-section
- [ ] If Arabic/bilingual, applied consistently across every section
- [ ] Passes `memory/quality-bar.md`

