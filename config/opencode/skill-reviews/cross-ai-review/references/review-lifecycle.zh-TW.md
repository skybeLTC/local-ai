# Cross-AI Review Lifecycle（繁中人工檢視版）

> 英文執行權威：[`../../../skills/cross-ai-review/references/review-lifecycle.md`](../../../skills/cross-ai-review/references/review-lifecycle.md)。本檔只供人工 review。

本 reference 用於 remediation、formal implementation、implementation review 與 technical completion。Always-required forward progress、authorization、substantive-judgment、peer-question closure 與最低 completion 規則由英文 `../SKILL.md` 持有。

## 固定 stages

1. **Diagnosis review**：確認 problem/cause/risk 是否成立。
2. **Remediation review**：確認 expected behavior、scope、boundaries、acceptance criteria。
3. **Formal implementation**：依 accepted remediation 建立或修改 exact candidate。
4. **Implementation review**：未建立／修改該 candidate 的另一端獨立 review；required validation 可在此 stage 前或進行中補齊。
5. **Completion judgment**：判斷 implementation、required validation、final independent review 與 open items 是否滿足 technical completion gate。

不要把 diagnosis consensus 寫成 remediation consensus、candidate existence 寫成 validation，或 review started 寫成 final review PASS。

## Stage-closing transition

某一端 independent review 若關閉 current stage 所需 consensus，除非有 actual gate，該端立即承接下一個合法 stage。Diagnosis consensus 但沒有 remediation 時，該端提出最小可 review remediation；remediation consensus 且 implementation eligibility 滿足時，該端實作；一端建立的 candidate 由另一端 review。

目前這一端能合法執行 next stage 時，不再比較哪一端理論上比較方便。Future handoff destination 或另一端也能 edit 都不是 gate。

## Remediation review

可 review 的 remediation 必須寫明 expected behavior、in/out scope、important boundaries、acceptance criteria 與 required evidence。Conditional acceptance 只有在 conditions 納入後才形成 consensus。Silence、重述或未檢查 evidence 的 `looks fine` 不算 independent acceptance。

## Formal implementation 與 state separation

Edit 前確認 valid authorization、accepted remediation 或 user 明確改變 review gate、exact current source/candidate、能實際 edit，以及選擇正確 implementation 所需 inputs。

Post-implementation validation capability 不是 implementation-eligibility requirement。即使沒有 compiler、syntax/static checker 或 target runtime，仍可建立 formal candidate；validation 另標為 `NOT_RUN / PARTIAL / PENDING / PASSED / BLOCKED`。若缺少的 runtime evidence 是選 implementation 本身的必要 input，才停止 dependent edit。

至少分開 candidate identity、validation、implementation review、technical completion，以及 apply/commit/push/install/deploy 狀態。

Remediation consensus 前就產生的 implementation 標為 premature，不因形式理由丟棄或重做。先獨立 review remediation；若接受，再 review exact existing candidate。只修改依賴 rejected/changed judgment 的部分。

新發現若改變 expected behavior、scope、important boundary、compatibility、data handling、risk 或 acceptance criteria，停止 dependent formal edits，回到相應 substantive review。不依賴新 judgment 且仍符合 accepted consensus 的既有工作可以保留。

## Implementation review 與 role swap

Review exact candidate，不只看 summary。檢查 accepted remediation fidelity、formal scope/dependency impact、新 defects/contradictions、current validation 能證明什麼，以及 candidate/validation/apply/deploy state 是否分開。

Source-level review 可在 required validation 未完成時開始；final acceptance 若依賴該 validation，review 保持 `IN_PROGRESS` 或 `BLOCKED`，不能宣告 PASS。

Reviewer 若只發現 accepted remediation 內的 implementation defect，而且有 valid authorization、exact candidate、能 edit，就直接修。缺 post-implementation validation capability 只形成 validation gap，不是退回原 implementer 的理由。Reviewer 成為 new candidate 的 implementer，另一端 review。

需要 changed remediation judgment 時，先回 remediation review。

## Peer questions 與 user decisions

每輪結束前，每個 relevant explicit peer question 都要有 `ANSWERED / UNRESOLVED / SUPERSEDED / NOT_APPLICABLE` disposition。`UNRESOLVED` 只阻塞 dependent actions。較新的 user decision 已回答時直接 relay；若同時產生新 substantive judgment，question 可以 `ANSWERED`，但 dependent formal edits 仍受 gate 阻擋。

## Completion

Technical completion 需要 formal deliverables implemented、required validation sufficient、final independent candidate review passed、沒有 unresolved substantive judgment、所有 relevant peer questions dispositioned，以及使用者要求的 current stage deliverable 完成。不要製造第三次 information-free confirmation；commit/push/install/deploy/user-review gate 保持分開。
