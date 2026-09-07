# Progressive Context Design for OpenCode

這個 skill 把 progressive disclosure 套用到 OpenCode 的實際 context model：有些文件會自動進入 agent runtime context，有些文件則在需要時作為 deeper documentation/context 載入。這不是 human-vs-AI 的讀者二分；README 也應該讓 agent 容易使用。

目標不是把資訊拆得越細越好，而是：

> 讓 AI 從自然入口開始，快速知道 scope、authority 與下一步；只有目前任務需要時才載入 deeper detail。

## OpenCode 的主要資訊層

| Layer | 主要責任 |
| --- | --- |
| Repository `README.md` | documentation/context owner；AI-friendly、human-readable 的 purpose、repository map、major boundary、下一個 authoritative entry |
| Repository `AGENTS.md` | automatically/runtime-loaded execution policy；該 repository 執行時必須遵守的 invariant / safety boundary |
| Subsystem `README.md` | documentation/context owner；AI-friendly、human-readable 的 subsystem architecture、ownership、maintenance、compatibility |
| `opencode.jsonc` / code comment | nearby value 或 implementation choice 的 local rationale |
| `prompts/*.md` | 單一 agent role 執行時需要的 contract |
| `skills/*/SKILL.md` | skill trigger、required behavior、minimum workflow、deeper references |
| Skill `README.md` / `references/` | design rationale、maintenance、extended rules、examples |
| Commit message | 一個 logical change 為什麼進入 history，以及當時驗證了什麼 |
| Migration/evidence artifact | 一次性 observation、comparison、尚未處理的 evidence |

這些是 responsibility defaults，不是強制每個 subsystem 都建立相同檔案數量。

## README 與 AGENTS 不是 human-vs-AI split

`README.md` 不是 human-only documentation，也不是只能給人看的背景資料；它通常應該同時讓 agents 與 humans 容易理解與使用。AI-friendly 和 human-readable 是相容的目標：前者包含 clear headings、exact paths / identifiers、explicit ownership、stable terminology、clear navigation，以及有幫助時的 concrete examples；後者包含 reasonable explanation、rationale、context，而不只是 terse machine directives。

`AGENTS.md` 也不是所有 AI-facing information 的集合。它是 automatically/runtime-loaded execution policy，應保存 agent 在執行時必須知道的 MUST / MUST NOT behavior、operational invariant 與 safety boundary。選擇放在 README 或 AGENTS 時，依 execution-time necessity 與 authority 判斷，不依預期讀者是 human 還是 AI 判斷。

Language/style 與 responsibility 是不同維度：語言與寫作風格依 repository convention 和 intended audience；語言不決定文件的 authority，也不決定它是否在 runtime 載入。這個 generic skill 不預設 README 或 AGENTS 的語言配對。

### Coexistence

同一個 repository 或 subsystem 可以同時有 README 與 AGENTS：

- `AGENTS.md` 放 minimum actionable execution rule，例如不要直接修改 generated files，並遵守指定的 source/update boundary。
- `README.md` 解釋這個 boundary 的 architecture、rationale、ownership 與 maintenance flow。

`AGENTS.md` 可以用精確 pointer 指向 README 的 deeper context；pointer 只能補充說明，不能取代執行時一定要知道、且必須位於 `AGENTS.md` 的 minimum actionable rule。

## Runtime context 與一般 documentation 不同

OpenCode 會在不同時機把 instruction 送進模型 context。`AGENTS.md`、primary/subagent prompt、`SKILL.md` 因此具有直接 token cost，也更容易造成 instruction dilution。

Runtime-loaded file 應優先保存：

- trigger / execution behavior
- hard invariant
- permission / safety boundary
- required output contract
- stop / failure condition
- 需要 deeper context 時的精確 reference

通常不應塞入：

- migration chronology
- provenance
- 長篇 design history
- 大量 example
- update procedure
- 只在維護 subsystem 本身時才需要的 rationale

詳見 `references/runtime-context.md`。

## Locality

如果理由只和附近的 JSONC value 有關，就把理由寫在附近。

例如 public shared config 只需要表達 agent tier intent；實際 machine-specific model mapping 與 provider-specific option 則由 private profile自己說明。

這樣正在修改 profile 的 AI 不需要先回頭讀一份大型 root README，才能理解一個 local decision。

詳見 `references/placement.md`。

## Public / private boundary

Progressive disclosure 只控制「去哪裡放資訊」，不改變 confidentiality policy。

Public layer 可以說：

```text
Machine-specific provider/model mappings are supplied through an
OPENCODE_CONFIG profile.
```

Private profile 才保存實際 mapping 與 local rationale。

Credential 仍然不應進任何 Git repository，即使 repository 是 private。

## Skill 自己也遵守這套規則

```text
SKILL.md
    -> invocation 當下需要的 behavior

README.md
    -> design rationale 與 maintenance

references/
    -> 只有特定問題需要時才載入
```

因此不要把這份 README 全部複製回 `SKILL.md`。

## Git history

Current documentation 回答「現在怎麼運作」。

Commit message 回答「這個 logical change 為什麼進入 history」。

如果某個 rationale 形成持續有效的 active rule，current authoritative document 仍要保存那條 rule；不能要求 future agent 每次挖 Git history 才知道目前 policy。

詳見 `references/commit-messages.md`。

## Maintenance

修改這個 skill 時：

1. 先判斷變更屬於 runtime behavior、design rationale，還是 focused reference。
2. 優先只修改 authoritative owner。
3. 確認 `SKILL.md` 沒因 maintenance detail 膨脹。
4. 檢查 references 的路徑與責任仍然精確。
5. 用 `references/review-checklist.md` 做 final review。
