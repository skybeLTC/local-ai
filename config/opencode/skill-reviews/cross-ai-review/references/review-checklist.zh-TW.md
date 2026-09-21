# Cross-AI Final Review Checklist（繁中人工檢視版）

> 英文執行權威：[`../../../skills/cross-ai-review/references/review-checklist.md`](../../../skills/cross-ai-review/references/review-checklist.md)。本檔只供人工 review。

Final implementation review、delivery、commit/deployment 或 closeout 時使用，只檢查適用 dimensions。

## Context 與 evidence

- 是否仍是同一 cross-AI task？Peer side 換 session 時，有沒有重新取得必要 context，而不是假設自動繼承？
- 最新 user requirements、scope、authorization、constraints、blockers 是否已套用？
- Material claims 是否用 exact available repo/files/Git/log/build/test evidence 查核，而不是 summary/memory？
- 缺 evidence 時，affected judgment/gate 與最小 missing input 是否明確？

## Peer-question coverage

- 每個仍 relevant explicit peer question 是否都有 `ANSWERED / UNRESOLVED / SUPERSEDED / NOT_APPLICABLE` disposition？
- Partial supersession 是否拆開，沒有藏住 open part？
- `UNRESOLVED` 是否指出 missing evidence/input、affected gate、仍可繼續的 independent work？
- 較新 user answer 是否直接套用；若它產生 new substantive judgment，是否另觸發 gate？

## Scope、authorization、forward progress

- Review 與 modification/commit/push/install/deploy authorization 是否分開？
- Handoff destination 與 exclusive implementation constraint 是否分開？
- `this round／這輪` 是否依 user context 解讀，而不是 workflow 自己重定義成 lifecycle round？
- 某端 independent review 關閉 current stage 後，是否由該端直接進 next legal stage，而沒有 information-free handoff？
- Next stage 是否依 lifecycle 判定，而不是一律 implementation？

## Candidate、validation、implementation review

- Candidate identity、validation、implementation-review status、technical completion、apply/commit/push/install/deploy 是否分開？
- Implementation eligibility 是否只依 authorization、accepted remediation、exact source/candidate、ability to edit、required implementation inputs，而沒有把 post-implementation validation capability 混入？
- Local validation unavailable 時，是否仍允許 formal candidate 並明示 validation gap？
- Runtime evidence 若是選擇正確 implementation 的 required input，是否先停止 dependent edit？
- Premature candidate 是否在 remediation consensus 後直接 review／修正，而不是形式上重做？
- Reviewer 修 implementation defect 後，是否成為 new candidate implementer，由另一端 review？
- Source-level review 是否可先開始，但 required validation 不足時不宣告 final PASS？

## OpenCode-specific independent-review topology

- Cross-AI task active 時，是否使用 external peer 作 independent reviewer，而不是派 `review*`／`critic*` duplication？
- 其他 subagents 是否只做 narrow factual investigation？

## Session export 與 file exchange

- 使用 session export 時，是否依英文 `session-export.md` 檢查 decompression/parsing、truncation、tool-result coverage、attachment/artifact coverage？
- 需要 file exchange 時，是否依英文 `file-exchange.md` 使用 verified current `.tar.zst` 或 explicit direct-access exemption？

## Completion

Technical workflow 只有在 formal deliverables implemented、required validation sufficient、final independent implementation review passed、沒有 unresolved substantive judgment、所有 relevant peer questions 有 disposition、current stage deliverable 完成時才算 complete。

Final reviewer PASS 後不再要求 implementer reconfirm。Commit/push/install/deploy/user-review gates 保持獨立，依各自 evidence/authorization 回報。
