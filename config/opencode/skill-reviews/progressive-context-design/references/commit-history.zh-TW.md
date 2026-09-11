# Git Commit History 作為 Progressive Context

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/commit-history.md`。

本 skill 對 Git history 的核心適用範圍由 `../../../skills/progressive-context-design/SKILL.md` 持有；本文件只處理 Git-specific history navigation。

本 reference 只處理 Git-specific history navigation。跨 history artifact 共通的 current/history、status 與 lifecycle 規則由 [history.md](history.zh-TW.md) 持有；實際 commit-message authoring 由適用的 `commit-message` 方法負責。

本文件使用以下固定術語：

- **history list**：列出多個 commits 並至少顯示 commit subject 的清單，例如 `git log --oneline`。
- **commit subject**：commit message 第一行，用於 history list 的第一層 navigation。
- **完整 commit message**：commit subject 加上存在時的 body。

## Progressive path

Git history 通常形成：

1. **history list / commit subject**：先判斷哪個 commit 可能 relevant；
2. **完整 commit message**：理解主要 semantic change、why、scope 與重要 state，並判斷是否需要深入；
3. **diff、source 或其他 evidence**：只有需要 implementation detail 或驗證依據時才深入。

這是 information role，不是固定 commit-message template。

## Subject 的 navigation responsibility

Commit subject 應讓讀者在 history list 中辨識主要 change object 與 semantic result。若大量 subject 只有 `update`、`fix`、`cleanup` 等無法區分的描述，第一層 navigation 失效，讀者被迫打開大量 commits。

Subject 不需要承載全部 rationale。只要足以篩選 relevance，就讓 deeper context 留在 full message。

## Full message 的 deeper context role

完整 commit message 應在有需要時提供足夠 context，讓讀者不必先讀 diff 就能理解 change 的主要 meaning、why、impact、constraints 或 validation state。

是否需要 body、使用什麼格式、type/scope、字數、語言、trailers 與 repo/organization conventions，都不由本 skill 決定。

## Current authority

Commit message 記錄該次變更當時的 semantics / rationale / evidence，不是現行規則 owner。Current policy、runtime instruction 或 configuration contract 改變後，必須更新其 現行權威；不能要求後續 agent 使用 Git archaeology 重建現行規則。

反過來，也不要把完整 commit evolution 全部複製到 current runtime context。需要 evolution rationale 時才沿 navigation path 回到 relevant commit。

## Review scope

本 skill 在 Git history 只 review：

- history list 是否能先篩選 relevant commits；
- full message 是否能支持是否深入 diff/source 的 decision；
- 現行權威與 Git history 是否分工正確；
- history evidence 是否被誤當 current fact；
- Git-specific path 是否能連到需要的 deeper evidence。

不要用本 skill 判斷 commit-message style 或 organization-specific formatting。
