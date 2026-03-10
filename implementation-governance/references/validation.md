# Validation Policy

## Default Rule

Validation depth must match blast radius.

Choose the smallest credible verification that covers the actual risk of the change.

## Validation By Change Kind

### `direct fix`

Prefer targeted validation of the corrected path.

Examples:

- the smallest relevant test selection
- a focused query or command
- a direct reproduction and confirmation path
- a narrow compile, typecheck, or lint target when that is the most relevant signal

### `local refactor`

Validate behavior parity at the owner level.

Prefer:

- existing tests that cover the owner
- targeted tests plus a narrow static check
- focused manual verification when automation does not exist

### `boundary extraction`

Validate before-and-after behavior around the extracted seam.

Prefer:

- targeted coverage of the owner and extracted boundary
- parity checks for the moved logic
- the narrowest integration check that proves the extraction did not alter behavior

### `cross-cutting refactor`

Use broader validation because the blast radius is broader.

Prefer:

- targeted coverage for each touched pattern
- broader compile, type, lint, or integration checks in the affected area
- selective regression coverage where contracts or multiple owners are involved

### `new feature slice`

Validate the new behavior directly and verify any touched contracts proportionately.

Prefer:

- focused verification of the new path
- nearby owner-level checks
- contract or integration checks when the feature crosses boundaries

## Validation Rules

- Prefer existing validation entrypoints before inventing new infrastructure.
- Add or update validation when the repo already supports it and the change would otherwise be weakly verified.
- Do not widen a narrow change into a broad test rewrite unless the request or risk clearly requires it.
- If credible automated validation is unavailable, use the best targeted static or manual verification available and state what remains unverified.

## Common Errors

- running broad validation when a targeted check would prove the change
- claiming a refactor is safe without parity checks
- treating compilation alone as sufficient for a behavioral change
- skipping validation details when the change affects a public contract or multiple owners
