# Contributing

Thanks for helping improve Forest For The Trees.

## Development Setup

Clone the repository, then validate the skill package from the repository root:

```bash
skills-ref validate "$PWD"
python3 -m py_compile scripts/validate-forest-for-the-trees.py
python3 scripts/validate-forest-for-the-trees.py --help
python3 scripts/validate-forest-for-the-trees.py "$PWD"
python3 -m json.tool evals/evals.json >/dev/null
npx skills add "$PWD" --list
```

If `skills-ref` is not installed, run the official reference implementation:

```bash
git clone --depth 1 https://github.com/agentskills/agentskills /tmp/agentskills
uv run --project /tmp/agentskills/skills-ref skills-ref validate "$PWD"
```

## Contribution Guidelines

- Keep the repository installable with `npx skills add srinitude/forest-for-the-trees`.
- Keep `SKILL.md` focused on the forest-level conceptual workflow.
- Put longer rationale in `references/`.
- Put trigger and functional coverage in `evals/`.
- Put deterministic repeated checks in `scripts/`.
- Preserve the boundary: this skill reconciles the root concept, then hands off to `grill-with-docs`.
- Avoid committing private product plans, credentials, API keys, generated caches, or proprietary context.

## Pull Requests

Before opening a pull request:

1. Run the validation commands above.
2. Update README or reference docs when behavior changes.
3. Keep commits focused and use clear commit messages.
4. Explain what changed, why it changed, and how it was validated.
