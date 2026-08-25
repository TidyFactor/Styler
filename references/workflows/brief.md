# Workflow: Design Brief Elicitation — One Outcome

Outcome: a validated, project-wide `.tidyfactor/design-brief.md` baseline file that locks D1–D5 choices, allowing subsequent component, section, and page commands to run silently and consistently without re-asking settled decisions.

## Steps

0. **Inspect Existing Baseline**: Check `brand.json`, existing CSS/Tailwind config, and existing component structure to pre-fill detected defaults.
1. **Batch Unresolved Decisions**: Extract D1 (Style), D2 (Typography), D3 (Layout), D4 (Motion), and D5 (Density) per `memory/decision-points.md`.
2. **Present Single-Round Elicitation**: Output the structured decision block presenting top 2–3 options for each unresolved decision, with 1 recommended default and concrete rationale. Halt and wait for user reply.
3. **Format & Write Brief**: Parse the user's responses and write `.tidyfactor/design-brief.md` with the following schema:

```markdown
# TidyFactor Design Brief

Generated: [DATE]
Project: [PROJECT_NAME]
Stack: [FRAMEWORK + CSS ENGINE]

## Confirmed Baseline
- **D1 Style Movement**: [e.g. Modern SaaS | Luxury Editorial | Swiss Utility | Neo-Brutalist]
- **D2 Typography Pairing**: [e.g. Plus Jakarta Sans + Tajawal | El Messiri + Plus Jakarta Sans]
- **D3 Layout Archetype**: [e.g. Bento Modular Grid | Split-Screen Fixed | Stacked Linear]
- **D4 Motion Approach**: [e.g. Restrained Micro (0.2s) | Narrative Scroll Reveal (0.6s) | Zero Motion]
- **D5 UI Density Scale**: [e.g. Balanced (Standard SaaS) | Compact (Data-Dense) | Expansive (Airy)]

## Stack & Bidi Constraints
- **Primary Language**: [ar | en | bilingual]
- **RTL Enforcement**: [Logical CSS properties required]
- **Token System**: [CSS Custom Properties | Tailwind v4 @theme | CVA]
```

4. **Confirm Success**: Inform user that the design brief is locked and that all downstream styling commands (`component`, `section`, `page`, `redesign`) will now execute automatically aligned to this baseline.

## Validation checklist
- [ ] Existing `brand.json` and CSS tokens inspected before asking questions
- [ ] Elicitation executed in a single batch round (no sequential questions)
- [ ] User selections accurately mapped to `.tidyfactor/design-brief.md`
- [ ] File `.tidyfactor/design-brief.md` written to disk
- [ ] Subsequent styling workflows can successfully read and honor this brief
