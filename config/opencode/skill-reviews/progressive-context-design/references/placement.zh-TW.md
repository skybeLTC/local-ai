# 資訊歸屬與 Hierarchy Rebalance

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/placement.md`。

本 reference 用於決定 durable information 的 natural owner，以及既有 hierarchy 是否需要拆分、上提、下沉、合併或移除中介層。核心單一 authority 與 local-owner-first 規則由 `../../../skills/progressive-context-design/SKILL.md` 持有。

## 先找 natural owner

先問三件事：

1. 哪些任務或讀者真的需要這段資訊？
2. 他們在什麼時點必須取得它？
3. 哪個最窄位置能可靠覆蓋這些需要者，而且不要求無關 scope 永久載入？

典型位置如下：

| 資訊 | 常見 natural owner |
| --- | --- |
| 跨專案仍需遵守的個人或平台行為 | 適用的 global instruction owner |
| 同一專案跨任務都適用的新增 invariant | project-level instruction owner |
| 完成特定 task 的方法 | task skill 的執行入口與 conditional references |
| 某 subtree 修改時 mandatory 的 local invariant | 接收平台能保證載入的最窄 local instruction owner |
| 用途、設計理由、生命週期、維護或一般導航 | README 或對應 guide |
| 單一設定值、局部行為、演算法 invariant 的鄰近理由 | source/config comment 或局部文件 |
| 過去變更、決策或狀態 | 對應 durable history owner |
| 支持特定版本或驗證結果的觀察 | evidence artifact，保留版本與來源 |

這是常見 mapping，不是檔名模板。若目標平台沒有某種 instruction file，就使用其實際可達的等價 owner。

## Local-owner-first 與 progressive stop

如果資訊已位於最接近作用對象的 natural owner，而且沒有更高層 runtime、navigation、public contract 或 maintenance dependency，review 在此停止，不向上建立摘要或索引。

例如一行演算法旁的註解若只解釋該實作不可見的 invariant，source comment 通常足夠。若規則是「任何修改這個 subtree 的 agent 都必須先做 X」，source comment 可能太晚才看見，這時需要更早且 guaranteed reachable 的 instruction owner。

## Parent 與 child

Parent 只持有 child 共通的 invariant、必要 inheritance contract 或進入 child 前必須知道的 navigation。Child 只持有 local delta、exception 與 additional constraint。

不要為了讓 child standalone 而全文複製 parent。若 child 例外於 shared rule，明確寫出例外條件與受影響 scope。

## Rebalance，而不是一直往下疊加

當 parent 累積大量 child-specific rules 時：

1. 分類哪些規則真正 shared；
2. 把 child-specific rules 下沉到各自 natural owner；
3. 若有更廣泛 shared rule，評估是否上提到適合的 ancestor；
4. 若 parent instruction layer 不再有 mandatory responsibility，考慮移除；
5. 若只剩一般導航且導航有持久價值，通常由 README 或 navigation owner 承擔；
6. 修改後重新檢查 inherited contract、reference loading 與 navigation。

Filesystem nesting、目錄相鄰或檔名一致都不能單獨證明 authority inheritance。

## 建立或移除資訊單位

不要為了填滿結構建立 README、AGENTS、reference、index 或中介層。只有以下至少一項成立時才值得分離：

- 適用範圍不同；
- 讀取時點不同；
- 維護責任不同；
- mandatory loading requirement 不同；
- 獨立導航價值成立。

反過來，若中介層不再提供這些價值，也要考慮合併或移除，而不是因為它已存在就永久保留。

## 搬移與 derived copy

搬移 authority 前指出原 owner、目的 owner 與所有引用者。搬移後原位置只保留仍有價值的最小導航，不留下第二份現行規則。

Derived mirror、generated copy 或必要摘要可以存在，但要有一份 authoritative source、明確同步關係與用途差異。若接收 runtime 可能同時把兩份當 authoritative instructions，先修正載入結構。

Placement 變更會改變 dependency graph，實際 propagation 依 [change-impact.md](change-impact.zh-TW.md)。
