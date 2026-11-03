#!/usr/bin/env python3
"""Validate and display a project-from-zero progress file; never mutate it."""

import argparse
import json
import sys
from pathlib import Path


STATUSES = {"not_started", "in_progress", "completed", "needs_review", "skipped"}
CHECKPOINTS = {"pending", "demonstrated", "waived"}
VERIFICATIONS = {"pending", "passed", "failed", "not_applicable"}


def validate(state):
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        raise ValueError("Expected a state object with schema_version 1")
    lessons = state.get("lessons")
    if not isinstance(lessons, list):
        raise ValueError("lessons must be a list")
    indexed = {}
    for lesson in lessons:
        if not isinstance(lesson, dict):
            raise ValueError("Each lesson must be an object")
        ident = lesson.get("id")
        if not isinstance(ident, str) or not ident.strip() or ident in indexed:
            raise ValueError("Lesson IDs must be nonempty, unique strings")
        for key in ("title", "phase"):
            if not isinstance(lesson.get(key), str) or not lesson[key].strip():
                raise ValueError(f"{ident}: {key} must be a nonempty string")
        for key, choices in (("status", STATUSES), ("checkpoint", CHECKPOINTS),
                             ("verification", VERIFICATIONS)):
            value = lesson.get(key)
            if not isinstance(value, str) or value not in choices:
                raise ValueError(f"{ident}: invalid {key}")
        prerequisites = lesson.get("prerequisites")
        evidence = lesson.get("evidence")
        for key, value in (("prerequisites", prerequisites), ("evidence", evidence)):
            if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
                raise ValueError(f"{ident}: {key} must be a list of strings")
        if len(prerequisites) != len(set(prerequisites)):
            raise ValueError(f"{ident}: duplicate prerequisites")
        if lesson["status"] == "completed":
            if lesson["checkpoint"] == "pending":
                raise ValueError(f"{ident}: completed lesson needs a checkpoint result")
            if lesson["verification"] not in {"passed", "not_applicable"}:
                raise ValueError(f"{ident}: completed lesson has unresolved verification")
            if not any(item.strip() for item in evidence):
                raise ValueError(f"{ident}: completed lesson needs recorded evidence")
        indexed[ident] = lesson

    for ident, lesson in indexed.items():
        for dependency in lesson["prerequisites"]:
            if dependency not in indexed:
                raise ValueError(f"{ident}: unknown prerequisite {dependency}")

    visiting, visited = set(), set()

    def visit(ident):
        if ident in visiting:
            raise ValueError(f"Prerequisite cycle at {ident}")
        if ident in visited:
            return
        visiting.add(ident)
        for dependency in indexed[ident]["prerequisites"]:
            visit(dependency)
        visiting.remove(ident)
        visited.add(ident)

    for ident in indexed:
        visit(ident)
    current = state.get("current_lesson")
    if current is not None and (not isinstance(current, str) or current not in indexed):
        raise ValueError("current_lesson must be null or an existing lesson ID")
    resume = state.get("resume", {})
    if not isinstance(resume, dict):
        raise ValueError("resume must be an object")
    for key in ("next_action", "blocker"):
        if resume.get(key) is not None and not isinstance(resume[key], str):
            raise ValueError(f"resume.{key} must be text or null")
    return indexed


def bar(count, total):
    filled = 20 * count // total
    return f"[{'#' * filled}{'-' * (20 - filled)}] {100 * count // total}% ({count}/{total})"


def render(state):
    indexed = validate(state)
    lessons = list(indexed.values())
    total = len(lessons)
    if not total:
        return "Roadmap not planned yet."
    completed = [lesson for lesson in lessons if lesson["status"] == "completed"]
    demonstrated = sum(lesson["checkpoint"] == "demonstrated" for lesson in completed)
    skipped = sum(lesson["status"] == "skipped" for lesson in lessons)
    review = sum(lesson["status"] == "needs_review" for lesson in lessons)
    lines = [f"Course:       {bar(len(completed), total)} completed",
             f"Demonstrated: {bar(demonstrated, total)} demonstrated",
             f"Skipped: {skipped} | Needs review: {review}"]
    current = state.get("current_lesson")
    if current:
        lesson = indexed[current]
        lines.append(f"Current: {current} — {lesson['title']} ({lesson['status']})")
        lines.append(f"Verification: {lesson['verification']}")
        gaps = [ident for ident in lesson["prerequisites"]
                if indexed[ident]["status"] != "completed"]
        if gaps:
            lines.append("Incomplete prerequisites: " + ", ".join(gaps))
    else:
        lines.append("Current: none")
    resume = state.get("resume", {})
    if resume.get("blocker"):
        lines.append(f"Blocker: {resume['blocker']}")
    if resume.get("next_action"):
        lines.append(f"Next: {resume['next_action']}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state", type=Path, help="Path to .project-learning/state.json")
    args = parser.parse_args()
    try:
        state = json.loads(args.state.read_text(encoding="utf-8"))
        print(render(state))
    except (OSError, ValueError, RecursionError) as error:
        print(f"Progress error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
