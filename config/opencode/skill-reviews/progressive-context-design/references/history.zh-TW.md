# Durable History 與 Current Authority

> 人工檢視版。英文權威來源：`../../../skills/progressive-context-design/references/history.md`。

本 skill 的 current/history 核心契約由 `../../../skills/progressive-context-design/SKILL.md` 持有；本文件只處理跨 history 類型共通的方法。

本 reference 處理 commits、ADR、changelog、migration record、decision record、handoff history 等 durable historical artifacts 共通的 information-architecture principles。Git-specific progressive path 另由 [commit-history.md](commit-history.zh-TW.md) 持有。

## History 不等於 現行權威

Historical record 說明過去在某個時間點做了什麼、為什麼、當時知道什麼或驗證到什麼。現在仍適用並會改變行為的規則，必須存在 current authoritative owner。

後續 agent 不應被迫 replay 全部 history 才能知道現況；反過來，也不要把每次歷史 rationale 永久塞進 runtime-loaded instructions。

## 能辨識狀態

如果 history artifact 可能被後續當作 decision evidence，應能判斷其 status，例如 current / accepted、superseded、deprecated、obsolete、historical-only 或其他目標實際使用的狀態。不要自行發明 status taxonomy；沿用目標已有 convention，沒有 convention 時使用最少且明確的狀態描述。

Superseded record 應能導向替代它的 current decision 或 newer record；現行權威也應在需要理解 evolution 時能找到 relevant history，但不必預載完整歷史。

## History navigation

History 的第一層應足以篩選 relevant records，再進入較深 rationale/evidence。具體第一層依 artifact type 不同：commit subject、ADR title/status、release heading、migration checkpoint 等。

不要為了統一而把所有 history type 強迫成同一 template。只有跨 artifact 都成立的 principles 放在本 reference；某一 history type 出現足夠獨立、重複且有明確 trigger 的 methodology 時，才拆出專門 reference。

## Migration evidence lifecycle

Migration note、handoff、temporary checkpoint 或 review artifact 若只在過渡期有價值，要明確知道：

- 哪些資訊尚未被現行權威吸收；
- 哪些 evidence 仍支援 deferred decision；
- 什麼條件成立後可以 archive / remove；
- remove 前有哪些 links / references / pending tasks 需要更新。

Temporary artifact 只因檔名含 `tmp` 或位於 test folder 不代表可以刪除；是否仍被後續工作依賴才是判準。

## Changelog / release / ADR 與 current docs

Changelog / release note 適合回答版本演進，不應變成 current runtime policy。ADR 保存 decision rationale 與狀態，不應要求每次 runtime 都載入。Migration/handoff 保存 transition evidence，不應無期限和 current docs 維護同一規則。

需要更深入 Git commit navigation 時，再讀 [commit-history.md](commit-history.zh-TW.md)。
