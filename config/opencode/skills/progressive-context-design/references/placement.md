# Information Placement Guide

當你不知道一段資訊在 OpenCode-oriented repository 中應該放哪裡時，依序判斷。

## README / AGENTS decision rule

先依 execution-time necessity 與 authority 判斷，不依預期讀者是 human 還是 AI 判斷：

- execution-time invariant、operational policy 或 safety boundary -> `AGENTS.md`
- architecture、rationale、lifecycle、orientation 或 navigation -> `README.md` / focused maintenance guide
- 兩者都需要 -> minimum actionable rule 放在 `AGENTS.md`，deeper explanation 放在 `README.md`；`AGENTS.md` 可以附上精確 pointer

不要只是為了寫「Before modifying this subsystem, read README.md」而建立 `AGENTS.md`。如果實際 mandatory policy 唯一存在 README，這會形成 policy indirection；pointer 可以補充 deeper context，但不能取代 `AGENTS.md` 中執行時所需的最小 actionable rule。

## 1. Agent 執行時是否一定需要？

如果是，把最低限度規則放進對應 runtime-loaded instruction：

- repository/project invariant -> `AGENTS.md`
- primary/subagent role behavior -> 對應 prompt
- skill execution protocol -> `SKILL.md`

只放執行需要的內容。Background、provenance、maintenance history 與大型 example 通常不應一起載入。

## 2. 是否只解釋附近的一個 value / implementation choice？

如果格式支援註解，把 rationale 放在附近。

常見例子：

- JSONC profile 為什麼選某個 provider/model
- 某個 threshold 為什麼只在這台 machine 使用
- provider-specific request option 為什麼存在
- compatibility workaround 為什麼還不能刪

不要要求正在編輯該檔案的 AI 為了 local rationale 回到 root README。

## 3. 是否描述完整 subsystem？

由 subsystem README / focused maintenance guide 擁有，例如：

- shared OpenCode config layering
- DCP architecture / update policy
- Cross-AI reviewer topology
- Command Guard lifecycle
- skill design / provenance

Runtime entry file 只保留操作當下需要的 rule，並指向 deeper owner。

## 4. 是否是 repository-wide orientation / invariant？

放在自然 repository entry：

- root `README.md`：purpose、map、responsibility、navigation
- root `AGENTS.md`：工作時一定不能違反的 repository invariant

不要把 subsystem implementation detail 拉到 root。

## 5. 是否是一個 logical change 的歷史 rationale？

放進 commit message。

若 rationale 同時形成目前仍有效的 rule，active rule 也要存在 current authoritative document。

## 6. 是否只是一次性 investigation / migration evidence？

保留在最適合的 evidence layer，例如：

- commit message
- migration note
- review artifact
- issue / PR history
- temporary, deliberately uncommitted evidence

不要因為 evidence 有價值，就把 active runtime instruction 變成 chronological archive。

## Public/private boundary

Public documentation 可以描述 private interface，但不要複製 private inventory。

Private profile 可以保存 machine-specific provider/model mapping 與 local rationale，但 credential 仍然不進 Git。

## Duplication test

複製完整 explanation 前先問：

> 未來兩份發生 divergence 時，哪一份算 authoritative？

若答案不清楚，就 reference，不要 duplicate。

好的 reference 要說明「為什麼去看」，並使用精確 path；避免只有 `see docs` 這類模糊導航。
