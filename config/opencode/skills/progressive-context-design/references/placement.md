# Information Placement and Hierarchy Rebalancing

Use this reference to choose the natural owner of durable information and decide whether an existing hierarchy should be split, lifted, sunk, merged, or have an intermediate layer removed. `../SKILL.md` owns the core single-authority and local-owner-first rules.

## Find the natural owner first

Ask:

1. Which tasks or readers actually need this information?
2. At what point must they obtain it?
3. What is the narrowest location that reliably reaches all of them without forcing unrelated scopes to load it?

Typical owners include:

| Information | Typical natural owner |
| --- | --- |
| Personal/platform behavior that applies across projects | applicable global instruction owner |
| New invariant shared across tasks in one project | project-level instruction owner |
| Method for one task class | task skill runtime entry plus conditional references |
| Mandatory invariant when modifying one subtree | narrowest local instruction owner the receiving platform can guarantee to load |
| Purpose, rationale, lifecycle, maintenance, general navigation | README or guide |
| Rationale for one setting, local behavior, or algorithm invariant | nearby source/config comment or local document |
| Past decisions, changes, states | durable history owner |
| Observation supporting one version or validation state | evidence artifact with version/source |

These are mappings, not filename templates. Use the target platform's actually reachable equivalent owner.

## Local-owner-first and progressive stop

If information already sits in the closest correct natural owner and has no higher-level runtime, navigation, public-contract, or maintenance dependency, stop the review there. Do not create an upper-level summary or index only for completeness.

A comment beside an algorithm is often enough for an implementation-only invariant. A rule such as "any agent modifying this subtree must do X first" may need an earlier guaranteed instruction owner because a source comment is encountered too late.

## Parent and child responsibilities

A parent owns only true shared invariants, necessary inheritance contracts, and navigation that must be known before entering children. A child owns local deltas, exceptions, and additional constraints.

Do not duplicate the entire parent contract to make a child standalone. State exceptions explicitly with their conditions and scope.

## Rebalance instead of appending forever

When a parent accumulates child-specific rules:

1. identify truly shared rules;
2. sink child-specific rules to their natural owners;
3. lift broader shared rules to an appropriate ancestor when needed;
4. remove the parent instruction layer if it no longer owns mandatory responsibility;
5. if only durable general navigation remains, usually move that role to README/navigation content;
6. recheck inherited contracts, reference loading, and navigation.

Filesystem nesting, directory adjacency, and matching filenames do not prove authority inheritance.

## Create or remove information units only for real boundaries

Create a separate README, AGENTS, reference, index, or intermediate layer only when at least one of these differs: scope, loading time, maintenance responsibility, mandatory-loading requirement, or independent navigation value.

If an intermediate layer no longer provides those values, merge or remove it instead of preserving it merely because it already exists.

## Moving authority and derived copies

Before moving authority, identify the old owner, new owner, and all dependents. After the move, keep only minimal forwarding information at the old location if it still has navigation value; do not leave a second current rule.

Derived mirrors, generated copies, and necessary summaries require one authoritative source, an explicit synchronization relation, and a distinct purpose. If the runtime could load both as authoritative instructions, fix the loading structure first.

Placement changes alter the dependency graph; propagate them through [change-impact.md](change-impact.md).
