# cross-ai-review

這是 OpenCode `cross-ai-review` 的人類／維護者入口。Runtime 從英文 `SKILL.md` 開始，再依 observable trigger 載入英文 `references/`；繁中人工檢視版放在 sibling `skill-reviews/cross-ai-review/`，不是 runtime authority。

## 文件地圖

| 路徑 | Runtime | 責任 |
| --- | --- | --- |
| `SKILL.md` | 是 | 自動適用、task continuity、peer attribution、question closure／decision relay、授權／實質判斷、forward progress、peer grilling、OpenCode delegation、reference trigger、最低完成條件 |
| `references/review-lifecycle.md` | 條件式 | stage transition、candidate／validation 狀態、premature candidate、實作 review 與 role swap |
| `references/session-export.md` | 條件式 | materialization 後的 structured export 完整性、截斷、tool result 與附件／artifact coverage |
| `references/file-exchange.md` | 條件式 | compressed input materialization、zstd handoff、多檔 bundle、task-workspace destination、舊 handoff 保留、安全與 direct-access exemption |
| `references/review-checklist.md` | 條件式 | final coverage、狀態與 completion gate |
| `../../skill-reviews/cross-ai-review/` | 否 | 英文 runtime Markdown 的台灣繁中人工檢視版；不是 execution source |
| `README.md` | 否 | 文件地圖、設計理由與維護方式 |

## 設計理由

Shared semantics 與 Web `cross-ai-review` 對齊，但 platform mechanics 不逐字同步。Consensus 解除該 judgment 的 review gate，不指定下一個 actor；有可合法進行的工作時持續前進，避免空確認／handoff。Diagnosis 與 remediation 仍分開 review，但 stage 不等於聊天 round。Implementation/reviewer 是 per-candidate 暫時角色；candidate identity、validation、implementation review 與 technical completion 分開表示。

明確 attributed peer content 不會因位於 user-role message 就取得使用者權限；回答 side question 後也不丟失原任務。既有 peer-question closure 保留，強化的是回覆本身能獨立 relay 必要的 user answers／decisions／constraints，並保留使用者來源歸屬，避免第一人稱措辭混淆說話者。Peer grilling 針對實際假設、證據或重要案例缺口，不是每輪例行盤問。

Compressed input 先 materialize 到隔離 storage，再正常讀取。Current side 的 handoff 使用 zstd；單檔可直接壓縮，多檔預設集中成一個 `.tar.zst`。Output destination 依 task workspace 固定，不隨 nested repo／tool workdir 漂移；舊 handoff 保留且不強制命名方案。Release format 與 handoff transport 是不同責任。

OpenCode-specific runtime 規則保留在本 skill，例如 cross-AI task 中全面禁用 `critic*`／`review*`、其他 factual subagent 的較低成本 tier 重評、direct repo/Git/toolchain evidence 與 absolute output-directory handling。Web `cross-ai-review` 由獨立的 Web skill／ZIP 維護；OpenCode tree 不保存 standalone Web protocol 副本，也不把 Web ZIP 變成 OpenCode runtime dependency。

## 語言與 review mirror

英文 runtime sources 是唯一執行 authority。繁中人工檢視版依目前 `opencode-skill-authoring` contract 放在 sibling：

```text
config/opencode/skill-reviews/cross-ai-review/
```

保留 runtime skill 的相對結構，Markdown 檔名在 `.md` 前加入 `.zh-TW`。不要把 translation-only mirror 放進 runtime `assets/`；所有英文 execution references 都要有對應 mirror。Repo-level mapping 與共用維護規則由 `skill-reviews/README.md` 的現行內容負責，本 README 只保留本 skill 必要導覽。

## 維護

修改 shared behavior 時，同時檢查 Web 版與 OpenCode 版，但只同步 shared semantics；兩端各自維護自己的平台 authority。修改 OpenCode runtime source 後，同輪更新對應 sibling 繁中 review mirror、README 導覽，以及直接上下游 dependencies。

不要從單獨壓出的 skill subtree 推論 sibling `skill-reviews/` 是否存在；repo-level topology 必須由 repo-level evidence 判定。
