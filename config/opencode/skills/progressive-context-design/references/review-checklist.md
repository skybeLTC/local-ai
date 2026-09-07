# Progressive Context Review Checklist

在 finalize substantial OpenCode documentation、instruction、skill、config-comment 或 commit-message change 前使用。

## Discoverability

- 自然入口能否發現這項資訊？
- 每個 deeper file 是否真的增加 orientation / authority？
- reference 是否使用精確 path，而不是 vague pointer？
- 是否存在 forwarding-only layer？

## Authority

- 每條 active rule 是否只有一個清楚 authoritative owner？
- 是否避免維護兩份完整、會獨立 drift 的 policy？
- README/AGENTS placement 是否依 runtime necessity 與 authority，而不是 human-vs-AI audience？
- README 在適當情況下是否同時 usable by agents and humans？
- mandatory execution rule 是否沒有只藏在 README，再靠 AGENTS 的「read this first」indirection？
- README/AGENTS overlap 時，是否一方擁有 rule，另一方只有 scoped summary/pointer 或 rationale？
- current state 是否和 historical rationale 分開？

## Runtime context cost

- `AGENTS.md`、prompt、`SKILL.md` 是否只保留 invocation 需要的 behavior？
- maintenance history / provenance / extended example 能否移到 supporting docs？
- runtime file 是否仍足夠 self-contained？

## Locality

- local JSONC/code rationale 是否能放在 value 附近？
- 正在編輯單一檔案的 AI 是否能理解重要 local constraint，而不必無意義 backtrack？

## Repository architecture

- root README 是否是 map，而不是 subsystem dump？
- root/project `AGENTS.md` 是否只保存 repository execution invariant？
- nested repositories / public-private boundaries 是否清楚？
- subsystem README 是否真的擁有它描述的 architecture / maintenance policy？

## Precision and evidence

- path、key、command、branch、identifier、expected outcome 是否精確？
- current value、example、verified fact、assumption 是否有區分？
- validation claim 是否只包含真的執行過的 check？
- intentional deferral / uncertainty 是否在會影響理解的位置可見？

## Security

- public documentation 是否避免 private provider/model inventory？
- private Git 是否仍排除 credential？
- progressive disclosure 是否沒有被誤用成「只要藏深一點就可以公開」？

## Commit message

- subject 是否描述 semantic result？
- opening paragraph 是否快速說清楚目的？
- body 是否保留 non-obvious rationale，而不是重述 filename diff？
- validation 是否精確？
- deferred work 是否只在真的影響 interpretation 時記錄？
- commit 是否是一個 coherent logical unit？

## Final test

Future AI 應能在不預先載入全部文件的情況下回答：

```text
What is this?
What is authoritative?
Why is it this way?
Where should I read next?
What was verified?
What is private, uncertain, or deferred?
```
