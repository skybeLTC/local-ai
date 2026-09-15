# Target OpenCode Runtime Contract

Use this reference before making decisions that depend on skill identity, discovery, source precedence, frontmatter, permissions, agent/profile integration, or runtime loading.

## 1. Identify the actual target

Collect only the evidence that can change the current decision, in this order when available:

1. the target checkout or installed binary and its actual source/schema/config behavior;
2. the exact fork, branch, tag, or commit specified for the task;
3. documentation that matches that target version;
4. current upstream documentation as a comparison point, not as proof of the target runtime.

Do not classify a target as V2 merely because its repository contains V2 packages or because current upstream documentation describes V2. Determine which implementation the actual entrypoint, config, skill tool, and selected profile use.

## 2. Choose the contract branch

- If the target runtime actually uses the current V2 skill/config contract required by this task, use the V2 branch below.
- If the target runtime still uses legacy V1 skill/config mechanics, read `legacy-v1.md` before making dependent decisions.
- If the target is mixed or transitional, classify each affected mechanism separately. Do not force an unrelated mechanism into V1 or V2 because another subsystem has migrated.
- If the evidence is insufficient and the distinction changes the skill ID, source registration, permission schema, metadata, or validation method, stop that dependent decision and obtain the smallest missing evidence.

## 3. V2 skill contract

For a target confirmed to use the current V2 contract:

- skill identity is path-derived; frontmatter `name` is a display label;
- a clear `description` is required for model-facing discovery even when runtime parsing allows it to be absent;
- directory-form skills should keep supporting files beside `SKILL.md` and use skill-relative paths;
- V2 may support fields such as `slash` and OpenCode metadata controls; use only fields confirmed by the target version;
- extra skill sources use the target's V2 `skills` configuration;
- V2 skill permissions use the target's ordered permission rules and the path-derived skill ID as the resource;
- supporting-file contents are not implied to be loaded merely because the skill body or a file sample is visible.

When upstream behavior is relevant, verify it against documentation matching the target version. Do not downgrade a confirmed V2 target merely to preserve legacy compatibility that the task does not require.

## 4. Legacy or transitional targets

When the current target uses legacy mechanics, do not rewrite the artifact as if V2 were already active. Preserve required current behavior and use `legacy-v1.md` for the exact branch. A future V1-to-V2 migration is a separate change with its own validation.

## 5. States that require separate evidence

Keep these states separate:

1. the candidate file exists;
2. the target discovers or registers the skill;
3. the selected agent is allowed to see/load it;
4. the skill body is actually loaded;
5. a required supporting reference is actually read before the dependent action;
6. the agent follows the intended behavior.

Evidence for one state does not prove the later states.
