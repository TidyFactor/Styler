# Workflow: Component Redesign — One Outcome

Outcome: one existing reusable component, redesigned in place, in the target stack's own conventions, with all its usages still working.

## Steps

0. **Step 0 One-Line Design Read & Decision Points Resolution**: Declare the component redesign's core design intent in a single sentence. Configure the 3-Dial System (`designVariance`, `motionIntensity`, `visualDensity`). Resolve decision points per `memory/decision-points.md` (check `.tidyfactor/design-brief.md` first; preserve existing direction silently unless explicit overhaul requested).
1. **Locate the component.** Find its actual definition (the JSX component, the Plates partial, the WordPress template part, the CSS class + markup pattern). If the user only described it verbally, find or confirm the real file before touching anything.
2. **Find every usage.** A component redesign that breaks 3 of its 12 call sites isn't done. List where it's used before changing its interface/props/markup shape.
3. **Classify it** against `memory/component-anatomy.md`'s atomic hierarchy (atom / molecule / organism). This determines how much it's allowed to compose vs. how self-contained it must stay.
4. **Apply the project's existing design direction** (check for an established `styles` choice; if none exists and this component is highly visible/brand-defining, run `styles` first rather than guessing).
5. **Define the full state matrix** for anything interactive: default → hover → focus-visible → active/pressed → disabled, plus loading/empty/error/success where relevant. Skipping states is the most common way a "redesigned" component still looks unfinished.
6. **Run Pre-Emit Self-Critique (1-5 Scoring on 7 Axes)**: Score the proposed component redesign on Philosophy (P), Hierarchy (H), Execution (E), Specificity (S), Restraint (R), Variety (V), and Decision Alignment (D). Any score < 3 triggers an immediate revision. Stamp the output header/comment: `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`.
7. **Enforce Mechanical Pre-Flight Checks**: Verify optical alignment, single-line CTAs, non-generic typography, and ensure zero AI anti-patterns or interchangeable UI components.
8. **Write the output in the target stack's own idiom** (see the loaded `memory/stacks/*.md` file) — matching naming conventions, file location, and styling approach already used in that codebase.
9. **Update every usage site** found in step 2 to match any interface change.

## Validation checklist
- [ ] Step 0 Design Read & Decision Points resolved per `memory/decision-points.md`
- [ ] Component's real definition file was found and edited (not a guess/duplicate created alongside it)
- [ ] Every existing usage site still renders correctly with the new definition
- [ ] Full interactive state matrix is present, not just default+hover
- [ ] Pre-Emit Self-Critique (7 Axes P/H/E/S/R/V/D) executed and stamped (`/* Pre-emit critique: ... */`)
- [ ] Mechanical pre-flight checks verified (optical alignment, single-line CTAs, zero AI anti-patterns)
- [ ] Output matches the target stack's existing naming/file/styling conventions — no second styling system introduced
- [ ] If Arabic/bilingual content is involved, `typography-arabic.md` rules were applied, not retrofitted
- [ ] Passes `memory/quality-bar.md`

