# Workflow

## Order Of Operations

1. Diagnose the immediate request and inspect for a deeper problem.
Inspect enough surrounding ownership, repetition, dependency direction, convention, testability, and change friction to determine whether the problem is isolated or points to a credible structural or foundational opportunity. Identify whether a contained solution would preserve or add a material code-health problem. Do not edit yet when the solution horizon is unresolved.

2. Set the solution horizon.
Use [Scope Options Policy](./scope-options.md) to choose `contained`, `structural`, or `foundational`. Honor an explicit user preference. When materially different credible options exist and the user has not selected one, present the options, make their code-health consequences visible, and use [Decision Preview Policy](./decision-previews.md) when a compact artifact would clarify their implementation shape. Recommend one and wait before implementation. Do not treat ordinary authority to implement as authority to choose among materially different horizons.

3. Identify the change kind.
Classify the work inside the selected horizon with one `primary change kind`: `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, or `new feature slice`. Add `secondary change kinds` only when they materially change scope, extraction, or validation.

4. Choose the smallest correct scope inside the selected horizon.
Decide what must change to fulfill the selected outcome and what should remain untouched. Do not widen the change with unrelated improvements, and do not collapse a selected structural or foundational outcome back into a contained patch. Make any contract surface touched by the change explicit. When a plan would be clearer with a concrete shape, use [Decision Preview Policy](./decision-previews.md) to show one consolidated intended-shape preview for the selected horizon. If the change affects a contract surface, escalate or confirm that broader consequence before applying the contract-change policy.

5. Choose the extraction outcome only after the scope is clear.
Decide whether the change should stay `inline`, become a `local helper`, move into a `local module`, or become a `boundary`. After extraction, keep the boundary at the nearest ownership level first. Prefer extracting pure local logic before sharing code that carries side effects or orchestration.

6. Re-run the workflow inside each meaningful boundary introduced by the task.
If the task introduces or reshapes a meaningful boundary, re-run the full workflow for that unit before materializing it fully.

7. Materialize the change using local implementation rules and the applicable convention decision.
Preserve local naming, file placement, entrypoint, dependency, side-effect, and validation conventions when they are clearly established in the area you are changing.
Keep responsibilities legible, public seams narrow, dependency direction obvious, and orchestration separate from pure local logic when mixing them would blur the unit's owned responsibility or seam.
Do not replace an acceptable local stack pattern merely because another is cleaner. When the selected structural or foundational horizon deliberately establishes a missing convention or corrects a harmful one, apply that convention across the selected coherent surface.

8. Match validation depth to the blast radius.
Meet the minimum validation floor for the change kind, solution horizon, and blast radius, then add more coverage only when the risk requires it.

9. Escalate instead of guessing when the consequence exceeds the selected horizon.
Ask before changing public contracts, promoting code into broader ownership with unclear placement, standardizing an unclear area, or making a high-risk change without credible validation.

## Recursive Boundary Pass

Use a recursive boundary pass when the task:

- scaffolds a new project area, package tree, or feature slice
- introduces a new module, package, service, adapter, or public seam
- splits one owner into sub-units with different reasons to change
- turns a high-level architecture plan into concrete files, folders, or packages

At each depth, re-run the same workflow:

1. keep the selected solution horizon fixed unless new evidence materially changes it
2. classify the local change kind if it still matters at this layer
3. confirm the smallest correct local scope and any contract surface
4. decide what stays `inline`, what becomes a `local helper` or `local module`, and what deserves a `boundary`
5. materialize the chosen unit with clear responsibility, narrow seams, obvious dependency direction, and explicit orchestration shape
6. recurse again only if that decision creates another meaningful boundary
7. apply local convention, validation, and escalation rules for the unit

Use [Change Scoping Policy](./scoping.md) as the canonical stop rule for when to stop descending.

## Default Sequence

When in doubt, follow this default sequence:

1. inspect for both the immediate problem and credible deeper causes
2. determine whether a contained change would leave a material task-connected code-health problem, then choose the solution horizon or open the decision gate
3. classify the change kind
4. choose the smallest complete scope inside that horizon and make any contract surface explicit
5. keep code `inline` unless clarity or ownership clearly improves with extraction
6. keep extracted code at the nearest ownership level first
7. re-run the same governance questions for each meaningful boundary created by the task
8. materialize each unit with clear responsibility, narrow seams, and obvious dependency direction
9. preserve or deliberately establish convention according to the selected horizon
10. meet the minimum relevant validation floor
11. escalate only when a consequence beyond the selected horizon is real and unclear

## Common Failure Modes

- widening a `direct fix` into unrelated cleanup
- silently choosing a contained patch when the request exposes a credible deeper problem
- treating general permission to implement as delegation to choose a materially different scope or quality outcome
- skipping the decision gate because one credible option has a strong recommendation
- describing an architectural option without showing its consumer or boundary shape when a compact preview would clarify the decision
- flooding a scope choice with implementation bodies, boilerplate, or repeated snippets
- presenting speculative cleanup as a foundational option
- collapsing a selected structural or foundational outcome back into the smallest patch
- forcing mixed work into one label and losing the real source of risk
- treating a `local refactor` as justification for new shared abstractions
- extracting code only to reduce file length or satisfy a style preference
- stopping at top-level architecture while leaving lower-level boundaries ad hoc
- materializing a boundary with incidental coupling or mixed responsibilities inside it
- widening a contract surface when an internal seam would suffice
- sharing orchestration code before the underlying logic has a stable local shape
- replacing an acceptable local stack pattern without a selected convention-setting outcome
- changing behavior and calling it a refactor
- skipping escalation when public contracts or broader ownership are affected
