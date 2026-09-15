# Target OpenCode Runtime Contract

凡 judgment 會依賴 skill identity、discovery、source precedence、frontmatter、permissions、agent/profile integration 或 runtime loading，都在做決定前讀本 reference。

## 1. 辨識 actual target

只取得會改變目前 decision 的必要 evidence。可取得時，優先順序如下：

1. target checkout 或 installed binary 的實際 source/schema/config behavior；
2. task 指定的 exact fork、branch、tag 或 commit；
3. 與該 target version 相符的 documentation；
4. current upstream documentation，只作為 comparison point，不作為 target runtime 的 proof。

不得只因 repo 內存在 V2 packages，或 current upstream docs 描述 V2，就把 target 判定為 V2。必須確認 actual entrypoint、config、skill tool 與 selected profile 實際使用哪個 implementation。

## 2. 選擇 contract branch

- Target runtime 實際使用本 task 需要的 current V2 skill/config contract 時，使用下方 V2 branch。
- Target runtime 仍使用 legacy V1 skill/config mechanics 時，在做相依決策前讀 `legacy-v1.md`。
- Target 是 mixed／transitional 時，逐一分類本次受影響 mechanisms；不得因某個 subsystem 已 migration，就強迫無關 mechanism 一起歸入 V1 或 V2。
- Evidence 不足，而且差異會改變 skill ID、source registration、permission schema、metadata 或 validation method 時，停止該相依 decision，取得最小缺失 evidence。

## 3. V2 skill contract

對已確認使用 current V2 contract 的 target：

- skill identity 由 path-derived ID 決定；frontmatter `name` 是 display label；
- 即使 runtime parser 允許省略，若 skill 要進 model-facing discovery，仍需要清楚 `description`；
- directory-form skill 應把 supporting files 放在 `SKILL.md` 旁，並使用 skill-relative paths；
- V2 可能支援 `slash` 與 OpenCode metadata controls；只使用 target version 已確認支援的 fields；
- additional skill sources 依 target V2 `skills` configuration；
- V2 skill permissions 使用 target 的 ordered permission rules，resource 採 path-derived skill ID；
- Runtime 顯示 skill body 或 supporting-file sample，不代表 supporting-file contents 已實際載入。

若需要 upstream behavior，使用與 target version 相符的 documentation 重新確認。已確認的 V2 target 不得只為保留 task 不需要的 legacy compatibility 而降級。

## 4. Legacy 或 transitional targets

Current target 使用 legacy mechanics 時，不得把 artifact 改寫成好像 V2 已實際 active。保留 current required behavior，並依 `legacy-v1.md` 處理。未來 V1-to-V2 migration 是另一個 change，須重新驗證。

## 5. 需要分開 evidence 的 states

以下 states 不可互相替代：

1. candidate file exists；
2. target discovers 或 registers skill；
3. selected agent 可以 see/load skill；
4. skill body 實際 loaded；
5. required supporting reference 在 dependent action 前實際 read；
6. agent 符合 intended behavior。

前一個 state 的 evidence 不能證明後一個 state。
