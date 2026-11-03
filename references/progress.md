# Portable progress and handoff

## Workspace records

Create these under the learning workspace as they become relevant:

```text
.project-learning/
  state.json           Machine-readable lesson status and resume point
  ROADMAP.md           Outcomes, prerequisites, and planned build order
  PROGRESS.md          Current bars and chronological meaningful outcomes
  ARCHITECTURE.md      Current, reference, and target views with mappings
  GLOSSARY.md          Terms and code vocabulary encountered so far
  QUESTIONS.md         Learner doubts, answers, and unresolved questions
  lessons/             One growing revision record per started lesson
  diagrams/            Mermaid sources for actual milestones
```

`state.json` is the authority for statuses and counts. Narrative files contain evidence and explanations. Do not overwrite existing records or create competing root-level progress files. If other tutors' logs exist, link relevant prior material and carry forward only confirmed progress. Do not automatically modify repository instruction files or `.gitignore`.

## State structure

Use schema version 1. This illustrative one-lesson state is valid; replace its project values and populate the real roadmap when starting a course:

```json
{
  "schema_version": 1,
  "project": {
    "name": "Example project",
    "reference_root": null,
    "learning_root": "/absolute/path/to/learning-project",
    "reference_revision": null
  },
  "learner": {
    "level": "beginner",
    "mode": "guided-build",
    "language": "English",
    "session_minutes": null,
    "preferences": [],
    "revisit": []
  },
  "current_lesson": "L01",
  "resume": {
    "step": "Explain the smallest useful project behavior",
    "file": null,
    "blocker": null,
    "next_action": "Ask the learner to identify an input and output"
  },
  "lessons": [
    {
      "id": "L01",
      "title": "Project orientation",
      "phase": "orientation",
      "prerequisites": [],
      "status": "in_progress",
      "checkpoint": "pending",
      "verification": "not_applicable",
      "evidence": []
    }
  ],
  "open_questions": [],
  "updated_at": null
}
```

Use actual timestamps with timezone when saving. Keep project paths explicit; reference_root may be null for a new project. Store compact learning preferences and gaps, never sensitive personal data or secret logs.

Fields and transitions:

- `status`: `not_started`, `in_progress`, `completed`, `needs_review`, or `skipped`.
- `checkpoint`: `pending`, `demonstrated`, or `waived`. Use `demonstrated` only for an actual learner explanation/application. Record a requested skip or reveal without inventing evidence.
- `verification`: `pending`, `passed`, `failed`, or `not_applicable`. Theory can be not_applicable. Implementation verification requires observed results or explicit learner reports, labeled accordingly.
- `evidence`: short strings recording what happened and linking to lesson notes, learner responses, or verification results. Evidence for a waived checkpoint records the learner's request.

A lesson becomes `completed` when its planned material/task is finished, its checkpoint is demonstrated or explicitly waived, and its required verification is passed (or not_applicable for theory). Otherwise keep it in progress, needs_review, or skipped. A waived checkpoint counts toward course completion but not demonstrated understanding. Move a lesson to needs_review when evidence reveals a relevant gap; record why. Do not erase its earlier history.

Stable lesson IDs must be unique and prerequisites must reference existing IDs without cycles. When the learner jumps, keep incomplete prerequisites visible; do not silently complete them. `current_lesson` may be null when nothing is active.

## Progress bars

Let N be the total number of planned lessons, C the number with status completed, and D the completed lessons whose checkpoint is demonstrated. Display:

```text
Course:        [######--------------] 30% (3/10 completed)
Demonstrated:  [####----------------] 20% (2/10 demonstrated)
Current: L04 — First runnable program
Skipped: 1 | Needs review: 1
Next: Create the entry point and explain its first block
```

Use 20 cells, filling `floor(20 * numerator / N)`; percentage is `floor(100 * numerator / N)`. For N=0 show “Roadmap not planned yet,” not 100%. Skipped and needs_review lessons remain in the denominator. The demonstrated bar measures completed lesson checkpoints, not a claim of overall technical mastery.

Explain denominator changes when lessons are added or removed. Avoid an invented percentage within an unfinished lesson; use named steps unless actual task counts are recorded. Show verification status separately when relevant.

For consistent rendering and state checks, use the bundled helper if Python 3 is available:

```text
python3 <installed-skill-directory>/scripts/progress.py <learning-root>/.project-learning/state.json
```

Resolve the two paths before suggesting an executable command. The script is read-only, uses only the standard library, and does not create course state. If Python is unavailable, apply the same calculations manually; do not install a runtime just to show a bar.

## Save and resume

After a meaningful step, record command purpose, execution source (agent/learner/suggested), outcome, changed files, dependency changes, failed attempts, and next action in PROGRESS.md. Log outcomes needed to resume, not every read-only discovery command. Preserve actual commands when useful, redacting secrets.

Update the current lesson, glossary, questions, architecture, and state as applicable. Write valid JSON completely, using an atomic replacement where available. Read before writing. If another agent/session changed state, reconcile rather than overwrite; do not run parallel tutors against the same state file.

At start/end and on a handoff between Codex and Claude, show the learning workspace path, lesson, last verified step, unresolved question/blocker, and exact next action. Both agents read the same files; no cloud synchronization or hidden memory is assumed. If the workspace is moved, reconcile paths before executing commands.

## Question log

Give substantive doubts stable IDs (`Q01`, `Q02`, ...). Record the learner's question, associated lesson/file/block, explanation, status (open/answered/revisit), and follow-up evidence. Add open/revisit IDs to `open_questions` in state. “Answered” means an explanation was provided; it does not by itself demonstrate learner understanding.

For end-of-course revision, use these questions, needs_review lessons, and learner gaps to choose exercises. Do not manufacture questions the learner never asked; mark tutor-generated practice separately.
