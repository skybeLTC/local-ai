# 英文 Runtime Sources 與台灣繁中 Review Mirrors

建立、修改、rename、刪除或 review runtime English text、review mirror 或 skill README 時使用本 reference。

## Authority 與 mapping

英文 runtime text 是唯一 execution authority。台灣繁中檔案只供 human review，不得獨立新增、刪除、強化或弱化 policy。

本 repository 使用：

```text
config/opencode/skills/<skill-id>/...
config/opencode/skill-reviews/<skill-id>/...
```

Review tree 保留 runtime skill-relative structure，並在 Markdown suffix 前加入 `.zh-TW`：

```text
SKILL.md                      -> SKILL.zh-TW.md
references/foo.md             -> references/foo.zh-TW.md
agents/reviewer.md            -> agents/reviewer.zh-TW.md
```

Skill 的 `README.md` 直接使用台灣繁體中文，不另外建立 English/mirror pair。

## Runtime isolation

- Translation-only files 不得放進 runtime skill directory 或 `assets/`。
- 不得把 `skill-reviews/` 註冊成 skill source。
- Runtime `SKILL.md`、references、prompts、config 與 permissions 不得依賴 review-mirror files。
- Target discovery rules 可能掃到 sibling review tree 時，交付前必須以 target-version evidence 證明 isolation。

## Synchronization

Runtime English text 改變時，同一 change 更新 matching review mirror。保留 actor、action、object、modality、condition、exception、negation、quantity、sequence、stop point、identifiers、paths、commands 與 code。翻譯語意，不翻譯 identifiers。

Files rename、move 或 delete 時，同輪更新 review mapping 與 maintenance navigation。File count 或 heading list 一致只能證明 structural coverage，不能單獨證明 semantic equivalence。

Code、structured-data keys、schemas、binaries 與其他不承載 natural-language instruction policy 的 resources，不因包含英文 token 就建立 translation copy。
