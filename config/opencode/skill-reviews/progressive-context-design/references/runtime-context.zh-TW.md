# 執行 Context、Reachability 與 Reference 分流

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/runtime-context.md`。

本 reference 用於設計 runtime-loaded instructions、skills、reference trigger、guaranteed reachability 與 progressive loading。最低義務由 `../../../skills/progressive-context-design/SKILL.md` 持有；本文件處理 loading topology 與驗證方法。

## 分開執行端與接收端

先記錄目前執行平台、產物接收平台、產物類型、可用工具與接收端實際載入機制。不要因目前在 Web ChatGPT authoring，就假設目標 repo、OpenCode 或其他 runtime 具有相同工具、檔案與權限。

## Loading layers

| 層級 | 必須能回答的問題 |
| --- | --- |
| skill name / description 或平台等價 selection metadata | 這個任務是否應選用此方法？ |
| guaranteed entry / 執行入口 | 最低 mandatory behavior、boundary、stop condition，以及哪些 deeper sources 已被觸發？ |
| 已觸發 reference | 該分支如何正確執行、處理例外並驗證？ |
| README / rationale / maintenance background | 為什麼如此設計、生命週期與維護方式是什麼？ |

共同且每次都必要的短規則留在 guaranteed entry。不要把 mandatory rule 外掛成每次都要猜路徑才能找到的文件，也不要因檔名看似特殊就假設接收 runtime 自動載入。

## OpenCode-specific loading evidence

對 OpenCode，要分開 skill advertisement/discovery、permission、skill body loading、supporting-file path advertisement 與實際 reference content reading。Supporting file 只出現在 runtime 顯示的 sampled file list，不能證明其內容已讀取。

只有在有效 OpenCode 版本、working directory/project lookup、config 或其他 runtime evidence 能證明相關任務會載入時，才把 `AGENTS.md` 或其他 instruction file 視為 guaranteed entry。不能只依 path nesting 推定 nested `AGENTS.md` 會自動載入。

## Guaranteed reachability

Mandatory local instruction 必須形成完整 path：

`guaranteed entry → observable trigger / routing condition → exact target → read-before decision/action`。

檔案存在、README 有連結、目錄結構看起來合理，都不能單獨證明 guaranteed reachability。若平台不會自動載入 nested instruction，就必須使用該平台實際支援的 routing mechanism；本 skill 只規定結果，不虛構平台能力。

## Reference trigger contract

每個執行 reference 必須同時具備：

1. **observable trigger**：由任務、artifact type 或具體 state 判定；
2. **exact source**：可解析的相對路徑；
3. **read-before point**：明確指出在哪個相依 judgment/action 前讀；
4. **required content boundary**：讀取範圍必須涵蓋會改變該動作的 constraints / exceptions；
5. **missing behavior**：reference missing、denied 或不可取得時怎麼停止與回報。

只讀檔名、目錄、標題或搜尋命中不能證明已取得必要內容。

## 拆分不能造成能力斷鏈

把既有方法拆進 reference 前，逐一建立 migration mapping：原本哪個 observable condition 會進入這段方法、拆分後入口如何辨識、何時讀、缺失時怎麼處理。

如果方法被移入 reference，但入口沒有可靠 trigger；或 trigger 只有「必要時」、「若覺得需要」等無法穩定判斷的條件，拆分即造成 capability regression。應修正 routing 或取消拆分。

每個新增 reference 也必須證明有獨立資訊價值；不要建立只轉介下一份文件的 forwarding chain。

## 多 references 同時成立

Reference trigger 不是 mutual-exclusive menu。當同一任務同時涉及 documentation、placement、runtime loading、change impact 等多個問題時，在各自相依 decision 前讀取所有必要 references。

Progressive loading 的目標是排除無關內容，不是強制 serial one-reference-at-a-time。若一份 reference 的 judgment 是另一份的前提，依 dependency order 讀取；沒有 dependency 時可在同一階段取得。

## Context 變更與重新讀取

已讀內容仍在 context、版本未變且條件仍相同時可沿用。以下情況要補讀：

- reference 已修改或版本改變；
- 關鍵內容已離開可用 context；
- 任務進入先前未觸發的 branch；
- target platform / artifact / scope 改變導致 trigger 重新判定。

## 驗證 loading topology

至少依本次變更影響範圍選擇案例檢查：

- trigger 明確成立；
- nearby case 成立 broad review 但不需要某 deeper reference；
- 多個 triggers 同時成立；
- trigger 是否成立無法判定；
- 必讀 reference missing / denied；
- 已讀內容版本改變或離開 context。

證據要支持 reference 在相依 judgment 前被讀取，且未觸發 reference 沒有被無條件預載。若目前 runtime 無法觀察 actual loading，明確回報驗證缺口；靜態 topology 正確不能被描述成已驗證自動載入。
