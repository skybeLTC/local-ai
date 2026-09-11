# Information-Architecture Review Dimensions

This is the stable final-review dimension inventory. `../SKILL.md` owns the minimum execution contract. Determine which dimensions apply to the current artifact/change and check only those; do not mechanically run every item, and do not change standards ad hoc between reviews.

If a recurring cross-case failure mode is not represented here, report it as a candidate review dimension with rationale. Do not silently add a one-off standard or permanently encode an isolated special case.

## 1. Target, scope, responsibility

- Are execution platform, receiving platform, artifact type, and actual loading mechanism distinguished?
- Are review and edit authorization separated?
- Are information architecture, engineering, skill authoring, commit-message authoring, and other specialized responsibilities separated?
- Do language, format, and classification come from applicable authority?

## 2. Natural owner and authority

- Does each current rule have one narrow natural owner that reliably reaches all required consumers?
- Does local information remain local unless a higher dependency exists?
- Do README, runtime instructions, skills, source comments, history, and evidence own information appropriate to their roles?
- Do derived mirrors/generated copies have one authoritative source and explicit synchronization?
- Is there any forwarding-only mandatory policy, competing current version, or history used as current policy?

## 3. Hierarchy balance

- Is a parent holding too many child-specific rules?
- Should shared invariants move upward or local rules downward?
- Do children contain only local deltas/exceptions/additional constraints instead of copied parent contracts?
- Does each intermediate instruction/navigation layer still have independent scope, loading, or navigation value?
- Is filesystem nesting being mistaken for authority nesting?

## 4. Progressive loading and reachability

- Does each execution reference have an observable trigger, exact path, read-before point, and missing behavior?
- Does mandatory local information have a path from a guaranteed runtime entry?
- Did reference splitting preserve capability reachability?
- Can simultaneous triggers load all required references?
- Are untriggered references left unloaded?
- Are uncertain triggers, missing/denied references, changed versions, and lost context handled explicitly?

## 5. Documentation and procedures

- Does durable documentation state scope, current status, natural entry, and deeper path clearly?
- Does README own rationale/maintenance/navigation without monopolizing mandatory runtime policy?
- Are procedure preconditions, warnings, stop points, observable results, decision criteria, and branches placed near affected actions?
- Are current procedure, historical example, fact, assumption, evidence, and open question distinguishable?

## 6. Repository navigation

- Can a consumer reach the true source of authority from natural entry points?
- Does each navigation item state when to enter, path root, and expected authority/evidence?
- Are nested/multiple repository ownership, Git history, and edit authorization clear?
- Does any navigation layer merely forward without new decision value?

## 7. History

- Can later agents know current state without replaying all history?
- Are historical records' current/superseded/obsolete or equivalent statuses identifiable?
- Do temporary migration/handoff artifacts have lifecycle/retirement criteria?
- When Git history applies, does subject -> full message -> diff/source provide effective progressive navigation?
- Has the information role of commits been confused with commit-message authoring authority?

## 8. Information boundaries

- Are source/destination public/private/confidential or other information scopes established?
- Is work staying within existing classification instead of broadening disclosure unilaterally?
- When classification looks wrong, is the rationale reported and the decision boundary preserved?
- Is mandatory information hidden where required consumers cannot access it?

## 9. Change-impact propagation

- Are all substantive change nodes represented?
- Were direct upstream and downstream dependencies rechecked?
- Were siblings included only when evidence signaled a relation?
- Did affected dependencies become new change nodes and continue propagation?
- Was hierarchy rebalance included rather than only link updates?
- Does every branch stop at an evidence-supported impact boundary?
- Are authorization, information-boundary, and evidence gaps kept unresolved rather than labeled unaffected?

## 10. Completion evidence

- Are structure checks, scenario exercises, runtime loading, behavior tests, and install/deploy state reported separately?
- Does each validation claim match the exact version/state supported by evidence?
- Do unresolved validation gaps state which judgment or next step they affect?

When a gap is found, identify the natural owner/authority, affected action, minimum necessary correction, and unresolved boundary. Review itself does not authorize unrelated edits.
