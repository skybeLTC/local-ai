---
name: progressive-context-design
description: Use when creating, editing, reviewing, or reorganizing OpenCode-facing documentation or instruction context, including README/AGENTS files, prompts, skills, JSONC comments, maintenance guides, runbooks, and Git commit messages. Optimize for progressive disclosure, clear authority, low runtime context cost, local rationale, and exact navigation.
---

# Progressive Context Design

Design OpenCode-facing knowledge so an agent can start from the smallest useful entry point and load deeper context only when the current task needs it.

## Required behavior

When changing documentation-like information:

1. Identify who needs the information and whether it is loaded automatically at runtime.
2. Put the information at the lowest authoritative layer that naturally owns it.
3. Keep repository/subsystem entry documents focused on scope, boundaries, invariants, authority, and navigation.
4. Put value-local rationale beside JSONC/code when the format supports comments.
5. Keep `AGENTS.md`, role prompts, and `SKILL.md` limited to behavior needed while acting.
6. Prefer one authoritative explanation plus a precise reference over duplicated policy.
7. Separate current supported state from Git-history rationale.
8. Preserve meaningful validation, compatibility constraints, intentional deferrals, and unresolved items without turning active runtime docs into an archive.
9. Keep public/private boundaries intact; progressive disclosure never justifies leaking private machine/provider/model details or credentials.
10. Use exact paths, keys, commands, identifiers, and expected outcomes when they are part of the maintained contract.

## OpenCode context budget

Treat these as expensive runtime context:

```text
AGENTS.md
prompts/*.md
skills/*/SKILL.md
other automatically injected instructions
```

Keep only execution-relevant behavior there. Move maintenance history, provenance, extended examples, and design explanation to README/reference files unless execution genuinely depends on them.

## Authority test

Before duplicating a rule, ask:

> If the copies diverge later, which one is authoritative?

If the answer is unclear, do not duplicate the full rule. Keep one owner and make the other layer a scoped summary or pointer.

## Read deeper only when needed

- Ownership or placement is unclear: read `references/placement.md`.
- Editing runtime-loaded instructions or another skill: read `references/runtime-context.md`.
- Drafting/reviewing a substantial commit message: read `references/commit-messages.md`.
- Finalizing a substantial documentation/context change: read `references/review-checklist.md`.
- Broader design rationale or maintenance of this skill: read `README.md`.

Do not load every reference just because this skill was invoked.
