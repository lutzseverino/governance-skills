# Implementation Governance

## Purpose

Group the implementation governance references by concern so solution-horizon selection, change classification, scope control, extraction, materialization, convention handling, validation, and escalation remain clear and independently maintainable.

Use [Workflow](./workflow.md) as the operational entry point when making a decision.

## Documents

- [Workflow](./workflow.md)
- [Scope Options Policy](./scope-options.md)
- [Change Kind Policy](./change-kinds.md)
- [Change Scoping Policy](./scoping.md)
- [Contract Change Policy](./contract-changes.md)
- [Extraction Policy](./extraction.md)
- [Materialization Policy](./materialization.md)
- [Convention Handling Policy](./conventions.md)
- [Validation Policy](./validation.md)
- [Escalation Policy](./escalation.md)

## Scope Boundaries

- Workflow defines the order of operations for a change.
- Scope options policy defines how to detect credible deeper problems, evaluate material code-health differences, choose a contained, structural, or foundational solution horizon, and pause for user selection when needed.
- Change kind policy defines what kind of work is being performed and what defaults it carries.
- Scoping policy defines how far the change should reach, how ownership levels are interpreted, and when broader ownership is justified.
- Contract change policy defines how an approved contract-affecting change should be carried out safely.
- Extraction policy defines whether code should stay `inline`, become a `local helper`, move into a `local module`, or become a `boundary`.
- Materialization policy defines how code inside a chosen unit should keep responsibility, public seams, dependency direction, and orchestration shape clear.
- Workflow is recursive when the task introduces meaningful new boundaries that must be materialized. Scoping defines which boundaries are meaningful and when recursion should stop.
- Convention handling defines how to preserve dominant local patterns, acceptable stack patterns, dependency shapes, and side-effect placement without silently standardizing a wider area.
- Validation policy defines how much validation the change needs based on risk and blast radius.
- Escalation policy defines when the next step should be confirmed instead of guessed.

## Decision Flow

1. Start with [Workflow](./workflow.md) to follow the decision sequence.
2. Use [Scope Options Policy](./scope-options.md) to evaluate code-health consequences, choose the solution horizon, or present credible alternatives before implementation.
3. Use [Change Kind Policy](./change-kinds.md) to classify the work with one `primary change kind` and any `secondary change kinds` that materially affect the plan.
4. Use [Change Scoping Policy](./scoping.md) to choose the smallest complete change inside the selected horizon, identify the correct owner level, and determine whether broader ownership is required.
5. If the change affects a contract surface, use [Contract Change Policy](./contract-changes.md) after approval to choose the narrowest safe contract change.
6. Use [Extraction Policy](./extraction.md) to decide what stays `inline` and what should become a `local helper`, `local module`, or `boundary`.
7. Re-apply the full [Workflow](./workflow.md) inside each meaningful boundary introduced by the task until [Change Scoping Policy](./scoping.md) says the remaining work is straightforward local implementation.
8. Use [Materialization Policy](./materialization.md) and [Convention Handling Policy](./conventions.md) to shape local code clearly and apply any selected convention-setting work coherently.
9. Use [Validation Policy](./validation.md) to meet the minimum validation floor for the change kind, horizon, and blast radius.
10. Use [Escalation Policy](./escalation.md) when consequences beyond the selected horizon, unclear ownership, or mixed conventions make the next step unsafe to assume.
