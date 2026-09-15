# Evaluation workflow

Use this reference when a skill change needs more than a smoke test: behavior comparison, regression coverage, human output review, or repeated benchmark runs.

## Decide what question the evaluation answers

Choose the lightest design that can answer the uncertainty:

- **Smoke test** — can OpenCode discover and load the skill, and do referenced scripts/files work?
- **Behavior test** — does the skill produce the expected observable result on representative prompts?
- **Migration test** — did a rewritten skill preserve or improve the behavior of the old version?
- **Baseline comparison** — does the skill add value over the same model without the skill?
- **Variance benchmark** — are repeated results stable enough to trust the comparison?
- **Human review** — is the subjective output actually better for the user?

Do not run a full benchmark when a smoke test or two representative cases answer the question.

## Test-case format

Store reusable cases in `evals/evals.json` when the evaluation is large enough to repeat. See `references/schemas.md` for the full schema.

Start with 2–3 realistic prompts. Include near misses or edge cases when discovery/triggering is the thing being tested.

Each case should record:

```json
{
  "id": 1,
  "prompt": "A realistic user request",
  "expected_output": "Observable properties of a successful result",
  "files": [],
  "expectations": []
}
```

Draft expectations after the task is understood. Prefer assertions that can be checked from outputs or artifacts; leave subjective qualities for human review.

## Workspace layout

Keep evaluation artifacts outside the runtime skill directory:

```text
<skill-name>-workspace/
└── iteration-1/
    └── eval-1/
        ├── eval_metadata.json
        ├── with_skill/
        │   └── run-1/
        │       ├── outputs/
        │       ├── grading.json
        │       └── timing.json
        └── without_skill/
            └── run-1/
                ├── outputs/
                ├── grading.json
                └── timing.json
```

Use descriptive eval names when useful instead of bare numbers.

Use these configuration directory pairs exactly:

- new skill vs no skill: `with_skill/` + `without_skill/`;
- existing-skill migration: `new_skill/` + `old_skill/`.

Do not use a generic `baseline/` configuration directory. The retained benchmark aggregator derives primary-vs-baseline order from sorted configuration directory names, and the viewer recognizes the four names above. Using the documented pairs keeps delta direction and viewer grouping correct.

## Make the comparison real

A baseline is valid only if the compared run cannot accidentally load the candidate skill.

For OpenCode, use one of these isolation methods:

- candidate config exposes/allows the candidate skill; baseline config omits it or sets it to `deny`;
- candidate uses the new skill directory; migration baseline uses a snapshot of the old version in an isolated config;
- for a simple one-off test, run a baseline agent whose permission set hides the skill and verify that the skill is absent from its available set.

Merely telling a baseline agent "do not use the skill" is not strong isolation if the skill remains available.

Keep model, task prompt, input files, and unrelated permissions the same across compared runs unless one of those variables is the thing being tested.

## Launch independent runs

When repeated independent execution is useful, launch candidate and baseline runs close together rather than finishing one configuration before starting the other. This reduces drift from changing environment or context.

For each run, give the executor:

- exact task prompt;
- input file paths;
- candidate skill name/path or the fact that it is hidden;
- output directory;
- artifacts the user cares about;
- a requirement to save evidence rather than only summarize it.

Do not let candidate and baseline runs share mutable output directories.

## Capture metadata

Write `eval_metadata.json` alongside each eval:

```json
{
  "eval_id": 1,
  "eval_name": "descriptive-name",
  "prompt": "The task prompt",
  "expectations": []
}
```

When the execution harness reports timing or token metadata, save it immediately in `timing.json`; do not invent unavailable metrics later.

## Grade against evidence

After runs finish:

1. Use `agents/grader.md` or an equivalent independent grader for explicit expectations.
2. For mechanically checkable properties, run a script or parser instead of eyeballing the result.
3. Save `grading.json` using the exact schema in `references/schemas.md`.
4. Every judgment should cite concrete output evidence; missing evidence is not a pass.

The viewer expects expectation entries with `text`, `passed`, and `evidence` fields.

## Aggregate repeated runs

When multiple runs per configuration matter, aggregate them with:

```bash
python scripts/aggregate_benchmark.py \
  <workspace>/iteration-N \
  --skill-name <skill-name>
```

This writes benchmark data with mean/stddev and candidate-vs-baseline deltas. Read `references/schemas.md` before manually constructing `benchmark.json`; the viewer relies on its field names.

Use `agents/analyzer.md` to look for patterns that averages hide:

- expectations that pass equally with and without the skill;
- high-variance or flaky cases;
- one case dominating the aggregate;
- quality improvements that cost disproportionate time/tokens;
- unsupported causal explanations.

## Human review

For subjective output, present the actual examples before revising the skill.

Headless/static mode:

```bash
python eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name <skill-name> \
  --benchmark <workspace>/iteration-N/benchmark.json \
  --static <workspace>/iteration-N/review.html
```

Omit `--benchmark` when no quantitative grading was run.

For later iterations, pass `--previous-workspace <workspace>/iteration-(N-1)` so the reviewer can compare outputs and feedback.

Read the user's feedback before revising. Empty feedback on a reviewed case can be treated as no requested change; do not manufacture a problem solely to keep iterating.

## Iterate without overfitting

When a case fails:

- generalize from the failure rather than adding one-off wording for that exact prompt;
- inspect the execution path, not only the final output;
- bundle repeated deterministic work into a script when several runs independently reinvent it;
- prune instructions that cause wasted steps or conflict with the intended workflow;
- rerun the affected representative cases after each material change.

Stop when the user is satisfied, the representative failures are resolved, or new iterations stop producing meaningful improvement.

## Blind comparison

For a high-value old-vs-new decision, use `agents/comparator.md` to compare anonymized outputs without revealing which version produced each result. Then use `agents/analyzer.md` to explain evidence-backed differences.

Blind comparison is optional. Human review plus direct behavioral checks is usually enough.
