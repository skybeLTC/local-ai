# local-ai

這個 repository 是本機 AI / OpenCode 環境的公開管理層。它保存可跨機器共用、可公開的設定與文件；OpenCode source fork 與 machine-specific private config 各自使用獨立 Git repository。

## Documentation convention

這個 repository 的 `README.md` 與 `AGENTS.md` 都是 AI-facing context，但責任不同，不以「human vs AI」區分。

- `README.md` 是 AI-friendly、human-readable 的 documentation/context owner。由這個 repository 追蹤的 README prose 預設使用臺灣繁體中文；technical identifiers、paths、commands、code 與必要 technical terms 保留原樣。
- `AGENTS.md` 是 agent execution policy。由這個 repository 追蹤的 AGENTS 預設使用英文，只保存執行時需要的 invariant、safety boundary、MUST / MUST NOT behavior 與精確 navigation。
- 同一個 scope 可以同時有 README 與 AGENTS。Mandatory execution rule 的 minimum actionable form 必須存在 `AGENTS.md`；README 負責 deeper rationale、architecture、lifecycle 與 maintenance context。
- 語言是這個 repository 的 writing convention，不決定 authority，也不改變 runtime-loading semantics。獨立 Git repository 仍遵循各自的 documentation / agent policy。

## Repository map

```text
~/local-ai/
├── README.md
├── AGENTS.md
├── bin/
│   └── opencodeTools
├── tools/
│   └── opencode/
│       ├── opencode-sessions
│       └── opencode-export-session
├── config/
│   └── opencode/
│       ├── README.md
│       ├── AGENTS.md
│       ├── opencode.jsonc
│       ├── tui.jsonc
│       ├── prompts/
│       └── skills/                    # present as skills are adopted
├── opencode-satellites/
│   └── README.md               # satellite layout invariant; child dirs are independent repositories
├── opencode/                   # independent OpenCode source repository
└── private/                    # independent private configuration repository
```

Root Git 以 `.gitignore` 排除 `/opencode/`、`/private/` 與 `/opencode-satellites/` 下除 `README.md` 以外的所有內容。這些目錄不是 root repository 的 vendored content，也不應被 root commit 吸收。

## Responsibility map

- `config/opencode/`：公開、provider-neutral 的 OpenCode shared configuration。架構與維護入口由 `config/opencode/README.md` 負責。
- `config/opencode/AGENTS.md`：所有 OpenCode primary/subagent 都需要的 global runtime rules。
- `config/opencode/prompts/`：各 agent 的 role-specific runtime contract。
- `config/opencode/skills/`（存在時）：可公開的 OpenCode skills；每個 skill 由自己的 `SKILL.md` 與 supporting documentation 負責。
- `opencode-satellites/`：OpenCode 周邊工具的 source checkout 集合。Root repository 只擁有 `opencode-satellites/README.md` 描述的 layout invariant 與 ignore rule；每個子目錄都是獨立 Git repository，其 branch、build、release 與 publication policy 由該 repository 自己負責。
- `opencode/`：OpenCode source/release maintenance repository。Source fork 的 branch、build、release 與 publication policy 不由這個 root repository 管理。
- `private/`：machine-specific provider/model profile 與其他不公開設定。Public repository 只描述它的 interface，不記錄實際 private mapping。

## Public OpenCode helpers

`bin/opencodeTools` 是公開的 CLI 入口；`tools/opencode/opencode-sessions` 處理通用 session 列表，`tools/opencode/opencode-export-session` 處理 session 匯出、metadata 過濾與壓縮。`--sessions`、`--export-session` 與 `--help` 不依賴 private repository。

如果同層另有 `private/bin/opencodeTools-private`，且目前的 `OPENCODE_CONFIG` 指向該 private checkout 的 work profile，dispatcher 才載入 private 擴充指令。擴充程式本身負責辨識環境；public 不保存 work 專屬指令清單或內部設定。

執行 `opencodeTools --export-session SESSION_ID`，會在目前目錄建立或覆蓋 `SESSION_ID.json` 與 `SESSION_ID.json.zst`。預設保留 OpenCode JSON 的物件層級、欄位名稱、欄位順序及 message 順序；刪除指定的模型／時間／執行統計、與頂層重複的 `sessionID`、工具 `callID`，以及文字恰為空字串的 reasoning part。其他 parts 的相對順序不變。保留 session／message／part 的 `id`、`parentID`、`messageID` 與 session directory。只有值的類型與內容完全相同時才刪除重複的工具 `title`、`metadata.output`、`metadata.todos`、`metadata.name`；移除 `tool.state.metadata.model`，其餘工具狀態、輸入輸出及附件保留。對已知 message part 的 metadata，只移除模型內部識別與加密資料，保留 `phase`、`compaction_continue`、`anthropic.caller` 與未知資料；工具附件內容及其 metadata 不做遞迴過濾。

使用 `--no-filter` 完全不進行過濾，逐位元組保留 OpenCode 原始 JSON，適合備份或 `opencode import`；預設過濾後的 JSON 不保證能匯入。兩種模式都以 `zstd -19 -T0 -v --rsyncable` 壓縮，並覆蓋同名檔案；產物權限為 `0600`。先在私有暫存目錄完成 JSON 與壓縮驗證，再逐一替換輸出檔；兩檔不是原子交易。預設 JSON 經重新序列化，保留 key／array 順序，但不保證原始空白及縮排。

檔案 URL 可能內含完整 base64 圖片或本機路徑；對話、工具輸出亦可能含有機密資訊。過濾 metadata 不等於去識別化，不可未檢查就加入 Git 或對外分享。依賴 `opencode`、`python3`、`zstd`。

Local runtime entry：`~/.local/bin/opencodeTools -> ~/local-ai/bin/opencodeTools`。切換此 symbolic link 須等兩個 repository 完成整合與驗證後再執行。

## Runtime layout

OpenCode global config directory：

```text
~/.config/opencode -> ~/local-ai/config/opencode
```

`config/opencode/opencode.jsonc` 保存 shared behavior。Machine-specific provider/model selection 透過額外的 `OPENCODE_CONFIG` profile overlay 提供；詳細責任邊界見 `config/opencode/README.md`。

## Security boundary

Credential 不屬於任何 Git repository，包括 private repository。

例如：

- `auth.json`
- OAuth access/refresh token
- API key
- SSH private key
- session/cache/database 中的 credential material

Private repository 是 visibility boundary，不是 credential store。

## Where to read next

- 修改 shared OpenCode config：先讀 `config/opencode/README.md`。
- 修改 agent runtime behavior：再讀對應的 `config/opencode/AGENTS.md` 或 `config/opencode/prompts/*.md`。
- 修改某個 skill：從該 skill 的 `SKILL.md` 開始，只在需要時沿著其 references 深入。
- 修改 OpenCode source fork：進入 `opencode/` 後使用該 repository 自己的 maintenance documentation。
- 新增或修改 satellite checkout：先讀 `opencode-satellites/README.md`，再進入該 satellite repository 使用它自己的 maintenance documentation。
- 修改 private profile：進入 `private/` 後使用該 repository 自己的 README / AGENTS 規則。
