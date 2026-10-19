---
name: commit-message
description: "Write, review, or revise Git commit messages based on actual changes, including after implementation work."
---

# Commit Message

## Writing and Review

Before writing a commit message, or reviewing or revising one against actual changes, inspect the target repository's Git commit history.

Use Git history to understand past terminology, conventions, and changes. Historical commit-message examples do not override an explicitly applicable current format requirement. If current applicable format requirements conflict and their priority is unresolved, ask the user before choosing a conflicting format.

Use the actual changes and available evidence to write, review, or revise the commit message.

If the evidence is insufficient to establish accuracy, investigate first. Ask the user only if the issue remains unresolved.

The commit message must be clear, specific, informative, and accurate. Do not present unverified causes, impacts, or validation results as facts.

Write for maintainers who did not participate in the current work, using the commit's actual changes and durable project context. Do not make session-only names or temporary workflow labels necessary to understand a change or validation claim; when validation matters, describe the recognizable test scope and result. Include background only when it helps explain this commit. Do not mention separate work that is not part of this commit merely because it was discussed in the session.

When reviewing an existing commit message, identify substantive issues and provide a revised message when correction is needed.

## Output

When writing or revising a commit message, include both a subject and a body.

By default, provide:

- **English canonical**: The complete English message suitable for a Git commit.
- **Taiwan Traditional Chinese review**: A complete, meaning-equivalent translation for review, not part of the actual Git commit message.

Both versions must convey the same meaning. By default, show both complete versions directly in the response, even when also writing files; file paths or summaries alone do not satisfy this output requirement. Follow a different delivery format if the user explicitly requests one.

This skill does not authorize modifying a Git repository or its history.
