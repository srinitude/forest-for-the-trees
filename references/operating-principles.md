# Operating Principles

This skill combines three source ideas:

- `grill-with-docs`: use relentless questioning, evidence checks, and reconciliation, but apply them here only to the root concept.
- `simplify`: preserve meaning while making the working language clearer, plainer, and less jargon-heavy.
- Nolan Lawson's "Using AI to write better code more slowly": slow down enough to understand the work before producing or reviewing details.

Source URLs:

- https://www.skills.sh/mattpocock/skills/grill-with-docs
- https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/

## What "Forest Before Trees" Means

The only job of this skill is to establish and reconcile what the product or artifact is trying to accomplish in objective language. A useful Forest Brief has:

- A specific actor.
- An observable outcome.
- A product or artifact boundary.
- Evidence that the work succeeded.
- Constraints that shape the work.
- Non-goals that prevent scope drift.
- Assumptions that would change the design if false.
- Reconciled tensions between purpose, actor, artifact, success evidence, constraints, and non-goals.

Do not begin detailed branch work here. Once these pieces are clear, hand the brief to `grill-with-docs`.

## Conceptual Reconciliation

Use the same level of seriousness that `grill-with-docs` applies to design branches, but keep the subject conceptual.

Challenge:

- Conflicting actors.
- Outcomes that cannot be observed.
- Artifacts that appear to be premature solutions.
- Success evidence that rewards the wrong thing.
- Non-goals that contradict the objective.
- Constraints that smuggle in design decisions.
- Assumptions that are too vague to test.
- Existing source material that describes a different purpose.

Reconcile by clarifying the forest. Do not reconcile by choosing an implementation path.

## Handoff Boundary

`forest-for-the-trees` stops at the forest. `grill-with-docs` walks the trees.

Do not resolve:

- Branches.
- Sub-branches.
- Domain terminology.
- Architecture.
- Workflows.
- Interfaces.
- Failure-mode trees.
- ADRs.
- Glossary updates.

The skill may ask multiple questions, but each one must be about the concept itself, not a branch of the future design.

## Plain-Language Contract

Use simple language as a correctness tool. When the objective cannot be stated plainly, the foundation is still unclear.

- Keep required technical terms, file names, commands, identifiers, and API names exact.
- Replace vague abstractions with concrete nouns and outcomes.
- Explain a technical term only when a reader would otherwise be stuck.
- Do not add claims that are not in the user's answer, the code, the docs, or verified context.
- Keep the user's tone when simplifying, unless that tone hides the decision.

## Slow Review Contract

This workflow intentionally slows down before branch review begins.

- Understand the artifact before improving it.
- Treat model output as a first draft that needs a clear purpose.
- Be willing to discover that the whole objective is wrong or too vague.
- Leave behind a concise, reconciled foundation for the next session.
