---
name: implementation-governance
description: Opinionated implementation governance for code changes across projects and languages. Use when implementing features, fixing bugs, refactoring, reviewing code, or planning a change and you need to diagnose immediate and deeper structural problems, weigh code-health outcomes, surface credible contained, structural, or foundational scope options with concise decision previews, pause for user choice when quality tradeoffs materially differ, and decide change kind, extraction, ownership, convention handling, escalation, or validation depth.
---

# Implementation Governance

Choose implementation scope deliberately, then make consistent implementation and materialization decisions inside it. Do not equate disciplined implementation with automatically choosing the narrowest intervention.

## Workflow

1. Diagnose the request at both the immediate and structural levels.
Read [references/workflow.md](references/workflow.md) and [references/scope-options.md](references/scope-options.md) first. Inspect enough surrounding code, ownership, repetition, convention, and change friction to determine whether the immediate problem is isolated or evidence of a deeper code-health problem.

2. Set the solution horizon before implementation.
Use the canonical horizons `contained`, `structural`, and `foundational`. Honor an explicit user preference. Treat a task-connected, evidence-backed improvement in correctness, ownership, consistency, testability, or future change cost as a reason to surface a broader option when its durable benefit is material relative to its cost and risk. When a contained solution and a credible broader solution differ materially in long-term quality, recommend an option, explain the tradeoff, and wait for the user's choice before editing. Use [references/decision-previews.md](references/decision-previews.md) to show the smallest consumer-oriented code or structural artifact that materially clarifies the difference. A strong recommendation does not remove this decision gate. Treat delegation as explicit only when the user authorizes choosing the solution horizon, scope, or architecture; ordinary permission to implement, fix, proceed, or make the appropriate change is not scope delegation. If the user explicitly delegates that decision, choose and continue. If no broader option is supported by evidence, continue with `contained` without manufacturing a choice.

3. Identify what kind of change the selected horizon requires.
Read [references/change-kinds.md](references/change-kinds.md) to classify the work with one `primary change kind` and any `secondary change kinds` that materially affect scope, extraction, or validation. Treat change kind and solution horizon as separate decisions.

4. Decide the correct scope and contract handling inside the selected horizon.
Use [references/scoping.md](references/scoping.md) to choose the smallest complete scope that fulfills the selected horizon, decide what stays with the current owner, and determine when broader ownership is justified.
If the change alters a public export, interface, schema, route shape, event payload, database contract, or external integration boundary, read [references/escalation.md](references/escalation.md) first. Read [references/contract-changes.md](references/contract-changes.md) only after that contract-affecting change is confirmed.

5. Decide what should stay inline and what should be extracted.
Use [references/extraction.md](references/extraction.md) to choose between `inline`, `local helper`, `local module`, and `boundary`.

6. Re-apply governance inside each meaningful boundary introduced by the task.
Use [references/workflow.md](references/workflow.md) to re-run the full workflow for each meaningful boundary introduced by the task. Use [references/scoping.md](references/scoping.md) and [references/extraction.md](references/extraction.md) to decide which new seams are meaningful and when to stop descending.

7. Materialize the chosen boundaries with local implementation rules.
Use [references/materialization.md](references/materialization.md) and [references/conventions.md](references/conventions.md) to preserve or deliberately improve conventions while keeping responsibilities, public seams, dependency direction, and orchestration shape clear inside each unit.

8. Decide how much validation the change needs.
Use [references/validation.md](references/validation.md) to match validation depth to the selected horizon, blast radius, and change kind.

9. Escalate when the next correct step is not safe to guess.
Use [references/escalation.md](references/escalation.md) when the change would alter public contracts, widen ownership beyond the selected horizon, standardize an unclear area, or otherwise create lasting consequences that remain unresolved.

## Working Rules

- Choose the solution horizon before letting narrow change-kind defaults constrain the design.
- Use `contained`, `structural`, and `foundational` consistently for solution horizons.
- Choose the smallest correct change within the selected horizon, not necessarily the smallest possible intervention.
- Do not omit a credible deeper option merely because a contained fix can satisfy the immediate request.
- Bias toward opening the decision gate when a contained fix would preserve or add a diagnosed, material code-health problem that a credible broader option would correct.
- Treat code health as task-connected decision evidence, not as a license for aesthetic cleanup or speculative abstraction.
- Do not infer scope delegation from general implementation authority; require explicit authority to choose among materially different horizons.
- Show implementation shape only when it improves the decision; prefer a consumer call site or owned seam over internal implementation detail.
- Require repository evidence for structural and foundational options; do not use the decision gate to advertise unrelated cleanup.
- Treat a deliberate convention-setting change as legitimate structural work when the missing or harmful convention contributes to the problem.
- Choose one `primary change kind` for the current task.
- Add `secondary change kinds` only when they materially affect scope, extraction, or validation.
- Use the canonical change kinds consistently: `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, and `new feature slice`.
- Use the canonical extraction outcomes consistently: `inline`, `local helper`, `local module`, and `boundary`.
- Preserve the dominant convention in a contained change; improve it deliberately only when the selected horizon includes that work.
- Re-run the full workflow at each meaningful boundary introduced by the task until [Change Scoping Policy](references/scoping.md) says the remaining work is straightforward local implementation.
- Do not stop at top-level architecture when the task includes scaffolding, package design, or other structural materialization.
- Materialize each unit with the simplest structure that keeps responsibility, public seams, and dependency direction clear.
- Separate pure local logic from orchestration when mixing them would obscure the unit's main responsibility.
- Shared abstractions must be earned by real reuse or clearly broader ownership.
- Prefer local ownership first after extraction unless the selected horizon and repository evidence justify broader ownership.
- Keep contract surfaces no wider than the selected outcome requires.
- Keep side effects at clear boundaries and prefer extracting pure local logic before sharing orchestration.
- Use narrower framework or domain skills for technology-specific structure. Use this skill to govern change strategy, scope, extraction pressure, and validation depth.

## Communicating Decisions

Before implementation, communicate a scope choice only when materially different credible options exist and the user has not already chosen. For each option, state:

- the outcome it pursues
- the affected surface
- the diagnosed code-health condition it corrects or knowingly leaves in place
- its durable upside
- its cost, migration burden, or risk
- why acting now or deferring is reasonable
- when implementation shape materially affects the choice, one compact decision preview using [Decision Preview Policy](references/decision-previews.md)

Recommend one option and ask for one clear choice even when the recommendation is strong. Do not begin edits while this required choice is unresolved. Include only credible options, usually two; do not force all three horizons into a menu.

For a review or plan, make the recommended horizon and meaningful alternatives visible before implementation details. After a horizon is selected, include one consolidated intended-shape preview when consumer usage, a boundary, contract, data shape, ownership, or flow is central to understanding the plan. Do not repeat every option.

For a completed implementation, lead with the outcome. Then state the selected horizon, consequential architecture or convention decisions, validation performed, and intentionally deferred opportunities. Mention change kind, extraction, contracts, or recursive boundary decisions only when they help the user understand the result. Do not emit a fixed field dump or empty labels.

## Reference Map

Use these references directly as needed:

- [references/overview.md](references/overview.md)
- [references/workflow.md](references/workflow.md)
- [references/scope-options.md](references/scope-options.md)
- [references/decision-previews.md](references/decision-previews.md)
- [references/change-kinds.md](references/change-kinds.md)
- [references/scoping.md](references/scoping.md)
- [references/contract-changes.md](references/contract-changes.md)
- [references/extraction.md](references/extraction.md)
- [references/materialization.md](references/materialization.md)
- [references/conventions.md](references/conventions.md)
- [references/validation.md](references/validation.md)
- [references/escalation.md](references/escalation.md)

## Not For

- framework-specific architecture or folder layouts that belong to a narrower skill
- language-specific style rules that are already governed by repo tooling or conventions
- broad software design philosophy that does not change the current implementation decision
