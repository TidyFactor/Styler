# Command: `styles` — Choose a Visual Design Style / Movement

## When to use
- A project has no established visual style or direction yet, or the user explicitly wants to select or reconsider it ("what design style should this take", "does this look Swiss or more like Glassmorphism", "pick a movement for this brand").
- Auto-loaded by `page`/`redesign`/`section` when no style direction is established yet for that project.

## Dispatch steps
1. Load `references/memory/design-styles.md`.
2. Match the brief's stated audience/positioning to 1-2 candidate directions — never present all of them as equally viable; narrow to the fit.
3. State the chosen direction explicitly before any other command runs against this project, so `typography`, `motion`, and every component/section/page decision downstream stays consistent with it.

## No dedicated workflow file
This is a decision, not a multi-step build. Once the direction is picked, hand off to whichever command triggered this (`page`, `redesign`, or a standalone request).
