# Workflow: Component Create — One Outcome

Outcome: one new reusable component, added to the target project's existing component library, in the target stack's own conventions.

## Steps

0. **Step 0 One-Line Design Read & Decision Points Resolution**: Declare the component's core design intent in a single sentence. Configure the 3-Dial System (`designVariance`, `motionIntensity`, `visualDensity`). Resolve decision points per `memory/decision-points.md` (check `.tidyfactor/design-brief.md` first).
1. **Confirm it doesn't already exist** under a different name — search the project's component library first. A "new" component that duplicates an existing one 90% is a naming/reuse problem, not a real gap (see `memory/component-anatomy.md`).
2. **Classify it** against `memory/component-anatomy.md`'s atomic hierarchy (atom / molecule / organism) — this determines how self-contained it must stay vs. how much it's allowed to compose.
3. **Apply the project's established design direction** (check for an established `styles` choice; run `styles` first if none exists and this component is highly visible/brand-defining).
4. **Define the full state matrix** for anything interactive: default → hover → focus-visible → active/pressed → disabled, plus loading/empty/error/success where relevant.
5. **Run Pre-Emit Self-Critique (1-5 Scoring on 7 Axes)**: Score the proposed component on Philosophy (P), Hierarchy (H), Execution (E), Specificity (S), Restraint (R), Variety (V), and Decision Alignment (D). Any score < 3 triggers an immediate revision. Stamp the output header/comment: `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`.
6. **Enforce Mechanical Pre-Flight Checks**: Verify optical alignment, single-line CTAs, non-generic typography, and ensure zero AI anti-patterns or interchangeable UI components.
7. **Write the output in the target stack's own idiom** (see the loaded `memory/stacks/*.md` file) — file location, naming, and styling approach matching what the project already does.
8. **Register it where the project expects new components to be discoverable** (export from an index file, add to a component catalog/storybook if one exists).

## Validation checklist
- [ ] Step 0 Design Read & Decision Points resolved per `memory/decision-points.md`
- [ ] Confirmed no existing component already covers this need under a different name
- [ ] Correctly classified (atom/molecule/organism) and sized accordingly
- [ ] Full interactive state matrix is present, not just default+hover
- [ ] Pre-Emit Self-Critique (7 Axes P/H/E/S/R/V/D) executed and stamped (`/* Pre-emit critique: ... */`)
- [ ] Mechanical pre-flight checks verified (optical alignment, single-line CTAs, zero AI anti-patterns)
- [ ] Output matches the target stack's existing naming/file/styling conventions
- [ ] Registered/exported the way the project expects new components to be found
- [ ] If Arabic/bilingual content is involved, `typography-arabic.md` rules were applied from the start
- [ ] Passes `memory/quality-bar.md`

