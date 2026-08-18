# Command: `motion` — Animation & Interaction Design

## When to use
- The task is specifically about adding, reviewing, or fixing motion/animation/micro-interactions — independent of a broader component/section/page build.
- Also auto-loaded by `section`, `page`, and `redesign` whenever motion is in scope.

## Dispatch steps
1. Load `references/memory/motion-principles.md`.
2. If a design direction is already chosen, check the direction's motion intensity via `references/commands/styles.md` (e.g. Minimalism/Swiss call for very little motion; Modern SaaS/Glassmorphism can carry more) — don't apply a flat default across every direction.
3. Detect the target stack, then load that stack's `references/memory/stacks/*.md` file and use its "Motion" section as the mechanism — never introduce a second animation library into a project that already has one.

## No dedicated workflow file
Motion work is applied within whatever component/section/page workflow is already running. If motion is the *entire* ask with nothing else changing, this command's steps above are sufficient on their own.
