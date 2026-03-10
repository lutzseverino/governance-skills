# Workflow

## Order Of Operations

1. Identify the change kind before changing structure.
Classify the task with one `primary change kind`: `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, or `new feature slice`. Add `secondary change kinds` only when they materially change scope, extraction, or validation.

2. Choose the smallest correct scope.
Decide what must change to satisfy the request and what should remain untouched. Do not widen the change just because nearby code could also be improved. Make any contract surface touched by the change explicit. If the change affects a contract surface, escalate or confirm that broader consequence before applying the contract-change policy.

3. Choose the extraction outcome only after the scope is clear.
Decide whether the change should stay `inline`, become a `local helper`, move into a `local module`, or become a `boundary`. After extraction, keep the boundary at the nearest ownership level first. Prefer extracting pure local logic before sharing code that carries side effects or orchestration.

4. Materialize the change using the dominant convention in the touched area.
Preserve local naming, file placement, entrypoint, dependency, side-effect, and validation conventions when they are clearly established in the area you are changing.
Do not replace an acceptable local stack pattern with a technically cleaner alternative unless the existing pattern is materially harmful, directly blocks the change, or the request explicitly includes standardization.

5. Match validation depth to the blast radius.
Meet the minimum validation floor for the change kind and blast radius, then add more coverage only when the risk requires it.

6. Escalate instead of guessing when the consequence is wider than the request.
Ask before changing public contracts, promoting code into broader ownership with unclear placement, standardizing a mixed area, or making a high-risk change without credible validation.

## Default Sequence

When in doubt, follow this default sequence:

1. classify the change kind
2. keep the scope local and make any contract surface explicit
3. keep code `inline` unless clarity or ownership clearly improves with extraction
4. keep extracted code at the nearest ownership level first
5. preserve the local convention in the touched area
6. keep an acceptable local stack pattern unless the task or the current harm clearly justifies breaking from it
7. meet the minimum relevant validation floor
8. escalate only when the wider consequence is real and unclear

## Common Failure Modes

- widening a `direct fix` into unrelated cleanup
- forcing mixed work into one label and losing the real source of risk
- treating a `local refactor` as justification for new shared abstractions
- extracting code only to reduce file length or satisfy a style preference
- widening a contract surface when an internal seam would suffice
- sharing orchestration code before the underlying logic has a stable local shape
- replacing an acceptable local stack pattern with a cleaner but disruptive one
- standardizing a mixed area without being asked
- changing behavior and calling it a refactor
- skipping escalation when public contracts or broader ownership are affected
