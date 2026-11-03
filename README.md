# Project From Zero

A reusable teaching skill for Codex and Claude Code. Learn a software project from its technology foundations, then reconstruct it incrementally in VS Code.

## What it teaches

- Stack basics and intermediate concepts in prerequisite order.
- Folder scaffolding and a first runnable program, followed by small feature increments.
- Block-by-block code explanations, vocabulary, commands, and execution traces.
- Architecture diagrams that evolve with the implementation.
- Learner questions, checkpoints, revision notes, and saved lesson progress.

Choose guided practice, agent-assisted building, or a read-only walkthrough. Progress distinguishes completed lessons from understanding demonstrated by the learner.

## Install

Clone this repository into the skill directory for your tool. These commands assume Git and a macOS/Linux shell; use an unused destination.

For Codex (default configuration):

```sh
git clone https://github.com/mightbeanshuu/project-from-zero.git ~/.codex/skills/project-from-zero
```

For Claude Code:

```sh
git clone https://github.com/mightbeanshuu/project-from-zero.git ~/.claude/skills/project-from-zero
```

If you use a custom Codex home directory, place the skill in its `skills` directory instead. A private repository requires GitHub access. You can also copy the complete skill folder to these locations. Start a new session after installation if the skill is not yet listed.

## Use

Ask either agent:

> Use project-from-zero to teach me the project at `/path/to/project`. Start from basics, explain every code block, and guide me lesson by lesson.

You can also begin with a project idea instead of an existing repository. During lessons, ask naturally: “explain this block,” “show the architecture,” “I am stuck,” “quiz me,” “progress,” or “resume.”

The tutor records the course in `.project-learning/` inside the chosen learning workspace. Codex and Claude can resume from those same files. For a reconstruction, the reference project and learning workspace remain separate.

## Files

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Main tutor instructions and workflow. |
| `references/curriculum.md` | Repository discovery, prerequisites, and build order. |
| `references/lesson-flow.md` | Lesson structure, VS Code steps, and code explanations. |
| `references/architecture.md` | Diagrams, architecture evolution, and glossary. |
| `references/progress.md` | Persistent state, completion rules, questions, and handoffs. |
| `scripts/progress.py` | Read-only progress display and state checks. |
| `agents/openai.yaml` | Codex skill display metadata. |

The progress helper uses Python 3 and the standard library. After the tutor creates a course state file, run from this repository:

```sh
python3 scripts/progress.py /path/to/learning-project/.project-learning/state.json
```

Python is optional for the teaching workflow; the tutor can calculate progress without the helper. Diagrams use Mermaid source with a text fallback when rendering is unavailable.
