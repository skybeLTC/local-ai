# Cross-AI Review Lifecycle

Read this for remediation, formal implementation, implementation review, and technical completion. `../SKILL.md` owns the always-required forward-progress, authorization, substantive-judgment, peer-question-closure, and minimum-completion rules.

## Fixed stages

1. **Diagnosis review**: establish whether the problem/cause/risk is real.
2. **Remediation review**: establish expected behavior, scope, boundaries, and acceptance criteria.
3. **Formal implementation**: create or modify an exact candidate according to accepted remediation.
4. **Implementation review**: the side that did not create/modify that candidate independently reviews it; required validation may be completed before or during this stage.
5. **Completion judgment**: decide whether implementation, required validation, final independent review, and open items satisfy the technical completion gate.

Do not collapse diagnosis consensus into remediation consensus, candidate existence into validation, or review started into final review PASS.

## Stage-closing transition

When one side's independent review closes the consensus required by the current stage, that side immediately enters the next legal stage unless an actual gate applies. Diagnosis consensus with no remediation means that side proposes the smallest reviewable remediation. Remediation consensus plus implementation eligibility means that side implements. A candidate created by one side is reviewed by the other side.

Do not compare which side is theoretically more convenient when the current side can legally perform the next stage. A future handoff destination or the fact that the other side can also edit is not a gate.

## Remediation review

A reviewable remediation states expected behavior, in/out scope, important boundaries, acceptance criteria, and required evidence. Conditional acceptance becomes consensus only after the conditions are incorporated. Silence, restatement, or an unchecked "looks fine" is not independent acceptance.

## Formal implementation and state separation

Before editing, confirm valid authorization, accepted remediation or an explicitly changed review gate, exact current source/candidate, ability to perform the edit, and all inputs required to select the correct implementation.

Post-implementation validation capability is not an implementation-eligibility requirement. A side may create a formal candidate even with no compiler, syntax checker, static checker, or target runtime. Record validation separately as `NOT_RUN`, `PARTIAL`, `PENDING`, `PASSED`, or `BLOCKED`. If missing runtime evidence is needed to choose the implementation itself, treat it as a required implementation input and stop dependent edits.

Track at least these independent dimensions when relevant:

| Dimension | Example states |
| --- | --- |
| candidate identity | exact version exists / absent |
| validation | NOT_RUN / PARTIAL / PENDING / PASSED / BLOCKED |
| implementation review | NOT_STARTED / IN_PROGRESS / BLOCKED / PASSED |
| technical completion | NOT_COMPLETE / COMPLETE |
| apply/commit/push/install/deploy | report each separately from evidence |

If implementation was produced before remediation consensus, mark it as premature instead of discarding or reimplementing it for formality. First review remediation independently; if accepted, review the exact existing candidate. Modify only parts that depend on a judgment that was rejected or changed.

If a new finding changes expected behavior, scope, an important boundary, compatibility, data handling, risk, or acceptance criteria, stop dependent formal edits and return to the corresponding substantive review. Preserve already-completed work that does not depend on the new judgment and still matches accepted consensus.

## Implementation review and role swap

Review the exact candidate, not only a summary. Check fidelity to accepted remediation, formal scope and dependency impact, new defects/contradictions, what current validation actually proves, and separation of candidate/validation/apply/deploy states.

Source-level implementation review may start before required validation is complete. If final acceptance depends on missing validation, keep implementation review `IN_PROGRESS` or `BLOCKED`; do not report final PASS yet.

If the reviewer finds only an implementation defect inside accepted remediation and has valid authorization, the exact candidate, and ability to edit it, the reviewer fixes it directly. Missing post-implementation validation capability creates a validation gap; it is not by itself a reason to return the edit to the original implementer. The reviewer becomes implementer of the new candidate, and the other side reviews that new candidate.

If the defect requires a changed remediation judgment, return to remediation review before dependent edits.

## Peer questions and user decisions

Before ending a cross-AI response, ensure every relevant explicit peer question has `ANSWERED`, `UNRESOLVED`, `SUPERSEDED`, or `NOT_APPLICABLE` disposition. `UNRESOLVED` blocks only dependent actions. If a newer user decision answers the question, relay that answer instead of asking again. If that answer also introduces a new substantive judgment, the question can be `ANSWERED` while dependent formal edits remain gated.

## Completion

Technical completion requires implemented formal deliverables, sufficient required validation, final independent candidate review passed, no unresolved substantive judgment, all relevant explicit peer questions dispositioned, and the user's requested stage deliverable complete.

Do not create a third information-free confirmation. A later commit/push/install/deploy/user-review gate remains separate from technical completion.
