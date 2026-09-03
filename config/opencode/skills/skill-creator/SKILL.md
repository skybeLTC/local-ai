---
name: skill-creator
description: Create, review, migrate, and improve OpenCode skills. Use when a user wants to add or edit a SKILL.md, merge guidance from another skill, design skill resources, validate skill structure, test skill behavior, benchmark a skill, or improve when and how a skill should be discovered.
---

# Skill Creator

Create or improve OpenCode skills as small, testable instruction systems. Preserve useful existing behavior, remove stale platform assumptions, and keep the runtime surface as small as the task allows.

## Core workflow

1. **Recover intent.** Read the conversation and existing files first. Reuse already-known requirements instead of asking again.
2. **Define observable success.** Identify representative inputs, expected outputs or behavior, important constraints, and what evidence will show the skill works.
3. **Inspect before editing.** For an existing skill, read its `SKILL.md`, referenced files, permission wiring, and any scripts that implement behavior. Separate live behavior from stale or platform-specific machinery.
4. **Plan the smallest skill surface.** Decide what belongs in `SKILL.md`, what should be a referenced file, what requires a deterministic script, and what should remain discoverable from the environment instead of being copied into docs.
5. **Draft or migrate.** Make the smallest coherent change that satisfies the requested behavior. Preserve the skill name unless the user explicitly wants a rename.
6. **Validate mechanics.** Check frontmatter, references, scripts, and OpenCode discovery/permissions where relevant.
7. **Test behavior.** Run representative cases. Use with-skill vs baseline or old-vs-new comparisons when the comparison answers a real question; do not benchmark by habit.
8. **Get human review when quality is subjective.** Surface concrete outputs, not just scores.
9. **Iterate from evidence.** Change the skill because a test, review, or observed failure justifies it—not because more instructions feel safer.

A skill is done when its intended cases are supported by direct evidence, its trigger/discovery behavior is understood, and no known stale or contradictory instructions remain in its active path.

## OpenCode skill mechanics

OpenCode discovers `SKILL.md` files from configured skill roots and supported external skill roots. In the currently tested runtime, symlinks are followed during discovery. Verify the current binary/source when discovery behavior is material to a migration.

For runtime behavior, the important frontmatter fields are:

- `name` — required skill identifier.
- `description` — the model-facing context pointer used to decide when the skill is relevant.

OpenCode's current skill parser uses `name` and optional `description`. Extra frontmatter may be preserved for portability, but do not rely on it to control OpenCode behavior unless the current OpenCode implementation explicitly supports it.

Permission semantics matter separately from frontmatter:

- `allow` — the agent can load the skill without an approval prompt.
- `ask` — the skill remains available to the agent, but loading it requires approval.
- `deny` — the skill is filtered from that agent's available skills.

`allow` does **not** guarantee invocation. It only permits loading. Model-driven invocation depends on the task matching the available skill metadata and the model choosing to call the skill tool.

Do not use Claude-specific fields such as `disable-model-invocation` as if they controlled OpenCode. If a skill should be hidden from an agent, express that with OpenCode permission rules.

## Writing for agents

Use these principles when writing `SKILL.md`, `AGENTS.md`, prompts, or referenced agent documentation.

### Context pointers

A pointer is always-loaded text that tells the agent when to reach additional material: for example, a skill description or an `AGENTS.md` line that names another document.

A strong pointer does two jobs:

- says what the target material is;
- names the distinct situations that should cause the agent to reach it.

Keep pointers short because they spend context on every turn. Front-load the discriminating concept. Do not pad them with synonyms that all describe the same trigger branch.

### Information hierarchy

Put information at the lowest level that still makes the workflow reliable:

1. **In-file steps** — actions needed by nearly every run, in execution order.
2. **In-file reference** — rules or facts consulted while executing those steps.
3. **Disclosed reference** — branch-specific or detailed material behind an explicit pointer to another file.

Use progressive disclosure when branch-specific reference material buries the main workflow. Keep a concept's definition, rules, and caveats together rather than scattering them across the skill.

### Completion criteria

Each meaningful step should have a checkable stopping condition. Prefer criteria that are both observable and exhaustive.

Weak: `understand the issue`.

Stronger: `identify the failing path, the evidence supporting it, and the smallest command that reproduces the failure`.

If an agent repeatedly rushes a step because later steps are visible, first sharpen the completion criterion. Split the sequence only when a real context boundary improves execution.

### Leading words

Prefer compact, established concepts that carry useful prior meaning—such as `tight loop`, `source of truth`, `red`, `rollback`, or `blast radius`—when they replace repeated explanations without losing precision.

Do not invent jargon merely to save tokens. A term earns its place only if it consistently sharpens behavior.

### Positive targets and guardrails

State the desired behavior directly. Use prohibitions for real guardrails, and pair them with the positive target when useful.

Example: prefer `keep edits scoped to the requested files; preserve adjacent formatting` over a long list of unrelated things not to touch.

### Pruning

Treat every instruction as carrying maintenance and attention cost.

- Keep each meaning in one authoritative place.
- Treat the environment—config, directory layout, `--help`, schemas—as a source of truth; do not cache easy lookups in prose.
- Remove stale branches, duplicated explanations, and instructions that do not change behavior.
- Shorten by deleting whole no-op sentences before micro-editing wording.

## Designing the skill

### Capture intent

Before writing, establish from existing context or targeted questions:

- What task should the skill enable?
- Which concrete user requests should make it relevant?
- What output or state change is expected?
- What must never be silently skipped?
- Which tools, files, connectors, or environment assumptions are real dependencies?
- What evidence would convince the user the skill works?

Ask only for material gaps. Do not repeat questions already answered in the conversation or source files.

### Choose supporting resources

Use supporting files only when they improve reliability or context efficiency:

- `scripts/` — deterministic or fragile operations worth implementing once.
- `references/` — detailed rules, schemas, examples, or branch-specific knowledge loaded only when needed.
- `assets/` — templates or output resources not intended as reasoning context.
- `agents/` — local instructions for specialized evaluation or comparison roles when the host workflow supports them.

Prefer a small `SKILL.md` that points clearly to deeper material over one large file that forces every branch through the same context.

### Description design

The description is the top-level discovery pointer. It should identify the skill's task and the distinct trigger branches that genuinely need it.

Good descriptions are specific enough to separate nearby skills but broad enough to cover the intended cases. Do not try to force invocation with repetitive synonyms or claims like "always use this" unless that behavior is truly required and tested.

When description behavior matters, test realistic near-miss cases as well as obvious positives. OpenCode does not provide a guaranteed auto-trigger contract; evaluate actual behavior instead of treating wording rules as certainty.

## Validation

For every changed skill:

1. Run `scripts/quick_validate.py <skill-directory>` when this skill's validator is available.
2. Check every referenced relative file exists.
3. Run syntax checks for changed scripts (`python -m py_compile`, `bash -n`, or the appropriate language check).
4. If discovery or permissions changed, verify with the actual OpenCode binary/config rather than inferring from JSON alone.
5. Inspect the final diff for unrelated changes and stale platform references.

The local validator is a structural sanity check, not the OpenCode runtime parser. Runtime behavior is decided by OpenCode itself.

## Behavioral evaluation

Use evaluation when it answers a concrete uncertainty: whether instructions improve results, whether a migration preserved behavior, whether a description has useful discrimination, or whether a script is reliable. For non-trivial comparisons, repeated runs, or human review, read `references/evaluation-workflow.md` before executing the evaluation.

### Test cases

Keep a small initial set of representative prompts. For each case record:

- prompt/input;
- expected result or observable properties;
- relevant files;
- explicit expectations that can be checked from output or artifacts.

Store structured cases using `references/schemas.md` when quantitative comparison is useful.

### With-skill and baseline comparisons

For objectively testable workflows, compare independent runs when practical:

- **with skill** vs **without skill** to measure whether the skill adds value;
- **new version** vs **old version** when migrating or tightening an existing skill.

Use independent agents/runs where available so the evaluator is not simply grading its own remembered draft. Match model and permissions when comparing configurations unless model variance is itself the question.

Do not add baseline runs for subjective work unless they help the user decide something.

### Human review

For outputs where quality is subjective, put the examples in front of the user early. The bundled review viewer can aggregate run outputs and feedback:

```bash
python eval-viewer/generate_review.py <workspace-path> --static <output.html>
```

Use the interactive server mode only when the environment supports opening a browser and the user benefits from it.

Read the resulting feedback before changing the skill. Human review is evidence; do not replace it with aggregate scores.

### Grading and benchmarking

The bundled evaluation roles are optional helpers:

- `agents/grader.md` — grade explicit expectations against evidence.
- `agents/comparator.md` — blind comparison of two outputs.
- `agents/analyzer.md` — analyze benchmark patterns without inventing causes.

`aggregate_benchmark.py` can summarize repeated run results when variance matters. Use `references/schemas.md` for the expected JSON layouts.

## Migrating an existing skill

When absorbing another skill into an existing one:

1. List the capabilities of both skills.
2. Mark each source section as **keep**, **merge**, **replace**, or **drop**.
3. Preserve behavior that is still valuable even if its original implementation is platform-specific.
4. Replace host-specific mechanics with current OpenCode mechanics instead of transliterating names.
5. Remove scripts and references that become unreachable after the migration.
6. Preserve applicable licenses and record third-party provenance when substantial external material is incorporated.
7. Validate the resulting skill as one coherent workflow, not as two documents pasted together.

Prefer merging when two skills serve the same user intent but one contributes principles and the other contributes execution machinery. Prefer separate skills when they have independent trigger branches or materially different permissions/tool needs.

## Platform-specific automation

Target the current OpenCode CLI, discovery rules, permission model, and event behavior. The previous automatic description optimizer depended on a different host's command files, subprocess CLI, and stream events, so it is intentionally not part of this OpenCode-native workflow. If description optimization is reintroduced later, implement and validate it against the current OpenCode CLI/event model first.

## Final review

Before reporting a skill migration complete, verify:

- the active workflow is internally consistent;
- descriptions and permissions reflect actual OpenCode semantics;
- referenced files and retained scripts are reachable and validated;
- obsolete host-specific code is gone from the active skill path;
- license/provenance obligations are preserved;
- tests support the claims being made;
- remaining limitations are stated explicitly.
