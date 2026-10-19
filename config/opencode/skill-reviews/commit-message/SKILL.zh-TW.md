---
name: commit-message
description: "根據實際 Git 變更撰寫、檢查或重寫 commit message，包括完成程式實作後的提交訊息。"
---

# Commit Message

## 撰寫與檢查

撰寫 commit message，或根據實際變更檢查、重寫既有 commit message 前，必須查看目標 repository 的 Git commit history。

Git commit history 用來了解過去的專案術語、慣例與變更，但既有 commit message 的格式範例不能覆蓋目前明確適用的格式規範。如果多份目前適用的格式規範發生衝突，而且優先順序尚未確定，須在採用有衝突的格式前詢問使用者。

根據實際變更與已取得的證據撰寫、檢查或重寫 commit message。

資訊不足以確認內容正確性時，先自行補查。補查後仍無法確認時，才詢問使用者。

Commit message 必須清楚、具體、資訊充分且準確。不得將未經證實的原因、影響或驗證結果寫成事實。

讓未參與本次工作的維護者能依 commit 的實際變更與持久的專案脈絡理解內容。不得把僅存在於目前對話或暫時工作流程的名稱當成理解變更或驗證結果所必需的資訊；有必要記錄測試時，應說明可辨識的測試範圍與結果。只納入有助於解釋本次 commit 的背景；不因某項未納入本次 commit 的獨立工作曾在對話中討論，就將它寫進 commit message。

檢查既有 commit message 時，指出實質問題；需要修正時，提供修正版本。

## 輸出

撰寫或重寫 commit message 時，必須包含 subject 與 body。

預設提供：

- **英文正式版**：可直接用於 Git commit 的完整英文訊息。
- **台灣繁體中文檢視版**：供檢查的完整語意對照，不屬於實際 Git commit message。

兩個版本必須語意一致。預設在回覆中直接完整呈現兩個版本；即使另外建立檔案，也不得只提供檔案路徑或摘要。使用者明確要求其他交付方式時，依該要求處理。

本 skill 不提供修改 Git repository 或 Git history 的授權。
