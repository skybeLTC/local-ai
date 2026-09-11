# 資訊架構驗收 Dimensions

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/review-checklist.md`。

本 skill 的最低執行契約由 `../../../skills/progressive-context-design/SKILL.md` 持有；本文件只提供穩定的 final-review dimensions inventory。

本 reference 是穩定的 review dimensions inventory。完成資訊架構 review 或交付實質資訊架構變更前，先判斷哪些 dimensions 與本次 artifact / change 有關，再只核對適用項目。不要為了形式機械跑完全部項目；也不要每次臨場更換判準。

若 review 中發現一個可重複、跨案例成立且目前未涵蓋的新 failure mode，將它明確標成「candidate review dimension」並說明理由；不要直接把一次性特例永久加入，也不要只在本次偷偷換標準。

## 1. Target、scope 與 responsibility

- 執行平台、接收平台、artifact type、實際 loading mechanism 是否分開？
- Review / edit authorization 是否區分？
- Information architecture 與 engineering、skill authoring、commit-message authoring 或其他專門方法的責任是否分開？
- 語言、格式與 classification 是否來自適用 authority？

## 2. Natural owner 與 authority

- 每條 現行規則 是否有一個能可靠覆蓋需要者的最窄 natural owner？
- Local information 是否留在 natural owner，而沒有無必要向上複製？
- README、runtime instruction、skill、source comment、history、evidence 是否持有適合其角色的資訊？
- Derived mirror / generated copy 是否有唯一 canonical owner 與同步關係？
- 是否存在 forwarding-only mandatory policy、competing current versions 或 history-as-current-policy？

## 3. Hierarchy balance

- Parent 是否塞入過多 child-specific rules？
- Shared invariant 是否應上提、local rule 是否應下沉？
- Child 是否只保留 local delta / exception / additional constraint，而沒有全文複製 parent？
- 中介 instruction/navigation layer 是否仍有獨立 scope、loading 或 navigation value？
- Filesystem nesting 是否被錯當 authority nesting？

## 4. Progressive loading 與 reachability

- 每個執行 reference 是否都有 observable trigger、exact path、read-before point 與 missing behavior？
- Mandatory local information 是否有從 guaranteed entry point 可達的 loading path？
- Reference 拆分後是否仍能從入口觸發，而沒有 capability 斷鏈？
- 多個 triggers 同時成立時是否能取得所有必要 references？
- 未觸發 reference 是否保持未預載？
- Trigger unknown、reference missing/denied、內容版本改變或離開 context 時是否有正確處理？

## 5. Documentation 與 procedure

- Durable documentation 是否清楚說明 scope、current status、natural entry 與 deeper path？
- README 是否承擔 rationale/maintenance/navigation，而沒有獨占 mandatory runtime policy？
- Procedure 的 precondition、warning、stop point、observable result、criterion 與 branch 是否靠近受影響 action？
- Current procedure、historical example、fact、assumption、evidence 與 open question 是否可區分？

## 6. Repository navigation

- 從自然入口是否能找到真正 source of truth？
- Navigation item 是否說明何時進入、path root 與預期找到什麼？
- Nested repo / multi-repo ownership、Git history 與 modification authorization 是否清楚？
- 是否存在只轉介、沒有新增 decision value 的 navigation layer？

## 7. History

- 後續 agent 是否不用 replay 全 history 就能知道 current state？
- Historical artifact 是否能辨識 current / superseded / obsolete 或目標實際使用的等價狀態？
- Temporary migration/handoff evidence 是否有 lifecycle / retirement condition？
- Git history 適用時，subject → full message → diff/source 的 progressive path 是否有效？
- Commit-message information role 是否被誤寫成 commit-message authoring authority？

## 8. Information boundary

- Source/destination 的 public/private/confidential 或其他資訊範圍是否已確認？
- 本 skill 是否只沿既有 classification 行事，而沒有自行擴大 disclosure？
- 若 classification 看起來不合理，是否提出具體理由與建議並停在 decision boundary？
- Mandatory information 是否被藏在接收者無法取得的 restricted location？

## 9. Change-impact propagation

- 本次所有 substantive change nodes 是否列入？
- Direct upstream / downstream dependency 是否重新確認？
- Sibling 是否只在 shared-contract / duplication / navigation 等實際 signal 下納入？
- 相依節點需要修改時是否成為新 change node 繼續傳播？
- Hierarchy rebalance 是否納入 propagation，而不是只更新 link？
- 每個 branch 是否停在有 evidence 的 影響邊界？
- Authorization、資訊邊界 或 evidence gap 是否保持 unresolved，而沒有被當成 unaffected？

## 10. Completion evidence

- Structure check、scenario exercise、actual runtime loading、behavior test、deployment/install state 是否分開回報？
- Validation claim 是否只涵蓋實際 evidence 支持的 version / state？
- 若有未驗證部分，是否說明它影響哪個 judgment 或下一步？

發現缺口時，指出 natural owner / authority、受影響 action、最小必要 correction 與任何未決 boundary。Review 本身不授權額外修改。
