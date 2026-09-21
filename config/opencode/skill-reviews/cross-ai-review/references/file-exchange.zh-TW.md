# Cross-AI 檔案交換（繁中人工檢視版）

> 英文執行權威：`../../../skills/cross-ai-review/references/file-exchange.md`。本檔只供人工 review。

當 `SKILL.md` 的 file-exchange gate 命中，或目前 cross-AI task 確實需要與 peer 交換檔案時讀取英文權威 reference。

## 何時必須交換

本輪同時符合以下條件時，在結束前建立或更新 current `.tar.zst`：

- 本輪建立或修改 named formal deliverable；
- peer AI 必須 implementation-review 該 deliverable；
- peer AI 不能直接 access exact current files 或 exact current commit。

以下情況不需要新 archive：只有 diagnosis/remediation 討論、peer 有 exact direct access、peer 已持有 exact unchanged current archive，或只有說明/log/evidence 改變而 formal deliverable 未變。

Direct-access exemption 必須在 final response 明確說明理由。Required-exchange case 中，diff、commit summary、`git show`、commit hash 或「已 commit」都不能取代 `.tar.zst`。

## Archive、內容與 timing

所有 peer file exchange 使用 `.tar.zst`；無法可靠建立時要明確說明 blocker，不得靜默換格式。

封裝本輪新增／修改的 formal deliverables、peer review 所需 supporting files、required validation evidence、peer 明確要求的檔案，以及本身屬 formal deliverable／必要 evidence 的 generated artifact。不要封裝純 incidental cache/temp/generated garbage。

完成本輪在 substantive gate 下能合理完成的工作後再封裝，不要要求使用者中途轉交 half-finished archive。保留 peer review/apply 所需的相對路徑，不封裝 credential、home-directory 雜項或 unrelated cache。

若 peer 已有 exact unchanged archive，直接 reuse；只有內容改變、peer 重新要求或本輪新修改需要 exchange 時才重建。

回覆結尾要明確寫出 handoff archive 的實際 path/filename；不要只寫「傳上面的檔案」。
