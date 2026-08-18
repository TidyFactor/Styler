# Command: `typography` — Font Pairing & Type Decisions (incl. Arabic)

## When to use
- The task is specifically about choosing/pairing/auditing fonts — for a brand, a page, or a component — independent of building anything yet.
- Also auto-loaded by `component`, `section`, `page`, and `redesign` whenever the content is Arabic or bilingual.

## Dispatch steps
1. Load `references/memory/typography-arabic.md` — covers both Latin and Arabic type decisions, including premium/luxury Arabic display options and pairing rules.
2. If a design direction is already chosen for the project, cross-check the pairing against `references/commands/styles.md`'s design movement rules — type choice should reinforce the direction, not fight it.

## No dedicated workflow file
This command is a lookup + decision, not a multi-step build — it doesn't need its own workflow file. If the request grows into "and now build the page using this type system," hand off to `page` or `redesign`.
