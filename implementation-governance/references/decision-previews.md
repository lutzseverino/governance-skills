# Decision Preview Policy

## Purpose

Use a decision preview to make an implementation choice or plan tangible without pre-implementing it in the conversation. Show the smallest artifact that reveals how consumers, contracts, ownership, or flow would differ.

## When To Show A Preview

Show a preview when it materially clarifies:

- how a consumer would use a new or changed capability
- where a new boundary or responsibility would live
- how a contract, event, schema, or data shape would change
- how ownership, dependencies, files, or runtime flow differ between credible horizons
- what an introduced system or convention would feel like in ordinary use

Omit the preview when the task is trivial, prose already makes the choice concrete, the options have the same relevant shape, or a snippet would be speculative rather than decision-useful.

## Choose The Smallest Useful Artifact

Prefer artifacts in this order:

1. a consumer-facing call site
2. a boundary signature, interface, route, event, schema, or data shape
3. a compact ownership, file-tree, dependency, or runtime-flow sketch
4. a minimal algorithm fragment only when behavior is the actual design difference

If consumer usage is unchanged between options, show the nearest seam or ownership difference instead of repeating identical call sites.

## Size And Fidelity

- Use at most one compact artifact per materially different option, or one combined comparison when that is clearer.
- Keep a code preview to the smallest discriminating lines, usually three to eight. Keep the complete decision preview comfortably under about twenty lines unless the user asks for more.
- Omit imports, setup, boilerplate, full implementation bodies, exhaustive types, error handling, and tests unless one of them is the decision itself.
- Prefer the repository's language, names, and conventions when inspection supports them.
- Label pseudocode, placeholder names, or unsettled contracts as illustrative.
- Do not imply that an illustrative preview is an implementation commitment; deeper inspection may refine details inside the selected horizon.
- Use comments only to point out the design difference.

## Horizon Choice Output

Place the preview beside the option it explains. Preserve the outcome, affected surface, code-health consequence, durable upside, cost or risk, and why-now reasoning required by [Scope Options Policy](./scope-options.md). The preview supplements those tradeoffs; it does not replace them.

Example:

```ts
// contained: the caller still owns channel selection
await sendSms(message)

// structural: the caller uses a channel-agnostic boundary
await notifications.send({ channel: "sms", message })
```

## Selected-Horizon Plan Output

After selection, show at most one consolidated intended-shape preview when it helps the user understand the plan. Prefer showing the ordinary consumer interaction and the owned seam it reaches. Do not repeat previews for rejected horizons or expand the preview into implementation scaffolding.
