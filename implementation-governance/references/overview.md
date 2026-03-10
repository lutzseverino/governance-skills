# Implementation Governance

## Purpose

Group the implementation governance references by concern so change classification, scope control, extraction, convention handling, validation, and escalation remain clear and independently maintainable.

Use [Workflow](./workflow.md) as the operational entry point when making a decision.

## Documents

- [Workflow](./workflow.md)
- [Change Kind Policy](./change-kinds.md)
- [Change Scoping Policy](./scoping.md)
- [Extraction Policy](./extraction.md)
- [Convention Handling Policy](./conventions.md)
- [Validation Policy](./validation.md)
- [Escalation Policy](./escalation.md)

## Scope Boundaries

- Workflow defines the order of operations for a change.
- Change kind policy defines what kind of work is being performed and what defaults it carries.
- Scoping policy defines how far the change should reach and when broader ownership is justified.
- Extraction policy defines whether code should stay `inline`, become a `local helper`, move into a `local module`, become an `owned boundary`, or be promoted into a `shared boundary`.
- Convention handling defines how to preserve dominant local patterns without silently standardizing a wider area.
- Validation policy defines how much verification the change needs based on risk and blast radius.
- Escalation policy defines when the next step should be confirmed instead of guessed.

## Decision Flow

1. Start with [Workflow](./workflow.md) to follow the decision sequence.
2. Use [Change Kind Policy](./change-kinds.md) to classify the work as a `direct fix`, `local refactor`, `boundary extraction`, `cross-cutting refactor`, or `new feature slice`.
3. Use [Change Scoping Policy](./scoping.md) to choose the smallest correct change and determine whether broader ownership is actually required.
4. Use [Extraction Policy](./extraction.md) to decide what stays `inline` and what should become a `local helper`, `local module`, `owned boundary`, or `shared boundary`.
5. Use [Convention Handling Policy](./conventions.md) to preserve dominant local patterns and avoid accidental standardization.
6. Use [Validation Policy](./validation.md) to match verification depth to the change kind and blast radius.
7. Use [Escalation Policy](./escalation.md) when broader consequences, unclear ownership, or mixed conventions make the next step unsafe to assume.
