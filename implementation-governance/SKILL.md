---
name: implementation-governance
description: Opinionated implementation guidance for code changes across projects and languages. Use when implementing features, fixing bugs, refactoring, reviewing code, or planning a change and you need to decide change kind, scope, extraction, ownership, convention handling, escalation, or validation depth without drifting into opportunistic cleanup or broad, unclear rewrites.
---

# Implementation Governance

Make consistent implementation decisions without drifting into broad, unclear, or opportunistic code changes.

## Workflow

1. Identify what kind of change this is.
Read [references/workflow.md](references/workflow.md) and [references/change-kinds.md](references/change-kinds.md) first to classify the work as a `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, or `new feature slice`.

2. Decide how wide the change should be.
Use [references/scoping.md](references/scoping.md) to keep the change at the smallest correct scope, decide what stays with the current owner, and determine when broader ownership is actually justified.

3. Decide what should stay inline and what should be extracted.
Use [references/extraction.md](references/extraction.md) to choose between `inline`, `local helper`, `local module`, `owned boundary`, and `shared boundary`.

4. Check local conventions before materializing the change.
Use [references/conventions.md](references/conventions.md) to preserve dominant local conventions, handle mixed areas carefully, and avoid silently standardizing a wider area than the request requires.

5. Decide how much validation the change needs.
Use [references/validation.md](references/validation.md) to match verification depth to blast radius and change kind.

6. Escalate when the next correct step is not safe to guess.
Use [references/escalation.md](references/escalation.md) when the change would alter public contracts, widen ownership, standardize a mixed area, or otherwise create lasting consequences beyond the immediate request.

## Working Rules

- Choose exactly one change kind for the current task.
- Use the canonical change kinds consistently: `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, and `new feature slice`.
- Use the canonical extraction outcomes consistently: `inline`, `local helper`, `local module`, `owned boundary`, and `shared boundary`.
- Prefer the smallest correct change.
- Preserve the dominant convention in the touched area before considering wider normalization.
- Shared abstractions must be earned by real reuse or clearly broader ownership.
- Prefer a local extraction before promoting code into broader shared scope.
- Use narrower framework or domain skills for technology-specific structure. Use this skill to govern change strategy, scope, extraction pressure, and validation depth.

## Output Expectations

For a review, plan, or implementation proposal:

- state the chosen change kind
- state the intended scope
- state the extraction outcome
- explain the convention decision
- explain the planned validation depth
- call out any escalation point or confirm that none is needed

Use this response shape:

```text
Change kind: ...
Scope: ...
Extraction outcome: ...
Convention decision: ...
Validation: ...
Escalation note: ...
```

## Reference Map

Use these references directly as needed:

- [references/overview.md](references/overview.md)
- [references/workflow.md](references/workflow.md)
- [references/change-kinds.md](references/change-kinds.md)
- [references/scoping.md](references/scoping.md)
- [references/extraction.md](references/extraction.md)
- [references/conventions.md](references/conventions.md)
- [references/validation.md](references/validation.md)
- [references/escalation.md](references/escalation.md)

## Not For

- framework-specific architecture or folder layouts that belong to a narrower skill
- language-specific style rules that are already governed by repo tooling or conventions
- broad software design philosophy that does not change the current implementation decision
