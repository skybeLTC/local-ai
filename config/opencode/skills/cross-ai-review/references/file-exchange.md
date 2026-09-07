# Cross-AI File Exchange

Read this when the `SKILL.md` file-exchange gate requires a handoff, or when the current cross-AI task otherwise needs files exchanged with the peer AI.

This file is the authoritative conditional runtime extension of `../SKILL.md` for handoff semantics and archive mechanics.

## When exchange is required

Create or update a current `.tar.zst` handoff before ending a round when all of the following are true:

- this round creates or changes a named formal deliverable;
- the peer AI must implementation-review that deliverable; and
- the peer AI cannot directly access the exact current files or exact current commit.

The following cases do not require a new archive:

- the round is diagnosis/remediation discussion only and formal implementation has not started;
- the peer AI can directly access and review the exact current files or commit (the direct-access exemption);
- the peer AI already has an archive containing the exact current formal deliverables, and no formal deliverable changed after it was produced; or
- only explanations, logs, or other evidence changed while the formal deliverables remained unchanged.

When using the direct-access exemption, state it explicitly in the final response with the reason. If a required exchange applies, a pasted diff, commit summary, `git show` output, commit hash, or claim that the files exist in Git is not a substitute for the `.tar.zst` handoff. Those items may accompany the archive or the explicit exemption.

## Archive format

Use `.tar.zst` for every file exchange with the peer AI.

If the current environment cannot reliably create `.tar.zst`, state the blocker explicitly. Do not silently substitute another format and claim the protocol was followed.

## What to package

Package:

- files this round adds or changes for a named formal deliverable;
- supporting files needed for peer review;
- required validation evidence;
- files the peer AI explicitly requested, even if unchanged this round;
- a generated artifact when it is itself a formal deliverable, required by the accepted implementation, necessary review evidence, or explicitly requested.

Do not package cache, temp files, or generated garbage that is purely incidental to investigation, build, or test and is neither requested, a required deliverable, nor necessary review evidence.

## Timing

Finish everything this round can reasonably complete under the substantive-judgment gate before packaging.

Do not ask the user to relay a half-finished archive mid-task when more work can still be completed in the current environment.

## Paths

Preserve the relative paths needed for the peer AI to understand, review, or apply the files.

If the workspace is reachable, place the `.tar.zst` at the workspace root. Otherwise, provide it for download.

Do not package unrelated home-directory content, repository caches, credential stores, or other incidental environment state.

## Security

Never package credential material, including:

- `auth.json`;
- access or refresh tokens;
- API keys;
- SSH private keys;
- credential-bearing session, cache, or database state.

Private repository visibility does not make credential material suitable for cross-AI file exchange.

## Reuse

If the user already forwarded an archive produced by the peer AI, use it directly.

Do not ask for the same archive again unless its content changed, the peer AI explicitly asks again, or this round produced new modifications that require a new exchange.

## User-facing handoff

At the end of the reply, explicitly remind the user to pass the archive to the peer AI for review and name the exact archive filename or path in that same reminder.

Do not write only “send the file above” or another vague pointer that forces the user to search backward.
