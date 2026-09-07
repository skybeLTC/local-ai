---
name: cross-ai-review
description: Cross-review workflow for two AIs collaborating on one task. Use when the user pastes another AI's output, response, or full session export — especially after "這是另一個 AI 的說法" or "上面這段來自另一個 AI" — and throughout later implementation, testing, validation, deployment, or closeout turns that clearly continue that cross-AI task, even without new peer content. Do not carry it into unrelated tasks. Covers diagnosis/remediation separation, substantive-judgment gating, local verification, implementation review, and .tar.zst exchange.
---

# Cross-AI Implementation Review（雙 AI 實作交叉審查）

## Ground every claim locally first

- Treat this as a task-scoped workflow. Once a task enters it, keep applying these rules to same-task status, evidence, implementation, testing, validation, deployment, and closeout turns even when no new peer content is pasted. Continue until that task is actually complete; do not carry the workflow into an unrelated task.
- Treat pasted content as one response from the peer AI, not a transcript of its full conversation; if the user also provides a full session export from the peer AI's side, read it in full and fold it in as additional context without switching to a different workflow for it — the rules in this skill still apply the same way. The user's newest instructions in *this* conversation take priority over anything the peer AI assumed or was told earlier.
- If something material has changed since the peer AI's response — new user requirements, constraints, decisions, evidence, blockers — surface it explicitly instead of silently reconciling it.
- The peer AI can be wrong. Whenever the repo, git state, command output, logs, build, or test results are directly available, check them yourself and act on that evidence instead of the peer's summary. Cite the evidence when you disagree. Do not nitpick wording or stall progress over low-probability, irrelevant, or purely hypothetical exceptions that would not change the conclusion; note small exceptions or residual risk briefly instead.
- Write what the peer AI needs to know directly into your reply. Do not produce a separate, duplicate "relay" message unless restructuring it materially improves clarity.
- Do not assume the peer AI has already seen a prompt, file, or artifact that appeared earlier in *this* conversation. If a review, judgment, or implementation depends on an exact source text and the conversation/export/archive you currently have does not contain it, obtain or relay that exact text — do not reconstruct it from a summary, memory, or a similar-looking version. If the exact text is already in the evidence you have, just use it; do not ask again.

## Separate diagnosis from remediation

Diagnosis ("X is broken/true") and remediation direction ("here is the intended fix's behavior, scope, and boundaries") are different claims. Agreeing a diagnosis is correct is not the same as having cross-reviewed remediation for it.

A remediation direction does not need to specify every line of code, but must be concrete enough to pin down expected behavior, the main boundary of the change, and any decision that would materially affect scope, observable behavior, interfaces, data handling, compatibility, risk handling, or acceptance criteria.

## The substantive-judgment gate

The moment you introduce, or notice, a substantive judgment that the peer AI has not reviewed yet:

1. Stop making further formal edits to source-of-truth/tracked files this round.
2. You may still read, run commands, build, or test purely to clarify the problem — that investigation, and any cache/temp/generated artifacts it produces, is not a formal edit.
3. Write up the judgment and its evidence, and hand it to the peer AI for review instead of implementing it.

The same gate applies to a question that needs the peer AI's answer before you can safely continue.

When you are the one reviewing a new diagnosis or remediation direction the peer AI proposed, check it independently against real evidence:

- If you disagree, or it produces a new substantive judgment of your own, stop formal edits and hand it back with your evidence — do not implement past that point.
- If diagnosis and remediation are already accepted by both sides with no new substantive judgment outstanding, and the environment is reliable enough to act on, implement it directly. Do not stop just to restate agreement.
- A judgment either side proposed in an earlier round, once independently accepted by the other with no new disagreement, already counts as consensus for later rounds.

Being asked to review does not mean the round must stay read-only — if the review lands on enough consensus and the environment supports it, continue straight into implementation in the same round. Only a new substantive judgment forces a stop; an explicit user instruction to stay read-only this round overrides that default.

If the peer AI only established "X is a bug" (a diagnosis) and no one has proposed remediation yet, do not implement — even when the fix looks obvious or seems to have only one reasonable shape. Propose the smallest remediation direction sufficient for review, with reasoning, and hand it to the peer AI first.

Adding more evidence for an already-agreed conclusion, extra tests, more explanation, or an equivalent code-level realization that does not change the accepted remediation is not a new substantive judgment — treat it as a routine implementation detail you can act on directly.

## Scope lock and artifact ownership

Before investigating or editing anything, classify every artifact into one of:

1. a named formal deliverable;
2. required validation evidence;
3. optional migration, deployment, or helper tooling.

Only named formal deliverables are eligible for formal implementation changes. A supplied archive is not automatically a formal deliverable — classify what is inside it separately. A migration or helper script can be reviewed as evidence or tooling without becoming part of the implementation scope.

The latest explicit user scope decision outranks earlier workflow assumptions, a peer AI's suggested remediation, and generic rules like "fix implementation defects directly."

If an out-of-scope helper or evidence artifact has a defect: report the exact defect and evidence; do not suggest fixing it, do not patch it, do not re-archive it, and do not let it become a completion blocker. Return to the named formal deliverables instead.

Reviewing an artifact is not authorization to modify it.

Once all named formal deliverables pass implementation review and the required validation, move to their commit/deployment gate. Do not reopen optional helpers or deployment tooling unless the user explicitly expands the scope.

## Implementation and implementation-review loop

Do not dispatch the `review` or `critic` subagent family (`reviewL`/`review`/`reviewH`, `criticL`/`critic`/`criticH`) for independent challenge, cross-review, or implementation review while this task is active — the external peer AI already fills that role for this workflow. Verify evidence yourself instead. Other subagents may still be used for narrowly scoped factual investigation, but not to recreate or substitute for the independent-reviewer role.

Lacking direct local repo access does not make the peer AI (or you, when you are the side without it) read-only. A supplied formal-deliverable archive can be unpacked, edited, and repackaged into an implementation candidate for the other side to apply and finish any environment-specific verification, as long as the available tools can reliably make that edit. Do not treat "no direct repo access" as automatically "cannot reliably fix" — check whether the deliverable itself is already in hand before deciding this needs an environment handoff.

Formal implementation, its tests, and implementation review all share the gate above. When an implementation merely fails to faithfully carry out an already-accepted remediation — a missed edit, an inverted condition, a dropped agreed validation — and fixing it needs no new or changed remediation judgment, stay inside this loop: fix it directly if you reliably can, verify it, and send the corrected implementation back for peer review. Do not declare the work done yourself.

If you cannot reliably fix it in this environment, name the exact implementation defect, the evidence, and where it deviates from the accepted remediation, and hand it to whichever side can act on it. The receiving side checks it independently: agrees and no new remediation judgment needed → fix, verify, resend for implementation review; disagrees → send evidence back rather than editing blindly. Only stop and return to remediation cross-review when the existing remediation itself is wrong, incomplete, or a new/changed remediation judgment is required.

Once implementation is done, report the actual change and verification evidence sufficient to check it. Implementation review exists to check faithfulness to the agreed remediation and to catch new problems — not to redo diagnosis or remediation confirmation that adds no information. If the implementation matches consensus, verification is sufficient, and nothing new surfaced, treat it as done; do not ask the implementer to re-confirm the review.

## Answering the peer AI and environment handoffs

Answer any question the peer AI asked. If a judgment, edit, or test needs a file, project fact, repo/git state, command output, log, build/test result, toolchain, or environment that is not available here, say exactly what the peer AI needs to supply or run — do not just ask vaguely for "more information", and do not accept "done" or "tests passed" claims from the peer as sufficient evidence on their own. If a formal change can only be made reliably in an environment the peer AI controls, say so plainly instead of pretending it is already implemented; state the agreed direction and the remaining work. This is an environment handoff, not a reason to reopen an already-settled judgment.

## File-exchange gate

- Every formal implementation-review round must end with either a verified current `.tar.zst` handoff or an explicit direct-access exemption; never leave the handoff status implicit.
- A current file handoff is required when this round creates or changes a formal deliverable that the peer AI must implementation-review and the peer AI does not have direct access to the exact current files or exact current commit. Before ending that round, read `references/file-exchange.md` and produce the required handoff.
- A pasted diff, commit summary, `git show` output, or claim that files are committed does not replace a required archive. If direct access makes an archive unnecessary, state that exemption and its reason explicitly in the final response.

## Before declaring the cross-AI task complete

When the task reaches final implementation review, delivery, commit/deployment, or closeout, read `references/review-checklist.md` and use it before reporting the cross-AI workflow complete.
