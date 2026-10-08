# Cross-AI File Exchange

Read this when the `../SKILL.md` file-exchange gate requires a handoff, or when the current cross-AI task otherwise needs files exchanged with the peer AI.

This file is the authoritative conditional runtime extension of `../SKILL.md` for input materialization and handoff mechanics.

## Materialize compressed inputs before inspection

Before substantive inspection of compressed input, materialize the needed content into isolated local working storage. For a compressed single file, decompress to a local file; for a bundle, extract the needed files into an isolated directory. Use the actual tools and storage available in the current environment, not a platform-specific command as a shared protocol requirement.

Before bundle extraction, inspect member paths and reject or isolate traversal, absolute paths, links escaping the destination, and entries that would overwrite unrelated files. Do not extract directly into a live repository or home configuration.

After materialization, read or parse the local files normally. Archive/compression commands remain suitable for integrity checks, member/path safety inspection, and decompression/extraction; do not repeatedly stream archive contents as the ordinary reading method. Reuse complete materialized content while the exact input is unchanged and available. A changed input, missing local copy, or incomplete extraction may require materialization again; this is not a literal one-command limit.

Keep materialized files associated with their source/version and avoid collisions between inputs. Complete decompression does not prove valid structure or full evidence coverage. If materialization is unavailable or incomplete, state the exact gap and keep affected conclusions unverified; independent work may continue.

## When exchange is required

Create a new verified zstd-compressed handoff, or reuse a sufficient unchanged one, before ending a round when all of the following are true:

- this round creates or changes a named formal deliverable;
- the peer AI must implementation-review that deliverable; and
- the peer AI cannot directly access the exact current files or exact current commit.

The following cases do not require a new handoff:

- the round is diagnosis/remediation discussion only and formal implementation has not started;
- the peer AI can directly access and review the exact current files or commit (the direct-access exemption);
- the peer AI already has a handoff containing the exact current formal deliverables and all files needed for this review, and those files remain unchanged; or
- only explanations, logs, or other evidence changed while the formal deliverables remained unchanged, and no new evidence files need to be exchanged.

When using the direct-access exemption, state it explicitly in the final response with the reason. If a required exchange applies, a pasted diff, commit summary, `git show` output, commit hash, or claim that the files exist in Git is not a substitute for the handoff. Those items may accompany the handoff or the explicit exemption.

## Handoff format and preservation

Use zstd compression for handoffs produced by the current side. Keep one logical handoff together in one compressed artifact whenever possible. A naturally single-file artifact may be compressed directly, for example as `.json.zst`; multiple related deliverables, supporting files, or evidence files are bundled by default into one `.tar.zst`. Do not split related handoff material into separate attachments without a concrete need.

This transport format does not change a formal deliverable's own release format. If the current environment cannot reliably create the required zstd-compressed artifact, state the blocker explicitly; do not silently substitute another format or merely change a filename suffix.

Never overwrite or automatically delete an existing handoff. If the chosen filename exists, use a different non-conflicting filename. No revision, version, or final-name scheme is required.

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

Before producing a handoff, establish and retain the absolute task-workspace output directory from the user's applicable task context. The task workspace is not automatically the repository root or current tool workdir. Entering a nested repository or changing workdir does not change the handoff destination. If the location is unresolved and matters, obtain that location before output. Place the handoff at that task-workspace root when reachable; otherwise provide it for download without claiming it was written to the user's filesystem.

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

If a sufficient exact handoff was already forwarded, use it directly and reuse its materialized files while they remain complete and applicable.

Do not ask for the same available input again. Request only missing current files/evidence when the existing material is insufficient. A new candidate, changed required evidence, or an unavailable/incomplete copy may require a new exchange.

## Verify the handoff

Check compression integrity, bundle member safety and paths when applicable, required content coverage, and absence of unrelated or credential-bearing files. When exact content matters, materialize a verification copy in fresh isolated storage and compare it with the selected final source. A readable archive or matching hash proves packaging, not behavior, installation, or deployment.

## User-facing handoff

In the closing section of the reply, explicitly remind the user to pass the handoff to the peer AI for review and name the exact filename or path in that same reminder. Keep any unanswered user questions prominently at the bottom as required by `../SKILL.md`.

Do not write only “send the file above” or another vague pointer that forces the user to search backward.
