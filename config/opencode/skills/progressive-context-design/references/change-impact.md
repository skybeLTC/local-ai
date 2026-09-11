# Change-Impact Propagation

Use this reference after a substantive change to durable information structure. Follow authority, loading, navigation, history, mirror, and other explicit dependencies until every branch reaches an evidence-supported impact boundary. `../SKILL.md` owns the core propagation requirement.

## 1. Build the change set

List known change nodes and their types: add, delete, move, rename, split, merge, lift, sink, authority change, reference-trigger change, or other material semantic change.

Formatting or spelling changes may be marked non-propagating only when evidence shows they do not change meaning, names, paths, references, loading, navigation, or scope. A small diff is not sufficient evidence.

## 2. Recheck upstream dependencies

For each change node, identify direct authorities, definitions, prerequisites, restrictions, sources, and inherited contracts. Confirm that the new content remains within the upstream authority's scope; names, conditions, rule strength, exceptions, and assumptions remain valid; the change has not exposed an overloaded, obsolete, or no-longer-natural owner; and any changed authority, scope, or loading relation has the correct removal, lift, or reconnection.

If an upstream source must change, add it as a change node and repeat.

## 3. Recheck downstream dependents

Find direct references, summaries, derived mirrors, navigation, loaders, consumers, history links, and other dependents. Confirm paths, filenames, stable IDs, and relative references resolve; semantics, conditions, exceptions, rule strength, and scope remain correct; reference triggers, loading order, guaranteed reachability, and stop conditions still reach the new content; README, indexes, history, mirrors, generated artifacts, and handoffs do not retain stale authority or semantics; and any consumed input/output/behavior contract still holds.

If a downstream dependent must change, add it as a change node and continue.

## 4. Inspect siblings only when signaled

Do not scan all siblings merely because they share a parent. Inspect a sibling when evidence shows a shared parent or inherited contract changed, a duplication/mirror/summary relation exists, hierarchy rebalance suggests misplaced child-specific rules, shared navigation or an index covers the sibling, or the sibling consumes the same authority. If the sibling must change, add it as a new change node and continue propagation.

## 5. Rebalance hierarchy

For each substantive information-architecture change, ask whether the parent has become a child-specific rule container, a child has developed an independent scope or maintenance responsibility, a shared rule should move up, a local rule should move down, or an intermediate instruction layer has lost distinct responsibility. Do not stop at confirming that a new file exists; also confirm that the old hierarchy remains appropriate.

## 6. Separate impact review from edit authorization

Necessary propagation may be edited when it is clearly part of the already authorized outcome, stays within the same repository/information/authorization boundary, and introduces no new product, engineering, or policy decision.

Stop dependent edits and report the impact when work crosses repository or authorization boundaries, crosses public/private/confidential boundaries, changes authority/classification, introduces a material persistent tradeoff, or lacks evidence needed for a safe propagation decision. Review may continue to an evidence-supported boundary even when editing is not authorized.

## 7. Define impact boundaries with evidence

A branch may stop when no further traceable dependency exists, direct evidence shows the next dependency's contract is unaffected, a clear authority/information boundary isolates the change, or further work needs an unresolved decision/evidence gap. The last case is an unresolved boundary, not verified unaffected.

"Not edited", "looks fine", "worked before", and familiarity are not stopping evidence.

## 8. Control scope

Build candidates from traceable relations: direct links, path/name/stable-ID searches, reference triggers, loader relations, authority/mirror mappings, README/index/navigation, and explicit dependencies in history/handoff. Expand only when new evidence reveals another relation, and retain why each candidate was added.

## 9. Final impact statement

Before completion be able to state which upstream dependencies, downstream dependents, and signaled siblings were reviewed; which nodes propagated further; whether hierarchy changed; where each branch stopped and why; and which authorization, information-boundary, or evidence gaps remain.

This checks dependency consistency. It does not by itself prove runtime loading, software behavior, installation, or deployment.
