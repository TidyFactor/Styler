# Command: `brief` — Design Brief Elicitation & Project Baseline Cache

## When to use
- Starting a new project or onboarding `tidyfactor-styler` to an existing repository.
- User explicitly runs `/brief`, "create design brief", "set up project styles", "حدد اختيارات التصميم للمشروع", or "interview me for design direction".
- Resolves all 5 key decision points (D1-D5) in one structured pass and caches answers in `.tidyfactor/design-brief.md` so subsequent commands execute without friction.

## Dispatch steps
1. Check if `.tidyfactor/design-brief.md` already exists. If yes, present current brief and ask whether to view, update specific fields, or regenerate completely.
2. Load `references/memory/decision-points.md`.
3. Load `references/workflows/brief.md`.
4. Execute the brief workflow and write out `.tidyfactor/design-brief.md`.
