# Convention Handling Policy

## Default Rule

Preserve the dominant convention in the touched area before considering wider normalization.

This skill does not define framework-specific layout or language-specific style rules. It governs how to react to conventions that already exist in the repo.

## What Counts As A Dominant Convention

Treat a convention as dominant when it is clearly established in the local area you are changing, not merely present somewhere else in the repository.

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
- error-handling and logging patterns

## Mixed Or Unclear Areas

If the touched area is mixed or unclear:

- preserve the current owner first
- avoid standardizing adjacent code that is outside the request
- use this skill's defaults when no dominant local pattern exists
- escalate when choosing one pattern would set a wider precedent

## Safe Defaults

When the local area does not establish a clear convention:

- keep the change local
- prefer explicit names over clever ones
- prefer narrow public surfaces
- prefer colocated validation when the repo already validates nearby code that way
- avoid introducing a new repo-wide pattern through a narrow task

## Convention Errors

- following a distant convention instead of the touched area
- normalizing mixed code without being asked
- treating one recent file as a repo-wide standard
- changing conventions and behavior in the same step without acknowledging it
