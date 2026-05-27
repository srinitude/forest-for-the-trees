# Forest For The Trees

[![skills.sh compatible](https://img.shields.io/badge/skills.sh-compatible-111111?style=flat-square)](https://skills.sh/s/srinitude/forest-for-the-trees)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Validate](https://github.com/srinitude/forest-for-the-trees/actions/workflows/validate.yml/badge.svg)](https://github.com/srinitude/forest-for-the-trees/actions/workflows/validate.yml)

A portable Agent Skills package for establishing and reconciling the forest-level concept before branch-level design grilling.

The skill creates a concise Forest Brief with a direct objective, actor, artifact boundary, success evidence, constraints, non-goals, load-bearing assumptions, and conceptual contradictions resolved. It is designed to run before `grill-with-docs`, so later design-tree questions have a stable foundation.

## Install

```bash
npx skills add srinitude/forest-for-the-trees
```

To preview the skills exposed by this repository:

```bash
npx skills add srinitude/forest-for-the-trees --list
```

## Use Cases

- Establish what a product, artifact, feature, spec, PR, or plan is trying to accomplish before detailed review.
- Reconcile conflicts between the intended actor, objective, artifact, success evidence, constraints, and non-goals.
- Convert vague or jargon-heavy intent into a plain-language Forest Brief.
- Create a handoff prompt for `grill-with-docs` without walking design branches inside this skill.

## Package Structure

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- evals/
|   `-- evals.json
|-- references/
|   `-- operating-principles.md
|-- requirements.txt
`-- scripts/
    `-- validate-forest-for-the-trees.py
```

## Validation

Validate the skill package:

```bash
skills-ref validate "$PWD"
```

If `skills-ref` is not installed, run the official reference implementation:

```bash
git clone --depth 1 https://github.com/agentskills/agentskills /tmp/agentskills
uv run --project /tmp/agentskills/skills-ref skills-ref validate "$PWD"
```

Validate the bundled script and eval corpus:

```bash
python3 -m py_compile scripts/validate-forest-for-the-trees.py
python3 scripts/validate-forest-for-the-trees.py --help
python3 scripts/validate-forest-for-the-trees.py "$PWD"
python3 -m json.tool evals/evals.json >/dev/null
```

Validate skills CLI discovery:

```bash
npx skills add "$PWD" --list
```

The same checks run in GitHub Actions for pushes and pull requests.

## Requirements

- Python 3.9 or newer.
- Node.js and `npx` for local skills CLI discovery checks.
- `uv` when running the upstream `skills-ref` fallback command.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

Please keep changes focused on the portable skill package: update `SKILL.md` for runbook behavior, `references/` for longer rationale, `evals/` for trigger and functional coverage, and `scripts/` for deterministic validation logic.

## Security

Report security concerns using the guidance in [SECURITY.md](SECURITY.md). Do not include secrets, private product plans, credentials, or proprietary context in public issues.

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
