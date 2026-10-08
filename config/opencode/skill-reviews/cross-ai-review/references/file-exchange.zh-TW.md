# Cross-AI 檔案交換（繁中人工檢視版）

> 英文執行權威：`../../../skills/cross-ai-review/references/file-exchange.md`。本檔只供人工 review。

當英文 `../SKILL.md` 的 file-exchange gate 命中，或目前 cross-AI task 確實需要與 peer 交換檔案時讀取英文權威 reference。

本檔對應英文 `../SKILL.md` 的 authoritative conditional runtime extension，涵蓋 input materialization 與 handoff mechanics。

## Compressed input 先 materialize 再檢查

實質檢查 compressed input 前，先把所需內容 materialize 到 isolated local working storage。Compressed single file 解成 local file；bundle 所需檔案解到 isolated directory。使用本端環境實際可用的 tools 與 storage，不把 platform-specific command 當成 shared protocol 要求。

Bundle extraction 前檢查 member paths，拒絕或隔離 traversal、absolute paths、逃出 destination 的 links，以及會覆寫無關檔案的 entries。不要直接解到 live repository 或 home configuration。

Materialization 後正常讀取或 parse local files。Archive／compression commands 仍適用於 integrity checks、member/path safety inspection 與 decompression/extraction；不要反覆 streaming archive contents 作為一般閱讀方式。Exact input 未變、materialized content 完整且可取得時，直接 reuse。Input 改變、local copy 遺失或 extraction 不完整時，可以重新 materialize；這不是字面上的單一 command 限制。

保留 materialized files 與 source/version 的關係，避免不同 inputs 碰撞。Complete decompression 不代表 structure 有效或 evidence coverage 完整。Materialization 不可用或不完整時，指出 exact gap，只把受影響 conclusions 保持 unverified；independent work 可以繼續。

## 何時必須交換

本輪同時符合以下條件時，在結束前建立新的 verified zstd-compressed handoff，或 reuse 足夠且未變更的既有 handoff：

- 本輪建立或修改 named formal deliverable；
- peer AI 必須 implementation-review 該 deliverable；
- peer AI 不能直接 access exact current files 或 exact current commit。

以下情況不需要新的 handoff：

- 只有 diagnosis/remediation 討論，尚未開始 formal implementation；
- peer AI 能直接取得並 review exact current files 或 commit（direct-access exemption）；
- peer 已有包含 exact current formal deliverables 與本次 review 所需全部 files 的 handoff，且這些 files 均未變；或
- 只有 explanations、logs 或其他 evidence 改變，formal deliverables 未變，而且沒有需要交換的新 evidence files。

Direct-access exemption 必須在 final response 明確說明理由。Required-exchange case 中，pasted diff、commit summary、`git show` output、commit hash 或「files 已在 Git」都不能取代 handoff；這些項目可以附在 handoff 或 explicit exemption 旁。

## Handoff 格式與保留

Current side 產出的 handoffs 使用 zstd compression。一個 logical handoff 的內容應盡量集中在一個 compressed artifact。Naturally single-file artifact 可直接壓縮，例如 `.json.zst`；多份相關 deliverables、supporting files 或 evidence files 預設 bundle 成單一 `.tar.zst`。沒有具體需要，不把相關 handoff material 拆成多個 attachments。

Transport format 不改變 formal deliverable 自己的 release format。無法可靠產出 required zstd-compressed artifact 時，明確指出 blocker；不得靜默換格式，或只改副檔名。

不得覆蓋或自動刪除既有 handoff。選定 filename 已存在時，使用另一個不衝突的 filename。不要求 revision、version 或 final-name scheme。

## 封裝內容

封裝：

- 本輪新增／修改的 named formal deliverable files；
- peer review 所需 supporting files；
- required validation evidence；
- peer 明確要求的 files，即使本輪未變；
- 本身屬 formal deliverable、accepted implementation 所要求、必要 review evidence 或被明確要求的 generated artifact。

不要封裝純 incidental cache、temp files 或 generated garbage；若它既未被要求、不是 required deliverable，也不是必要 review evidence，就不納入。

## Timing

先完成本輪在 substantive-judgment gate 下能合理完成的工作，再封裝。

當前環境還能完成更多工作時，不要求使用者中途 relay half-finished archive。

## Paths

保留 peer 理解、review 或 apply files 所需的相對路徑。

產出 handoff 前，依使用者適用 task context 確認並保留 absolute task-workspace output directory。Task workspace 不自動等於 repository root 或 current tool workdir。進入 nested repository 或改 workdir，不改變 handoff destination。Location 未定且會影響結果時，先取得該 location 再 output。可取得時，把 handoff 放在該 task-workspace root；否則提供 download，不宣稱已寫到使用者 filesystem。

不要封裝 unrelated home-directory content、repository caches、credential stores 或其他 incidental environment state。

## Security

不得封裝 credential material，包括：

- `auth.json`；
- access 或 refresh tokens；
- API keys；
- SSH private keys；
- credential-bearing session、cache 或 database state。

Private repository visibility 不代表 credential material 適合 cross-AI file exchange。

## Reuse

已轉交足夠的 exact handoff 時，直接使用；其 materialized files 仍完整且適用時，直接 reuse。

不要重複要求同一份仍可取得的 input。既有 material 不足時，只要求缺少的 current files/evidence。New candidate、changed required evidence 或 unavailable/incomplete copy 可能需要新 exchange。

## 驗證 handoff

檢查 compression integrity、適用時的 bundle member safety 與 paths、required content coverage，以及沒有 unrelated 或 credential-bearing files。Exact content 重要時，在新的 isolated storage materialize verification copy，與選定 final source 比較。Archive 可讀或 hash 相符只能證明 packaging，不證明 behavior、installation 或 deployment。

## User-facing handoff

在回覆 closing section 明確提醒使用者把 handoff 交給 peer AI review，並在同一提醒寫出 exact filename 或 path。依英文 `../SKILL.md` 要求，把未回答的 user questions 顯眼留在最下面。

不要只寫「傳上面的檔案」等模糊指引，讓使用者往回找。
