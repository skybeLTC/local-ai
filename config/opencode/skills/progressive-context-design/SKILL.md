---
name: progressive-context-design
description: "Use when creating, modifying, reviewing, or reorganizing durable textual or instructional artifacts, including prompts, skills, README files, AGENTS instructions, guides, runbooks, design docs, repository navigation, history, and other persistent text that later people or AI systems will rely on. Design single authority, natural ownership, progressive loading, reference triggers, guaranteed reachability, hierarchy rebalancing, change-impact propagation, current/history separation, and information-boundary handling. Do not use this skill as the authority for software correctness, software architecture, test design, or commit-message authoring."
---

# Progressive Context Design

Give a person or AI the smallest context needed to choose the correct next step, then load deeper information only when observable conditions require it. The objective is not to maximize document layers. The objective is to make authority, scope, loading paths, navigation, and history reliably reachable at reasonable context cost.

## Fixed terms

- **durable artifact**: persistent information expected to be relied on again by a later person, AI, or process. One-time scratchpads, disposable debug output, and temporary notes that no later work relies on are outside this scope.
- **runtime entry**: an information source the receiving runtime guarantees or is explicitly configured to load and that therefore owns the minimum mandatory rules for its scope, such as an applicable `SKILL.md`, `AGENTS.md`, or platform equivalent.
- **natural owner**: the single authoritative source closest to the information's subject while still being reliably reachable by every consumer that needs it, given the applicable scope, loading time, and maintenance responsibility.
- **reference trigger**: an observable task, artifact, or state condition that makes a specific reference mandatory before a dependent judgment or action.
- **guaranteed reachability**: mandatory information can be reached from a guaranteed runtime entry through an explicit loading path before it is needed. File existence alone does not establish reachability.
- **current rule**: a rule that is still active and can change current behavior.
- **history**: a durable record of past decisions, changes, states, or evidence. History is not current authority.
- **evidence**: a traceable observation that supports a specific version, state, or validation result.
- **change node**: a rule, document, section, reference, path, authority relation, or other information unit added, removed, moved, renamed, split, merged, or materially changed by the task.
- **upstream dependency**: a direct authority, definition, prerequisite, source, inherited contract, or restriction used by a change node.
- **downstream dependent**: an information unit that references, summarizes, mirrors, navigates to, loads, consumes, or otherwise depends on a change node.
- **impact boundary**: the point where concrete evidence supports stopping propagation in one review direction.

## Confirm target and responsibility

- Distinguish the current execution platform, artifact receiving platform, artifact type, actual loading mechanism, and authoritative sources. Authoring for another platform does not imply access to that platform or the user's machine.
- Preserve already established target, language, scope, and authorization. Review does not authorize editing. Information-architecture work does not authorize changing code, APIs, configuration values, test strategy, or other engineering decisions.
- When a task creates, modifies, or reviews a durable textual or instructional artifact, apply this skill's information-architecture checks. A small edit or source-local comment is not automatically exempt; if the natural owner is already correct and no higher-level dependency exists, stop there.
- Follow the receiving target's authoritative language and format rules. This skill does not define a universal language policy.
- When information architecture overlaps engineering, skill authoring, commit-message authoring, or another specialized method, keep each method as the authority for its own responsibility. Read `references/scope-boundaries.md` only when the responsibility boundary is not already resolved by the user or a higher-authority instruction and resolving it can materially change the judgment or edit scope. Do not read it solely because the artifact is source code or the task mentions another domain.
- Commit-message formatting and wording are not owned by this skill. This skill owns only the information-layer role of Git history and current/history separation.

## Establish natural authority and progressive stop

- Keep each current rule in the narrowest natural owner that still reliably reaches every consumer that needs it. Other locations may contain only necessary navigation, summaries, or derived mirrors; do not create competing current versions.
- Do not create README, AGENTS, reference, or intermediate layers merely because a directory template suggests them. Create an information unit only when a distinct scope, loading time, maintenance responsibility, mandatory loading need, or navigation value exists.
- Keep local information local. If a source comment fully owns an implementation invariant and no runtime, navigation, or maintenance dependency exists above it, do not duplicate it upward.
- `AGENTS.md`, `SKILL.md`, or another runtime instruction owner has authority only when the receiving runtime actually gives it that loading role. A filename alone does not create authority.
- `README.md` owns purpose, deeper rationale, architecture, lifecycle, maintenance, and general navigation. It may coexist with runtime instructions, but it must not be the only owner of mandatory runtime behavior.
- Derived mirrors or generated copies are allowed only with one explicit authoritative source, traceable synchronization, and a runtime structure that cannot mistake the mirror for a second authority.
- History and evidence do not replace current rules. A later reader should not have to replay all history to reconstruct current behavior.

## Rebalance information hierarchy

- Information hierarchy is not append-only. Review whether a parent has accumulated child-specific responsibilities, a child has become an independent authority, a shared rule should move upward, a local rule should move downward, or an intermediate instruction layer no longer has a distinct purpose.
- Parents own true shared invariants. Children own only local deltas, exceptions, and additional constraints; do not repeat the full parent contract.
- If siblings are substantially independent and an intermediate layer provides only generic navigation or no mandatory responsibility, consider shrinking or removing that instruction layer. Filesystem nesting is evidence, not proof of authority nesting.
- After splitting, merging, lifting, sinking, or removing information, recheck loading, navigation, authority, and change-impact relations. Content still existing somewhere does not prove the structure remains usable.

## Propagate change impact

- A substantive information-architecture change requires review beyond the changed node. Recheck direct upstream dependencies and direct downstream dependents; inspect siblings only when a shared contract, duplication, navigation relation, or other dependency signal exists.
- If a dependency must change, make it a new change node and continue until every branch reaches an evidence-supported impact boundary.
- Necessary propagation within the user's authorized outcome and the same repository, information, and authorization boundary may be edited together when it introduces no new product, engineering, or policy decision. Stop dependent edits and ask when propagation crosses repository or information boundaries, changes authority/classification, requires a material tradeoff, or lacks necessary evidence.
- Do not scan the whole repository by default. Expand along traceable references, authority, loading, navigation, mirrors, history links, and other concrete dependency relations.
- For traversal, hierarchy rebalance, edit boundaries, and stopping criteria, read `references/change-impact.md` when triggered.

## Design progressive loading and guaranteed reachability

- A runtime entry must constrain minimum mandatory behavior without requiring README and must be able to decide which deeper references are triggered.
- Every execution reference needs an observable trigger, exact relative path, and read-before point. When its trigger is true, read it before the dependent judgment or action.
- Splitting content into a reference is valid only if capability remains reachable. Preserve this chain: `observable trigger -> exact reference -> read-before decision/action -> required content -> missing/unavailable behavior`. If the entry can no longer determine when the method is required, the split is a regression.
- Multiple reference triggers may be true at the same time. Read every required reference before its dependent judgment. Progressive loading means excluding unrelated content, not limiting work to one reference at a time.
- If trigger applicability is uncertain, read the minimum content needed to decide it. If a mandatory reference is missing or inaccessible, report the gap and affected judgment, stop actions that depend on it, and continue only independent work.
- Do not preload untriggered references. Previously read content may be reused only while it remains in context, unchanged, and applicable; reread affected content when version, context, or task conditions change.
- Mandatory local instructions need a loading path from a guaranteed entry. Use the receiving platform's actual mechanism; never infer automatic loading from filenames alone.

## Preserve meaning, procedures, and information boundaries

- When moving, splitting, summarizing, or referencing a current rule, preserve actor, action, object, rule strength, and all conditions, exceptions, negation, and quantity boundaries that can change behavior.
- Use one primary name for one concept across runtime entries, references, README, history, and source comments. If different names mean different concepts, define the distinction explicitly.
- For procedures embedded in artifacts, place prerequisites before dependent actions, warnings and stop conditions before affected actions, and observations and decision criteria next to the step they control.
- Distinguish current rules, history, examples, facts, assumptions, evidence, and unresolved items.
- Public, private, confidential, or other information classification comes from the applicable policy or project authority. This skill only designs placement, references, summaries, and navigation within those existing boundaries. If classification appears wrong, explain why and request a decision; do not reclassify unilaterally.

## Reference triggers

Compare every invocation against this table. If multiple rows match, read all required references before their dependent decisions. Do not preload unmatched references.

| Reference trigger | Read before |
| --- | --- |
| The task overlaps engineering, skill authoring, commit-message authoring, or another specialized method; the responsibility boundary is not already resolved by the user or a higher-authority instruction; and resolving it can materially change the judgment or edit scope | Read [scope-boundaries.md](references/scope-boundaries.md) before deciding responsibility or editable scope. |
| Adding, moving, copying, or summarizing durable information; choosing or changing an owner; finding duplication, a missing owner, an overloaded parent; or rebalancing hierarchy | Read [placement.md](references/placement.md) before deciding placement, split, lift, sink, or removal. |
| Adding, deleting, moving, renaming, or materially changing durable information structure, authority, a reference trigger, navigation, history relation, or loading relation | Read [change-impact.md](references/change-impact.md) before defining the full impact set and edit order; after edits, traverse again to the impact boundary. |
| Creating, modifying, moving, merging, or reviewing runtime-loaded instructions, another skill, reference triggers/routing, loading assumptions, or a guaranteed loading path | Read [runtime-context.md](references/runtime-context.md) before designing or judging loading behavior. |
| The artifact primarily exists for persistent reading, understanding, or execution, including README, guide, runbook, design doc, ADR, migration note, handoff, changelog, or release note | Read [documentation.md](references/documentation.md) before organizing, writing, or reviewing the document. |
| Creating or changing repository/subsystem entry points, directory navigation, source-of-truth discovery, nested-repository boundaries, or forwarding locations | Read [repository-navigation.md](references/repository-navigation.md) before designing or changing navigation. |
| Referencing, summarizing, synchronizing, or moving content across public/private/confidential or other information scopes, or when existing classification may need reconsideration | Read [information-boundaries.md](references/information-boundaries.md) before disclosure, movement, or a reclassification recommendation. |
| The task involves durable historical records, current/superseded/obsolete state, migration-evidence lifecycle, or current/history authority separation | Read [history.md](references/history.md) before deciding history placement, status, or navigation. |
| The task involves Git commit history, commit subject/body as history navigation, or progressive traversal from Git history into diff/source | Read [history.md](references/history.md), then [commit-history.md](references/commit-history.md), before Git-specific history judgments. |
| Completing an information-architecture review or delivering an artifact with substantive information-architecture changes | Read [review-checklist.md](references/review-checklist.md) before the final conclusion or handoff. |

## Completion

Use the stable review-dimension inventory in [review-checklist.md](references/review-checklist.md), but check only dimensions that actually apply. At minimum, determine whether natural ownership, single authority, mandatory-information reachability, required reference loading, navigation, duplication/drift risk, current/history separation, applicable information boundaries, and change-impact boundaries are correct when those dimensions apply.

If review reveals a recurring cross-case failure mode not covered by the inventory, report it as a candidate review dimension. Do not silently invent a one-off standard, and do not permanently add a special case without deciding that it generalizes.

Report structure checks, scenario exercises, actual runtime loading tests, behavior tests, and deployment state separately. Do not claim a state without supporting evidence.
