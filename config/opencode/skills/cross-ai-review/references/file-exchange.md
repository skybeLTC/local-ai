# Cross-AI File Exchange

Read this only when the current cross-AI task actually needs files exchanged with the peer AI.

This file is a conditional runtime extension of `../SKILL.md`.

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
