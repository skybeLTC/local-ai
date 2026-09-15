# OpenCode 共用 skills

這個目錄保存可公開、可重用的 OpenCode skills。每個 skill 的 `SKILL.md` 是 runtime entry point，持有最低必要 workflow；只有 `SKILL.md` 以明確 reference trigger 指向的檔案，才在對應 branch 成為 deeper runtime rule。Skill-local `README.md` 保存維護、設計與導覽內容，不應在每次 invocation 預載。

共用 skill permission 由 `../opencode.jsonc` 持有。跨多個 skill 的第三方 provenance 與 notice 集中記錄在這裡，不複製進 runtime `SKILL.md`。

## Matt Pocock integrations

Upstream: `https://github.com/mattpocock/skills.git`

| Local integration | Upstream path | Imported tag | Imported commit | Mode | Local adaptations |
| --- | --- | --- | --- | --- | --- |
| `diagnosing-bugs/` | `skills/engineering/diagnosing-bugs` | `v1.2.3` | `6acc160e4e0cd062dbbbd7a1b26ae92855edf07e` | curated copy | `agents/openai.yaml` omitted；OpenCode permission 設於 `../opencode.jsonc`；`SKILL.md` 與 `scripts/hitl-loop.template.sh` 其餘維持 upstream 內容 |
| `grilling/` | `skills/productivity/grilling` | `v1.2.3` | `6acc160e4e0cd062dbbbd7a1b26ae92855edf07e` | curated copy | `agents/openai.yaml` omitted；OpenCode permission 為 global `deny`、primary `build` `allow`；`SKILL.md` 其餘維持 upstream 內容 |
| `opencode-skill-authoring/` | `skills/productivity/writing-for-agents` | `v1.2.3` | `6acc160e4e0cd062dbbbd7a1b26ae92855edf07e` | principles merged | 既有 Apache-2.0 skill authoring workflow 曾吸收 Matt Pocock 的 writing-for-agents principles；OpenCode mechanics、migration、validation 與 evaluation 仍由本地 authority 持有；upstream skill 不另外安裝 |

上述 Matt Pocock-derived integrations 共用的 MIT notice 位於 `licenses/mattpocock-skills.MIT.txt`。`opencode-skill-authoring/` 另外保留自己的 Apache-2.0 notice 於 `opencode-skill-authoring/LICENSE.txt`；兩份 notice 的 provenance 不可互換。
