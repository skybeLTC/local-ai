# Evaluation workflow

Skill change 需要超過 smoke test 的證據時使用本 reference，例如 behavior comparison、regression coverage、human output review 或 repeated benchmark runs。

## 決定 evaluation 要回答哪個問題

選擇能回答目前 uncertainty 的最輕量設計：

- **Smoke test** — OpenCode 是否能 discover/load skill，referenced scripts/files 是否可用？
- **Behavior test** — Skill 在代表 prompts 上是否產生預期可觀察結果？
- **Migration test** — Rewritten skill 是否保留或改善 old version behavior？
- **Baseline comparison** — 相同 model 在沒有 skill 時相比，skill 是否帶來增益？
- **Variance benchmark** — Repeated results 是否穩定到足以信任 comparison？
- **Human review** — Subjective output 對使用者而言是否真的較好？

Smoke test 或兩個 representative cases 已能回答時，不要啟動 full benchmark。

## Test-case format

Evaluation 大到值得重複執行時，把 reusable cases 放在 `evals/evals.json`。完整 schema 見 `references/schemas.md`。

先用 2–3 個 realistic prompts。若測的是 discovery/triggering，加入 near misses 或 edge cases。

每個 case 記錄：

```json
{
  "id": 1,
  "prompt": "A realistic user request",
  "expected_output": "Observable properties of a successful result",
  "files": [],
  "expectations": []
}
```

理解 task 後再寫 expectations。優先使用能從 outputs 或 artifacts 機械／明確檢查的 assertions；subjective qualities 留給 human review。

## Workspace layout

Evaluation artifacts 放在 runtime skill directory 外：

```text
<skill-name>-workspace/
└── iteration-1/
    └── eval-1/
        ├── eval_metadata.json
        ├── with_skill/
        │   └── run-1/
        │       ├── outputs/
        │       ├── grading.json
        │       └── timing.json
        └── without_skill/
            └── run-1/
                ├── outputs/
                ├── grading.json
                └── timing.json
```

有助理解時使用 descriptive eval names，不必只用數字。

以下 configuration directory pairs 必須照寫：

- new skill vs no skill：`with_skill/` + `without_skill/`；
- existing-skill migration：`new_skill/` + `old_skill/`。

不要使用 generic `baseline/` configuration directory。保留的 benchmark aggregator 會依 sorted configuration directory names 推導 primary-vs-baseline order，viewer 也只辨識上述四種名稱。使用既定 pairs 才能維持 delta direction 與 viewer grouping 正確。

## 讓 comparison 真正成立

Baseline 只有在 compared run 不可能意外載入 candidate skill 時才有效。

對 OpenCode，可用以下 isolation methods：

- candidate config expose/allow candidate skill；baseline config 不提供它，或把它設為 `deny`；
- candidate 使用 new skill directory；migration baseline 在 isolated config 使用 old version snapshot；
- 簡單 one-off test 可讓 baseline agent 的 permission set 隱藏 skill，並確認 available set 中確實沒有該 skill。

如果 skill 仍可取得，只叫 baseline agent「不要使用 skill」不算強 isolation。

除非某變數本身就是測試對象，compared runs 的 model、task prompt、input files 與 unrelated permissions 要保持一致。

## 啟動 independent runs

需要 repeated independent execution 時，candidate 與 baseline runs 應在相近時間啟動，不要先完整做完一邊再做另一邊，以降低 environment/context drift。

每個 run 都給 executor：

- exact task prompt；
- input file paths；
- candidate skill name/path，或明確說明該 skill 已被隱藏；
- output directory；
- 使用者關心的 artifacts；
- 保存 evidence 的要求，不能只留下 summary。

Candidate 與 baseline runs 不得共用 mutable output directories。

## Capture metadata

每個 eval 旁建立 `eval_metadata.json`：

```json
{
  "eval_id": 1,
  "eval_name": "descriptive-name",
  "prompt": "The task prompt",
  "expectations": []
}
```

Execution harness 有提供 timing 或 token metadata 時，立即存入 `timing.json`；之後不得捏造 unavailable metrics。

## 依 evidence grading

Runs 完成後：

1. 對 explicit expectations 使用 `agents/grader.md` 或等價 independent grader。
2. 對 mechanically checkable properties，使用 script/parser，不要只靠目視。
3. 依 `references/schemas.md` exact schema 保存 `grading.json`。
4. 每個 judgment 都要 cite concrete output evidence；missing evidence 不能算 pass。

Viewer 期待 expectation entries 具有 `text`、`passed` 與 `evidence` fields。

## 彙整 repeated runs

只有多個 runs/configuration 的 variance 會影響判斷時，使用：

```bash
python scripts/aggregate_benchmark.py \
  <workspace>/iteration-N \
  --skill-name <skill-name>
```

它會寫入含 mean/stddev 與 candidate-vs-baseline deltas 的 benchmark data。若要手動建立 `benchmark.json`，先讀 `references/schemas.md`；viewer 依賴其中的 field names。

用 `agents/analyzer.md` 找 averages 可能遮住的 patterns：

- with/without skill 同樣容易 pass 的 expectations；
- high-variance 或 flaky cases；
- 單一 case 主導 aggregate；
- quality improvement 是否付出不成比例的 time/tokens；
- unsupported causal explanations。

## Human review

Subjective output 要先把 actual examples 給使用者看，再修改 skill。

Headless/static mode：

```bash
python eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name <skill-name> \
  --benchmark <workspace>/iteration-N/benchmark.json \
  --static <workspace>/iteration-N/review.html
```

沒有 quantitative grading 時省略 `--benchmark`。

Later iterations 可傳 `--previous-workspace <workspace>/iteration-(N-1)`，讓 reviewer 比較 outputs 與 feedback。

修改 skill 前先讀使用者 feedback。Reviewed case 的 feedback 為空，可以視為沒有 requested change；不要只為了繼續 iterate 而捏造問題。

## 避免 overfitting 的 iteration

Case 失敗時：

- 從 failure generalize，不要只針對 exact prompt 加 one-off wording；
- inspect execution path，不只看 final output；
- 多個 runs 各自重做相同 deterministic work 時，考慮抽成 script；
- prune 造成 wasted steps 或與 intended workflow 衝突的 instructions；
- 每次 material change 後重新跑 affected representative cases。

當使用者滿意、representative failures 已解決，或新 iteration 不再帶來 meaningful improvement 時停止。

## Blind comparison

高價值 old-vs-new decision 可使用 `agents/comparator.md`，對 anonymized outputs 做 comparison，不揭露由哪一版本產生。再用 `agents/analyzer.md` 說明 evidence-backed differences。

Blind comparison 是 optional。多數情況 human review 加 direct behavioral checks 已足夠。
