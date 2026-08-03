# Scope Options Policy

## Default Rule

Inspect before narrowing. Determine whether the immediate request is isolated or reveals a deeper problem that deserves an explicit implementation option.

Do not choose a narrow solution merely because it can satisfy the literal request. Do not choose a broad solution merely because adjacent code can be improved.

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
- the requested change is awkward because a stable seam or convention is missing
- nearby code shows an incomplete or conflicting architectural direction
- a broader change would remove more complexity than it introduces

Name the evidence. A general preference for cleaner code is not sufficient.

## Decision Gate

Present a scope choice before implementation when all of these are true:

- at least two horizons are credible
- the options differ materially in affected surface, ownership, contracts, migration burden, validation, or architectural precedent
- the user's requested horizon is not already clear

Include only credible options; two are usually enough. For each option, state the pursued outcome, affected surface, durable upside, and cost or risk. Recommend one and explain why.

Wait for the user's selection before editing. If the user explicitly delegates the decision, choose the recommended horizon and continue.

Do not open the decision gate when the task is trivial, only one safe approach exists, the wider idea is unrelated cleanup, or the user already selected a horizon.

## Lock The Selected Horizon

After selection:

- define the intended outcome and coherent affected surface
- name important non-goals
- choose the smallest complete change that fulfills that horizon
- do not silently collapse back to `contained` during implementation
- do not expand beyond the selected horizon without new evidence and another explicit decision when consequences materially change

Treat the horizon as the user's desired intervention level. Treat file scope, ownership, extraction, contracts, and validation as implementation decisions made inside it.
