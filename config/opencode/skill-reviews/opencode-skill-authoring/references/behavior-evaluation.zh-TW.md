# Skill Behavior 與 Trigger Evaluation

建立 skill、實質修改 behavior 或 description、改變 reference loading，或判斷 candidate 是否比 baseline 改善時使用本 reference。

## 1. 先定義要回答的問題

只選能回答目前 uncertainty 的 evidence：

| 問題 | 最小有用 evidence |
| --- | --- |
| Candidate 結構是否有效？ | Frontmatter、paths、references、mirrors 與 target-contract static checks。 |
| Target OpenCode 是否 discover？ | Target version/profile/scope 的 actual listing 或等價 evidence。 |
| Selected agent 是否能 see/load？ | Effective permission 加上 runtime visibility/loading evidence。 |
| Description 是否有正確 discrimination？ | 不明示 skill 名稱的 positive cases 與 nearby negative cases。 |
| Loaded skill 是否遵守 contract？ | Representative runtime outputs 與必要 execution evidence。 |
| Reference routing 是否有效？ | Trigger state 加上 reference 在 dependent judgment/action 前已讀的 evidence。 |
| New version 是否改善或保留 behavior？ | 同一 target/inputs 下可比較的 old/new runs。 |
| Skill 是否比 baseline 有增益？ | Candidate 真正不可取得的 baseline，而不是只叫 agent 忽略它。 |
| Subjective result 是否可接受？ | 給 human reviewer 看的 concrete outputs。 |

不得只因 tooling 存在就跑 benchmark。

## 2. 建立有辨識力的 cases

每個 affected behavior 記錄：

- input 或 prompt；
- required outcome；
- must/must-not constraints；
- observable evidence；
- pass/fail criterion。

Negative/control case 只有在能辨識 changed rule 時才加入。若 change 修正 known regression，優先使用 old-version FAIL/new-version PASS reproduction。

## 3. 分開 automatic selection 與 explicit loading

測試若直接說 skill 名稱或直接呼叫 skill tool，只能證明 loaded 後的 behavior。要評估 automatic selection，先確認 model-facing visibility，使用不提 skill 名稱的 realistic requests，加入 nearby non-trigger requests，並觀察 target runtime 能提供的 actual selection evidence。

Runtime 無法提供足夠 selection/loading evidence 時，回報 limitation，不得從結果猜測 success。

## 4. 保持 comparison 可解釋

除非某變數本身就是測試對象，否則固定 target version、task input、model/variant、agent/profile、permissions、other instructions 與 repository state。可行時，compared runs 使用獨立 context。

Mandatory correctness 與 authorization constraints 優先於 style score 或 average。兩個 candidate 都違反 contract 時，兩者都回報 fail。

## 5. 只有需要時才使用 bundled evaluation workflow

Repeated runs、explicit expectations、blind comparison、quantitative grading 或 human-review viewer output 時讀 `evaluation-workflow.md`。產生或讀取 structured JSON formats 前讀 `schemas.md`。

Evidence 足以決策時停止。只保存理解結論需要的 version、cases、results 與 remaining gaps；不要把 transient traces 變成 runtime policy。
