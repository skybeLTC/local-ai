# Durable Documentation Structure

Use this reference when an artifact primarily exists for persistent reading, understanding, or execution: README, guide, runbook, design doc, ADR, migration note, handoff, changelog, release note, and similar durable documentation. `../SKILL.md` owns the README/runtime-instruction authority boundary; this file handles document structure and reading paths.

## Define the document role

Identify whether the document primarily provides entry/navigation, conceptual explanation, executable procedure, design decision, migration/handoff state, release/history, or another durable purpose. Multiple roles may coexist, but current procedure, historical examples, rationale, and status must remain distinguishable.

Root-level documentation should focus on overall purpose, scope, major responsibilities, and natural entry points. Move subsystem details downward only when they have independent scope, lifecycle, maintenance responsibility, or navigation value. Do not create a README merely because a directory exists.

## AI-friendly does not mean more documents

A durable document should let a reader determine its scope, what is current/authoritative, where to go next, and which deeper details are conditional. Do not create higher-level documentation when a local source comment already owns the information. Conversely, do not leave a mandatory workflow rule only in deep README material when it must be guaranteed earlier.

## README and guides

README is suitable for purpose, architecture overview, lifecycle, maintenance, rationale, and general navigation. It may reference runtime instruction owners, but it must not be a forwarding-only substitute for mandatory policy.

Keep one understandable or executable topic per document unit. Split only for meaningful differences in scope, loading time, or maintenance responsibility; do not split sentence-by-sentence or force tightly coupled procedure steps across many files.

## Runbooks and procedures

- Put environment, version, inputs, tools, and permissions shared by the whole procedure at the entry; local preconditions immediately before the affected step.
- Put warnings, constraints, and stop conditions before the affected action.
- Keep observable result and decision criterion next to the action they control.
- Put branches where their conditions occur and preserve an unknown path when the condition cannot be determined.
- When later actions depend on an unavailable result or approval, mark the stop point before those dependent actions; unrelated work may continue.

This skill owns procedural information structure, not command correctness, engineering validation, or domain-specific method.

## Design docs and ADRs

Separate current decisions, constraints, alternatives, evidence, and open questions. If ADRs use status, make current/accepted, superseded, deprecated, or the target's equivalent state explicit. Historical decisions must not be mistaken for current runtime rules.

Do not force runtime agents to read complete ADR rationale to learn current rules. Keep current authority in the correct owner and use ADRs for decision history.

## Migration notes and handoffs

Distinguish verified current state, modified-but-unverified state, deferred decisions/known gaps, historical checkpoints, and evidence/entry points required for continuation. Temporary handoff evidence needs an explicit lifecycle: when it remains necessary, when current docs have absorbed it, and when it may be removed.

## Changelog and release notes

Use them primarily to answer what externally relevant change occurred in which release. Do not turn them into complete implementation rationale or current policy authority; link to deeper history/design/source when needed.

## History, examples, and current procedure

Clearly label examples, old commands, screenshots, and historical state. Do not make readers infer validity from dates or surrounding context. When current/history separation spans artifact types, read [history.md](history.md).
