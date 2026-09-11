# Durable Documentation 結構

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/documentation.md`。

本 reference 用於主要用途是讓人或 AI 持久閱讀、理解或執行的文件，例如 README、guide、runbook、design doc、ADR、migration note、handoff、changelog 與 release note。`../../../skills/progressive-context-design/SKILL.md` 持有 README / runtime instruction 的 authority boundary；本文件只處理文件結構與閱讀路徑。

## 先確認文件角色

同一份文件先確定主要角色：入口導航、概念說明、執行程序、設計決策、migration/handoff、release/history 或其他 durable purpose。不同角色可以共存，但不要讓 current procedure、historical example、rationale 與 status 混到讀者無法判斷哪個現在有效。

Root-level 文件聚焦整體目的、scope、主要責任與自然入口。Subsystem 細節只有在具有獨立 scope、lifecycle、maintenance responsibility 或 navigation value 時才下沉；也不要只因 directory 存在就建立 README。

## AI-friendly 不等於更多文件

文件應讓接收者能回答：

- 我現在在看什麼 scope？
- 哪些內容是 authoritative / current？
- 下一步需要去哪裡？
- 哪些 detail 只有特定條件才值得讀？

如果 local source comment 已足夠承擔資訊，不必為了索引它而建立上層文件。反過來，如果一個 mandatory workflow rule 只有在深入 README 後才看得到，就需要重新 placement。

## README 與 guide

README 適合用途、主要 architecture、lifecycle、maintenance、rationale 與 general navigation。它可以引用 runtime instruction owner，但不能作為 mandatory policy 的 forwarding-only substitute。

一個文件單位處理一個可理解或可執行主題。只有 scope、讀取時點或維護責任不同時才拆分；不要逐句拆檔，也不要把互相高度耦合的步驟拆到讀者必須反覆跳轉。

## Runbook / procedure

- 整段程序共同需要的環境、版本、輸入、工具與權限放在入口；只影響單一步驟的 precondition 放在該步驟前。
- Warning、constraint 與 stop condition 放在受影響 action 前。
- 會決定下一步的 observable result 與 criterion 留在對應 action 附近。
- Branch 放在 condition 實際發生的位置；condition 無法判定時保留 unknown path，不把未知當成功或失敗。
- 後續 action 依賴尚未取得的 result / approval 時，在相依 action 前明示停止點；不把無相依的其他工作一併阻塞。

本 skill 只負責 procedure 的資訊可執行性；command correctness、工程驗證與 domain-specific 方法仍由適用技術方法負責。

## Design doc 與 ADR

Design doc 應清楚分開 current decision、constraints、alternatives、evidence 與 open questions。ADR 類文件若具有 status，必須能辨識 accepted/current、superseded、deprecated 或其他實際狀態；歷史 decision 不應被誤讀成 current runtime rule。

不要因 ADR 記錄完整 rationale，就要求 runtime agent 每次先讀完整 ADR 才知道現行規則。Current authority 仍需存在正確 owner；ADR 保留 decision history。

## Migration note 與 handoff

Migration / handoff 應清楚區分：

- 已完成且已驗證的 current state；
- 已修改但未驗證的 state；
- deferred decision / known gap；
- historical source / previous checkpoint；
- 下一個工作需要的 evidence 或 entry point。

如果 handoff 只是 temporary evidence，要有 lifecycle：何時仍需保存、何時 current docs 已吸收資訊、何時可移除。

## Changelog / release note

Changelog / release note 主要回答「哪個 release 發生哪些 externally relevant changes」。不要讓它變成完整 implementation rationale 或 current policy owner；需要 deeper context 時導向對應 history、issue、design doc 或 source。

## History、example 與 current procedure

Example、舊 command、screenshot 與 historical state 必須明確標示。不要讓讀者必須從日期或上下文猜哪段仍有效。涉及跨 history 類型的 current/history 分工時，依 [history.md](history.zh-TW.md)。
