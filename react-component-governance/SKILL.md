---
name: react-component-governance
description: Opinionated, standalone React component architecture guidance for React projects. Use when reviewing or designing component boundaries, deciding whether UI should stay inline, become a local helper, become a component boundary, or become another boundary kind, surfacing credible wider React architecture options, classifying components as presentational, interactive, or container, applying compound, headless, or polymorphic patterns, setting packaging and ownership rules, or reasoning about providers, pages, forms, loading, and error shells.
---

# React Component Governance

Make consistent React component architecture decisions without drifting into ad hoc local conventions.

## Workflow

1. Inspect the immediate UI question and its surrounding React architecture.
Read [references/workflow.md](references/workflow.md) and [references/extraction.md](references/extraction.md) first. Check whether the local problem is isolated or reveals recurring boundary confusion, missing packaging or ownership convention, duplicated behavior, or a misplaced responsibility.

2. Surface a meaningful React architecture choice before editing.
When both a local answer and a materially different, evidence-backed wider React architecture option are credible, explain both, recommend one, and wait for the user's choice unless the user already expressed a preference or delegated the decision. Do not manufacture a wider option from unrelated cleanup.

3. Decide whether a meaningful boundary should exist at all.
Choose whether UI should stay `inline`, become a `local helper`, become a `component boundary`, or become another boundary kind.

4. Decide what kind of boundary the extraction creates.
If the result is a `component boundary`, read [references/classification.md](references/classification.md) to classify it as `presentational`, `interactive`, or `container`.
If the result is a `headless behavior boundary`, `provider/infrastructure boundary`, or `support boundary`, keep that boundary kind explicit and do not force a component role onto it.

5. Check boundary cases when the structure is not an ordinary reusable UI component.
Read [references/boundary-cases.md](references/boundary-cases.md) for providers, pages, form coordinators, and loading or error shells before finalizing classification, packaging, or ownership for those cases.

6. Add optional patterns only when they strengthen the chosen role.
Use [references/patterns.md](references/patterns.md) for `compound`, `headless hook plus UI shell`, and `slot-based or polymorphic` patterns.

7. Decide packaging and ownership.
Read [references/packaging.md](references/packaging.md) and [references/ownership.md](references/ownership.md) to determine folder shape, public API boundaries, local-first placement, and promotion rules for the chosen boundary.

## Working Rules

- Operate independently; do not require another governance skill to make React component architecture decisions.
- Choose exactly one primary role only when the extracted boundary is a `component boundary`.
- Use the canonical outcome terms consistently: `inline`, `local helper`, `component boundary`, `headless behavior boundary`, `provider/infrastructure boundary`, and `support boundary`.
- Treat patterns as optional modifiers, not as replacements for responsibility.
- Surface a wider React architecture option when repository evidence shows that the local problem comes from a recurring boundary, packaging, convention, or ownership problem.
- Require evidence for wider options; do not turn a component task into unrelated frontend cleanup.
- Prefer local scope first when no selected or clearly justified wider outcome exists. Shared abstractions must be earned by reuse or broader ownership.
- Prefer the smallest boundary that improves clarity inside the selected outcome.
- Do not treat same-owner support files on their own as evidence that a new `component boundary` is required.
- Treat flat reusable packaging as an area-level convention, not as a per-component choice inside one local owner.
- Prefer boundary-prefixed filenames for extracted support files so IDE and search discovery remain obvious.
- Adapt filesystem examples to the repo you are in. Do not assume every project uses the same folder names.

## Communicating Decisions

Before implementation, present alternatives only when the local and wider React architecture outcomes are both credible and materially different. For each option, state the boundary outcome, affected UI surface, ownership or packaging consequence, durable upside, and cost or risk. Recommend one and ask for one clear choice. Do not edit while that required choice is unresolved.

For a review or plan, make the recommended boundary outcome and any meaningful alternative visible before detailed file structure.

For a completed implementation, lead with the outcome. Then explain consequential boundary classification, optional pattern, packaging, ownership, and boundary-case decisions, followed by validation and deliberately deferred opportunities. Omit decisions that do not help the user understand the result; do not emit a fixed field dump or empty labels.

## Reference Map

Use these references directly as needed:

- [references/overview.md](references/overview.md)
- [references/workflow.md](references/workflow.md)
- [references/classification.md](references/classification.md)
- [references/extraction.md](references/extraction.md)
- [references/packaging.md](references/packaging.md)
- [references/ownership.md](references/ownership.md)
- [references/boundary-cases.md](references/boundary-cases.md)
- [references/roles.md](references/roles.md)
- [references/patterns.md](references/patterns.md)

## Not For

- generic React setup, Vite config, routing, or build tooling
- broad code-quality guidance outside UI boundary and component architecture decisions
- domain modeling outside UI boundary and component architecture decisions
