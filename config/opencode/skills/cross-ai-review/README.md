# cross-ai-review

這是 OpenCode `cross-ai-review` 的人類／維護者入口。Runtime 從英文 `SKILL.md` 開始，再依 observable trigger 載入英文 `references/`；繁中人工檢視版放在 sibling `skill-reviews/cross-ai-review/`，不是 runtime authority。

## 文件地圖

| 路徑 | Runtime | 責任 |
| --- | --- | --- |
| `SKILL.md` | 是 | 自動適用、證據與 session continuity、peer-question closure、授權／實質判斷、stage-closing forward progress、reference trigger、最低完成條件 |
| `references/review-lifecycle.md` | 條件式 | stage transition、candidate／validation 狀態、premature candidate、實作 review 與 role swap |
| `references/session-export.md` | 條件式 | compressed/structured export 完整性、截斷、tool result 與附件／artifact coverage |
| `references/file-exchange.md` | 條件式 | `.tar.zst` handoff、封裝、安全與 direct-access exemption |
| `references/review-checklist.md` | 條件式 | final coverage、狀態與 completion gate |
| `../../skill-reviews/cross-ai-review/` | 否 | 英文 runtime Markdown 的台灣繁中人工檢視版；不是 execution source |
| `README.md` | 否 | 文件地圖、設計理由與維護方式 |

## 設計理由

Shared semantics 與 Web `cross-ai-review` 對齊，但 platform mechanics 不逐字同步。核心 invariant 是：某一端的獨立 review 關閉目前 stage 後，若沒有實際 gate，該端直接承接下一個合法 stage。Implementation/reviewer 是 per-candidate 暫時角色；candidate identity、validation、implementation review 與 technical completion 分開表示。

OpenCode-specific runtime 規則保留在本 skill，例如 subagent independent-review restriction、OpenCode direct repo/Git/toolchain evidence 與 `.tar.zst` handoff mechanics。Web `cross-ai-review` 由獨立的 Web skill／ZIP 維護；OpenCode tree 不保存 standalone Web protocol 副本，也不把 Web ZIP 變成 OpenCode runtime dependency。

## 語言與 review mirror

英文 runtime sources 是唯一執行 authority。繁中人工檢視版依目前 `opencode-skill-authoring` contract 放在 sibling：

```text
config/opencode/skill-reviews/cross-ai-review/
```

保留 runtime skill 的相對結構，Markdown 檔名在 `.md` 前加入 `.zh-TW`。不要把 translation-only mirror 放進 runtime `assets/`；所有英文 execution references 都要有對應 mirror。Repo-level mapping 與共用維護規則由 `skill-reviews/README.md` 的現行內容負責，本 README 只保留本 skill 必要導覽。

## 維護

修改 shared behavior 時，同時檢查 Web 版與 OpenCode 版，但只同步 shared semantics；兩端各自維護自己的平台 authority。修改 OpenCode runtime source 後，同輪更新對應 sibling 繁中 review mirror、README 導覽，以及直接上下游 dependencies。

不要從單獨壓出的 skill subtree 推論 sibling `skill-reviews/` 是否存在；repo-level topology 必須由 repo-level evidence 判定。
