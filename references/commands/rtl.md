# Command: `rtl` — RTL CSS Engineering

## When to use
- The task is specifically about building or fixing RTL correctness — logical properties, mirroring, bidi text handling, a component that "looks wrong in Arabic," converting a physical-CSS codebase to direction-agnostic.
- Also auto-loaded by `component`, `section`, `page`, and `redesign` whenever the target carries Arabic/bilingual content — RTL correctness is not optional/separate from those outcomes, it's part of what "done" means for Arabic work.

## Dispatch steps
1. Determine which outcome this is:
   - RTL correctness **is the entire ask** (standalone fix/audit/conversion) → load `references/workflows/rtl-audit-fix.md`.
   - RTL work is happening **as part of** a `component`/`section`/`page`/`redesign` task already in progress → no separate workflow; apply `rtl-css-engineering.md`'s checklist within that workflow's own steps.
2. Load `references/memory/rtl-css-engineering.md`.
3. Detect the target stack, then load that stack's `memory/stacks/*.md` file for its logical-properties support level (e.g. confirm the project's Tailwind version supports logical utilities before assuming `ps-`/`pe-` classes exist).
4. If the task also involves font/type decisions (not just layout direction), also load `references/memory/typography-arabic.md`.

## No separate standard section
The bar this command holds work to is already stated once, in `SKILL.md`'s non-negotiable constraint 5 and in `rtl-css-engineering.md` itself — not repeated here.
