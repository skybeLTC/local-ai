# Repository Navigation

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/repository-navigation.md`。

本 skill 的 authority、placement 與 change-impact 核心契約由 `../../../skills/progressive-context-design/SKILL.md` 持有；本文件只處理 navigation 方法。

本 reference 用於 repo/subsystem entry、source-of-truth discovery、directory navigation、forwarding location 與 nested repo boundary。它回答「不知道細節內容的人如何可靠找到 natural owner」，不決定 source module / service architecture。

## Navigation 與 placement 分開

Placement 回答資訊應由誰持有；navigation 回答接收者從已知入口如何找到該 owner。不要因某資訊位於正確檔案，就假設陌生 agent 能可靠找到；也不要為了導航方便，把 authority 複製到多處。

## 建立 repo / subsystem entry

入口先說明主要目的、scope、responsibility boundary 與自然入口，不列完整 file tree。每個 navigation item 要讓讀者知道：

- 什麼情況需要進入；
- 路徑相對於哪個 root；
- 進入後預期找到哪類 authority / evidence。

Subsystem layer 只有在提供獨立 scope、lifecycle、maintenance responsibility 或 navigation value 時存在。若中介層只把讀者再導向下一層，且沒有新的 decision value，考慮移除或合併。

## Source-of-truth discovery

當多個相似檔案、mirror、generated artifact 或 historical copy 共存時，navigation 必須能辨識 現行權威。不要使用「看起來最新」、「目錄比較上層」或修改時間作唯一 authority 判據。

Derived mirror 可以被 navigation 指到，但需清楚標示 canonical / derived relation，避免 agent 從 mirror 反向維護 authority。

## Nested repos

Nested Git repos 要分開指出：

- 哪個 path 由哪個 repo 管理；
- 哪些 configuration / docs 是 shared，哪些只屬特定 repo 或 environment；
- cross-repo link 的接收者是否實際可取得；
- modification authorization 是否跨 repo 成立。

目錄相鄰、nested、被 parent ignore 或具有相同檔名，都不能證明共用 Git history、authority 或修改授權。

## Navigation change

移動 entry 或 owner 後，更新所有有實際 navigation dependency 的 links / indexes / handoffs。舊位置若仍需要協助 discovery，只保留最小必要 forwarding information；不要保留第二份 current policy。

Navigation change 同時可能影響 placement、runtime loading 與 change-impact propagation；符合 trigger 時必須讀取對應 references。
