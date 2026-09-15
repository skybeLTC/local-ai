# Legacy OpenCode V1

Read this reference only when the target runtime actually uses legacy V1 skill/config mechanics or the task explicitly covers V1 or V1-to-V2 migration.

## V1 baseline

Confirm the exact fork, because legacy OpenCode versions can differ. Common V1 characteristics include:

- directory-form skills under `.opencode/skills/<name>/SKILL.md` or `~/.config/opencode/skills/<name>/SKILL.md`;
- compatibility discovery from `.claude/skills/` or `.agents/skills/` when the target implements it;
- YAML frontmatter with required `name` and `description`;
- `name` acting as the runtime skill identifier;
- project conventions that keep `name` lowercase kebab-case and aligned with the directory;
- `permission.skill` and agent-level permission overlays rather than V2 ordered `permissions` rules;
- fork-specific `skills.paths`, `skills.urls`, profile overlays, or source precedence.

Supporting-file loading must be verified from the target implementation. Do not infer V1 behavior from V2 documentation.

## Current-project target evidence

For the `local-ai` snapshot used in this migration, OpenCode fork `c73cc038da91dde71cd432d1386532bdd16b808c` routes the normal CLI skill path through `packages/opencode/src/skill/index.ts` and `packages/opencode/src/tool/skill.ts`. That path uses frontmatter `name` as the runtime identifier and V1-style permission evaluation. Treat this statement as version-scoped evidence, not as a permanent OpenCode rule; re-check it when the target fork changes.

## V1-to-V2 migration

When migration is explicitly in scope:

1. preserve the intended behavior before changing platform mechanics;
2. re-evaluate the skill ID under the actual V2 path-derived rules;
3. convert legacy extra-source configuration to the V2 source contract;
4. convert V1 permission objects to the target V2 ordered permission rules;
5. validate discovery, visibility, loading, reference use, and behavior on the V2 target;
6. remove V1-only compatibility only after the maintained environments no longer depend on it.

Do not keep a lowest-common-denominator artifact by default. If one artifact must intentionally support both contracts and the requirements conflict, surface that decision explicitly.
