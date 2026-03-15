# Materialization Policy

## Default Rule

Materialize the chosen unit with the simplest structure that keeps responsibility, public seams, dependency direction, and orchestration shape clear.

This policy governs code inside an already chosen owner, module, package, service, or boundary. It does not replace extraction, ownership, or convention decisions.

## Keep Responsibilities Legible

Shape the unit so its main responsibility remains obvious while reading it.

- keep one clear local reason to change per unit
- separate pure transformation or validation logic from orchestration when mixing them obscures the unit's role
- do not bury the main responsibility under incidental setup, mapping, or wiring

## Keep Seams Narrow

Expose only the entrypoints, collaborators, types, configuration, or state the owner actually needs.

- prefer narrow local APIs over broad helper surfaces
- keep internal helpers and intermediate details private by default
- avoid expanding a unit's visible surface only for hypothetical reuse

## Keep Dependency Direction Obvious

Make it clear what depends on what inside the chosen unit.

- let orchestration depend on lower-level logic, not the reverse
- keep pure logic free of unnecessary infrastructure or side-effect dependencies
- avoid sibling units reaching into each other's internals when one narrow seam would suffice

## Split Only For Real Reasons

Split local code again only when clarity, responsibility, or dependency direction materially improves.

- do not split only to shorten a file
- do not split when nearby convention already makes the current structure obvious
- split when incidental coupling would otherwise remain hidden inside one unit

## Naming Rule

Name local units by responsibility and role in the design, not by incidental mechanics.

- prefer names that explain what the unit owns or coordinates
- avoid names that only describe the implementation trick used inside it

## Common Errors

- mixing orchestration and pure logic until the unit's role becomes blurry
- exposing helper details that the owner does not actually need
- letting siblings share incidental dependencies instead of a narrow seam
- splitting local code aggressively without improving responsibility or coupling
