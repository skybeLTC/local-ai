# Scope Boundaries

This reference separates information architecture from engineering, skill authoring, commit-message authoring, and other specialized methods. `../SKILL.md` owns this skill's core scope; this file only resolves responsibility boundaries.

## This skill owns

- natural ownership, single authority, scope, and navigation for durable information;
- runtime entries, guaranteed reachability, reference triggers, and progressive loading;
- hierarchy rebalancing and change-impact propagation after information-structure changes;
- information structure for README, guides, runbooks, design docs, ADRs, migration/handoff material, repository navigation, and other durable documentation;
- separation of current information from durable history;
- the information role of Git history as progressive context;
- placement, references, summaries, and movement inside already established public/private/confidential boundaries.

## Engineering methods own

This skill does not decide software correctness, source-module decomposition, algorithms, APIs, performance, concurrency, configuration values, test strategy, or build implementation. Do not introduce wrappers, abstractions, or source refactors merely to satisfy information architecture.

If a task fixes code and updates documentation, engineering methods establish correct behavior and evidence; this skill decides how established information should be stored and navigated. Finding an implementation issue during documentation review does not grant permission to edit code.

## Skill-authoring methods own

The receiving platform's skill-authoring method owns skill format, metadata, packaging, platform capabilities, release structure, discovery/permission integration, and behavioral-evaluation methodology.

This skill may review authority, placement, reference loading, documentation, history, and change impact inside a skill, but it must not create a second packaging or validation contract.

## Commit-message methods own

This skill only reviews the information layers of commit subject, full commit message, and diff/source in history navigation, plus separation of current docs from history.

Actual commit-message format, wording, type, scope, body structure, repository conventions, organization conventions, and authoring evidence belong to the applicable `commit-message` method. If that method is unavailable, this skill may report a history-navigation gap but must not invent a replacement commit-message standard.

## When the boundary is unclear

Terms such as "architecture", "review a skill", or "update documentation" can span multiple responsibilities. Ask only when the different interpretations would materially change scope, authorization, or output and available evidence cannot resolve the difference.
