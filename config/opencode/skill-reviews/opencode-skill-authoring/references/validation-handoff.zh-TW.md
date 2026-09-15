# Validation 與 Handoff

Final conclusion、packaging、installation instructions 或 handoff 到另一 environment／AI 前使用本 reference。

## 1. 驗證 final source

檢查 final candidate，不檢查 intermediate draft：

- frontmatter 可解析，且符合 actual target contract；
- skill ID/name、directory、description 與 permission resource 內部一致；
- 所有 runtime-relative references 可解析；
- 每個 execution reference 都能從 observable trigger 到達；
- `SKILL.md` 持有最低 mandatory workflow，README 沒有藏 required runtime policy；
- English runtime sources 與 `skill-reviews/<skill-id>/` mirrors 有完整 structural mapping，runtime 不依賴 mirror tree；
- renamed IDs/paths 不得留在 direct consumers，除非明確作為 history；
- changed scripts 通過對應 syntax checks；
- formal artifact 不包含 unrelated generated files、cache、secrets、Git metadata 或 sandbox-only paths。

Local validator 或 archive integrity check 都不能證明 OpenCode discovery、loading 或 behavior。

## 2. 分開驗證 target runtime state

以下 states 分開回報：

| State | 必要 evidence |
| --- | --- |
| Authored/modified | Exact final source 與 diff。 |
| Static checks passed | Actual frontmatter/path/reference/mirror/contract checks。 |
| Discovered | 指定 target version/profile/scope 的 evidence。 |
| Visible/loadable to agent | Effective permission 與 model-facing/runtime evidence。 |
| Body loaded | Actual skill-load output 或等價 record。 |
| Reference loaded | Required reference 在 dependent action 前已讀的 evidence。 |
| Behavior validated | Representative target-runtime result。 |
| Installed/applied | Authorized target-path/config change 加上 verification。 |
| Committed/pushed/deployed | Actual repository 或 deployment evidence。 |

前一列 evidence 不得升格成後一列 claim。

## 3. Packaging

Archive format 依 receiving workflow。對本使用者 Linux/OpenCode handoff，預設 `.tar.zst`；Web ChatGPT skill release 使用 `.zip`，兩者是不同 artifact type。

Handoff archive：

1. 只包含 intended formal files 與必要 review/evidence files；
2. 拒絕 absolute paths、`..` traversal、accidental symlinks、cache、secrets 與 unrelated Git metadata；
3. 記錄 manifest 與 relevant hashes；
4. 測 archive integrity；
5. 解壓到 fresh location，比對 extracted formal files 與 selected source；
6. 在 extracted copy 重新跑 static checks。

Archive integrity 只證明 packaging，不證明 installation 或 runtime behavior。

## 4. User-action stop points

下一個結果若依賴使用者必須在 target machine 執行的 command，只提供 next necessary step、expected observation 與 decision criterion。Prerequisite evidence 尚未取得前，不提供 dependent modification commands。

Current environment 可以直接取得 evidence 時，應自行取得，不把 investigation 轉交使用者。

## 5. Git publication

Repository commit/push authorization 與 skill authoring 分開。任何 push 前，都要 inspect actual remote、remote branch SHA、local HEAD、intended publication commit、parent topology、ahead/behind、exact publication range、file scope、`git diff --check`、final diff、local-only commit exclusion 與 working tree/index state。

Approval 後若 remote、HEAD、publication SHA/range 或 material working state 改變，舊 approval 失效。使用者尚未明確批准 inspected publication state 前，不提供 push command。
