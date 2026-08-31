# Progressive Context Design for OpenCode

這個 skill 把 progressive disclosure 套用到 OpenCode 的實際 context model：有些文件只是 documentation，有些文件同時會直接進入 agent runtime context。

目標不是把資訊拆得越細越好，而是：

> 讓 AI 從自然入口開始，快速知道 scope、authority 與下一步；只有目前任務需要時才載入 deeper detail。

## OpenCode 的主要資訊層

| Layer | 主要責任 |
| --- | --- |
| Repository `README.md` | purpose、repository map、major boundary、下一個 authoritative entry |
| Repository `AGENTS.md` | 該 repository 執行時必須遵守的 invariant / safety boundary |
| Subsystem `README.md` | subsystem architecture、ownership、maintenance、compatibility |
| `opencode.jsonc` / code comment | nearby value 或 implementation choice 的 local rationale |
| `prompts/*.md` | 單一 agent role 執行時需要的 contract |
| `skills/*/SKILL.md` | skill trigger、required behavior、minimum workflow、deeper references |
| Skill `README.md` / `references/` | design rationale、maintenance、extended rules、examples |
| Commit message | 一個 logical change 為什麼進入 history，以及當時驗證了什麼 |
| Migration/evidence artifact | 一次性 observation、comparison、尚未處理的 evidence |

這些是 responsibility defaults，不是強制每個 subsystem 都建立相同檔案數量。

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
