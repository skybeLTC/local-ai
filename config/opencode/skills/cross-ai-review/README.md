# Cross-AI Implementation Review（雙 AI 實作交叉審查）

這是 `cross-ai-review` skill 的人類／維護者入口。它說明 package topology、authority、permission 與維護規則；實際執行時只從 `SKILL.md` 開始，再依 task phase 有條件載入 `references/`。

## Package map

```text
skills/cross-ai-review/
├── README.md
├── SKILL.md
├── references/
│   ├── file-exchange.md
│   └── review-checklist.md
└── assets/
    ├── web-prompt.md
    └── skill-review.zh-TW.md
```

| 檔案 | OpenCode 是否載入 | 角色 |
|---|---|---|
| `SKILL.md` | 是，`skill` 工具觸發時載入 | runtime entry、核心 cross-AI protocol authority 與 mandatory handoff trigger |
| `references/file-exchange.md` | handoff gate 命中或真的要交換檔案時 | `.tar.zst` handoff contract、封裝範圍、security、reuse、handoff mechanics |
| `references/review-checklist.md` | final implementation review / delivery / commit/deployment / closeout | final protocol checklist 與 handoff completion gate |
| `assets/web-prompt.md` | 否 | 給沒有安裝 native skill 的 Web AI 直接貼上使用的 portable fallback |
| `assets/skill-review.zh-TW.md` | 否 | `SKILL.md` 的人工繁中 review 副本；不是 runtime authority |

`SKILL.md` 與它明確引用的 `references/` 一起構成 OpenCode side 的 runtime contract。README 不重複維護 protocol detail。

## Handoff contract rationale

正式 implementation review 的 file handoff 不等同於「看過一段 patch」。Pasted diff、commit summary 或 `git show` output 只能呈現內容；當 peer AI 無法直接讀取 exact current files 或 commit 時，不能取代可獨立取得、解包與查核、且包含 exact current formal deliverables 的 `.tar.zst` handoff。這也是為什麼 required-exchange case 不能只靠「檔案已經 commit」的宣告結束。

規則刻意是 conditional，而不是每一個 cross-AI turn 都產生 tar：只有 formal deliverable 被建立或變更、peer AI 必須做 implementation review、且 peer AI 沒有 exact current direct access 時，才需要新的/current archive。Peer AI 能直接 review exact current files 或 commit 時，direct-access exemption 是有效且較低成本的結果；但 final response 仍必須明確寫出 exemption 與原因，不能讓 handoff 狀態消失。

mandatory trigger 放在 runtime-loaded `SKILL.md`，因為 agent 必須在決定結束 round 前就知道何時不能自行略過 handoff。archive format、reuse、security 與封裝細節則留在 `references/file-exchange.md`；`review-checklist.md` 在 closeout 強制檢查 archive 或 exemption。這樣能修正 omission failure mode，又不把完整 archive procedure 複製進每次 invocation 的 runtime context。

## 為什麼 `references/` 與 `assets/` 都存在

兩者責任不同：

- `references/` 是 OpenCode runtime 的 conditional context。只有目前 phase 需要時才載入，降低每次 skill invocation 的 context 成本。
- `assets/` 是給人或另一個環境使用的 companion artifacts，不是 OpenCode runtime reference。

`assets/web-prompt.md` 必須能獨立使用，因此不能要求另一端另外取得 OpenCode 的 `references/`。它可以保留 file-exchange 等必要 protocol detail，即使 OpenCode side 已把相同語意拆成 conditional reference。

`assets/skill-review.zh-TW.md` 只鏡射 `SKILL.md` entry/core sections，方便人工快速 review；`references/*.md` 直接 review 英文 authoritative runtime extension，不再另外維護翻譯 mirror，以免增加 drift source。

## Topology difference

OpenCode side 通常：

- 直接擁有 local repo / Git / toolchain；
- 一般收到 peer AI 的一則 response；
- 可以直接查本機 evidence。

Web / ChatGPT side通常：

- 可能沒有 direct local repo access；
- 可能收到完整 OpenCode session export；
- 可以直接讀 supplied files / archives；
- 如果 formal deliverable 已提供且工具足夠，仍可修改工作副本。

因此兩端要保持 protocol semantics 一致，但不要求逐字相同。

## Permission design

`../../opencode.jsonc` 對 `cross-ai-review` 的 permission：

- top-level `permission.skill.cross-ai-review = "deny"`：預設不開放給其他 agent。
- `agent.build.permission.skill.cross-ai-review = "allow"`：只有 primary `build` 明確允許載入。

這是 workflow scope，不是 incidental wiring。Cross-AI protocol 屬於主要對話層級；subagent 不應自行啟動另一套 peer-review lifecycle。

## Maintenance invariants

核心 protocol 有實質變動時，至少 review：

```text
SKILL.md
references/file-exchange.md
references/review-checklist.md
assets/web-prompt.md
assets/skill-review.zh-TW.md
```

維護時遵守：

- `SKILL.md` 保留每次 invocation 都需要的 core behavior 與 conditional reference trigger。
- `references/` 保存只有特定 phase 才需要的 runtime detail。
- `assets/web-prompt.md` 保持 standalone；不要因 OpenCode 有 references 就把 portable fallback 改成需要外部檔案。
- `assets/skill-review.zh-TW.md` 只跟 `SKILL.md` entry/core sections 同步，不鏡射 references。
- 只改 topology-specific wording 時，不需要機械式修改所有檔案。
- Current-state policy 留在這些 authoritative documents；Git commit message 保存 change rationale 與當次 validation，不取代 current policy。
