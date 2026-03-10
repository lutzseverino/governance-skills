# Workflow

## Order Of Operations

1. Identify the change kind before changing structure.
Classify the task as a `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, or `new feature slice`. Different change kinds have different defaults for scope, extraction, and validation.

2. Choose the smallest correct scope.
Decide what must change to satisfy the request and what should remain untouched. Do not widen the change just because nearby code could also be improved.

3. Choose the extraction outcome only after the scope is clear.
Decide whether the change should stay `inline`, become a `local helper`, move into a `local module`, become an `owned boundary`, or be promoted into a `shared boundary`.

4. Materialize the change using the dominant convention in the touched area.
Preserve local naming, file placement, entrypoint, and validation conventions when they are clearly established in the area you are changing.

5. Match validation depth to the blast radius.
Choose the smallest credible verification that still covers the actual risk of the change.

6. Escalate instead of guessing when the consequence is wider than the request.
Ask before changing public contracts, promoting code into broader ownership with unclear placement, standardizing a mixed area, or making a high-risk change without credible validation.

## Default Sequence

When in doubt, follow this default sequence:

1. classify the change kind
2. keep the scope local
3. keep code `inline` unless clarity or ownership clearly improves with extraction
4. preserve the local convention in the touched area
5. run the most targeted credible validation available
6. escalate only when the wider consequence is real and unclear

## Common Failure Modes

- widening a `direct fix` into unrelated cleanup
- treating a `local refactor` as justification for new shared abstractions
- extracting code only to reduce file length or satisfy a style preference
- standardizing a mixed area without being asked
- changing behavior and calling it a refactor
- skipping escalation when public contracts or broader ownership are affected
