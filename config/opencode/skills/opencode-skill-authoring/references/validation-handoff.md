# Validation and Handoff

Use this reference before final conclusions, packaging, installation instructions, or handoff to another environment or AI.

## 1. Validate the final source

Check the final candidate, not an intermediate draft:

- frontmatter parses and matches the actual target contract;
- skill ID/name, directory, description, and permission resource are internally consistent;
- all runtime-relative references resolve;
- every execution reference is reachable from an observable trigger;
- `SKILL.md` owns the minimum mandatory workflow and README does not hide required runtime policy;
- English runtime sources and `skill-reviews/<skill-id>/` mirrors have complete structural mapping and no runtime dependency on the mirror tree;
- renamed IDs/paths do not survive in direct consumers unless intentionally historical;
- changed scripts pass the appropriate syntax checks;
- unrelated generated files, cache, secrets, Git metadata, or sandbox-only paths are excluded from the formal artifact.

A local validator or archive integrity check does not prove OpenCode discovery, loading, or behavior.

## 2. Validate the target runtime state separately

Report these states independently:

| State | Required evidence |
| --- | --- |
| Authored/modified | Exact final source and diff. |
| Static checks passed | Actual frontmatter/path/reference/mirror/contract checks. |
| Discovered | Evidence from the specified target version/profile/scope. |
| Visible/loadable to agent | Effective permission and model-facing/runtime evidence. |
| Body loaded | Actual skill-load output or equivalent record. |
| Reference loaded | Evidence that the required reference was read before the dependent action. |
| Behavior validated | Representative target-runtime result. |
| Installed/applied | Authorized target-path/config change plus verification. |
| Committed/pushed/deployed | Actual repository or deployment evidence. |

Do not promote evidence from one row into a later row.

## 3. Packaging

Use the archive format required by the receiving workflow. For this user's Linux/OpenCode handoffs, default to `.tar.zst`; Web ChatGPT skill releases use `.zip` and are a different artifact type.

For a handoff archive:

1. include only the intended formal files plus necessary review/evidence files;
2. reject absolute paths, `..` traversal, accidental symlinks, cache, secrets, and unrelated Git metadata;
3. record a manifest and relevant hashes;
4. test archive integrity;
5. extract to a fresh location and compare the extracted formal files to the selected source;
6. re-run the static checks on the extracted copy.

Archive integrity proves packaging only, not installation or runtime behavior.

## 4. User-action stop points

When the next result depends on a command the user must run on the target machine, provide only the next necessary step, expected observation, and decision criterion. Do not provide dependent modification commands before the prerequisite evidence is known.

If the current environment can obtain the evidence directly, obtain it rather than transferring the investigation to the user.

## 5. Git publication

Repository commit/push authorization is separate from skill authoring. Before any push, inspect the actual remote, remote branch SHA, local HEAD, intended publication commit, parent topology, ahead/behind state, exact publication range, file scope, `git diff --check`, final diff, local-only commit exclusion, and working tree/index state.

If remote, HEAD, publication SHA/range, or material working state changes after approval, the approval is stale. Do not provide a push command until the user explicitly approves the inspected publication state.
