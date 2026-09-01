# Cross-AI Final Review Checklist

Read this when the cross-AI task reaches final implementation review, delivery, commit/deployment, or closeout.

This file is a conditional runtime extension of `../SKILL.md`. It turns the existing protocol into a final checklist; it does not replace the core substantive-judgment and scope rules.

## Context

- Is the current peer response or supplied session export actually represented in the evidence being used?
- Have the user's newest requirements, constraints, decisions, and blockers in this conversation been applied?
- Has any material change since the peer AI's last response been surfaced explicitly?

## Evidence

- Were material claims checked against directly available repo state, Git state, files, logs, command output, build output, or test results?
- When an exact source text or artifact was needed, was the exact version used rather than reconstructed from memory or a summary?
- Are peer claims such as “done” or “tests passed” backed by sufficient evidence rather than accepted at face value?

## Consensus

- Has diagnosis been cross-reviewed?
- Has the remediation direction been cross-reviewed?
- Is any new substantive judgment still waiting for peer review?
- If a problem is only an implementation defect within the accepted remediation, was it kept inside the implementation-review loop instead of unnecessarily reopening remediation?

## Scope

- Are the named formal deliverables explicit?
- Is required validation evidence explicit?
- Have optional migration, deployment, or helper artifacts remained outside formal implementation scope unless the user expanded scope?
- Has reviewing an artifact been kept separate from authorization to modify it?

## Implementation

- Does the implementation faithfully match the accepted remediation?
- Was required validation actually run, or explicitly handed off to the environment that can run it?
- If the current side could not reliably implement or validate something, was the missing file, state, command output, log, toolchain, or environment named precisely?
- If a new remediation judgment emerged, were formal edits stopped and the judgment returned to the peer AI?

## Independent-review topology

- While this cross-AI task is active, was the external peer AI used for the independent-review role instead of dispatching the `review*` or `critic*` subagent family as a duplicate reviewer?
- Were other subagents limited to narrowly scoped factual investigation when used?

## File exchange

If files must be exchanged, read `file-exchange.md` and confirm its archive, path, security, reuse, and handoff rules were followed.

## Completion

Treat the cross-AI implementation workflow as complete only when all of the following are true:

```text
named formal deliverables implemented
+ required validation sufficient
+ peer implementation review passed
+ no unresolved substantive judgment
```

Once those conditions are satisfied, do not create an information-free confirmation loop by asking the implementer to reconfirm the review result.
