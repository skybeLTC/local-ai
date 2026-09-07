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
├── config/
│   └── opencode/
│       ├── README.md
│       ├── AGENTS.md
│       ├── opencode.jsonc
│       ├── prompts/
│       └── skills/                    # present as skills are adopted
├── opencode/                   # independent OpenCode source repository
└── private/                    # independent private configuration repository
```

Root Git 以 `.gitignore` 排除 `/opencode/` 與 `/private/`。這兩個目錄不是 root repository 的 vendored content，也不應被 root commit 吸收。

## Responsibility map

- `config/opencode/`：公開、provider-neutral 的 OpenCode shared configuration。架構與維護入口由 `config/opencode/README.md` 負責。
- `config/opencode/AGENTS.md`：所有 OpenCode primary/subagent 都需要的 global runtime rules。
- `config/opencode/prompts/`：各 agent 的 role-specific runtime contract。
- `config/opencode/skills/`（存在時）：可公開的 OpenCode skills；每個 skill 由自己的 `SKILL.md` 與 supporting documentation 負責。
- `opencode/`：OpenCode source/release maintenance repository。Source fork 的 branch、build、release 與 publication policy 不由這個 root repository 管理。
- `private/`：machine-specific provider/model profile 與其他不公開設定。Public repository 只描述它的 interface，不記錄實際 private mapping。

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
- 修改 private profile：進入 `private/` 後使用該 repository 自己的 README / AGENTS 規則。
