# Workflow: New Production Page — One Outcome

Outcome: one new page/route/view added to an already-existing, already-shipping project, indistinguishable in quality/consistency from the pages already there.

## Steps

0. **Step 0 One-Line Design Read & Decision Points Resolution**: Declare the page's core design intent in a single sentence. Configure the 3-Dial System (`designVariance`, `motionIntensity`, `visualDensity`). Resolve decision points (D1-D5) per `memory/decision-points.md` (check `.tidyfactor/design-brief.md` first).
1. **Confirm the established design direction** for this project (`styles`) and its typography (`typography`) before writing anything. A new page that doesn't match the project's existing pages is a defect, not a fresh take.
2. **Confirm the target stack's routing/file convention** from `memory/stacks/*.md` — where new pages live, how they're registered/routed, what the project's own naming pattern is.
3. **If the target is a TidyFactor production track** (PHP Micro/Kernel, Webletz, tidyfactor-html), defer to that skill's own page/module contract — this workflow supplies the design, that skill's rules govern the file structure and registration.
4. **Compose from existing components/sections first.** Check what the project already has in its component library before designing anything new; a "new page" is usually mostly-existing-parts arranged in a new order, not all-new components.
5. **Design any genuinely new sections/components needed**, following `component-anatomy.md` and the project's established direction.
6. **Apply Arabic/bilingual typography from the start** if relevant — not retrofitted after an English-first draft.
7. **Apply motion consistent with the established direction.**
8. **Run Pre-Emit Self-Critique (1-5 Scoring on 7 Axes)**: Score the proposed page layout on Philosophy (P), Hierarchy (H), Execution (E), Specificity (S), Restraint (R), Variety (V), and Decision Alignment (D). Any score < 3 triggers an immediate revision pass. Stamp the output header/comment: `/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */`.
9. **Enforce Mechanical Pre-Flight Checks**: Verify eyebrow cap (`ceil(sectionCount / 3)`), hero top padding cap (`pt-24`), single-line CTAs, optical alignment, and zero AI anti-patterns or interchangeable UI components.
10. **Wire the page into the project's actual navigation/routing** — a page that exists but isn't reachable isn't done.

## Validation checklist
- [ ] Step 0 Design Read & Decision Points resolved per `memory/decision-points.md`
- [ ] Matches the project's established design direction and typography — not a fresh, unrelated take
- [ ] Uses the target stack's actual routing/file convention (confirmed, not assumed)
- [ ] If a TidyFactor production track, its own page/module contract was followed
- [ ] Existing components/sections reused before new ones were built
- [ ] Any new components follow `component-anatomy.md`'s naming/state discipline
- [ ] Pre-Emit Self-Critique (7 Axes P/H/E/S/R/V/D) executed and stamped (`/* Pre-emit critique: ... */`)
- [ ] Mechanical pre-flight checks verified (eyebrow cap, hero top padding cap `pt-24`, single-line CTAs, optical alignment)
- [ ] Height/spacing checked at mobile and desktop, no unjustified viewport overflow
- [ ] Page is actually wired into navigation/routing, not orphaned
- [ ] If Arabic/bilingual, `typography-arabic.md` applied from the start
- [ ] Passes `memory/quality-bar.md`

