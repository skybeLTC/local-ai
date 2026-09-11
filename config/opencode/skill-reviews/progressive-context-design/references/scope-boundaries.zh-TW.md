# 範圍界線

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/scope-boundaries.md`。

本 reference 用於區分資訊架構與工程、skill authoring、commit-message authoring 或其他專門方法。`../../../skills/progressive-context-design/SKILL.md` 持有本 skill 的核心適用範圍；本文件只處理 responsibility boundary。

## 本 skill 負責

- durable information 的 natural owner、單一 authority、適用範圍與 navigation；
- runtime 執行入口、guaranteed reachability、reference trigger 與 progressive loading；
- hierarchy rebalance 與既有資訊結構修改後的 change-impact propagation；
- README、guide、runbook、design doc、ADR、migration/handoff、repo navigation 與其他 durable documentation 的資訊結構；
- current information 與 durable history 的分工；
- commit history 作為 progressive context 的資訊角色；
- 在既有 public/private/confidential classification 下安排引用、摘要、同步與搬移。

## 工程方法負責

本 skill 不判斷程式正確性、原始碼模組拆分、演算法、API、效能、並行、設定值、測試策略或 build 實作，也不能以「progressive context」為理由新增 wrapper、抽象層或程式重構。

如果任務是「修正程式並補文件」，工程方法先建立正確行為與證據；本 skill 再決定已確立資訊應如何被持久保存與導航。Review 文件時即使發現實作問題，也不因此取得修改程式的授權。

## Skill authoring 方法負責

建立、移植、package 或驗證 skill 的格式、metadata、平台能力、release 結構與 behavioral evaluation methodology，由接收平台適用的 skill-authoring 方法負責。

本 skill 可以 review skill 內部的 authority、placement、reference loading、documentation、history 與 change-impact，但不建立第二套 skill packaging 或 validation contract。

## Commit-message 方法負責

本 skill 只判斷 commit subject、完整 commit message、diff/source 在 history navigation 中的資訊層級，以及 current docs 與 history 的分工。

實際 commit message 的格式、措辭、type、scope、body、repo convention、organization convention 與 authoring evidence，由適用的 `commit-message` 方法持有。該方法不可用時，本 skill仍可指出 history-navigation 缺口，但不能自行建立第二套 commit-message authoring 規範。

## 邊界不明時

「架構」可能指資訊架構或軟體架構；「review skill」可能同時包含 package correctness 與 information architecture；「更新文件」可能同時要求驗證實作。只有不同解讀會改變修改範圍、權限或輸出時，才取得最小必要釐清；可由已取得 evidence 唯一判定時不要重問。
