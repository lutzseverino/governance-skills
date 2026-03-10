<div align="center">
    <h1 align="center">Governance Skills</h1>
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

Opinionated implementation guidance for code changes across projects and languages. Use it to decide change kind, scope, extraction, ownership, convention handling, escalation, and validation depth.

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

Opinionated React component architecture guidance for extraction, classification, packaging, ownership, and boundary cases.

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
      change-kinds.md
      scoping.md
      extraction.md
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

## Use

Use `$implementation-governance` when you need help deciding how wide a code change should be, what should stay local, when extraction is justified, how to handle mixed conventions, and how much validation is proportionate.

Use `$react-component-governance` when you need help deciding whether UI should stay inline or be extracted, what kind of component or non-component boundary should exist, and how extracted React code should be packaged and owned.
