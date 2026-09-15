# Skill Behavior and Trigger Evaluation

Use this reference when creating a skill, materially changing its behavior or description, changing reference loading, or deciding whether a candidate improved over a baseline.

## 1. Define the question first

Choose only the evidence needed for the current uncertainty:

| Question | Minimum useful evidence |
| --- | --- |
| Is the candidate structurally valid? | Frontmatter, paths, references, mirrors, and target-contract static checks. |
| Does target OpenCode discover it? | Actual listing or equivalent evidence from the target version/profile/scope. |
| Can the selected agent see/load it? | Effective permission plus runtime visibility/loading evidence. |
| Does the description discriminate correctly? | Positive cases and nearby negative cases that do not name the skill explicitly. |
| Does the loaded skill follow its contract? | Representative runtime outputs and necessary execution evidence. |
| Does reference routing work? | Trigger state plus evidence that the reference was read before the dependent judgment/action. |
| Is the new version better or behavior-preserving? | Comparable old/new runs on the same target and inputs. |
| Does the skill add value over baseline? | A baseline where the candidate is genuinely unavailable, not merely instructed to be ignored. |
| Is a subjective result acceptable? | Concrete outputs shown to the human reviewer. |

Do not run a benchmark solely because the tooling exists.

## 2. Build discriminating cases

For every affected behavior, record:

- input or prompt;
- required outcome;
- must/must-not constraints;
- observable evidence;
- pass/fail criterion.

Add negative/control cases when they distinguish the changed rule. Prefer an old-version FAIL/new-version PASS reproduction when the change fixes a known regression.

## 3. Separate automatic selection from explicit loading

A test that names the skill or directly invokes the skill tool proves only behavior after loading. To evaluate automatic selection, confirm model-facing visibility, use realistic requests that do not name the skill, include nearby non-trigger requests, and observe the actual selection behavior available from the target runtime.

If the runtime does not expose enough selection/loading evidence, report the limitation instead of inferring success.

## 4. Keep comparisons interpretable

Hold the target version, task input, model/variant, agent/profile, permissions, other instructions, and repository state constant unless one of those variables is the subject of the test. Use independent contexts for compared runs when practical.

Mandatory correctness and authorization constraints take priority over style scores or averages. If both candidates violate the contract, report both failures.

## 5. Use the bundled evaluation workflow only when needed

For repeated runs, explicit expectations, blind comparison, quantitative grading, or human-review viewer output, read `evaluation-workflow.md`. Read `schemas.md` before producing or consuming its structured JSON formats.

Stop when the decision has enough evidence. Preserve the version, cases, results, and remaining gaps needed to understand the conclusion; do not turn transient traces into runtime policy.
