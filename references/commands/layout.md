# Command: `layout` — Select Macrostructure Layout Archetype

## When to use
- Choosing or changing the macrostructure surface blueprint for a new or existing production page/section (`fullbleed`, `editorial`, `spatial`, `interface`, `minimal`, `product`, `store`, `auto`).
- Also auto-loaded by `page`, `section`, and `redesign` when selecting structural rhythm.

## Dispatch steps
1. Load `references/memory/layout-archetypes.md`.
2. Match the product context, content density, and user goal to 1 of the 8 layout archetypes.
3. Detect the target stack, then apply the layout container pattern matching that framework (React Grid, PHP layout partials, WordPress containers, or CSS custom properties).

## No dedicated workflow file
This command is a structural decision. Once the layout archetype is selected, hand off to `page` or `section` to build or restyle the markup.
