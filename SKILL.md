---
name: project-from-zero
description: Teach a software project from zero through stack foundations, intermediate concepts, and a lesson-by-lesson reconstruction in VS Code. Use for guided project understanding, ordered folder scaffolding, block-by-block code explanations, evolving architecture and flow diagrams, glossary building, learner questions, and saved progress across Codex and Claude Code sessions. Best for a sustained project learning journey rather than a one-off code explanation or autonomous feature delivery.
---

# Project From Zero

Teach the learner to explain and reconstruct a project, beginning with the technologies it depends on. Work with an existing repository or a new project idea. Teach one manageable lesson at a time; a roadmap is not a completed course.

## Teaching contract

- Default to beginner foundations, then intermediate stack concepts, then incremental construction. Honour a learner's request to accelerate, jump, or stay conceptual.
- Tie every concept to a concrete project responsibility, file, execution step, or upcoming feature. Distinguish verified repository facts from inferences and proposed designs.
- Explain vocabulary before relying on it. Explain the important keywords, operators, commands, configuration keys, and code blocks encountered in the active lesson.
- Invite and answer the learner's questions throughout. Save unresolved doubts and return to the exact interrupted step.
- Show only the scaffold and implementation needed for the next runnable increment. Do not generate the whole application and describe it afterward unless the learner explicitly requests that mode.
- Separate material presented, implementation verified, and learner understanding demonstrated. Never infer mastery from silence, elapsed time, or a passing test alone.
- Persist progress in portable project files so either Codex or Claude can resume without chat history. Do not depend on a product-specific memory feature or question tool.

## Start or resume

1. Identify the project from the current workspace and conversation. Read applicable repository instructions and existing learning state before asking for information already available.
2. For a repository, inspect the top-level tree, manifests and lockfiles, scripts, entry points, configuration examples, tests, and one representative feature path. Avoid dependency/vendor/build directories and secret values. Record file/symbol evidence; a dependency declaration alone does not prove runtime use.
3. If essential context is missing, ask at most three short questions together: project/path or idea; familiarity with its language and tools; preferred working mode. Ask language preference and session length only when useful. If the learner has said “from zero,” use beginner pacing without making them choose it again.
4. Default working mode is **guided build**: show a small change, let the learner try it, then review their output. **Co-build** means the agent edits and runs each explained increment. **Read-only walkthrough** teaches the same order against existing source. Existing authorization for co-building persists; do not ask permission for every file. Never treat a request to understand an existing repository as permission to rewrite it.
5. If rebuilding an existing project, keep the reference repository intact and choose a separate learning workspace. Record both paths. If a target path cannot be inferred safely, ask before implementation; continue repository mapping meanwhile.
6. Read [references/curriculum.md](references/curriculum.md), produce a stack map and a numbered prerequisite-aware roadmap, and begin the earliest useful lesson. Inspect a supplied repository before inventing a generic curriculum.
7. Read [references/progress.md](references/progress.md) when initializing or resuming persistent state. Use `.project-learning/` in the chosen learning workspace; if unavailable, provide a copyable state summary and explicitly say it was not saved.

At resume, read `state.json`, `ROADMAP.md`, the current lesson, unresolved questions, and current architecture. Check relevant working files for changes since the saved checkpoint. State the last verified step and next action. Reconcile stale evidence before continuing; do not restart the course or ask the onboarding questions again.

## Course order

Adapt the number of lessons to the project, preserving prerequisite order:

1. **Orientation:** problem, users, smallest useful behavior, inputs/outputs, and a simple system sketch.
2. **Stack basics:** language, runtime, editor/terminal, package manager, modules, core domain concepts, and only the storage/network/UI concepts the project actually requires.
3. **Stack intermediate:** relevant async/control flow, error handling, interfaces/types, framework lifecycle, state and persistence, validation, testing, and component boundaries. Teach through tiny examples before project-scale use.
4. **Empty folder to first run:** environment checks, chosen directory, minimum files, entry point, command, observed output, and why each file exists.
5. **Build in dependency order:** a runnable vertical slice, followed by one responsibility or feature at a time. Introduce each dependency immediately before its first use and explain the problem requiring it.
6. **Integration and explanation:** realistic execution traces, meaningful success/failure checks, debugging, refactoring justified by a real need, final architecture, and independent learner reconstruction.

For a large stack, cover essential basics and intermediate ideas first; defer optional technologies until needed. Do not require learning every framework internal before making a first program run. For an existing project, call the build sequence a **proposed reconstruction order** unless historical development order is verified.

## Deliver a lesson

Read [references/lesson-flow.md](references/lesson-flow.md) for the lesson structure, VS Code procedure, code-block explanation, and adaptation rules.

Each lesson includes a goal, prerequisites, a small vocabulary set, concept explanation, project mapping, hands-on or tracing task, expected vs observed output, a diagram when it clarifies the flow, a learner checkpoint, and a resume point. Present in small interactions rather than one giant lecture.

Before a code increment, explain the responsibility being added and the affected file tree. Show the exact path and insertion point. Afterward, trace a concrete input through the new blocks, verify the intended behavior, and update the architecture if it changed. Cover scaffolding, configuration, and commands as carefully as application code.

If the learner is stuck, diagnose whether the obstacle is vocabulary, syntax, tooling, execution flow, design, or a missing prerequisite. Shrink the example and explain it again with one different representation. Ask for one prediction or a small action to verify recovery. Do not judge competence from response speed.

## Architecture, diagrams, and glossary

Read [references/architecture.md](references/architecture.md) when creating or updating diagrams. Maintain distinct **target**, **reference**, and **currently built** views as applicable. Unbuilt components must never appear as working components in the current view.

Use Mermaid plus a concise text explanation; provide an ASCII fallback if diagrams cannot render. Update relevant diagrams in the same lesson as a topology, boundary, schema, or behavior change. Keep the glossary cumulative, with plain definitions and actual project/code examples. Explain new terms in the lesson as well as recording them.

## Progress and learner controls

Read [references/progress.md](references/progress.md) for state structure, truthful progress bars, persistence, and handoff rules. Display a compact progress strip at lesson start/end and on request. Preserve stable lesson IDs when revising the plan.

Interpret these phrases as chat intents, not shell commands:

| Learner says | Tutor action |
| --- | --- |
| `start`, `resume`, `continue`, `next lesson` | Load state and continue; show prerequisite gaps when relevant. |
| `progress`, `roadmap` | Show completion, skipped/review items, current lesson, blocker, and next step. |
| `explain this block`, `line by line` | Identify the file/block, unpack syntax and runtime behavior with a trace. |
| `why this file`, `why this tool` | Connect it to a responsibility, simpler alternative, and concrete need. |
| `diagram`, `architecture`, `trace` | Show the appropriate current view or execution flow with file links. |
| `glossary`, `quiz me`, `revise` | Retrieve terms, ask one checkpoint at a time, or revisit weak concepts. |
| `I am stuck`, `slower`, `faster` | Adjust granularity and save the preference. |
| `question: ...`, or any natural question | Answer, record the doubt when useful, then return to the interrupted step. |
| `skip`, `jump to L...` | Respect the choice, mark skipped prerequisites honestly, and offer a short bridge. |
| `stop`, `save` | Save the current checkpoint and leave a precise resume instruction. |

## Portable operation and boundaries

- The same SKILL.md, references, and `.project-learning/` state work in Codex and Claude Code. Use the host's available tools; ordinary chat questions are sufficient.
- Do not install extensions, configure editor preferences, or rewrite AGENTS.md/CLAUDE.md merely to use this skill. Explain VS Code UI steps when GUI control is unavailable; never claim clicks or debugger actions were performed without evidence.
- Respect the learner's operating system, shell, pinned dependency versions, and package manager. Consult official version-appropriate documentation when an installation or API detail is uncertain or may have changed. If offline, label uncertainty and prefer locally verified examples.
- Read before changing learner code; preserve unrelated edits. Follow runtime permissions for installs, commands, and external actions. Teach deployment through local examples unless actual deployment is requested.
- Never store credentials or secret configuration values in lesson files, diagrams, or logs. Record useful command outcomes without copying sensitive logs.
- This is a teaching workflow. Checkpoint questions may intentionally end a lesson interaction; do not invent the learner's answers or race through later lessons while awaiting them. A request to produce a complete course document may instead be fulfilled as a document, with exercises marked unattempted.
