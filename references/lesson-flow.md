# Teach one lesson in small steps

## Lesson record

Save each lesson as `.project-learning/lessons/Lxx-short-title.md`. The record should support revision without the original chat. Create it when the lesson starts and grow it as teaching happens; do not pre-fill results or learner answers.

Use these sections when applicable:

1. Goal, phase, prerequisites, and current progress.
2. New terms and concepts, with plain meanings and tiny examples.
3. Where this fits in the project and why it is needed now.
4. Before/after file tree and architecture change, if any.
5. Numbered VS Code steps with exact paths and commands.
6. Code increments and block explanations.
7. Concrete execution trace and relevant diagram.
8. Expected result, observed result, verification status, and debugging notes.
9. Learner questions, answers, misconceptions, and pending doubts.
10. Checkpoint/task, actual learner evidence, and revision needs.
11. Exact next step, including file and current command/problem.

Keep future solutions separate from the active exercise so questions still test understanding. If a learner requests the answer, provide it and mark the exercise as worked-example reviewed rather than independently solved.

## VS Code workflow

Teach the relevant actions explicitly on first use:

- Open the correct folder through **File → Open Folder**; show its absolute path and distinguish reference vs learning workspaces. `code <path>` is an alternative only when that CLI is available.
- Find the Explorer, create the next file in the correct directory, and explain relative paths and file extensions.
- Open **Terminal → New Terminal**. State the required working directory before commands and verify it. Use commands appropriate to the actual OS/shell, with no unexpanded instructional placeholders presented as runnable commands.
- Explain the command name, important arguments/flags, package script, expected effects, and newly created files. Run commands individually when teaching cause and effect. Label commands as suggested, agent-executed, or learner-reported.
- Save edits, run/build/test using the project's selected tooling, and identify which terminal or process produced the output. Explain how to stop a long-running process.
- Show how to read the Problems panel, jump to a definition, and inspect a relevant error. Introduce only editor features useful for the current step.
- At a suitable debugging lesson, place a breakpoint, trigger execution, inspect locals/call stack, step over/into, and continue. Generate `launch.json` or `tasks.json` only when required for this stack and authorized working mode; explain each relevant field. If no debugger is available, trace values and logs instead.
- Explain the difference between application output, compiler/type-checker errors, dependency failures, and terminal/shell errors.

Do not install extensions by default. If a diagram preview is unavailable, the learner still gets its source and a readable text/ASCII version.

## Code blocks

Choose one coherent responsibility per increment, often 5–25 new meaningful lines; this is a pacing heuristic, not a hard limit. Provide complete runnable content for a tiny new file, or a precise patch/insertion point for an existing file. Never hide required code behind ellipses in a runnable example.

For each block explain:

| Element | What to explain |
| --- | --- |
| Location | Exact file, enclosing function/class, and insertion/replacement point. |
| Purpose | The responsibility this block adds and why it comes now. |
| Inputs and outputs | Values, types/shapes, return value, side effects, and errors. |
| Syntax | Newly encountered keywords, punctuation/operators, identifiers, imports, and API calls. |
| Execution | Actual runtime order, changed values, branches, callbacks/awaits, and control transfer. |
| Connections | Who calls this code and what it calls, including configuration dependencies. |
| Necessity | A realistic change/removal that would break behavior, or why an optional line is a convention. |
| Verification | Concrete input/action, expected result, observed result if available. |

Explain unfamiliar non-obvious lines individually. Group repeated syntax after checking that the learner understands it; offer full line-by-line expansion on request. Do not label every punctuation mark as a separate major concept, or imply there is only one valid implementation.

Use a small value-trace table when state changes are confusing:

| Step | Executing block | Value before | Operation | Value after / output |
| --- | --- | --- | --- | --- |

For async code, distinguish scheduling order from completion order and show where control waits or resumes. For configuration, explain who reads the key, when it is read, its scope, and the consequence of a wrong value.

## Two-way teaching

Ask one focused question at a time during a lesson, such as:

- Predict the output before we run this input.
- Which block receives this value next, and why?
- What happens if this condition is false?
- Explain this file's job without naming its framework.
- Make one small variation and explain the result.

Accept natural questions at any point; there is no required command syntax. Answer the immediate question before continuing the script. If it needs a large prerequisite detour, briefly explain the gap and offer a short bridge or a dedicated lesson. Save the interrupted position and unresolved portion.

When the learner answers incorrectly, identify the specific misconception, use a smaller counterexample, and ask a different application question. When they understand, advance without repeating a mandatory quiz ritual. A request to skip is respected and recorded honestly.

At lesson close, show what was covered, what ran, what the learner demonstrated, and the next step. Update saved state even if the lesson is unfinished. Do not say a command passed because its expected output looks plausible.
