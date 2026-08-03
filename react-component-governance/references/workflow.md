# Workflow

Use this order when making React component architecture decisions:

1. Inspect the immediate UI question and its architectural context.
Check nearby boundaries, repeated behavior, packaging, ownership, and conventions. Decide whether the problem is isolated or reveals a credible wider React architecture problem.

2. Open a decision gate only when materially different outcomes are credible.
If both a local answer and a wider React architecture option are supported by repository evidence, explain their boundary, affected surface, ownership or packaging consequence, upside, and cost. Recommend one and wait for the user's choice unless the user already expressed a preference or delegated the decision.

3. Start with extraction.
Decide whether the UI should stay `inline`, become a `local helper`, become a `component boundary`, or become another boundary kind.

4. If the extracted boundary is a `component boundary`, choose one primary role.
Classify the component as `presentational`, `interactive`, or `container`.

5. If the extracted boundary is not a `component boundary`, classify the boundary kind instead.
Use one of these:

- `headless behavior boundary`
- `provider/infrastructure boundary`
- `support boundary`

6. Check boundary cases before finalizing downstream decisions.
Use special guidance for providers, pages, form coordinators, and loading or error shells before finalizing classification, packaging, or ownership.

7. Add optional patterns only when they strengthen the chosen role.
Patterns such as `compound`, `headless hook plus UI shell`, and `slot-based or polymorphic` are modifiers, not replacements for responsibility.

8. Decide packaging.
Make the public API boundary and local file ownership obvious. Apply a selected convention-setting outcome across its coherent React area rather than leaving contradictory partial examples.

9. Decide ownership.
Keep code in the narrowest scope that fully owns its reason to change unless the selected wider outcome and repository evidence establish broader ownership.
If a broader owner is appropriate but the correct broader owner is not clear from the repo structure, ask the user before promoting the boundary.

## Decision Outcome Rule

Do not force a primary component role onto boundaries whose main value is:

- reusable behavior with no required UI shell
- infrastructure or context wiring
- local support for another owner such as loading or error handling

Do not omit a credible wider React architecture option merely because an inline or local extraction can solve the immediate request. Do not present speculative reuse or unrelated cleanup as a wider option.
