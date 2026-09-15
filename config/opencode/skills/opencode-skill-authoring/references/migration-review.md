# Migration, Responsibility, and Change Impact

Use this reference for cross-platform migration, absorbing another skill, renaming a skill, changing responsibility/authority, or modifying an existing skill with dependent consumers.

## 1. Compare exact sources

Separate:

- behavior still required from the current OpenCode implementation;
- the requested change;
- behavior contributed by another skill or platform;
- source-platform mechanics that must not be copied literally;
- target-OpenCode mechanics that must remain local;
- unverified claims or historical results.

Use the exact versions selected for the task. Do not substitute a summary for source files when deciding semantic deltas.

## 2. Classify each capability

| Decision | Meaning |
| --- | --- |
| Keep | The capability still belongs here and remains valid. Identify its owner and validation. |
| Merge | Two sources serve the same user intent with compatible rules. Keep one current authority. |
| Replace | The required result remains, but the old platform mechanism is wrong for the target. |
| Remove | The capability is obsolete, duplicate, or belongs elsewhere. Record the reason and impact. |
| Unresolved | Evidence or authorization is insufficient. Stop only work that depends on this decision. |

Do not merge merely because two files use similar words. Separate skills can remain correct when trigger branches, permissions, tools, or responsibility differ materially.

## 3. Handle names and authority deliberately

A skill name/ID is not immutable. Evaluate rename when responsibility has narrowed or expanded, the old ID creates ambiguity or collision risk, navigation already points to a different stable name, or a migration would otherwise leave competing authorities.

Do not rename only to make two platforms look identical. If a rename is chosen, update all direct consumers in the same coherent change: directory, frontmatter/ID representation, permission resource, references, review-mirror path, README/navigation, scripts or schemas that encode the old name, validation fixtures, and handoff instructions.

Never leave the old and new skills both active merely as aliases unless the target runtime has a deliberate alias mechanism and the user requires it.

## 4. Propagate impact along real dependencies

Start from the direct change nodes and inspect:

- `description`, skill ID/name, and `SKILL.md`;
- execution references and reference triggers;
- sibling review mirrors and their mapping owner;
- skill README and repository navigation;
- scripts/templates that encode the changed path or contract;
- skill sources, profile/agent integration, and permissions;
- install, validation, archive, or handoff procedures.

Any dependent item that must change becomes a new change node. Continue until evidence shows the next dependency is unaffected. Do not scan or refactor unrelated repository areas by default.

## 5. Preserve external provenance and useful tooling

If external material remains substantially incorporated, preserve the applicable license/notice and provenance. Existing deterministic helpers, evaluators, viewers, or benchmark tools should be removed only when their capability is no longer required, their owner has moved, or evidence shows they are stale or harmful. File age or lack of recent edits is not enough.

## 6. Migration completion

Before declaring the migration complete, account for every promised capability and every intentional removal. State where each impact branch stopped and why. Structural equivalence is not behavior validation; use `behavior-evaluation.md` when behavior or trigger quality changed.
