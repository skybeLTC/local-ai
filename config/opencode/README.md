# OpenCode shared config

這個目錄保存可公開、可跨機器共用的 OpenCode behavior configuration。它刻意不綁定特定 provider、帳號或 model；machine-specific provider/model mapping 由額外的 `OPENCODE_CONFIG` profile 提供。

## Entry points

- `opencode.jsonc`：shared runtime wiring、agent role、permission、step budget 與 provider-portable agent options。
- `AGENTS.md`：所有 primary/subagent 都需要進 context 的 global runtime rules。
- `prompts/`：各 agent 的 role-specific contract；只有該角色執行時才需要對應細節。
- `skills/`（存在時）：可公開的 workflow / knowledge skills；每個 skill 由自己的 `SKILL.md` 決定 runtime behavior，README / references 保存 deeper design 與 maintenance detail。
- `README.md`：只負責這個 subsystem 的跨檔案架構、authority 與 maintenance boundary。

需要理解某個 agent 時，先看 `opencode.jsonc` 的該 agent，再沿著 `prompt` file reference 讀對應 `prompts/*.md`。需要理解某個 skill 時，從該 skill 的 `SKILL.md` 開始，不要預先載入整個 skill directory。

## Config layering

共用設定由 global `opencode.jsonc` 載入。每台機器再透過 `OPENCODE_CONFIG` 載入自己的 private profile overlay。

Private profile 負責：

- provider 定義與 endpoint reference
- `model` / `small_model`
- `agent.*.model`
- 只有特定 provider/model 才應持有的 model-level or execution options
- machine-specific/private skill source registration（`skills.paths`）與其 named skill permission，當 skill 本身不適合放在 public config 時

Public config 不應包含 credential、account identifier、private endpoint 或 machine-specific model inventory。

## Shared versus provider-specific agent policy

Agent tier 的 reasoning intent 屬於 shared role policy，所以 public config 同時保留：

- `reasoningEffort`：OpenAI/Codex-style reasoning control。
- `effort`：Anthropic-style adaptive reasoning control。

兩者是 provider-specific pass-through options，用來表達同一個 low/medium/high tier intent。採用新的 provider/model 時仍必須做 runtime compatibility validation；不能假設所有 provider 都會安全忽略不認識的 option。

以下設定屬於 provider/model-specific behavior，應跟著實際 model assignment 放在 private profile，而不是 public shared role：

- `thinking`
- `sandboxMode`
- `approvalPolicy`
- 其他只對單一 transport/model family 有意義的 request option

## Permission boundary

Top-level permission 採 restrictive baseline，再由 agent 只開啟角色需要的能力。

Git publication 類操作維持 explicit deny，避免 agent 自行 push/upload。

Skill-specific permission 應跟著 skill 本身的 adoption 一起加入；不要預先為尚未存在的 skill 維護 named rule。

## Runtime-managed package state

OpenCode 可能在 config directory 維護 plugin dependency metadata。以下內容屬於 runtime-managed state，不應從舊 snapshot migration，也不由這個 repository 當成人工維護的 source of truth：

```text
node_modules/
package.json
package-lock.json
bun.lock
```

`config/opencode/.gitignore` 本身是 tracked policy file，但也保留 `.gitignore` self-ignore entry，避免 OpenCode 的 config-directory bootstrap 反覆修改它。

## Documentation placement

文件採 progressive disclosure：

1. `~/local-ai/README.md`：repository map 與 public/private/repository boundary。
2. 這份 README：OpenCode shared-config subsystem 的 architecture 與 authority。
3. `opencode.jsonc`：value-local rationale 與 nearby compatibility constraint。
4. `AGENTS.md` / `prompts/*.md` / `skills/*/SKILL.md`：執行時真正需要的 behavior。
5. skill/plugin/subsystem README 與 references：只在維護該 subsystem 或需要 deeper context 時讀取。
6. Git commit message：保存 logical change 的 historical rationale 與當次 validation，不取代 current documentation。
