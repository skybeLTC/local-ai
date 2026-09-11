# 變更影響傳播

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/change-impact.md`。

本 reference 用於 durable information structure 發生實質變更後，沿 authority、loading、navigation、history 與同步 dependency 找出需要重新確認或修改的資訊。`../../../skills/progressive-context-design/SKILL.md` 持有必須傳播到有證據支持的影響邊界 的核心規則。

## 1. 建立變更集合

列出本次已知變更節點與類型：新增、刪除、搬移、重新命名、拆分、合併、上提、下沉、authority 改變、reference trigger 改變或其他實質語意修改。

純排版、拼字或可證明不改變語意、名稱、路徑、引用、載入、導航與適用範圍的修改可以記錄為不需傳播；不能只因 diff 很小就套用例外。

## 2. 往上游確認

對每個變更節點找出直接 authority、定義、前提、限制、來源與 inherited contract，至少確認：

- 新內容仍在上游 authority 的 scope 內；
- 名稱、條件、規則強度、例外與假設仍一致；
- 變更是否暴露上游 owner 過載、過期或已不再是 natural owner；
- authority、scope 或 loading relation 改變時，原上游 relationship 是否應移除、上提或改接。

若上游需要修改，把它加入變更集合並重新執行本程序。

## 3. 往下游確認

找出直接引用、摘要、derived mirror、navigation、loader、consumer、history link 或其他依賴者，至少確認：

- path、filename、stable ID 與相對引用仍可解析；
- 下游使用的 semantics、條件、例外、規則強度與 scope 仍正確；
- reference trigger、loading order、guaranteed reachability 與 stop condition 仍能取得新內容；
- README、index、history、mirror、generated artifact 或 handoff 沒有保留舊 authority 或舊語意；
- 下游若依賴 input/output/behavior contract，該 contract 仍成立。

若下游需要修改，把它加入變更集合並繼續傳播。

## 4. 何時檢查 siblings

不要因有共同 parent 就掃全部 siblings。只有出現以下 signal 時才檢查 sibling：

- shared parent rule 或 inherited contract 改變；
- duplication、mirror 或 summary relation；
- hierarchy rebalance 顯示部分 child-specific rule 可能放錯層；
- navigation 或 index 同時描述多個 siblings；
- 新 evidence 顯示 sibling 消費同一 authority。

Sibling 因此需要修改時，也成為新變更節點。

## 5. Hierarchy rebalance

每次 substantial information-architecture change 都要問：

- parent 是否因這次變更更像 child-specific rule container？
- child 是否已經形成獨立 scope 或 maintenance responsibility？
- shared rule 是否應上提？
- local rule 是否應下沉？
- 中介 instruction layer 是否只剩一般 navigation，或已無獨立 responsibility？

不要只確認「新檔案已建立」，也要確認舊 hierarchy 是否仍合理。

## 6. Edit scope 與 decision boundary

Impact traversal 與 edit authorization 分開判斷。

如果額外修改是完成使用者已授權 outcome 明確必要的一部分，仍在同一 repo / information / authorization boundary 內，而且不新增產品、工程或 policy decision，可以一起修改。

以下狀況先停止相依 edit，回報 impact 與建議並取得決定：

- 跨 repo 或超出目前修改授權；
- 跨 public/private/confidential 或其他資訊 boundary；
- 需要改變新的 authority / classification；
- 存在兩個以上會造成不同持久行為的合理取捨；
- 必要 evidence 不足以判定安全且正確的 propagation。

Review 可以繼續到 evidence-supported boundary；不能因沒有 edit authorization 就假裝沒有 impact。

## 7. 判定影響邊界

每個 traversal branch 都需要具體停止理由。可以停止的典型情況：

- 沒有下一個可追溯 dependency；
- 有下一個 dependency，但直接 evidence 顯示本次變更沒有改變它與目前節點的 contract；
- authority／資訊邊界明確隔離此變更；
- 繼續需要尚未授權或尚未取得的 decision/evidence，此時標記為 unresolved boundary，而不是 verified unaffected。

「沒直接編輯」、「看起來沒問題」、「以前如此」或「熟悉這區」都不是停止理由。

## 8. 控制範圍

優先使用可追溯關係建立候選集合：direct links、path/name/stable-ID search、reference trigger、loader relation、authority/mirror mapping、README/index/navigation、history/handoff 中明示 dependency。只有新 evidence 指出 additional relation 時才擴大。

每次擴大都保留「哪個變更節點導致這個候選」的追溯關係，不把 impact review 退化成無條件整庫掃描。

## 9. 最終判定

完成前應能說明：

1. 哪些上游依賴重新確認；
2. 哪些下游依賴者重新確認；
3. 哪些 siblings 因實際 signal 被納入；
4. 哪些節點因此繼續傳播；
5. hierarchy 是否需要 rebalance；
6. 每個方向在哪個影響邊界停止，以及證據；
7. 是否仍有 authorization、information-boundary 或 evidence gap。

這個程序驗證 dependency consistency，不代表 runtime 自動載入、程式行為、安裝或部署狀態已被實際測試。
