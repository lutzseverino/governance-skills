# Change Scoping Policy

## Default Rule

Choose the smallest correct change.

The correct scope is the narrowest set of files, owners, and contracts that must change to satisfy the request safely.

## Keep The Change Local By Default

Prefer the current owner when:

- the behavior belongs clearly to the touched owner
- the change corrects or clarifies existing behavior
- the extracted logic is only used by one owner
- broader reuse is speculative rather than present

## Widen Scope Only For Real Reasons

Broader scope is justified when one or more of these are true:

- the same change is required across multiple owners
- the extracted code clearly belongs to a broader owner that already exists
- the current owner mixes responsibilities in a way that directly blocks a correct change
- a public contract, schema, API, or integration boundary must change to satisfy the request

## Ownership Rules

- Keep code with its nearest clear owner.
- Promote code into broader shared scope only when ownership is clearly broader than the current area.
- If broader ownership seems correct but the right home is unclear from the repo structure, ask the user instead of guessing.
- Do not create a new shared home only because multiple future uses seem possible.

## Mixed-Area Rule

If the touched area contains mixed conventions or uneven structure:

- preserve the dominant pattern of the local owner you are changing
- avoid widening the change just to make nearby code uniform
- escalate if choosing one pattern would effectively standardize a wider area

## Common Scoping Errors

- fixing one bug by rewriting the whole subsystem
- promoting local code into shared scope before real reuse exists
- broad cleanup during a feature request
- changing unrelated call sites because they are nearby
- guessing broader ownership when the architecture does not make it clear
