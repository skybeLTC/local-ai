# progressive-context-design

這個 OpenCode skill 設計 durable textual / instructional artifacts 的資訊權責、載入、導覽與歷史結構，讓 AI 或人類先取得足以判斷下一步的最小 context，再依明確條件深入。適用對象不限於 README 或 prompt，也包含 skills、runtime instructions、guides、runbooks、design docs、source comments、repo navigation、handoffs、history 等會被後續工作依賴的持久資訊。

英文 `SKILL.md` 與英文 `references/*.md` 是 OpenCode runtime 權威。同步繁中檢視版位於 `../../skill-reviews/progressive-context-design/`，不放在 runtime skill directory，也不是第二份 runtime 權威；runtime references 只指向英文來源。

## 文件地圖

| 文件 | 內容責任 |
| --- | --- |
| [SKILL.md](SKILL.md) | 適用範圍、核心契約、natural owner、progressive loading、guaranteed reachability、hierarchy rebalance、變更影響與全部 reference trigger |
| [scope-boundaries.md](references/scope-boundaries.md) | 資訊架構與工程、skill authoring、commit-message authoring 等方法的責任界線 |
| [placement.md](references/placement.md) | local-owner-first、parent/child responsibility、上提／下沉／拆分／移除中介層與權威歸屬 |
| [change-impact.md](references/change-impact.md) | upstream/downstream propagation、sibling signal、hierarchy rebalance、edit/decision boundary 與停止條件 |
| [runtime-context.md](references/runtime-context.md) | OpenCode runtime entry、guaranteed reachability、reference trigger、multi-reference loading 與防斷鏈方法 |
| [documentation.md](references/documentation.md) | README、guide、runbook、design doc、ADR、migration/handoff、changelog/release note 等 durable documentation 的資訊組織 |
| [repository-navigation.md](references/repository-navigation.md) | repo/subsystem entry、source-of-truth discovery、nested repo 與 navigation layer |
| [information-boundaries.md](references/information-boundaries.md) | 既有 public、private、confidential 或其他資訊範圍下的引用、摘要、同步與搬移 |
| [history.md](references/history.md) | 跨 history 類型共通的 current/history 分工、狀態與 lifecycle |
| [commit-history.md](references/commit-history.md) | Git-specific `subject → full message → diff/source` progressive path |
| [review-checklist.md](references/review-checklist.md) | 穩定的 information-architecture review dimensions inventory |
| `../../skill-reviews/progressive-context-design/` | 英文 runtime source 的同步繁中人工檢視版；不屬於 runtime skill tree |
| README.md | 用途、設計理由、文件地圖與維護方式 |

## 核心設計

目標不是「文件越多越 AI-friendly」，而是讓資訊在需要時可靠可達，而且在不需要時不佔 context。入口持有最低必要契約；條件式方法由 reference trigger 控制；README 保存深入理由與維護資訊；local invariant 留在最接近作用對象的 natural owner；history 保存演進背景，但不取代現行權威。

Review 的起點可以很廣，但 loading 與修改範圍必須漸進。即使是一行 source comment 也可以落入 durable text review；若它已是正確 natural owner，而且沒有上層 runtime、navigation 或 maintenance dependency，review 就應在該處停止，不為形式完整再製造 README 或索引。

## Hierarchy 不是 append-only

資訊結構會隨責任演進。若 parent 逐漸累積大量 child-specific 規則，應重新判斷哪些是真正 shared、哪些應下沉到 child、哪些應上提到更廣 scope，以及中介 instruction layer 是否仍有獨立存在理由。Filesystem nesting 只是一項 evidence，不自動等於權威階層。

## Progressive loading 與 reference reachability

Reference 拆分只有在功能仍可達時才成立。每個 execution reference 都必須由 `SKILL.md` 提供 observable trigger、exact path、read-before point 與 missing-reference behavior。多個 trigger 同時成立時，讀取所有必要 references；progressive loading 的核心是不載入無關內容，而不是一次只能讀一份。

如果把方法拆進 reference 後，入口已無法可靠判斷何時需要它，即使檔案仍存在，也視為功能退化。

## OpenCode runtime adaptation

`AGENTS.md`、`SKILL.md` 或其他 instruction file 只有在目標 OpenCode 的實際 loading mechanism 賦予它 runtime role 時，才是 guaranteed entry。不要只因檔名或目錄位置推定 OpenCode 一定載入。

本 skill 只持有 platform-neutral information-architecture methodology 加上 OpenCode 所需的 loading terminology；OpenCode skill packaging、V2 metadata、permission、discovery 與 validation methodology 仍由 `opencode-skill-authoring` 類方法負責。

## History 的分層

`history.md` 處理各類 durable history 共通的 current/history、status 與 lifecycle；`commit-history.md` 只處理 Git-specific progressive path。實際 commit-message authoring、格式與措辭仍由專門的 `commit-message` 方法負責。

## 維護與譯文

修改英文 runtime source 時，同輪更新 `../../skill-reviews/progressive-context-design/` 下對應的 `.zh-TW.md`。繁中檢視版必須保持規則強度、條件、例外、術語與程序順序一致，但 runtime entry、execution references 與 skill source 不得指向或包含該 review tree。

新增或拆分 reference 前，先確認它具有獨立、可觀察 trigger，而且 `SKILL.md` 仍能在正確時點觸發它。修改後依 `change-impact.md` 重新走 upstream/downstream dependencies 到有證據支持的影響邊界。
