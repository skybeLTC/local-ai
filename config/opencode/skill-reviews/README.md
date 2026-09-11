# OpenCode skill 人工檢視版

這個目錄保存 `../skills/` 中 OpenCode skills 的台灣繁體中文人工檢視版。它與 runtime skill tree 相鄰，但不是 skill source，也不是第二份 runtime 權威。

## 權威與 mapping

英文 runtime source 仍由 `../skills/<skill>/` 持有。需要繁中檢視版的英文 Markdown source，依相同 skill-relative 結構放在這裡，並在 `.md` 前加入 `.zh-TW`：

```text
../skills/<skill>/SKILL.md
<-> <skill>/SKILL.zh-TW.md

../skills/<skill>/references/<path>.md
<-> <skill>/references/<path>.zh-TW.md
```

若 skill 後續加入其他需要翻譯的英文文字 source，也保留其相對路徑；不要為了翻譯把副本放回 runtime skill directory 或 `assets/`。

Skill 的 `README.md` 依本專案慣例直接使用台灣繁體中文，不另外建立 mirror。程式碼、schema、structured data、指令、logs、識別字與沒有自然語言翻譯需求的 binary/resource 不因含英文而建立檢視副本。

## Runtime boundary

- 不要把 `skill-reviews/` 註冊到 OpenCode `skills` source。
- Runtime `SKILL.md`、execution references、agent prompts 與 config 不得把這裡的檔案當成執行來源。
- Review mirror 可以被人工或維護流程讀取，但不能因 mirror 的存在宣稱 OpenCode 已載入其內容。
- 若目標 OpenCode 的 discovery 或 loading 規則改變，重新確認此 sibling tree 仍位於 runtime skill source 之外。

目前目標 OpenCode fork `c73cc038da91dde71cd432d1386532bdd16b808c` 的已確認行為是：config directory 的 V2 skill sources 使用 `<config>/skill` 與 `<config>/skills`；directory-form skill 以 `**/SKILL.md` 發現，skill invocation 的 supporting-file sample 只掃被載入 skill 自己的 directory。因此 sibling `skill-reviews/` 不屬於該 skill 的 discovery 或 supporting-file sample。這項結論只適用於已驗證的目標版本；版本或 source registration 改變時需重查。

## 同步規則

修改英文 runtime source 時，同輪更新對應繁中檢視版。Mirror 必須保留原文的規則強度、行為者、動作、對象、條件、例外、否定、數量限制、停止點、術語與程序順序；不能自行增加或移除 runtime policy。

新增、搬移、重新命名或刪除英文 source 時，同輪更新 mapping。檔案存在、數量一致或 heading 對齊只能證明結構完整性，不能單獨證明翻譯語意一致。
