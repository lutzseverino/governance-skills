# Extraction Policy

## Canonical Outcomes

Use these outcome terms consistently:

- `inline`
- `local helper`
- `local module`
- `owned boundary`
- `shared boundary`

## Outcome Definitions

### `inline`

Keep the code in its current function, method, type, class, file, or owner.

Choose `inline` when:

- the change is small and directly supports the surrounding logic
- the responsibility is still clear while reading the owner
- extraction would only move code without creating a clearer seam

### `local helper`

Extract a private helper that still belongs entirely to the current owner.

Choose `local helper` when:

- a repeated branch, calculation, mapping, or formatting rule appears inside one owner
- a named step would make the owner scan more cleanly
- the helper does not need its own file or public surface

Keep a `local helper` in the same file by default. Move it into a sibling file only when it is used by another file owned by the same boundary or the owner already contains multiple extracted local helpers.

### `local module`

Extract a sibling file, module, class, or equivalent unit that still belongs to one owner.

Choose `local module` when:

- the extracted code needs its own imports, dependencies, state, or configuration
- multiple related helpers naturally belong together
- the code should stay local to one owner but no longer belongs in the main file

Do not create a `local module` just to shorten a file.

### `owned boundary`

Extract a named boundary with a distinct responsibility that is still clearly owned by one feature, package, service, component, or domain area.

Choose `owned boundary` when:

- the responsibility is distinct and likely to remain owned by one area
- the code benefits from a narrow local API or entrypoint
- the new unit has a clearer responsibility than a helper or simple sibling module

Prefer an `owned boundary` before a `shared boundary`.

### `shared boundary`

Promote code into broader shared scope with a stable responsibility and multiple real owners.

Choose `shared boundary` only when:

- reuse already exists across two or more independent owners
- ownership is clearly broader than the current local area
- the abstraction is stable enough to deserve a shared public surface

Do not create a `shared boundary` for speculative reuse.

## Objective Signals

Use these as concrete extraction signals:

- repeated logic inside one owner
- a distinct dependency set or configuration
- a stable local API or seam
- multiple local helpers that form one responsibility
- actual reuse across independent owners
- clearly broader ownership than the current area

## Guardrails

- Do not extract only to reduce line count.
- Do not promote code into shared scope only because it looks reusable.
- Do not create a boundary without a distinct responsibility.
- If broader placement seems right but the correct destination is unclear, ask the user instead of inventing a new shared home.
