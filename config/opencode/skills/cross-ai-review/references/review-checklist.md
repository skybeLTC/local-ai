# Cross-AI Final Review Checklist

Read this at final implementation review, delivery, commit/deployment, or closeout. Check only dimensions that apply.

## Context and evidence

- Is this still the same cross-AI task? If a peer side moved to a new session, was necessary context recovered instead of assumed to transfer automatically?
- Are the user's newest requirements, scope, authorization, constraints, and blockers applied?
- Were material claims checked against exact available repo/files/Git/log/build/test evidence instead of summaries or memory?
- If evidence is missing, is the affected judgment/gate and minimum missing input explicit?

## Peer-question coverage

- Does every still-relevant explicit peer question have `ANSWERED`, `UNRESOLVED`, `SUPERSEDED`, or `NOT_APPLICABLE` disposition?
- Were partially superseded questions split so an open part was not hidden?
- Does each `UNRESOLVED` item identify missing evidence/input, affected gate, and independent work that may continue?
- Were newer user answers applied directly, and did any new substantive judgment from them trigger its own gate?

## Scope, authorization, and forward progress

- Was review kept separate from modification/commit/push/install/deploy authorization?
- Was a handoff destination kept separate from an exclusive implementation constraint?
- Was user-relative wording such as "this round" interpreted from user context rather than redefined as an internal lifecycle round?
- When a side's independent review closed the current stage, did that side enter the next legal stage instead of creating an information-free handoff?
- Was the next stage chosen from the lifecycle rather than assuming it is always implementation?

## Candidate, validation, and implementation review

- Are candidate identity, validation, implementation-review status, technical completion, and apply/commit/push/install/deploy reported separately?
- Did implementation eligibility depend on authorization, accepted remediation, exact source/candidate, ability to edit, and required implementation inputs—not on post-implementation validation capability?
- If local validation was unavailable, was a formal candidate still allowed while the validation gap remained explicit?
- If runtime evidence was required to choose the implementation, was dependent editing stopped until that input existed?
- Was a premature candidate preserved/reviewed after remediation consensus instead of reimplemented for formality?
- If a reviewer fixed an implementation defect, did the reviewer become implementer of the new candidate and the other side review it?
- Did source-level review start when useful without claiming final PASS before required validation was sufficient?

## OpenCode-specific independent-review topology

- While this cross-AI task was active, was the external peer used for the independent-review role instead of dispatching `review*` or `critic*` as a duplicate reviewer?
- Were other subagents limited to narrowly scoped factual investigation?

## Session export and file exchange

- If a session export was used, was `session-export.md` applied to decompression/parsing, truncation, tool-result coverage, and attachment/artifact coverage?
- If file exchange was required, was `file-exchange.md` applied, with a verified current `.tar.zst` or explicit direct-access exemption?

## Completion

Treat the technical workflow as complete only when formal deliverables are implemented, required validation is sufficient, final independent implementation review passed, no substantive judgment remains unresolved, all still-relevant peer questions have dispositions, and the user's requested stage deliverable is complete.

Do not ask the implementer to reconfirm a final reviewer PASS. Keep commit/push/install/deploy/user-review gates separate and report them from their own evidence/authorization.
