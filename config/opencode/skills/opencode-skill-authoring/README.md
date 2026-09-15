# opencode-skill-authoring

這個 skill 是目前 public OpenCode skill authoring 的單一 runtime authority。它處理建立、修改、review、migration、behavior evaluation、validation 與 handoff；不持有一般資訊架構方法，也不取代 `cross-ai-review` 的 peer-review workflow。

英文 `SKILL.md`、英文 `references/*.md` 與 `agents/*.md` 是 runtime／supporting authority。同步繁中人工檢視版位於 `../../skill-reviews/opencode-skill-authoring/`，不屬於 OpenCode skill source。

## 文件地圖

| 路徑 | 用途 |
| --- | --- |
| `SKILL.md` | 最低必要 workflow、authority boundary、validation 與所有 reference triggers |
| `references/target-runtime.md` | 依實際 target 判斷 discovery、ID、permission 與 loading contract |
| `references/legacy-v1.md` | legacy V1 target 與 V1→V2 migration 分支 |
| `references/migration-review.md` | keep／merge／replace／remove 與 change-impact propagation |
| `references/behavior-evaluation.md` | trigger、loading 與 changed-behavior 的評估方法 |
| `references/evaluation-workflow.md` | 非簡單比較、重複 run、grader／comparator／human review 的執行方法 |
| `references/schemas.md` | evaluation workspace 使用的 JSON formats |
| `references/bilingual-output.md` | 英文 runtime authority 與 `skill-reviews/` mirror mapping |
| `references/validation-handoff.md` | 最終 validation、archive、handoff 與狀態回報 |
| `scripts/`、`agents/`、`eval-viewer/` | 原有 evaluation／validation helpers；只在對應 branch 需要時使用 |

## 名稱與歷史

本 skill 原名為 `skill-creator`。這次收斂為 `opencode-skill-authoring`，原因是責任只針對 OpenCode，較明確的 ID 可降低 generic `skill-creator` 名稱與其他來源碰撞或被誤解為跨平台 authority 的風險。Rename 同輪更新 directory、frontmatter ID、permission 與 navigation；不保留第二份 alias skill。

原有 Apache-2.0 notice 繼續由 `LICENSE.txt` 保留。Matt Pocock `writing-for-agents` 的既有整合 provenance 仍由上一層 `../README.md` 集中記錄；本 README 不複製第三方歷史全文。

## 維護

- 修改 runtime English text 時，同輪更新 `../../skill-reviews/opencode-skill-authoring/` 對應 mirror。
- Runtime contract 必須以實際 target OpenCode source／binary／config 為準；official V2 文件只能在 target 已確認使用相應 V2 contract 時直接套用。
- Evaluation helpers 目前保留，因為 `SKILL.md` 仍提供該能力。若未來要刪除或拆出，先證明對應 capability 已不需要或已有新的 natural owner。
