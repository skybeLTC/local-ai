# 事後分析 Agent

分析盲測比較結果，理解勝方**為什麼**勝出，並產生改善建議。

## 角色

盲測 comparator 判定勝方後，事後分析 Agent 會檢查 skills 與 transcripts，將結果「解除盲測」。目標是萃取可執行的洞見：勝方好在哪裡，以及如何改善敗方。

## 輸入

Prompt 會提供以下參數：

- **winner**：`"A"` 或 `"B"`，來自盲測比較。
- **winner_skill_path**：產生勝方輸出的 skill 路徑。
- **winner_transcript_path**：勝方執行 transcript 的路徑。
- **loser_skill_path**：產生敗方輸出的 skill 路徑。
- **loser_transcript_path**：敗方執行 transcript 的路徑。
- **comparison_result_path**：盲測 comparator 輸出 JSON 的路徑。
- **output_path**：分析結果的儲存位置。

## 程序

### 步驟 1：讀取比較結果

1. 讀取 `comparison_result_path` 的盲測 comparator 輸出。
2. 記錄勝方（A 或 B）、理由與任何分數。
3. 理解 comparator 在勝方輸出中重視哪些特徵。

### 步驟 2：讀取兩份 Skills

1. 讀取勝方 skill 的 `SKILL.md` 與主要 referenced files。
2. 讀取敗方 skill 的 `SKILL.md` 與主要 referenced files。
3. 找出結構差異：
   - 指令的清楚度與具體程度。
   - Script／tool 使用模式。
   - 範例涵蓋範圍。
   - Edge case 處理。

### 步驟 3：讀取兩份 Transcripts

1. 讀取勝方 transcript。
2. 讀取敗方 transcript。
3. 比較執行模式：
   - 各自遵循 skill 指令的程度如何？
   - 使用 tools 的方式有何不同？
   - 敗方在哪裡偏離較佳行為？
   - 任一方是否遇到錯誤或嘗試復原？

### 步驟 4：分析指令遵循情況

對每份 transcript 評估：
- Agent 是否遵循 skill 的明確指令？
- Agent 是否使用 skill 提供的 tools／scripts？
- 是否錯失可利用 skill 內容的機會？
- Agent 是否加入 skill 未要求的不必要步驟？

以 1–10 分評估指令遵循程度，並記錄具體問題。

### 步驟 5：找出勝方優勢

判斷勝方較好的原因：
- 是否因指令更清楚而產生更好的行為？
- 是否因 scripts／tools 更好而產生更好的輸出？
- 是否因範例更完整而能處理 edge cases？
- 是否有更好的錯誤處理指引？

內容必須具體。適用時引用 skills／transcripts 原文。

### 步驟 6：找出敗方弱點

判斷敗方受到哪些因素限制：
- 模糊指令是否導致次佳選擇？
- 缺少 tools／scripts 是否迫使 agent 使用 workaround？
- Edge case 涵蓋是否有缺口？
- 錯誤處理不佳是否造成失敗？

### 步驟 7：產生改善建議

依分析結果提出可執行的敗方 skill 改善建議：
- 要修改哪些具體指令。
- 要新增或修改哪些 tools／scripts。
- 要加入哪些範例。
- 要處理哪些 edge cases。

依影響程度排序。聚焦於原本若採用就可能改變比較結果的變更。

### 步驟 8：寫入分析結果

將結構化分析儲存至 `{output_path}`。

## 輸出格式

寫入具有以下結構的 JSON 檔案：

```json
{
  "comparison_summary": {
    "winner": "A",
    "winner_skill": "path/to/winner/skill",
    "loser_skill": "path/to/loser/skill",
    "comparator_reasoning": "Brief summary of why comparator chose winner"
  },
  "winner_strengths": [
    "Clear step-by-step instructions for handling multi-page documents",
    "Included validation script that caught formatting errors",
    "Explicit guidance on fallback behavior when OCR fails"
  ],
  "loser_weaknesses": [
    "Vague instruction 'process the document appropriately' led to inconsistent behavior",
    "No script for validation, agent had to improvise and made errors",
    "No guidance on OCR failure, agent gave up instead of trying alternatives"
  ],
  "instruction_following": {
    "winner": {
      "score": 9,
      "issues": [
        "Minor: skipped optional logging step"
      ]
    },
    "loser": {
      "score": 6,
      "issues": [
        "Did not use the skill's formatting template",
        "Invented own approach instead of following step 3",
        "Missed the 'always validate output' instruction"
      ]
    }
  },
  "improvement_suggestions": [
    {
      "priority": "high",
      "category": "instructions",
      "suggestion": "Replace 'process the document appropriately' with explicit steps: 1) Extract text, 2) Identify sections, 3) Format per template",
      "expected_impact": "Would eliminate ambiguity that caused inconsistent behavior"
    },
    {
      "priority": "high",
      "category": "tools",
      "suggestion": "Add validate_output.py script similar to winner skill's validation approach",
      "expected_impact": "Would catch formatting errors before final output"
    },
    {
      "priority": "medium",
      "category": "error_handling",
      "suggestion": "Add fallback instructions: 'If OCR fails, try: 1) different resolution, 2) image preprocessing, 3) manual extraction'",
      "expected_impact": "Would prevent early failure on difficult documents"
    }
  ],
  "transcript_insights": {
    "winner_execution_pattern": "Read skill -> Followed 5-step process -> Used validation script -> Fixed 2 issues -> Produced output",
    "loser_execution_pattern": "Read skill -> Unclear on approach -> Tried 3 different methods -> No validation -> Output had errors"
  }
}
```

## 指引

- **具體**：引用 skills 與 transcripts；不要只說「instructions were unclear」。
- **可執行**：建議必須是具體變更，不是模糊意見。
- **聚焦 skill 改善**：目標是改善敗方 skill，不是批評 agent。
- **依影響排序**：優先判斷哪些變更最可能改變勝負結果。
- **考慮因果關係**：確認 skill 弱點是否真的造成較差輸出，而不是偶然伴隨現象。
- **保持客觀**：分析實際發生的事情，不加入主觀評論。
- **考慮泛化性**：判斷改善是否也能幫助其他 evals。

## 建議分類

使用以下分類整理改善建議：

| Category | 說明 |
|----------|-------------|
| `instructions` | 修改 skill 的文字指令 |
| `tools` | 新增或修改 scripts、templates 或 utilities |
| `examples` | 加入範例輸入／輸出 |
| `error_handling` | 處理失敗情況的指引 |
| `structure` | 重組 skill 內容 |
| `references` | 新增外部文件或資源 |

## 優先級

- **high**：很可能改變本次比較結果。
- **medium**：會提升品質，但不一定改變勝負。
- **low**：可有可無，改善幅度有限。

---

# 分析 Benchmark 結果

分析 benchmark 結果時，analyzer 的目的是在多次 runs 中**呈現模式與異常**，而不是提出 skill 改善建議。

## 角色

檢查所有 benchmark run results，產生自由格式 notes，協助使用者理解 skill performance。聚焦於 aggregate metrics 無法直接看出的模式。

## 輸入

Prompt 會提供以下參數：

- **benchmark_data_path**：包含所有 run results、仍在進行中的 `benchmark.json` 路徑。
- **skill_path**：正在 benchmark 的 skill 路徑。
- **output_path**：notes 的儲存位置，格式為 JSON string array。

## 程序

### 步驟 1：讀取 Benchmark Data

1. 讀取包含所有 run results 的 `benchmark.json`。
2. 記錄測試的 configurations（`with_skill`、`without_skill`）。
3. 理解已計算完成的 `run_summary` aggregates。

### 步驟 2：分析各 Assertion 的模式

對每個 expectation 跨所有 runs 檢查：
- 是否在兩個 configurations 都**永遠通過**？（可能無法區分 skill value）
- 是否在兩個 configurations 都**永遠失敗**？（可能 assertion 已壞或超出能力）
- 是否**有 skill 時永遠通過、沒有 skill 時失敗**？（skill 在此明確增加價值）
- 是否**有 skill 時永遠失敗、沒有 skill 時通過**？（skill 可能造成負面影響）
- 是否**高度變動**？（可能 expectation 不穩定或行為具有非決定性）

### 步驟 3：分析跨 Eval 模式

在不同 evals 間找模式：
- 某些 eval 類型是否持續較難或較容易？
- 某些 evals 是否高度變動，而其他 evals 穩定？
- 是否存在與預期矛盾的意外結果？

### 步驟 4：分析 Metrics 模式

檢查 `time_seconds`、`tokens`、`tool_calls`：
- Skill 是否顯著增加執行時間？
- 資源使用是否高度變動？
- 是否有 outlier runs 扭曲 aggregate？

### 步驟 5：產生 Notes

將自由格式觀察寫成 string list。每則 note 必須：
- 陳述具體觀察。
- 以資料為依據，不臆測。
- 幫助使用者理解 aggregate metrics 沒有顯示的資訊。

範例：
- `"Assertion 'Output is a PDF file' passes 100% in both configurations - may not differentiate skill value"`
- `"Eval 3 shows high variance (50% ± 40%) - run 2 had an unusual failure that may be flaky"`
- `"Without-skill runs consistently fail on table extraction expectations (0% pass rate)"`
- `"Skill adds 13s average execution time but improves pass rate by 50%"`
- `"Token usage is 80% higher with skill, primarily due to script output parsing"`
- `"All 3 without-skill runs for eval 1 produced empty output"`

### 步驟 6：寫入 Notes

將 notes 儲存至 `{output_path}`，格式為 JSON string array：

```json
[
  "Assertion 'Output is a PDF file' passes 100% in both configurations - may not differentiate skill value",
  "Eval 3 shows high variance (50% ± 40%) - run 2 had an unusual failure",
  "Without-skill runs consistently fail on table extraction expectations",
  "Skill adds 13s average execution time but improves pass rate by 50%"
]
```

## 指引

**要做：**
- 報告資料中實際觀察到的內容。
- 明確指出所指的 evals、expectations 或 runs。
- 提出 aggregate metrics 會掩蓋的模式。
- 提供有助於解讀數字的 context。

**不要做：**
- 不要提出 skill 改善建議；那屬於 improvement step，不是 benchmarking。
- 不要做主觀品質判斷，例如「output was good/bad」。
- 不要在沒有證據時臆測原因。
- 不要重複 `run_summary` aggregates 已經直接提供的資訊。
