# Migration、Responsibility 與 Change Impact

跨平台 migration、吸收另一個 skill、rename skill、改變 responsibility/authority，或修改已有 dependent consumers 的 existing skill 時使用本 reference。

## 1. 比較 exact sources

分開：

- current OpenCode implementation 中仍受要求的 behavior；
- 本次 requested change；
- 另一個 skill 或 platform 提供的 behavior；
- 不應逐字搬入的 source-platform mechanics；
- 必須留在 target OpenCode 的 target-specific mechanics；
- 未驗證 claims 或 historical results。

使用 task 已選定的 exact versions。決定 semantic delta 時，summary 不能取代 source files。

## 2. 逐項分類 capability

| Decision | 意義 |
| --- | --- |
| Keep | Capability 仍屬於此處且仍有效；指出 owner 與 validation。 |
| Merge | 兩個 sources 服務同一 user intent，規則相容；只保留一個 current authority。 |
| Replace | Required result 仍成立，但 old platform mechanism 對 target 不正確。 |
| Remove | Capability 已 obsolete、duplicate 或屬於其他 owner；記錄理由與 impact。 |
| Unresolved | Evidence 或 authorization 不足；只停止依賴此 decision 的工作。 |

不能只因兩份文件文字相似就 merge。Trigger branches、permissions、tools 或 responsibility 有實質差異時，分開 skills 仍可能是正確設計。

## 3. 有意識地處理名稱與 authority

Skill name/ID 不是不可變。Responsibility 已收窄或擴張、舊 ID 造成 ambiguity／collision risk、navigation 已指向另一個穩定名稱，或 migration 否則會留下 competing authorities 時，應評估 rename。

不得只為了讓兩個 platform 看起來一致就 rename。決定 rename 後，在同一 coherent change 更新所有 direct consumers：directory、frontmatter/ID representation、permission resource、references、review-mirror path、README/navigation、寫死舊名的 scripts 或 schemas、validation fixtures 與 handoff instructions。

除非 target runtime 有明確 alias mechanism 而且使用者要求，不得同時保留 old/new skill 都 active 只為做 alias。

## 4. 沿實際 dependency 傳播 impact

從 direct change nodes 開始，檢查：

- `description`、skill ID/name 與 `SKILL.md`；
- execution references 與 reference triggers；
- sibling review mirrors 與其 mapping owner；
- skill README 與 repository navigation；
- 寫入 changed path/contract 的 scripts/templates；
- skill sources、profile/agent integration 與 permissions；
- install、validation、archive 或 handoff procedures。

任何 dependent item 需要改，就成為新的 change node；直到 evidence 顯示下一個 dependency 不受影響才停止。預設不要掃描或重構 unrelated repository areas。

## 5. 保留 external provenance 與有用 tooling

External material 仍被實質納入時，保留 applicable license/notice 與 provenance。Existing deterministic helpers、evaluators、viewers 或 benchmark tools 只有在 capability 已不需要、owner 已搬移，或 evidence 顯示它們 stale／harmful 時才移除。檔案很久沒改或沒有近期使用紀錄，單獨都不足以證明 obsolete。

## 6. Migration completion

宣告 migration complete 前，逐項交代 promised capabilities 與 intentional removals。說明每條 impact branch 在哪裡停止，以及停止理由。Structural equivalence 不是 behavior validation；behavior 或 trigger quality 改變時依 `behavior-evaluation.md`。
