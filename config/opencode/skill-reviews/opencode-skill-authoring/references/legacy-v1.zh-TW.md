# Legacy OpenCode V1

只有 target runtime 實際使用 legacy V1 skill/config mechanics，或 task 明確處理 V1／V1-to-V2 migration 時才讀本 reference。

## V1 baseline

Legacy OpenCode versions 可能有 fork 差異，因此先確認 exact fork。常見 V1 特徵包括：

- directory-form skills 位於 `.opencode/skills/<name>/SKILL.md` 或 `~/.config/opencode/skills/<name>/SKILL.md`；
- target 有實作時，可從 `.claude/skills/` 或 `.agents/skills/` 做 compatibility discovery；
- YAML frontmatter，且 `name` 與 `description` 為 required；
- `name` 作為 runtime skill identifier；
- project convention 讓 `name` 使用 lowercase kebab-case 並與 directory 對齊；
- 使用 `permission.skill` 與 agent-level permission overlays，而不是 V2 ordered `permissions` rules；
- fork-specific `skills.paths`、`skills.urls`、profile overlays 或 source precedence。

Supporting-file loading 必須從 target implementation 驗證；不得從 V2 documentation 反推 V1 behavior。

## Current-project target evidence

本次 migration 使用的 `local-ai` snapshot 中，OpenCode fork `c73cc038da91dde71cd432d1386532bdd16b808c` 的 normal CLI skill path 會經過 `packages/opencode/src/skill/index.ts` 與 `packages/opencode/src/tool/skill.ts`。這條 path 以 frontmatter `name` 作為 runtime identifier，並使用 V1-style permission evaluation。這段只能視為 version-scoped evidence，不是永久 OpenCode rule；target fork 改變時要重新確認。

## V1-to-V2 migration

Task 明確包含 migration 時：

1. 先保留 intended behavior，再改 platform mechanics；
2. 依 actual V2 path-derived rules 重新判斷 skill ID；
3. 把 legacy extra-source config 轉成 V2 source contract；
4. 把 V1 permission objects 轉成 target V2 ordered permission rules；
5. 在 V2 target 驗證 discovery、visibility、loading、reference use 與 behavior；
6. 只有 maintained environments 都不再依賴 V1 時，才移除 V1-only compatibility。

預設不要維持 lowest-common-denominator artifact。如果同一 artifact 明確必須同時支援兩種 contract，而且 requirement 衝突，提出該 decision 讓使用者明確決定。
