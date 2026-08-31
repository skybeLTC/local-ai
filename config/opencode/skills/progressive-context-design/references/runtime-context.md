# Runtime Context Guide

OpenCode 的 runtime-loaded instruction 會直接消耗模型 context，因此它和一般 documentation 的成本不同。

常見 runtime context：

```text
AGENTS.md
prompts/*.md
skills/*/SKILL.md
automatically injected project instructions
```

## 應優先保留

- trigger condition
- execution sequence
- hard safety / permission boundary
- invariant
- required tool behavior
- required output format
- stop / failure condition
- 什麼情況需要載入哪個 deeper reference

## 通常移出去

- design history
- provenance
- migration chronology
- maintenance/update procedure
- extended example
- 長篇 compatibility discussion
- 只有修改 subsystem 本身時才需要的 rationale

## Self-contained 不等於 comprehensive

Runtime-loaded file 仍必須足夠 self-contained，讓 agent 能正確執行。

判斷方式：

> 少了這段資訊，agent 在這次 invocation 會不會更容易做錯？

如果會，保留。

如果只影響「理解這個 subsystem 當初怎麼設計或怎麼維護」，通常移到 README/reference。

## OpenCode skill pattern

```text
SKILL.md
├── trigger
├── required behavior
├── minimum workflow
├── stop / failure rules
└── conditional references

README.md
├── design rationale
├── architecture
├── maintenance
└── provenance

references/
└── only-on-demand deeper rules
```

不要只因為資料「跟 skill 有關」就全部塞進 `SKILL.md`。
