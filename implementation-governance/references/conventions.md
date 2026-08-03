# Convention Handling Policy

## Default Rule

Preserve the dominant convention in the touched area by default. Deliberately establish or correct a convention when a selected structural or foundational horizon includes that outcome.

This skill does not define framework-specific layout or language-specific style rules. It governs how to react to conventions that already exist in the repo.

## What Counts As A Dominant Convention

Choose conventions using this precedence order:

1. current owner
2. sibling files or the same local module, class, or package
3. the surrounding feature, service, or local area
4. broader repo-wide convention
5. this skill's defaults

Treat a convention as dominant when it is clearly established at the highest applicable level, not merely present somewhere else in the repository.

Use these signals:

- nearby siblings follow the same pattern
- the pattern appears intentional rather than transitional
- the pattern is active in current code, not only in stale files

## What To Preserve

When clearly established in the touched area, preserve:

- file and folder placement
- naming style
- entrypoint or public surface shape
- local validation placement
- dependency acquisition patterns
- side-effect placement and orchestration boundaries
- error-handling and logging patterns

## Acceptable vs Materially Harmful Local Patterns

Treat a local stack pattern as acceptable when it is clearly established in the touched area, supports the current change safely, and does not directly create correctness, ownership, or maintenance problems for the task at hand.

Treat a local stack pattern as materially harmful when one or more of these are true:

- it directly causes bugs or hidden behavior
- it forces unclear ownership or responsibility mixing
- it creates repeated churn, workaround code, or failed fixes in the same area
- it blocks the selected outcome unless the surrounding structure changes

If the local pattern is acceptable, align with it even when a different pattern would be cleaner in the abstract.

If the local pattern is materially harmful:

- surface convention repair as a structural or foundational scope option when it would address the diagnosed problem
- keep the fix as local as possible when that resolves the immediate problem
- after the wider option is selected, apply the convention across its complete coherent surface
- escalate when the convention or affected ownership remains unclear

## Convention-Setting Changes

Treat a convention-setting change as deliberate implementation work, not opportunistic cleanup, when the selected horizon includes it and repository evidence shows that the missing, mixed, or harmful convention contributes to the problem.

When establishing a convention:

- name the problem the convention resolves
- choose the narrowest ownership level at which the convention is coherent
- update the complete selected surface instead of leaving contradictory partial examples
- reinforce the convention through types, tests, tooling, documentation, or a clear exemplar when proportionate
- avoid presenting a local convention as repo-wide unless the foundational horizon genuinely covers the repository

## Mixed Or Unclear Areas

If the touched area is mixed or unclear:

- preserve the highest-precedence level that is still clear
- avoid standardizing adjacent code that is outside the request
- use this skill's defaults when no dominant local pattern exists
- surface a wider option when choosing one pattern would resolve the diagnosed problem
- escalate when the user selected wider convention work but the correct precedent remains unclear

## Safe Defaults

When the local area does not establish a clear convention:

- keep the change local
- prefer explicit names over clever ones
- prefer narrow public surfaces
- prefer keeping side effects near clear boundaries rather than scattering them across helpers
- prefer pure local helpers or modules before introducing shared orchestration
- prefer colocated validation when the repo already validates nearby code that way
- avoid introducing a new repo-wide pattern through a narrow task

## Convention Errors

- following a distant convention instead of the touched area
- replacing an acceptable local stack pattern just because another one is cleaner in the abstract
- normalizing mixed code without being asked
- treating one recent file as a repo-wide standard
- changing conventions and behavior in the same step without acknowledging it
