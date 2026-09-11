---
name: progressive-context-design
description: "建立、修改、review 或重整 durable textual / instructional artifacts 時使用，包含 prompts、skills、README、AGENTS instructions、guides、runbooks、design docs、repository navigation、history，以及其他後續人員或 AI 會依賴的持久文字。設計單一權威、natural owner、progressive loading、reference triggers、guaranteed reachability、hierarchy rebalance、change-impact propagation、current/history separation 與 information-boundary handling。不以本 skill 作為 software correctness、software architecture、test design 或 commit-message authoring 的權威。"
---

# 漸進式 Context 設計

> 人工檢視版。英文權威來源：`../../skills/progressive-context-design/SKILL.md`。

讓需要資訊的人或 AI 先取得足以判斷正確下一步的最小 context，再依可觀察條件載入更深資訊。資訊架構的目標不是增加文件層數，而是讓權威、適用範圍、載入路徑、導航與歷史都能以合理成本可靠取得。

## 固定術語


- **durable artifact**：預期會被後續人員、AI 或流程再次依賴的持久資訊產物；純一次性 scratchpad、暫時 debug output 或不再被依賴的臨時筆記不屬於此範圍。
- **執行入口**：接收 runtime 保證或明確設定會載入，且必須持有最低必要規則的資訊來源，例如適用的 `SKILL.md`、`AGENTS.md` 或平台等價入口。
- **natural owner**：在目前適用範圍、讀取時點與維護責任下，最接近資訊作用對象且足以讓需要者可靠取得的單一權威來源。
- **reference trigger**：可從任務、產物或狀態觀察到的條件；成立後，對應 reference 在相依判斷或動作前成為必讀。
- **guaranteed reachability**：mandatory information 可從接收平台保證可達的入口，沿明確 loading path 在需要時被取得；檔案存在本身不算可達。
- **現行規則**：目前仍適用並會改變行為的規則。
- **歷史**：說明過去決策、變更、狀態或結果的 durable record；歷史不等於現行權威。
- **證據**：支持特定版本、狀態或驗證結果的可追溯觀察。
- **變更節點**：本次新增、刪除、搬移、重新命名或實質修改的規則、文件、段落、reference、路徑、權威關係或其他資訊單位。
- **上游依賴**：變更節點用來取得權威、定義、前提、來源、inherited contract 或限制的直接資訊來源。
- **下游依賴者**：引用、摘要、鏡像、導覽、載入、消費或依賴變更節點契約的直接資訊單位。
- **影響邊界**：在某個檢查方向，有具體證據支持停止繼續傳播的位置。

## 確認目標與責任

- 分開辨識目前執行平台、產物接收平台、產物類型、實際載入方式與權威來源。為另一平台撰寫內容，不代表目前擁有該平台或使用者機器的存取能力。
- 沿用已確立的目標、語言、適用範圍與授權。Review 不授權修改；資訊架構工作也不授權改變程式、API、設定值、測試策略或其他工程決策。
- 只要任務建立、修改或 review durable textual / instructional artifact，就先套用本 skill 的資訊架構檢查。Artifact 很短、位於 source code 內或只改少量文字，不代表可以跳過；若 natural owner 已正確、沒有更高層依賴，就在該處 progressive stop。
- 語言與格式依目標已有的權威規則；本 skill 不建立跨平台語言政策。
- 任務同時包含資訊架構與工程、skill authoring、commit-message authoring 或其他專門方法時，讓各方法持有自己的單一責任。只有責任界線尚未由使用者或較高權威指令明確決定，而且釐清界線會實質改變判斷或可修改範圍時，才讀取 `references/scope-boundaries.zh-TW.md`；不能只因產物位於 source code 或任務提到另一個領域就讀取。
- 主要任務若只是撰寫、重寫或 review commit message 的格式與措辭，不由本 skill 主導。只有 commit/history 的資訊層級、導航與 current/history 分工屬於本 skill。

## 建立自然權威與 progressive stop

- 每條現行規則由能可靠覆蓋所有需要者的最窄 natural owner 持有。其他位置只保留必要導航、摘要或同步產物，不建立競爭版本。
- 不依檔名或目錄模板強制建立 README、AGENTS、reference 或中介層。只有新的適用範圍、讀取時點、維護責任或導航價值成立時才建立新資訊單位。
- Local information 優先留在 natural owner。若一個演算法 invariant 已由鄰近 source comment 充分承擔，而且沒有更高層 runtime、navigation 或 maintenance dependency，就不要再向 README、AGENTS 或其他上層複製。
- `AGENTS.md`、`SKILL.md` 或其他 runtime instruction owner 只在接收平台實際賦予其載入角色時，持有該 scope 執行時 mandatory 的最低規則、門檻、停止條件與 loading trigger。檔名本身不會創造權威。
- `README.md` 負責用途、深入理由、架構、生命週期、維護與一般導覽。README 與執行入口可以共存，但 README 不能成為 mandatory runtime rule 的唯一 owner。
- Derived mirror 或 generated copy 可以存在，但必須有一份明確 authoritative source、可追溯同步關係，且接收 runtime 不能把 mirror 誤當第二份權威。
- 歷史與證據不能取代現行規則。後續讀者不應被迫 replay 全部 history 才能知道現況。

## 重平衡資訊 hierarchy

- Information hierarchy 不是 append-only。Review 或修改時要檢查 parent 是否累積過多 child-specific responsibility、child 是否已形成獨立 authority、shared rule 是否應上提、local rule 是否應下沉，以及中介 instruction layer 是否還有存在理由。
- Parent 只持有真正 shared invariant；child 只持有 local delta、exception 或 additional constraint，不全文複製 parent。
- 如果 sibling 幾乎完全獨立，而中介層只剩一般導覽或沒有 mandatory responsibility，就考慮縮小或移除該中介 instruction layer。一般導覽可由 README 或其他 navigation owner 承擔；filesystem nesting 不等於 information authority nesting。
- 拆分、合併、上提、下沉或移除資訊後，必須重新檢查 loading、navigation、authority 與 change-impact 關係；不能只因內容都還存在就判定結構仍可用。

## 傳播變更影響

- 實質資訊架構變更不能只驗證變更節點本身。必須沿直接上游依賴與直接下游依賴者重新確認；只有 shared contract、duplication 或其他相依證據出現時才擴到 siblings。
- 如果相依資訊因此需要修改，該資訊成為新的變更節點並繼續傳播，直到每個方向都有有證據的影響邊界。
- 能在使用者已授權 outcome、同一資訊與授權邊界內完成，而且不引入新的產品或工程決策的必要 propagation，可以一起修改。跨 repo、public/private 或其他資訊邊界、改變新的 authority、存在實質取捨，或缺少安全判定 propagation 所需的必要 evidence 時，先停止相依修改，回報影響與建議並取得決定。
- 不無條件掃描完整 repo。沿引用、權威、載入、導航、同步副本、history link 與其他可追溯 dependency 擴大。
- 詳細 traversal、hierarchy rebalance 與停止條件由 `references/change-impact.zh-TW.md` 持有。

## 設計 progressive loading 與 guaranteed reachability

- 執行入口必須能在不讀 README 的情況下約束最低必要行為，並能判斷哪些 references 已被觸發。
- 每個執行 reference 都必須有可觀察 trigger、精確相對路徑與讀取時點。Trigger 成立後，先讀對應 reference，再做相依判斷或動作。
- 拆分 reference 只有在 capability 仍可達時才成立。任何從入口拆出的執行方法都必須保留：`observable trigger → exact reference → read-before decision/action → required content → missing/unavailable behavior`。拆分後若入口無法可靠判斷何時需要它，視為功能退化。
- 多個 reference trigger 可以同時成立；必須在各自相依判斷前讀取所有必要 references。Progressive loading 的限制是不載入無關內容，不是一次只能使用一份 reference。
- Reference trigger 是否成立無法判定時，先讀能判斷適用性的最小內容。必讀 reference 缺失或無法取得時，指出缺口與受影響判斷，停止依賴該 reference 的動作；獨立工作可以繼續。
- 未觸發 reference 不預載。已讀內容仍在 context、版本未變且仍適用時可以沿用；內容變更、遺失或任務進入新條件時補讀。
- Mandatory local instruction 必須有從 guaranteed entry point 可到達的 loading path；平台-specific mechanism 由接收平台的權威規則決定，本 skill 不假設某個檔名一定會自動載入。

## 保留語意、程序與資訊邊界

- 搬移、拆分、摘要或引用現行規則時，保留原本的行為者、動作、對象、規則強度，以及會改變結果的條件、例外、否定與數量邊界。
- 同一概念跨入口、reference、README、history 與 source comment 時沿用同一主要名稱。不同名稱若代表不同概念，就明確定義差異。
- 程序若是產物的一部分，前提要位於相依動作前；警告與停止條件放在受影響動作前；會決定下一步的觀察與判準放在對應步驟附近。
- 分開現行規則、歷史、範例、事實、假設、證據與未決事項。
- Public、private、confidential 或其他資訊 classification 由適用的 policy / project authority 決定。本 skill 只在既有 boundary 下安排 placement、引用、摘要與 navigation；若現有 classification 看起來不合理，提出理由與建議並詢問，不自行重新分類。

## Reference triggers

每次啟用本 skill 都比對下表。符合任一列時，必須在指定動作前讀取該 reference；同時符合多列就讀取所有相依 references。不要預載未觸發內容。

| Reference trigger | 必讀時點與來源 |
| --- | --- |
| 任務同時包含工程、skill authoring、commit-message authoring 或其他專門工作；責任界線尚未由使用者或較高權威指令明確決定；而且釐清界線會實質改變判斷或可修改範圍 | 決定責任與可修改內容前讀 [scope-boundaries.md](references/scope-boundaries.zh-TW.md) |
| 新增、移動、複製、摘要 durable information；決定或改變 owner；發現 duplication、missing owner、overloaded parent；或進行 hierarchy rebalance | 決定 placement、拆分、上提、下沉或移除前讀 [placement.md](references/placement.zh-TW.md) |
| 新增、刪除、搬移、重新命名或實質修改 durable information structure、authority、reference trigger、navigation、history relationship 或 loading relationship | 決定完整影響範圍與修改順序前讀 [change-impact.md](references/change-impact.zh-TW.md)；修改後依同一方法重新走到影響邊界 |
| 建立、修改、移動、合併或 review runtime-loaded instruction、skill、reference trigger、reference routing、載入假設或 guaranteed loading path | 設計或判斷載入行為前讀 [runtime-context.md](references/runtime-context.zh-TW.md) |
| Artifact 的主要用途是讓人或 AI 持久閱讀、理解或執行，例如 README、guide、runbook、design doc、ADR、migration note、handoff、changelog 或 release note | 組織、撰寫或 review 文件前讀 [documentation.md](references/documentation.zh-TW.md) |
| 建立或修改 repo / subsystem 入口、directory navigation、source-of-truth discovery、nested repo boundary 或 forwarding location | 設計或修改導航前讀 [repository-navigation.md](references/repository-navigation.zh-TW.md) |
| 要跨 public、private、confidential 或其他不同資訊範圍引用、摘要、同步或搬移內容，或現有 classification 看起來可能需要調整 | 決定揭露、搬移或提出 reclassification 建議前讀 [information-boundaries.md](references/information-boundaries.zh-TW.md) |
| 任務涉及 durable historical record、current / superseded / obsolete 狀態、migration evidence lifecycle，或歷史與現行 authority 的分工 | 決定 history placement、status 或 navigation 前讀 [history.md](references/history.zh-TW.md) |
| 任務涉及 Git commit history、commit subject / body 作為 history navigation，或需要從 Git history 漸進深入 diff/source | 在判斷 Git-specific history navigation 前先讀 [history.md](references/history.zh-TW.md)，再讀 [commit-history.md](references/commit-history.zh-TW.md) |
| 完成資訊架構 review，或交付有實質資訊架構變更的產物 | 最終結論或交付前讀 [review-checklist.md](references/review-checklist.zh-TW.md) |

## 完成條件

完成前，使用 [review-checklist.md](references/review-checklist.zh-TW.md) 的穩定檢查項目集合，只核對本次實際適用的 dimensions；不要為了形式機械執行無關項目。至少要能判斷 natural owner、單一 authority、mandatory information reachability、必要 reference loading、navigation、duplication/drift risk、history/current 分工、適用資訊邊界與影響邊界是否正確。

若 review 中發現一個可重複、跨案例成立且目前 checklist 未涵蓋的新 failure mode，明確指出這個候選 dimension；不要只在本次臨時加標準，也不要未經判斷就把一次性特例永久加入 checklist。

結構檢查、情境演練、實際 runtime loading 測試與部署狀態分開回報。沒有對應證據就保持未驗證。
