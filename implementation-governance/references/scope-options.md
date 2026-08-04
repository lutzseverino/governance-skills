# Scope Options Policy

## Default Rule

Inspect before narrowing. Determine whether the immediate request is isolated or reveals a deeper problem that deserves an explicit implementation option.

Do not choose a narrow solution merely because it can satisfy the literal request. Do not choose a broad solution merely because adjacent code can be improved.

Treat code health as a consequence of the implementation decision, not as a separate horizon or a blanket reason to refactor.

## Solution Horizons

### `contained`

Solve the requested problem safely while preserving the surrounding architecture and conventions.

Use when the issue is isolated, the current owner remains appropriate, or the evidence does not justify broader change.

### `structural`

Solve the requested problem and correct the local design condition that caused or amplified it.

Use when the affected area has a missing or harmful convention, confused responsibility, repeated workaround, unstable seam, or dependency problem that can be corrected within a coherent local area.

### `foundational`

Solve the problem by reshaping broader ownership, contracts, dependencies, or architecture and establish a durable project-level direction.

Use when the problem crosses owners or layers, the current architecture repeatedly produces the same failure, or a coherent migration would leave the project materially simpler and more consistent.

## Opportunity Scan

Surface a structural or foundational option when repository evidence shows one or more of these:

- the same defect, workaround, or special case appears across multiple owners
- the current ownership or dependency direction contributes directly to the problem
- prior local fixes have created repeated churn or contradictory behavior
- a contained implementation would add another exception, duplicated rule, or hard-to-test path
- the requested change is awkward because a stable seam or convention is missing
- nearby code shows an incomplete or conflicting architectural direction
- the current task already touches the seam whose repair would make future changes materially safer or cheaper
- a broader change would remove substantially more complexity, defect risk, or future change cost than it introduces

Name the evidence. A general preference for cleaner code is not sufficient.

## Material Code-Health Threshold

Treat a code-health difference as material when all of these are credible:

- **task-connected**: the condition exists in the same owner, seam, dependency path, or convention involved in the request
- **diagnosed**: current code shows concrete complexity, fragility, contradictory behavior, ownership ambiguity, weak testability, or repeated change friction
- **durable**: the broader option would improve correctness, comprehension, ownership, consistency, testability, or future change cost beyond the immediate edit
- **proportionate**: the durable benefit is meaningful relative to migration burden, compatibility risk, implementation cost, and validation cost
- **actionable**: the broader option has a coherent affected surface and a credible migration and validation path

Do not require an existing production defect when the contained change would clearly deepen an observed harmful pattern. Do require more than hypothetical reuse, stylistic preference, or the possibility that adjacent code could be cleaner.

When these conditions hold, make the quality difference visible to the user rather than silently optimizing for minimum initial effort.

## Decision Gate

Present a scope choice before implementation when all of these are true:

- at least two horizons are credible
- the options differ materially in code health, future change cost, defect risk, affected surface, ownership, contracts, migration burden, validation, or architectural precedent
- the user's requested horizon is not already clear

Include only credible options; two are usually enough. For each option, state the pursued outcome, affected surface, diagnosed code-health condition it corrects or leaves in place, durable upside, cost or risk, and why acting now or deferring is reasonable. Recommend one and explain why.

Wait for the user's selection before editing even when one option is clearly recommended. When the conditions above hold, prefer opening the gate over silently choosing `contained`.

Treat delegation as explicit only when the user authorizes the agent to choose the solution horizon, scope, or architecture. General permission to implement, fix, proceed, use initiative, or make the appropriate change delegates implementation execution, not a materially different quality or scope outcome. If the user explicitly delegates the horizon decision, choose the recommended option and continue.

Do not open the decision gate when the task is trivial, only one credible approach exists, the quality difference is immaterial or speculative, the wider idea is unrelated cleanup, or the user already selected a horizon.

## Calibration Examples

- Fix an isolated conditional with no repeated pattern or ownership concern: choose `contained` and continue without a menu.
- Add another special case to a flow already split across contradictory validators: present `contained` and `structural`, recommend based on the diagnosed health cost, and wait.
- Change behavior that repeatedly fails across service boundaries because ownership is misplaced: present the credible narrower and `foundational` outcomes when a coherent migration exists, then wait.
- Notice unrelated duplication near a routine edit: do not open the gate unless it meets the material code-health threshold.

## Lock The Selected Horizon

After selection:

- define the intended outcome and coherent affected surface
- name important non-goals
- choose the smallest complete change that fulfills that horizon
- do not silently collapse back to `contained` during implementation
- do not expand beyond the selected horizon without new evidence and another explicit decision when consequences materially change

Treat the horizon as the user's desired intervention level. Treat file scope, ownership, extraction, contracts, and validation as implementation decisions made inside it.
