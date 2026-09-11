# Git Commit History as Progressive Context

`../SKILL.md` owns the core scope for Git history. This reference handles Git-specific history navigation only. Cross-history current/status/lifecycle principles are in [history.md](history.md). Actual commit-message authoring belongs to the applicable `commit-message` method.

Fixed terms:

- **history list**: a list of commits that at least shows commit subjects, such as `git log --oneline`;
- **commit subject**: the first line of a commit message and the first navigation layer in a history list;
- **full commit message**: subject plus body when present.

## Progressive path

Use Git history as:

1. **history list / subject** to filter potentially relevant commits;
2. **full commit message** to understand the main semantic change, rationale, scope, constraints, or validation state and decide whether deeper inspection is needed;
3. **diff, source, or other evidence** only when implementation detail or verification evidence is required.

This is an information-role model, not a commit-message template.

## Subject navigation responsibility

A subject should distinguish the main change object and semantic result in a history list. Large numbers of indistinguishable `update`, `fix`, or `cleanup` subjects force unnecessary opening of commits and weaken first-layer navigation.

The subject need not contain all rationale; deeper context belongs in the full message when needed.

## Full-message role

When a body is useful, the full message should provide enough context to understand the change's main meaning, rationale, impact, constraints, or validation state without reading the diff first.

Whether a body is required, its format, type/scope conventions, language, trailers, and repository/organization style are outside this skill.

## Current authority

A commit message records the semantics, rationale, and evidence of that change at that time. It is not the current rule owner. When current policy, runtime instructions, or configuration contracts change, update their current authority rather than requiring Git archaeology.

Do not copy complete commit evolution into runtime context either. Follow the history path only when evolution rationale is needed.

## Review scope

Review whether subjects filter relevant commits, full messages support the decision to enter diff/source, current authority and Git history are separated, historical evidence is not mistaken for current fact, and the Git path reaches deeper evidence when needed.

Do not use this skill to judge commit-message style or organization-specific formatting.
