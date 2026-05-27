#!/usr/bin/env python3
"""Validate the forest-for-the-trees skill package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_DESCRIPTION_TERMS = [
    "forest-level objective",
    "validate",
    "reconcile",
    "product",
    "artifact",
    "grill-with-docs",
    "Forest Brief",
    "success evidence",
    "non-goals",
    "load-bearing assumptions",
    "conceptual contradictions",
    "Does not recursively explore design branches",
    "CONTEXT.md",
    "ADRs",
]

REQUIRED_BODY_PHRASES = [
    "does not replace it",
    "rigorous as `grill-with-docs`, but only at the conceptual level",
    "Solely establish the forest-level objective",
    "Thoroughly validate and reconcile the concept before handoff",
    "Do not recursively explore the design tree",
    "Do not update `CONTEXT.md`",
    "Do not create ADRs",
    "one conceptual question at a time",
    "Conceptual Reconciliation Loop",
    "Objective test",
    "Actor test",
    "Artifact test",
    "Success evidence test",
    "Scope test",
    "Constraint test",
    "Assumption test",
    "Coherence test",
    "Source reconciliation test",
    "Forest Brief",
    "Success evidence",
    "Load-bearing assumptions",
    "Conceptual reconciliation",
    "Handoff To grill-with-docs",
    "plain adult reader",
    "branch-level grilling",
]

FORBIDDEN_BODY_PHRASES = [
    "Walk Branches Recursively",
    "Map The Design Tree",
    "Record the branch map",
    "Spawn only the sub-branches",
    "Use `references/CONTEXT-FORMAT.md`",
    "Use `references/ADR-FORMAT.md`",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    raw_frontmatter, body = match.groups()
    data: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"frontmatter line is not key: value: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data, body


def validate_skill_md(root: Path) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        fail("missing SKILL.md")
    text = skill_path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    if frontmatter.get("name") != "forest-for-the-trees":
        fail("frontmatter name must be forest-for-the-trees")
    description = frontmatter.get("description", "")
    if not description or "TODO" in description:
        fail("description must be complete")
    if len(description) > 1024:
        fail("description must be 1024 characters or less")
    lowered_description = description.lower()
    missing_terms = [
        term for term in REQUIRED_DESCRIPTION_TERMS
        if term.lower() not in lowered_description
    ]
    if missing_terms:
        fail(f"description missing trigger or boundary terms: {missing_terms}")
    if "TODO" in body:
        fail("SKILL.md body still contains TODO")
    lowered_body = body.lower()
    missing_phrases = [
        phrase for phrase in REQUIRED_BODY_PHRASES
        if phrase.lower() not in lowered_body
    ]
    if missing_phrases:
        fail(f"SKILL.md body missing required decisions: {missing_phrases}")
    forbidden = [
        phrase for phrase in FORBIDDEN_BODY_PHRASES
        if phrase.lower() in lowered_body
    ]
    if forbidden:
        fail(f"SKILL.md body still contains recursive branch behavior: {forbidden}")


def validate_references(root: Path) -> None:
    operating = root / "references" / "operating-principles.md"
    if not operating.is_file():
        fail("missing references/operating-principles.md")
    text = operating.read_text(encoding="utf-8")
    for phrase in [
        "Forest Before Trees",
        "Conceptual Reconciliation",
        "Handoff Boundary",
        "Plain-Language",
    ]:
        if phrase.lower() not in text.lower():
            fail(f"operating-principles.md missing {phrase}")
    for removed in ["CONTEXT-FORMAT.md", "ADR-FORMAT.md"]:
        if (root / "references" / removed).exists():
            fail(f"{removed} should not exist in this foundation-only skill")


def validate_openai_yaml(root: Path) -> None:
    openai_path = root / "agents" / "openai.yaml"
    if not openai_path.is_file():
        fail("missing agents/openai.yaml")
    text = openai_path.read_text(encoding="utf-8")
    for phrase in [
        "display_name",
        "Forest For The Trees",
        "short_description",
        "default_prompt",
        "$forest-for-the-trees",
        "grill-with-docs",
    ]:
        if phrase not in text:
            fail(f"agents/openai.yaml missing {phrase}")


def validate_evals(root: Path) -> None:
    eval_path = root / "evals" / "evals.json"
    if not eval_path.is_file():
        fail("missing evals/evals.json")
    try:
        data = json.loads(eval_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"evals/evals.json is invalid JSON: {exc}")
    if data.get("skill") != "forest-for-the-trees":
        fail("eval corpus must identify skill=forest-for-the-trees")
    trigger_evals = data.get("trigger_evals")
    functional_evals = data.get("functional_evals")
    if not isinstance(trigger_evals, list) or len(trigger_evals) < 12:
        fail("trigger_evals must contain at least 12 cases")
    if not isinstance(functional_evals, list) or len(functional_evals) < 7:
        fail("functional_evals must contain at least 7 cases")
    should = [case for case in trigger_evals if case.get("should_trigger") is True]
    should_not = [
        case for case in trigger_evals if case.get("should_trigger") is False
    ]
    if len(should) < 5 or len(should_not) < 5:
        fail("trigger_evals must cover both trigger and anti-trigger cases")
    prompts = "\n".join(case.get("prompt", "") for case in trigger_evals)
    if "Walk down every branch" not in prompts:
        fail("trigger evals must include recursive branch anti-trigger")
    all_text = json.dumps(data)
    for phrase in [
        "conceptual_reconciliation",
        "conceptual_contradiction",
        "source_purpose_conflict",
        "no_branch_despite_rigor",
    ]:
        if phrase not in all_text:
            fail(f"evals missing {phrase}")
    for case in trigger_evals + functional_evals:
        for field in ["id", "prompt"]:
            if not case.get(field):
                fail(f"eval case missing {field}: {case}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "skill_dir",
        nargs="?",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Path to the forest-for-the-trees skill directory.",
    )
    args = parser.parse_args()
    root = args.skill_dir.resolve()
    validate_skill_md(root)
    validate_references(root)
    validate_openai_yaml(root)
    validate_evals(root)
    print(f"OK: forest-for-the-trees skill package validated at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
