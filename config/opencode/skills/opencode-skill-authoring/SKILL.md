---
name: opencode-skill-authoring
description: Create, review, migrate, validate, and improve skills that OpenCode will discover or execute. Use for SKILL.md changes, skill resources, discovery or permission wiring, cross-platform skill migration, behavioral evaluation, and skill delivery; do not use merely to run an existing skill or for unrelated OpenCode configuration.
---

# OpenCode Skill Authoring

Create and maintain OpenCode skills as small, testable instruction systems. Preserve useful behavior, adapt platform mechanics to the actual target runtime, and keep one clear runtime authority for each behavior.

## Terms

- **target OpenCode**: the exact OpenCode version or fork, profile, skill source, and scope that will discover, validate, or execute the artifact.
- **runtime source**: English files that OpenCode or its agents may read as instructions, including `SKILL.md`, execution references, and evaluation agent prompts.
- **review mirror**: the synchronized Taiwan Traditional Chinese copy under the sibling `skill-reviews/<skill-id>/` tree. It is never a second runtime authority.
- **reference trigger**: an observable task, artifact, or state condition that makes a reference required before a dependent judgment or action.
- **target validation**: evidence obtained from the target OpenCode runtime rather than inferred from copied files or a different version.

## Core workflow

1. **Recover intent and authorization.** Read the conversation and exact current files first. Reuse already-decided requirements. Distinguish review, candidate editing, formal source editing, installation, commit, push, and deployment authorization.
2. **Identify the target runtime.** Determine the target OpenCode version or fork, actual skill source, profile or agent, effective permissions, and loading path when those facts affect the result. Do not assume the authoring environment and target runtime are the same.
3. **Define observable success.** Identify representative requests, required behavior, important constraints, and the evidence that would demonstrate success.
4. **Inspect before editing.** For an existing skill, read its `SKILL.md`, triggered references, relevant scripts, permission wiring, and directly dependent navigation. Separate live behavior from stale or platform-specific machinery.
5. **Classify the change.** For migrations or absorbed guidance, distinguish shared behavior intent from source-platform mechanics and target-OpenCode mechanics. Preserve the intent; reimplement mechanics for the target runtime.
6. **Choose the smallest coherent runtime surface.** Keep always-needed rules in `SKILL.md`; place conditional detail behind explicit reference triggers; use deterministic scripts only when they materially improve reliability.
7. **Choose the skill ID deliberately.** A skill may be renamed when evidence shows that a new ID better represents responsibility, avoids collision, or resolves authority drift. Do not rename merely for cosmetic consistency, and do not preserve an obsolete name as a blanket rule. When the ID changes, update every direct consumer in the same coherent change.
8. **Implement one runtime authority.** Do not leave competing current authoring skills, duplicate mandatory rules, or a review mirror that can be loaded as runtime policy.
9. **Validate mechanics and behavior.** Check structure first, then discovery, permissions, loading, reference use, and changed behavior according to the target runtime and actual impact.
10. **Deliver with evidence.** Report separately what was reviewed, modified, statically checked, behavior-tested, loaded in the target runtime, installed, committed, pushed, or deployed.

## Authoring rules

- Confirm the exact source version before precise comparison. A summary, old export, or similarly named skill is not a substitute for the specified source.
- A skill cannot grant permissions. If a required action is denied, do not bypass the restriction through another tool, wrapper, agent, or equivalent command.
- `description` is the model-facing discovery pointer when the target runtime advertises skills by description. Make it specific enough to cover intended requests and exclude nearby tasks.
- Do not treat file existence, discovery, permission, body loading, reference loading, and correct behavior as the same state. Each claim requires evidence for that state.
- Supporting files are conditional detail, not a reason to preload the whole skill directory. Every execution reference must have an observable trigger, exact path, read-before point, and missing-reference behavior.
- Keep OpenCode runtime mechanics in this skill. Use `progressive-context-design` for broader durable information architecture when it is available, but do not make this skill unusable if that sibling skill is absent.
- Keep behavioral evaluation proportional to the uncertainty. Do not benchmark by habit.
- Preserve applicable licenses and provenance when external material remains incorporated.

## Validation

For every changed skill:

1. Parse the final frontmatter and check the target runtime's actual contract.
2. Check every runtime-relative reference and supporting file used by the changed path.
3. Run syntax checks for changed scripts.
4. Use `scripts/quick_validate.py` only as a structural helper with the matching contract; it is not the OpenCode runtime parser.
5. If discovery, skill ID, source registration, or permissions changed, verify them with the actual target OpenCode binary/config when that runtime is available.
6. Test changed behavior with representative cases. Use old/new or with/without comparisons only when they answer a real uncertainty.
7. Inspect the final diff for unrelated changes, stale IDs or paths, duplicate authority, and obsolete platform assumptions.

## Evaluation tooling

For non-trivial comparisons, repeated runs, quantitative grading, or human review, read `references/evaluation-workflow.md` before executing the evaluation. Use `references/schemas.md` for the bundled workspace and JSON formats when those formats are needed.

The bundled helpers remain optional:

- `agents/grader.md` evaluates explicit expectations against evidence.
- `agents/comparator.md` performs blind output comparison.
- `agents/analyzer.md` analyzes comparison results without inventing causes.
- `scripts/aggregate_benchmark.py` summarizes repeated runs when variance matters.
- `eval-viewer/generate_review.py` prepares human-review output when concrete examples should be inspected.

Do not run the full evaluation stack merely because it exists.

## Reference triggers

Read every triggered reference before the dependent judgment or action. Already-read content can be reused while its version and conditions remain unchanged.

| Trigger | Required reference and read-before point |
| --- | --- |
| Creating or changing metadata, skill ID/name, discovery, skill sources, permission wiring, agent/profile integration, or any behavior that depends on OpenCode version | Read `references/target-runtime.md` before choosing the runtime contract or integration. |
| Evidence shows the target still uses legacy V1 skill/config mechanics, or the task explicitly covers V1 or V1-to-V2 migration | Read `references/legacy-v1.md` before making V1-specific or compatibility decisions. |
| Creating, modifying, renaming, deleting, or reviewing English runtime text, Taiwan Traditional Chinese review mirrors, or a skill README | Read `references/bilingual-output.md` before deciding source/mirror placement or synchronization. |
| Migrating from another platform or skill, absorbing guidance, renaming a skill, changing responsibility/authority, or modifying an existing skill with dependent consumers | Read `references/migration-review.md` before deciding keep/merge/replace/remove or the impact boundary. |
| Creating a new skill, materially changing behavior or description, changing reference loading, or judging whether a candidate is better than a baseline | Read `references/behavior-evaluation.md` before designing or interpreting the evaluation. |
| Running a non-trivial comparison, repeated benchmark, bundled grader/comparator/analyzer workflow, or human-review viewer | Read `references/evaluation-workflow.md` before running it; read `references/schemas.md` before producing or consuming its structured formats. |
| Completing a review, packaging a candidate, handing work to another environment or AI, or reporting discovery/loading/behavior status | Read `references/validation-handoff.md` before the final conclusion or handoff. |

If a required reference is missing or unreadable, stop only the dependent judgment or action, report the gap, and continue independent work.

## Completion

A skill change is complete only to the extent supported by evidence. A coherent candidate can be complete as an authored artifact without being installed or runtime-validated. Do not convert a static check into a runtime claim, or a runtime load into a behavior claim.
