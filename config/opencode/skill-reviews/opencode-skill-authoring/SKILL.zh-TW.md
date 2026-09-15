---
name: opencode-skill-authoring
description: "建立、review、migration、validate 與改進 OpenCode 會 discover 或 execute 的 skills。用於 SKILL.md 變更、skill resources、discovery 或 permission wiring、cross-platform skill migration、behavior evaluation 與 skill delivery；不要只因執行既有 skill 或不相關的 OpenCode 設定而使用。"
---

# OpenCode Skill 編寫

建立並維護 OpenCode skills，將它們視為小型、可測試的指令系統。保留仍有價值的行為，依實際 target runtime 適配平台機制，並讓每項行為只有一個明確的 runtime 權威。

## 固定術語

- **target OpenCode**：本次 artifact 實際要被發現、驗證或執行的精確 OpenCode 版本或 fork、profile、skill source 與 scope。
- **runtime source**：OpenCode 或其 agent 可能作為指令讀取的英文檔案，包括 `SKILL.md`、執行 references 與 evaluation agent prompts。
- **review mirror**：位於 sibling `skill-reviews/<skill-id>/` tree 的同步台灣繁體中文副本；它絕不是第二份 runtime 權威。
- **reference trigger**：可從 task、artifact 或 state 觀察到的條件；成立後，對應 reference 在相依 judgment 或 action 前成為必讀。
- **target validation**：從 target OpenCode runtime 取得的證據，而不是從 copied files 或不同版本推論的結果。

## 核心流程

1. **找回 intent 與 authorization。** 先讀 conversation 與 exact current files，沿用已決定的 requirement。分清 review、candidate edit、formal source edit、installation、commit、push 與 deployment 授權。
2. **辨識 target runtime。** 當結果會受影響時，確認 target OpenCode 版本或 fork、actual skill source、profile 或 agent、effective permissions 與 loading path。不要假設 authoring environment 與 target runtime 是同一環境。
3. **定義可觀察的成功條件。** 找出代表性 requests、required behavior、important constraints，以及能證明成功的 evidence。
4. **先 inspect 再 edit。** 修改既有 skill 時，讀取其 `SKILL.md`、已觸發 references、相關 scripts、permission wiring 與直接相依 navigation。分開 live behavior、stale machinery 與 source-platform-specific machinery。
5. **分類變更。** Migration 或吸收另一份 guidance 時，分清 shared behavior intent、source-platform mechanics 與 target-OpenCode mechanics。保留 intent，以 target runtime 的實際機制重新實作。
6. **選擇最小且完整的 runtime surface。** 每次都需要的規則留在 `SKILL.md`；conditional detail 放在有明確 reference trigger 的 deeper files；只有 deterministic script 明顯提升可靠性時才使用。
7. **有意識地選 skill ID。** Evidence 顯示新 ID 更能代表 responsibility、避免 collision 或修正 authority drift 時，可以 rename。不得只為形式一致而 rename，也不得把「永遠保留舊名」當預設規則。ID 改變時，同一 coherent change 更新所有 direct consumers。
8. **維持單一 runtime authority。** 不得留下彼此競爭的 current authoring skills、重複 mandatory rules，或可能被 runtime 載入的 review mirror。
9. **驗證 mechanics 與 behavior。** 先做 structure checks，再依 target runtime 與實際 impact 驗證 discovery、permission、loading、reference use 與 changed behavior。
10. **依 evidence 交付。** 分開回報已 review、已修改、static check、behavior test、target runtime loading、installed、committed、pushed 與 deployed。

## 編寫規則

- 精確比較前確認 exact source version。Summary、舊 export 或同名 skill 不能取代本次指定來源。
- Skill 不能授予 permission。必要 action 被 deny 時，不得改用其他 tool、wrapper、agent 或等價 command 繞過限制。
- 當 target runtime 以 description advertise skill 時，`description` 是 model-facing discovery pointer。內容須能涵蓋 intended requests 並排除 nearby tasks。
- 不得把 file existence、discovery、permission、body loading、reference loading 與 correct behavior 視為同一 state；每項 claim 都要有對應 evidence。
- Supporting files 是 conditional detail，不是 preload 整個 skill directory 的理由。每個 execution reference 都必須有 observable trigger、exact path、read-before point 與 missing-reference behavior。
- OpenCode runtime mechanics 由本 skill 持有。若 `progressive-context-design` 可用，較廣泛的 durable information architecture 交由它處理；但本 skill 不得因 sibling skill 缺失而變得不可用。
- Behavioral evaluation 的強度依 uncertainty 決定，不得因已有 benchmark tooling 就習慣性跑 benchmark。
- 外部 material 仍被實質納入時，保留適用的 license 與 provenance。

## Validation

每個 changed skill：

1. 解析 final frontmatter，並依 actual target runtime contract 檢查。
2. 檢查 changed path 會使用的每個 runtime-relative reference 與 supporting file。
3. 對 changed scripts 執行對應 syntax checks。
4. `scripts/quick_validate.py` 只作為與 target contract 相符的 structural helper；它不是 OpenCode runtime parser。
5. 若 discovery、skill ID、source registration 或 permission 有變更，而且 target runtime 可取得，使用 actual target OpenCode binary/config 驗證。
6. 用代表案例測 changed behavior。只有 old/new 或 with/without comparison 能回答實際 uncertainty 時才做比較。
7. 檢查 final diff 是否有 unrelated changes、stale IDs／paths、duplicate authority 與 obsolete platform assumptions。

## Evaluation tooling

若需要非簡單比較、repeated runs、quantitative grading 或 human review，執行前先讀 `references/evaluation-workflow.md`。需要 bundled workspace／JSON formats 時，依 `references/schemas.md`。

Bundled helpers 仍是 optional：

- `agents/grader.md`：依 evidence 評估 explicit expectations。
- `agents/comparator.md`：執行 blind output comparison。
- `agents/analyzer.md`：分析 comparison results，不捏造原因。
- `scripts/aggregate_benchmark.py`：當 variance 影響判斷時彙整 repeated runs。
- `eval-viewer/generate_review.py`：需要人工檢查 concrete examples 時準備 human-review output。

不得只因完整 evaluation stack 已存在就全部執行。

## Reference triggers

在相依 judgment 或 action 前，先讀所有已觸發 reference。版本與條件未改變時，可以沿用仍在 context 的已讀內容。

| Trigger | 必讀 reference 與 read-before point |
| --- | --- |
| 建立或修改 metadata、skill ID/name、discovery、skill sources、permission wiring、agent/profile integration，或任何依 OpenCode version 才能判斷的 behavior | 選擇 runtime contract 或 integration 前讀 `references/target-runtime.md`。 |
| Evidence 顯示 target 仍使用 legacy V1 skill/config mechanics，或 task 明確處理 V1／V1-to-V2 migration | 做任何 V1-specific 或 compatibility decision 前讀 `references/legacy-v1.md`。 |
| 建立、修改、rename、刪除或 review English runtime text、台灣繁中 review mirror 或 skill README | 決定 source/mirror placement 或 synchronization 前讀 `references/bilingual-output.md`。 |
| 從另一平台或 skill migration、吸收 guidance、rename skill、改變 responsibility/authority，或修改已有 dependent consumers 的 existing skill | 決定 keep/merge/replace/remove 或 impact boundary 前讀 `references/migration-review.md`。 |
| 建立新 skill、實質修改 behavior 或 description、改變 reference loading，或判斷 candidate 是否優於 baseline | 設計或解讀 evaluation 前讀 `references/behavior-evaluation.md`。 |
| 執行非簡單 comparison、repeated benchmark、bundled grader/comparator/analyzer workflow 或 human-review viewer | 執行前讀 `references/evaluation-workflow.md`；產生或讀取 structured formats 前讀 `references/schemas.md`。 |
| 完成 review、打包 candidate、handoff 到另一 environment／AI，或回報 discovery/loading/behavior status | final conclusion 或 handoff 前讀 `references/validation-handoff.md`。 |

Required reference 缺失或不可讀時，只停止依賴該 reference 的 judgment/action，回報缺口，獨立工作可以繼續。

## 完成條件

Skill change 只在 evidence 支持的範圍內算完成。Coherent candidate 可以在尚未 install 或 runtime-validate 時，作為「已編寫 artifact」完成；不得把 static check 說成 runtime claim，也不得把 runtime load 說成 behavior claim。
