# OpenCode shared config

這個目錄保存可公開、可跨機器共用的 OpenCode behavior configuration。它刻意不綁定特定 provider、帳號或 model；machine-specific provider/model mapping 由額外的 `OPENCODE_CONFIG` profile 提供。

## Entry points

- `opencode.jsonc`：shared runtime wiring、agent role、permission、step budget 與 provider-portable agent options。
- `AGENTS.md`：所有 primary/subagent 都需要進 context 的 global runtime rules。
- `prompts/`：各 agent 的 role-specific contract；只有該角色執行時才需要對應細節。
- `skills/`（存在時）：可公開的 workflow / knowledge skills；每個 skill 由自己的 `SKILL.md` 決定 runtime behavior，README / references 保存 deeper design 與 maintenance detail。
- `skill-reviews/`（存在時）：`skills/` 中英文文字來源的台灣繁中人工檢視版；不是 OpenCode skill source，也不持有第二份 runtime authority。詳細 mapping 與同步規則由 `skill-reviews/README.md` 持有。
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

OpenCode config validation 使用 sibling `~/local-ai/opencode` checkout 產生的 version-matched schema；schema generation 與 maintenance contract 由 `~/local-ai/opencode/SKY_README.md` 維護。

## Shared role 與 reasoning tier

Agent role 與 reasoning tier 是兩個獨立維度。`generalL/general/generalH` 等同一 role 的三個 agent ID 共用同一份 role prompt 與 role capability；`L`、default、`H` 只表示該次委派工作需要的 reasoning capacity，不代表 workflow risk、domain 或另一套角色行為。

Public config 保留 provider-portable tier intent：

- `reasoningEffort`：OpenAI/Codex-style reasoning control。
- `effort`：Anthropic-style adaptive reasoning control。
- `steps`：目前沿用既有 provisional budget；尚未宣稱最佳化，只有實際 step exhaustion 或明顯浪費等證據出現時再獨立調整。

`reasoningEffort` 與 `effort` 是 provider-specific pass-through options，用來表達同一個 low/medium/high tier intent。採用新的 provider/model 時仍必須做 runtime compatibility validation；不能假設所有 provider 都會安全忽略不認識的 option。

以下設定屬於 provider/model-specific behavior，應跟著實際 model assignment 放在 private profile，而不是 public shared role：

- `thinking`
- `sandboxMode`
- `approvalPolicy`
- 其他只對單一 transport/model family 有意義的 request option

Workflow intensity 由 `prompts/build.md` 控制流程保障強度，與 reasoning tier 分開判斷。高風險任務不自動等於 H-tier；H-tier 也不隱含特定 BSP/kernel/Yocto 等 domain knowledge。

## Permission boundary

Top-level permission 採 restrictive baseline，再由 agent 開啟角色需要的能力。同一 role 的 reasoning tiers 原則上維持相同 capability；目前 `generalL/general/generalH` 都可使用 edit、web 與 `diagnosing-bugs`，tier 不再用來移除 role capability。

Local read-only inspection 原則上不因 agent tier 額外阻擋；機密性、隱私或其他明確資料邊界仍優先。External web 即使是 read-only，也屬於 egress boundary，因此只在需要 external/upstream access 的 role 開啟：build、general 與 scout。

`bash` 維持 restrictive `ask` baseline；不要用 command-name allowlist 假裝能可靠判定 read-only，因 shell redirection、pipeline 或其他 composition 仍可造成寫入。Git publication 類操作維持 explicit deny，避免 agent 自行 push/upload。

Skill-specific permission 應跟著 skill 本身的 adoption 一起加入；不要預先為尚未存在的 skill 維護 named rule。

## 英文 runtime source 與台灣繁中檢視版

`AGENTS.md` 與 `prompts/*.md` 的英文檔是 OpenCode runtime authority。對本專案自行建立或修改的全英文文字 runtime artifact，使用同層、同 basename 的 `.zh-TW.md` 作同步台灣繁中 mirror，例如：

```text
AGENTS.md <-> AGENTS.zh-TW.md
prompts/build.md <-> prompts/build.zh-TW.md
```

OpenCode skill 的繁中檢視版不放進 `skills/<skill>/` runtime tree。英文來源仍位於 `skills/<skill>/...`，對應繁中檢視版放在 sibling `skill-reviews/<skill>/...`，並保留 skill-relative 結構與 `.zh-TW.md` suffix；完整 mapping 與同步規則見 `skill-reviews/README.md`。

所有繁中檢視版都只供人工 review 與維護，不建立第二份 runtime authority。Runtime config、`SKILL.md` 與 execution references 不得把繁中檢視版當作執行來源。修改英文 authority 時同步更新 mirror；只修改翻譯措辭時不得改變英文 runtime contract。`opencode.jsonc`、程式碼、指令與 logs 等非文字執行產物不因包含英文而建立翻譯副本。

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
6. `skill-reviews/`：只保存 OpenCode skill 的繁中人工檢視副本，不加入 runtime loading/navigation path。
7. Git commit message：保存 logical change 的 historical rationale 與當次 validation，不取代 current documentation。
