---
name: forest-for-the-trees
description: Use when the user needs to slow down and establish, validate, and reconcile the forest-level objective and concept for a product, artifact, feature, spec, PR, or plan before using grill-with-docs. Creates a direct, observable Forest Brief with purpose, actor, success evidence, constraints, non-goals, load-bearing assumptions, and conceptual contradictions resolved. Does not recursively explore design branches, update CONTEXT.md, or create ADRs.
---

# Forest For The Trees

Use this skill to directly and objectively establish what the agent and user are trying to accomplish before any branch-level grilling begins.

This skill is intentionally narrow. It creates the foundation for `grill-with-docs`; it does not replace it.

The work should be as rigorous as `grill-with-docs`, but only at the conceptual level. Interrogate the forest until it is coherent enough to support a later design-tree grill.

## Hard Rules

- Solely establish the forest-level objective and the evidence that it succeeds.
- Thoroughly validate and reconcile the concept before handoff.
- Do not recursively explore the design tree.
- Do not walk branches, sub-branches, workflows, interfaces, object models, implementation paths, or failure-mode trees.
- Do not update `CONTEXT.md`.
- Do not create ADRs.
- Ask one conceptual question at a time when a required Forest Brief field is missing, vague, contradictory, untestable, or unsupported.
- For each question, provide your recommended answer and why that answer makes the forest more coherent.
- If a missing field can be answered by checking nearby docs, specs, code, or prior conversation, inspect that evidence before asking.
- Keep wording plain. Preserve necessary technical identifiers, but replace jargon that hides what is actually being accomplished.
- Treat the result as a handoff artifact for `grill-with-docs`.

## Workflow

1. Inspect the user's request and any obvious local context only enough to understand the concept.
2. Draft the Forest Brief with the evidence available.
3. Run the Conceptual Reconciliation Loop.
4. If the brief has a central gap or contradiction, ask one focused conceptual question with a recommended answer.
5. When the user answers, simplify the answer into the brief without adding unsupported claims.
6. Repeat the reconciliation loop until the forest is stable enough for `grill-with-docs` to use as its foundation.
7. End with a ready-to-use `grill-with-docs` handoff prompt.

## Forest Brief

Produce this artifact and keep it concise:

```md
## Forest Brief

Objective:
We are trying to accomplish [observable outcome] for [specific actor] by creating/changing [product or artifact].

Why this matters:
[The concrete problem, opportunity, or constraint this exists to address.]

Success evidence:
[How we will objectively know it worked.]

Scope boundary:
[What is inside this effort.]

Non-goals:
[What this should not try to solve.]

Constraints:
[Known limits on runtime, platform, budget, policy, timing, data, users, or maintenance.]

Load-bearing assumptions:
[The assumptions that would change the work if false.]

Conceptual reconciliation:
[Important tensions found and how they were resolved.]

Ready for grill-with-docs:
[Yes/No, plus the one reason.]
```

The objective must be specific enough that a later `grill-with-docs` question can be judged with: "Does this help accomplish the stated outcome?"

## Conceptual Reconciliation Loop

Run this loop after every draft or answer. This is the core of the skill.

Check the Forest Brief against these tests:

- Objective test: the outcome is observable, not a mood, slogan, or implementation preference.
- Actor test: the beneficiary, operator, reviewer, or affected party is named clearly enough to judge tradeoffs later.
- Artifact test: the thing being created or changed is named without slipping into design details.
- Success evidence test: the proof of success would let a skeptical reviewer say yes or no.
- Scope test: the scope boundary and non-goals do not contradict the objective.
- Constraint test: constraints are real limits, not hidden feature decisions.
- Assumption test: each load-bearing assumption could be checked or falsified later.
- Coherence test: every field supports the same forest instead of describing competing products, audiences, or outcomes.
- Source reconciliation test: when existing docs, code comments, issues, specs, or conversation history make conflicting claims about purpose, surface the conflict and reconcile it conceptually.

Do not resolve the conflict by designing a solution. Resolve it by clarifying what the work is for.

Examples:

- "You say this is for founders, but the success evidence is about investor satisfaction. Which actor is primary?"
- "You say the artifact is a dashboard, but the objective is faster weekly decisions. Is the dashboard essential, or is the real artifact a decision workflow?"
- "You list personalization as a non-goal, but the success evidence requires user-specific recommendations. Which one should change?"
- "The repo docs describe this as an onboarding tool, but the prompt describes a reporting tool. Which purpose should `grill-with-docs` treat as fixed?"

When a test fails, ask one conceptual question. Do not continue to the next conceptual tension until the current one is resolved or explicitly marked unknown.

## Clarifying Question Format

Use this when a required Forest Brief field is missing, vague, contradictory, untestable, or unsupported:

```md
Current forest:
[One-sentence objective draft, or "Not established yet."]

Missing piece:
[The single conceptual gap or contradiction that blocks a useful Forest Brief.]

Question:
[One focused question.]

Recommended answer:
[Direct recommendation, clearly labeled as a recommendation.]

Why this matters:
[How this answer will anchor the later grill-with-docs session.]
```

## Plain-Language Discipline

Use the simplification discipline from `simplify`:

- Write for a plain adult reader.
- Preserve the user's intended meaning.
- Keep useful structure.
- Do not add unsupported claims.
- Preserve commands, file paths, API names, identifiers, product names, and exact technical terms when changing them would alter meaning.
- Explain or replace jargon when it makes the objective harder to judge.

## Explicit Non-Scope

If the user asks this skill to explore branches, respond by first completing the Forest Brief, then recommend `grill-with-docs` for the branch walk.

Do not do any of the following inside this skill:

- Build a design tree.
- Choose implementation modules.
- Resolve domain terminology.
- Add glossary terms.
- Write ADRs.
- Produce tickets, PRDs, issue plans, or implementation plans.
- Review a PR for bugs.
- Decide UI, API, schema, workflow, or architecture details beyond what is necessary to state the forest-level objective.

## Completion

The skill is complete when:

- The objective is direct and observable.
- The actor and artifact are named.
- Success evidence is concrete.
- Non-goals and constraints prevent obvious scope drift.
- Load-bearing assumptions are visible.
- Conceptual contradictions are resolved, explicitly marked unknown, or handed off as forest-level risks.
- Existing source claims about purpose have been checked when available and reconciled at the concept level.
- The output can be pasted into `grill-with-docs` as the starting point.

End with:

```md
## Forest Brief
[Completed brief]

## Handoff To grill-with-docs
Use `grill-with-docs` with this Forest Brief as the fixed foundation. Challenge every branch against the Objective and Success evidence. If a branch-level answer changes the forest, pause and revise the Forest Brief before continuing.
```
