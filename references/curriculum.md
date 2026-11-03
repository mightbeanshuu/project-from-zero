# Discover the project and order its lessons

## Evidence-backed stack map

Inspect code and existing documentation before choosing topics. Use this compact table:

| Technology/concept | Job in this project | Evidence (file/symbol) | Basics needed | Intermediate concepts | First build lesson |
| --- | --- | --- | --- | --- | --- |

Include the language, runtime, package/build tools, framework, data stores, relevant protocols, test tools, and deployment configuration only when present or intentionally proposed. Mark rows as verified, inferred, or proposed. A configuration file indicates intended configuration, not proof a service is deployed.

Identify the core domain independently of libraries: for example, scheduling rules, a rate-limit decision, a parser grammar, or cart totals. Explain the domain before the framework that hosts it. Avoid assuming every project is a web app.

## Roadmap

Use stable IDs such as `L01`, `L02`, with prerequisites expressed as IDs. A lesson may span several interactions. Keep phases readable and lesson goals small enough to demonstrate in one session; split a large lesson instead of adding unrelated responsibilities.

Each roadmap row contains:

| ID | Phase | Outcome the learner can demonstrate | Prerequisites | Files/artifacts | Verification/checkpoint |
| --- | --- | --- | --- | --- | --- |

Provide an approximate duration only when useful, labeled as an estimate. Explain why the next lesson comes next. Newly discovered prerequisites become new IDs; never renumber completed lessons or erase their evidence.

## Basics before intermediate concepts

Teach only concepts that matter to this project, using short prerequisite chains. Examples:

- Variables and functions → modules → entry point → package scripts.
- Values and collections → state changes → persistence → transactions.
- Function calls → callbacks/tasks → async flow → concurrency hazards.
- Input/output → protocol messages → request lifecycle → middleware/error paths.
- UI elements → events → state → rendering → component data flow.
- Processes and files → environment configuration → external service connection → failure recovery.

For each technology, explain its job, what runs it, its inputs/outputs, the simplest example, how this project uses it, and one limitation or alternative. Introduce intermediate details through an observable problem; avoid a catalogue of APIs.

Use prerequisite checks to calibrate, not as entrance exams. Let the learner show an existing understanding and skip repetitions explicitly. Beginners should see a useful tiny example early even when the main reconstruction begins later.

## Scaffolding and build order

1. Define the smallest behavior that can run locally.
2. Check available tool versions; explain any required setup before using it.
3. Create/open the learning root, then the smallest tool configuration and entry point required by that stack.
4. Run it and inspect output. Explain any generated files, scripts, and lockfiles that matter now.
5. Add a pure domain operation or the smallest relevant behavior and observe its result.
6. Connect the user-facing entry point to that behavior.
7. Add persistence, network calls, UI, validation, or other boundaries only in the order demanded by the chosen feature.
8. Exercise a successful flow and an appropriate failure flow; introduce focused tests when they verify real behavior.
9. Add later features by repeating this cycle; refactor when an actual responsibility needs separation.

This is a dependency strategy, not a universal file layout. Respect framework-required bootstrapping and explain generated scaffolding rather than pretending all files were handwritten. When a generator creates many files, identify required-now, generated-support, and later-use files, without dumping all of them into the lesson.

Before each addition, explain:

- What behavior is missing?
- Why does this file/module/dependency belong here?
- What must exist first?
- What new input/output or state change will become possible?
- How will we know the increment works?

Show an annotated tree of the files relevant now, marking new or changed files. Keep a separate final target tree if useful; never create empty layers merely to resemble a finished architecture.

## Existing repositories

Trace one representative execution from entry point to output, then infer a teachable reconstruction order. Record the reference path and commit if available. Re-read files when citing current line numbers. Use file plus symbol anchors when line numbers would become stale.

Distinguish simplified learning implementations from the reference behavior. Keep a short parity list: implemented, simplified, and deferred. Do not claim a small clone reproduces security, performance, concurrency, or operational properties that have not been implemented and checked.

## End-of-course evidence

Ask the learner to reconstruct one selected feature, explain the architecture, trace an input, diagnose a planted or real bug, and explain a design tradeoff. Save which tasks were actually demonstrated. Record remaining gaps and a revision route rather than declaring expertise from course completion alone.
