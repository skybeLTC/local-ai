# Durable History and Current Authority

Use this reference for principles shared by commits, ADRs, changelogs, migration records, decision records, handoff history, and other durable historical artifacts. `../SKILL.md` owns the core current/history contract. Git-specific navigation is in [commit-history.md](commit-history.md).

## History is not current authority

Historical records describe what happened, why, what was known, or what was validated at a past point. Rules that still govern behavior must exist in a current authoritative owner.

Later agents should not have to replay all history to reconstruct current state. Conversely, do not permanently load every historical rationale into runtime instructions.

## Make status identifiable

When a historical artifact can be used as decision evidence, make its actual status identifiable: current/accepted, superseded, deprecated, obsolete, historical-only, or the target's established equivalent. Do not invent a new status taxonomy when the project already has one; when no convention exists, use the smallest clear status description needed.

A superseded record should lead to the replacing decision or newer record. Current authority should be able to lead back to relevant history when evolution matters without preloading that history.

## Progressive history navigation

The first history layer should be enough to filter relevant records before deeper rationale/evidence. The first layer varies by artifact type: commit subject, ADR title/status, release heading, migration checkpoint, and so on.

Do not force every history type into one template. Keep only cross-artifact principles here; create a specialized reference only when a history type has independent, recurring methodology and a clear trigger.

## Migration-evidence lifecycle

For migration notes, handoffs, temporary checkpoints, and review artifacts that matter only during transition, track which information is not yet absorbed into current authority, which evidence still supports deferred decisions, what conditions allow archive/removal, and which links/references/pending tasks must change first.

A `tmp` filename or test-folder location does not prove an artifact is disposable. Later dependency is the criterion.

## Changelog, release, ADR, and current docs

Use changelog/release notes for version evolution, ADRs for decision rationale/status, and migration/handoff for transition evidence. None should indefinitely duplicate current runtime policy.

Read [commit-history.md](commit-history.md) only when Git-specific history navigation is needed.
