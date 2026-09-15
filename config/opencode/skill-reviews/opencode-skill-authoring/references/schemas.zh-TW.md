# JSON Schemas

本文件定義 `opencode-skill-authoring` 使用的 JSON schemas。

---

## evals.json

定義 skill 的 evals。檔案位於 skill directory 內的 `evals/evals.json`。

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's example prompt",
      "expected_output": "Description of expected result",
      "files": ["evals/files/sample1.pdf"],
      "expectations": [
        "The output includes X",
        "The skill used script Y"
      ]
    }
  ]
}
```

**欄位：**
- `skill_name`：與 skill frontmatter 相符的名稱。
- `evals[].id`：唯一的 integer identifier。
- `evals[].prompt`：要執行的 task。
- `evals[].expected_output`：供人閱讀的成功結果描述。
- `evals[].files`：選用的 input file paths 清單，相對於 skill root。
- `evals[].expectations`：可驗證陳述的清單。

---

## history.json

追蹤 Improve mode 的版本演進。檔案位於 workspace root。

```json
{
  "started_at": "2026-01-15T10:30:00Z",
  "skill_name": "pdf",
  "current_best": "v2",
  "iterations": [
    {
      "version": "v0",
      "parent": null,
      "expectation_pass_rate": 0.65,
      "grading_result": "baseline",
      "is_current_best": false
    },
    {
      "version": "v1",
      "parent": "v0",
      "expectation_pass_rate": 0.75,
      "grading_result": "won",
      "is_current_best": false
    },
    {
      "version": "v2",
      "parent": "v1",
      "expectation_pass_rate": 0.85,
      "grading_result": "won",
      "is_current_best": true
    }
  ]
}
```

**欄位：**
- `started_at`：開始 improvement 的 ISO timestamp。
- `skill_name`：正在改善的 skill 名稱。
- `current_best`：目前表現最佳版本的 identifier。
- `iterations[].version`：版本 identifier（v0、v1、...）。
- `iterations[].parent`：此版本衍生自哪個 parent version。
- `iterations[].expectation_pass_rate`：grading 得到的 pass rate。
- `iterations[].grading_result`：`"baseline"`、`"won"`、`"lost"` 或 `"tie"`。
- `iterations[].is_current_best`：此版本是否為目前最佳版本。

---

## grading.json

Grader agent 的輸出。檔案位於 `<run-dir>/grading.json`。

```json
{
  "expectations": [
    {
      "text": "The output includes the name 'John Smith'",
      "passed": true,
      "evidence": "Found in transcript Step 3: 'Extracted names: John Smith, Sarah Johnson'"
    },
    {
      "text": "The spreadsheet has a SUM formula in cell B10",
      "passed": false,
      "evidence": "No spreadsheet was created. The output was a text file."
    }
  ],
  "summary": {
    "passed": 2,
    "failed": 1,
    "total": 3,
    "pass_rate": 0.67
  },
  "execution_metrics": {
    "tool_calls": {
      "Read": 5,
      "Write": 2,
      "Bash": 8
    },
    "total_tool_calls": 15,
    "total_steps": 6,
    "errors_encountered": 0,
    "output_chars": 12450,
    "transcript_chars": 3200
  },
  "timing": {
    "executor_duration_seconds": 165.0,
    "grader_duration_seconds": 26.0,
    "total_duration_seconds": 191.0
  },
  "claims": [
    {
      "claim": "The form has 12 fillable fields",
      "type": "factual",
      "verified": true,
      "evidence": "Counted 12 fields in field_info.json"
    }
  ],
  "user_notes_summary": {
    "uncertainties": ["Used 2023 data, may be stale"],
    "needs_review": [],
    "workarounds": ["Fell back to text overlay for non-fillable fields"]
  },
  "eval_feedback": {
    "suggestions": [
      {
        "assertion": "The output includes the name 'John Smith'",
        "reason": "A hallucinated document that mentions the name would also pass"
      }
    ],
    "overall": "Assertions check presence but not correctness."
  }
}
```

**欄位：**
- `expectations[]`：附有 evidence 的已評分 expectations。
- `summary`：通過／失敗數量的 aggregate。
- `execution_metrics`：Tool 使用情況與 output size，來自 executor 的 `metrics.json`。
- `timing`：Wall clock timing，來自 `timing.json`。
- `claims`：從 output 擷取並驗證的 claims。
- `user_notes_summary`：Executor 標記的問題。
- `eval_feedback`：選用；只有 grader 找到值得提出的問題時，才包含 eval 改善建議。

---

## metrics.json

Executor agent 的輸出。檔案位於 `<run-dir>/outputs/metrics.json`。

```json
{
  "tool_calls": {
    "Read": 5,
    "Write": 2,
    "Bash": 8,
    "Edit": 1,
    "Glob": 2,
    "Grep": 0
  },
  "total_tool_calls": 18,
  "total_steps": 6,
  "files_created": ["filled_form.pdf", "field_values.json"],
  "errors_encountered": 0,
  "output_chars": 12450,
  "transcript_chars": 3200
}
```

**欄位：**
- `tool_calls`：每種 tool type 的呼叫次數。
- `total_tool_calls`：所有 tool calls 的總數。
- `total_steps`：主要執行步驟數量。
- `files_created`：建立的 output files 清單。
- `errors_encountered`：執行期間遇到的 errors 數量。
- `output_chars`：Output files 的總字元數。
- `transcript_chars`：Transcript 的字元數。

---

## timing.json

某次 run 的 wall clock timing。檔案位於 `<run-dir>/timing.json`。

**取得方式：** subagent task 完成時，task notification 會包含 `total_tokens` 與 `duration_ms`。必須立即儲存；這些值不會在其他位置持久化，事後也無法復原。

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3,
  "executor_start": "2026-01-15T10:30:00Z",
  "executor_end": "2026-01-15T10:32:45Z",
  "executor_duration_seconds": 165.0,
  "grader_start": "2026-01-15T10:32:46Z",
  "grader_end": "2026-01-15T10:33:12Z",
  "grader_duration_seconds": 26.0
}
```

---

## benchmark.json

Benchmark mode 的輸出。檔案位於 `benchmarks/<timestamp>/benchmark.json`。

```json
{
  "metadata": {
    "skill_name": "pdf",
    "skill_path": "/path/to/pdf",
    "executor_model": "provider/model-id",
    "analyzer_model": "most-capable-model",
    "timestamp": "2026-01-15T10:30:00Z",
    "evals_run": [1, 2, 3],
    "runs_per_configuration": 3
  },

  "runs": [
    {
      "eval_id": 1,
      "eval_name": "Ocean",
      "configuration": "with_skill",
      "run_number": 1,
      "result": {
        "pass_rate": 0.85,
        "passed": 6,
        "failed": 1,
        "total": 7,
        "time_seconds": 42.5,
        "tokens": 3800,
        "tool_calls": 18,
        "errors": 0
      },
      "expectations": [
        {"text": "...", "passed": true, "evidence": "..."}
      ],
      "notes": [
        "Used 2023 data, may be stale",
        "Fell back to text overlay for non-fillable fields"
      ]
    }
  ],

  "run_summary": {
    "with_skill": {
      "pass_rate": {"mean": 0.85, "stddev": 0.05, "min": 0.80, "max": 0.90},
      "time_seconds": {"mean": 45.0, "stddev": 12.0, "min": 32.0, "max": 58.0},
      "tokens": {"mean": 3800, "stddev": 400, "min": 3200, "max": 4100}
    },
    "without_skill": {
      "pass_rate": {"mean": 0.35, "stddev": 0.08, "min": 0.28, "max": 0.45},
      "time_seconds": {"mean": 32.0, "stddev": 8.0, "min": 24.0, "max": 42.0},
      "tokens": {"mean": 2100, "stddev": 300, "min": 1800, "max": 2500}
    },
    "delta": {
      "pass_rate": "+0.50",
      "time_seconds": "+13.0",
      "tokens": "+1700"
    }
  },

  "notes": [
    "Assertion 'Output is a PDF file' passes 100% in both configurations - may not differentiate skill value",
    "Eval 3 shows high variance (50% ± 40%) - may be flaky or model-dependent",
    "Without-skill runs consistently fail on table extraction expectations",
    "Skill adds 13s average execution time but improves pass rate by 50%"
  ]
}
```

**欄位：**
- `metadata`：Benchmark run 的資訊。
  - `skill_name`：Skill 名稱。
  - `timestamp`：Benchmark 執行時間。
  - `evals_run`：Eval names 或 IDs 清單。
  - `runs_per_configuration`：每個 config 的 run 次數，例如 3。
- `runs[]`：各次 run 的結果。
  - `eval_id`：數值型 eval identifier。
  - `eval_name`：供人閱讀的 eval 名稱；viewer 會用作 section header。
  - `configuration`：新 skill 與無 skill 比較時使用 `"with_skill"`／`"without_skill"`；既有 skill migration 時使用 `"new_skill"`／`"old_skill"`。同一 benchmark 內必須一致使用其中一組；viewer 會辨識這些 exact strings，據此分組並設定 primary／baseline styling。
  - `run_number`：Integer run number（1、2、3...）。
  - `result`：包含 `pass_rate`、`passed`、`total`、`time_seconds`、`tokens`、`errors` 的 nested object。
- `run_summary`：依 configuration 統計的 aggregates。
  - 選定的 configuration pair（`with_skill`／`without_skill` 或 `new_skill`／`old_skill`）：每一方都有 `pass_rate`、`time_seconds`、`tokens` objects，內含 `mean` 與 `stddev` fields。
  - `delta`：差異字串，例如 `"+0.50"`、`"+13.0"`、`"+1700"`。
- `notes`：Analyzer 提供的自由格式 observations。

**重要：** viewer 會以 exact field names 讀取資料。若使用 `config` 取代 `configuration`，或把 `pass_rate` 放在 run 的 top level 而不是 nested under `result`，viewer 會顯示空值／零值。手動產生 `benchmark.json` 時必須依本 schema。

---

## comparison.json

Blind comparator 的輸出。檔案位於 `<grading-dir>/comparison-N.json`。

```json
{
  "winner": "A",
  "reasoning": "Output A provides a complete solution with proper formatting and all required fields. Output B is missing the date field and has formatting inconsistencies.",
  "rubric": {
    "A": {
      "content": {
        "correctness": 5,
        "completeness": 5,
        "accuracy": 4
      },
      "structure": {
        "organization": 4,
        "formatting": 5,
        "usability": 4
      },
      "content_score": 4.7,
      "structure_score": 4.3,
      "overall_score": 9.0
    },
    "B": {
      "content": {
        "correctness": 3,
        "completeness": 2,
        "accuracy": 3
      },
      "structure": {
        "organization": 3,
        "formatting": 2,
        "usability": 3
      },
      "content_score": 2.7,
      "structure_score": 2.7,
      "overall_score": 5.4
    }
  },
  "output_quality": {
    "A": {
      "score": 9,
      "strengths": ["Complete solution", "Well-formatted", "All fields present"],
      "weaknesses": ["Minor style inconsistency in header"]
    },
    "B": {
      "score": 5,
      "strengths": ["Readable output", "Correct basic structure"],
      "weaknesses": ["Missing date field", "Formatting inconsistencies", "Partial data extraction"]
    }
  },
  "expectation_results": {
    "A": {
      "passed": 4,
      "total": 5,
      "pass_rate": 0.80,
      "details": [
        {"text": "Output includes name", "passed": true}
      ]
    },
    "B": {
      "passed": 3,
      "total": 5,
      "pass_rate": 0.60,
      "details": [
        {"text": "Output includes name", "passed": true}
      ]
    }
  }
}
```

---

## analysis.json

Post-hoc analyzer 的輸出。檔案位於 `<grading-dir>/analysis.json`。

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
    "Included validation script that caught formatting errors"
  ],
  "loser_weaknesses": [
    "Vague instruction 'process the document appropriately' led to inconsistent behavior",
    "No script for validation, agent had to improvise"
  ],
  "instruction_following": {
    "winner": {
      "score": 9,
      "issues": ["Minor: skipped optional logging step"]
    },
    "loser": {
      "score": 6,
      "issues": [
        "Did not use the skill's formatting template",
        "Invented own approach instead of following step 3"
      ]
    }
  },
  "improvement_suggestions": [
    {
      "priority": "high",
      "category": "instructions",
      "suggestion": "Replace 'process the document appropriately' with explicit steps",
      "expected_impact": "Would eliminate ambiguity that caused inconsistent behavior"
    }
  ],
  "transcript_insights": {
    "winner_execution_pattern": "Read skill -> Followed 5-step process -> Used validation script",
    "loser_execution_pattern": "Read skill -> Unclear on approach -> Tried 3 different methods"
  }
}
```
