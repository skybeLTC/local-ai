---
name: commit-message
description: "Write, review, or revise Git commit messages based on actual changes, including after implementation work."
---

# Commit Message

## Writing and Review

Before writing a commit message, or reviewing or revising one against actual changes, inspect the target repository's Git commit history.

Use the actual changes and available evidence to write, review, or revise the commit message.

If the evidence is insufficient to establish accuracy, investigate first. Ask the user only if the issue remains unresolved.

The commit message must be clear, specific, informative, and accurate. Do not present unverified causes, impacts, or validation results as facts.

When reviewing an existing commit message, identify substantive issues and provide a revised message when correction is needed.

## Output

When writing or revising a commit message, include both a subject and a body.

By default, provide:

- **English canonical**: The complete English message suitable for a Git commit.
- **Taiwan Traditional Chinese review**: A complete, meaning-equivalent translation for review, not part of the actual Git commit message.

Both versions must convey the same meaning.

This skill does not authorize modifying a Git repository or its history.
