# 資訊邊界

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/information-boundaries.md`。

本 skill 的資訊邊界核心契約由 `../../../skills/progressive-context-design/SKILL.md` 持有；本文件只處理既有 classification 下的 placement 與 disclosure 方法。

本 reference 用於既有 public、private、confidential 或其他 visibility / disclosure boundary 下的引用、摘要、同步與搬移。它處理 information placement，不建立 privacy、security、organization 或 project classification policy。

本文件將「誰可以取得這份資訊」稱為**資訊範圍**，與規則的「適用範圍」分開。

## 先確認既有 classification

先辨識 source 與 destination 的資訊範圍、各自 authority，以及本次操作是否跨 boundary。Directory nesting、repo adjacency、相似名稱或同一 host 都不能證明 visibility / ownership 相同。

如果適用 authority 尚未決定內容能否揭露，而且這會影響相依工作，停止 disclosure / move decision，不自行擴大資訊範圍。

## 發現 classification 看起來不合理

本 skill 可以指出：目前 classification 造成 mandatory information 無法到達需要者、public/private ownership 與實際責任不一致、或 maintenance cost 明顯異常。

這時提供具體理由、受影響行為與建議 classification，並詢問使用者或適用 authority 是否要調整。未取得決定前仍按現有 boundary 行事。

## 引用與摘要

較廣資訊範圍的入口需要導向較窄範圍的 component 時，只保留該範圍真正可以且需要知道的 responsibility、interface、input type 或 navigation information。不要為了文件自足複製 private settings、internal identifiers 或其他 restricted detail。

如果接收者無法取得 restricted reference，就不能把執行所需 mandatory rule 只放在該 reference。應重新 placement 可揭露的最低必要規則，而不是建立 hidden dependency。

## 搬移與同步

資訊從較窄範圍移到較廣範圍前，重新確認 disclosure authorization、derived copies 與所有 dependents。搬移後更新 links 並確認舊位置沒有留下 competing current version。

需要 redaction 時保留足以支持任務判斷的結構，並標示已遮蔽；不要用 invented value 取代 unavailable evidence。

Information-boundary change 也會改變 dependency graph，符合條件時依 [change-impact.md](change-impact.zh-TW.md) 傳播。
