<div align="center">
  <h1>Governance Skills</h1>
    <p>Opinionated governance skills for disciplined software change and architecture decisions.</p>
    <p>
        <img alt="skills" src="https://img.shields.io/badge/skills-2-0f172a">
        <a href="https://github.com/lutzseverino/governance-skills/blob/main/LICENSE">
            <img alt="license" src="https://img.shields.io/github/license/lutzseverino/governance-skills">
        </a>
        <a href="https://github.com/lutzseverino/governance-skills/commits/main">
            <img alt="last commit" src="https://img.shields.io/github/last-commit/lutzseverino/governance-skills">
        </a>
    </p>
</div>

## Included Skills

### [`implementation-governance`](./implementation-governance/)

Opinionated implementation guidance for code changes across projects and languages. Use it to detect when a small request reveals a deeper code-health problem, present materially different contained, structural, and foundational outcomes with concise decision previews, and govern change kind, scope, extraction, ownership, conventions, escalation, and validation depth.

<p>
    <a href="https://skills.sh/lutzseverino/governance-skills/implementation-governance">
        <img alt="skills.sh implementation-governance" src="https://img.shields.io/badge/skills.sh-listed-0f172a">
    </a>
    <a href="https://agentskill.sh/@lutzseverino/implementation-governance">
        <img alt="agentskill.sh implementation-governance" src="https://img.shields.io/badge/agentskill.sh-listed-1f2937">
    </a>
</p>

Entry points: [SKILL.md](./implementation-governance/SKILL.md), [overview](./implementation-governance/references/overview.md)

### [`react-component-governance`](./react-component-governance/)

Opinionated, standalone React component architecture guidance for extraction, classification, packaging, ownership, boundary cases, and meaningful local-versus-wider architecture choices.

<p>
    <a href="https://skills.sh/lutzseverino/governance-skills/react-component-governance">
        <img alt="skills.sh react-component-governance" src="https://img.shields.io/badge/skills.sh-listed-0f172a">
    </a>
    <a href="https://agentskill.sh/@lutzseverino/react-component-governance">
        <img alt="agentskill.sh react-component-governance" src="https://img.shields.io/badge/agentskill.sh-listed-1f2937">
    </a>
</p>

Entry points: [SKILL.md](./react-component-governance/SKILL.md), [overview](./react-component-governance/references/overview.md)

## Repository Layout

```text
governance-skills/
  implementation-governance/
    SKILL.md
    agents/
      openai.yaml
    references/
      overview.md
      workflow.md
      scope-options.md
      decision-previews.md
      change-kinds.md
      scoping.md
      contract-changes.md
      extraction.md
      materialization.md
      conventions.md
      validation.md
      escalation.md
  react-component-governance/
    SKILL.md
    agents/
      openai.yaml
    references/
      overview.md
      workflow.md
      extraction.md
      classification.md
      roles.md
      patterns.md
      packaging.md
      ownership.md
      boundary-cases.md
```

## Install

Install a specific skill from this repository with `skills.sh`:

```bash
npx skills add lutzseverino/governance-skills --skill implementation-governance
npx skills add lutzseverino/governance-skills --skill react-component-governance
```

If a project already uses `skills.sh`, update installed skills with:

```bash
npx skills update
```

## Development

Run the canonical local validation gate before opening a pull request:

```bash
./scripts/validate
```

The gate validates skill package structure, metadata, internal Markdown links,
and GitHub Actions workflows, then runs its regression suite. Repository-wide
contribution and pull-request rules are defined in
[`CONTRIBUTING.md`](./CONTRIBUTING.md) and pinned through
[`.repository-standards.json`](./.repository-standards.json).

## Documentation

See [`docs/README.md`](docs/README.md) for repository-maintainer documentation
and the canonical authoring templates. Runtime guidance remains in each
skill's `references/` directory.

## Use

Use `$implementation-governance` when you want an agent to inspect both the immediate problem and task-connected code-health opportunities, surface materially different scope options with compact consumer or boundary previews before editing, and govern the selected implementation coherently.

Use `$react-component-governance` independently when you need help deciding whether UI should stay inline or be extracted, whether a local request reveals a wider React architecture opportunity, what kind of component or non-component boundary should exist, and how extracted React code should be packaged and owned.

## License

Licensed under the terms in [`LICENSE`](LICENSE).
