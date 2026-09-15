# English Runtime Sources and Taiwan Traditional Chinese Review Mirrors

Use this reference whenever runtime English text, a review mirror, or a skill README is created, changed, renamed, deleted, or reviewed.

## Authority and mapping

English runtime text is the only execution authority. Taiwan Traditional Chinese files are human-review mirrors and must not add, remove, strengthen, or weaken policy.

For this repository:

```text
config/opencode/skills/<skill-id>/...
config/opencode/skill-reviews/<skill-id>/...
```

Preserve the runtime skill-relative structure in the review tree and add `.zh-TW` before the Markdown suffix:

```text
SKILL.md                      -> SKILL.zh-TW.md
references/foo.md             -> references/foo.zh-TW.md
agents/reviewer.md            -> agents/reviewer.zh-TW.md
```

A skill `README.md` itself is written in Taiwan Traditional Chinese and does not receive a second English/mirror pair.

## Runtime isolation

- Do not place translation-only files in the runtime skill directory or `assets/`.
- Do not register `skill-reviews/` as a skill source.
- Runtime `SKILL.md`, references, prompts, config, and permissions must not depend on review-mirror files.
- If the target discovery rules could scan the sibling review tree, prove isolation with target-version evidence before delivery.

## Synchronization

When runtime English text changes, update the matching review mirror in the same change. Preserve actor, action, object, modality, condition, exception, negation, quantity, sequence, stop point, identifiers, paths, commands, and code. Translate meaning, not identifiers.

When files are renamed, moved, or deleted, update the review mapping and maintenance navigation in the same change. A matching file count or heading list proves only structural coverage, not semantic equivalence.

Code, structured-data keys, schemas, binaries, and other resources that do not carry natural-language instruction policy do not receive translation copies merely because they contain English tokens.
