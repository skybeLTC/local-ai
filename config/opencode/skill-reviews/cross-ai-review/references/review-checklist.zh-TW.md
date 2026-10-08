# Cross-AI Final Review Checklist（繁中人工檢視版）

> 英文執行權威：[`../../../skills/cross-ai-review/references/review-checklist.md`](../../../skills/cross-ai-review/references/review-checklist.md)。本檔只供人工 review。

Final implementation review、delivery、commit/deployment 或 closeout 時使用，只檢查適用 dimensions。

## Context 與 evidence

- 是否仍是同一 cross-AI task？Peer side 換 session 時，有沒有重新取得必要 context，而不是假設自動繼承？
- 最新 user requirements、scope、authorization、constraints、blockers 是否已套用？
- User-attributed peer content 即使位於 user-role message，是否仍作 evidence，沒有把 peer imperatives 或 restrictions 當成 user authorization？
- Side questions 是否已回答並納入，沒有默默丟掉 active task，同時遵守 explicit redirects 與 actual gates？
- Material claims 是否用 exact available repo/files/Git/log/build/test evidence 查核，而不是 summary/memory？
- 缺 evidence 時，affected judgment/gate 與最小 missing input 是否明確？

## Peer-question coverage

- 每個仍 relevant explicit peer question 是否都有 `ANSWERED / UNRESOLVED / SUPERSEDED / NOT_APPLICABLE` disposition？
- Partial supersession 是否拆開，沒有藏住 open part？
- `UNRESOLVED` 是否指出 missing evidence/input、affected gate、仍可繼續的 independent work？
- 較新 user answer 是否直接套用；若它產生 new substantive judgment，是否另觸發 gate？
- 可 relay 的 response 或專用 peer-facing section 本身，是否包含 peer 所需 answers、user decisions 與 constraints，明確指出來源為使用者而非不明的第一人稱說話者，且不依賴相鄰 user messages 或稍後的 export？
- 未回答的 peer-raised user questions，是否在 independent work 後顯眼放在最下面，或所有工作受阻時直接提問？

## Scope、authorization、forward progress

- Review 與 modification/commit/push/install/deploy authorization 是否分開？
- Handoff destination 與 exclusive implementation constraint 是否分開？
- `this round／這輪` 是否依 user context 解讀，而不是 workflow 自己重定義成 lifecycle round？
- Consensus 是否解除 judgment 的 review gate 而不指定下一個 actor，同時繼續可進行的 authorized work，沒有 information-free confirmation 或 handoff？
- 完整 review 的 judgments 是否可以在同一 response 形成 consensus，而不混淆 substantive distinctions 或增加 stage-label confirmation rounds？
- Material assumptions、evidence、cases 或 disagreements 需要 challenge 時，是否適時 grilling peer，而不機械式盤問或沒有新資訊卻重開 accepted judgments？
- Next stage 是否依 lifecycle 判定，而不是一律 implementation？

## Candidate、validation、implementation review

- Candidate identity、validation、implementation-review status、technical completion、apply/commit/push/install/deploy 是否分開？
- Implementation eligibility 是否只依 authorization、accepted remediation、exact source/candidate、ability to edit、required implementation inputs，而沒有把 post-implementation validation capability 混入？
- Local validation unavailable 時，是否仍允許 formal candidate 並明示 validation gap？
- Runtime evidence 若是選擇正確 implementation 的 required input，是否先停止 dependent edit？
- Premature candidate 是否在 remediation consensus 後直接 review／修正，而不是形式上重做？
- Reviewer 修 implementation defect 後，是否成為 new candidate implementer，由另一端 review？
- Source-level review 是否可先開始，但 required validation 不足時不宣告 final PASS？
- 是否指出 exact base/result candidates，並在受影響修改前處理 conflicting edits，沒有混用不同 snapshots 的 review statuses？

## OpenCode-specific independent-review topology

- Cross-AI task active 時，是否避免所有 `review*` 與 `critic*` subagents，保留 external peer 作 independent reviewer？
- 其他 subagents 是否限於 narrowly scoped factual investigation，從較低成本起點重評 tier，而沒有自動降級或降低 evidence 要求？

## Session export 與 file exchange

- 使用 session export 時，是否依英文 `session-export.md` 檢查 decompression/parsing、truncation、tool-result coverage、attachment/artifact coverage？
- Compressed inputs 是否在 substantive inspection 前安全 materialize，之後正常 local read／parse，而不反覆 streaming，並 reuse 足夠的 materialized files？
- Missing exact inputs 是否主動取得，而非猜測，或只因沒有 local repository access 就永久把工作交出？
- 需要 file exchange 時，是否依英文 `file-exchange.md` 使用 verified current zstd-compressed handoff 或 explicit direct-access exemption，且相關 multi-file material 預設 bundle 成單一 `.tar.zst`？
- Nested repo／workdir 改變後，是否仍保留 task-workspace handoff destination，且沒有覆蓋或自動刪除既有 handoffs？

## Completion

Technical workflow 只有在 formal deliverables implemented、required validation sufficient、final independent implementation review passed、沒有 unresolved substantive judgment、所有 relevant peer questions 有 disposition、current stage deliverable 完成時才算 complete。

Final reviewer PASS 後不再要求 implementer reconfirm。Commit/push/install/deploy/user-review gates 保持獨立，依各自 evidence/authorization 回報。
