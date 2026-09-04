# OpenCode shared skills

This directory contains public, reusable OpenCode skills. Each skill's
`SKILL.md` is its runtime entry point and owns the minimum workflow; referenced
files may own deeper runtime rules when that `SKILL.md` explicitly points to
them. Skill-local README files hold maintenance and design context that should
not be loaded on every invocation.

Shared skill permissions are owned by `../opencode.jsonc`. Third-party
provenance and notices that apply across more than one skill are recorded here
instead of being duplicated into runtime `SKILL.md` files.

## Matt Pocock integrations

Upstream: `https://github.com/mattpocock/skills.git`

| Local integration | Upstream path | Imported tag | Imported commit | Mode | Local adaptations |
| --- | --- | --- | --- | --- | --- |
| `diagnosing-bugs/` | `skills/engineering/diagnosing-bugs` | `v1.2.3` | `6acc160e4e0cd062dbbbd7a1b26ae92855edf07e` | curated copy | `agents/openai.yaml` omitted; OpenCode permissions are configured in `../opencode.jsonc`; `SKILL.md` and `scripts/hitl-loop.template.sh` otherwise unchanged |
| `grilling/` | `skills/productivity/grilling` | `v1.2.3` | `6acc160e4e0cd062dbbbd7a1b26ae92855edf07e` | curated copy | `agents/openai.yaml` omitted; OpenCode permission is global `deny` with primary `build` `allow`; `SKILL.md` otherwise unchanged |
| `skill-creator/` | `skills/productivity/writing-for-agents` | `v1.2.3` | `6acc160e4e0cd062dbbbd7a1b26ae92855edf07e` | principles merged | Matt Pocock principles were merged into the existing Apache-licensed skill creator; upstream `SKILL-MECHANICS.md` and `agents/openai.yaml` were reviewed and omitted or replaced with OpenCode-native guidance; the upstream skill is not installed separately |

The Matt Pocock-derived integrations above retain the upstream MIT notice at
`licenses/mattpocock-skills.MIT.txt`. `skill-creator/` also retains its own
Apache-2.0 notice at `skill-creator/LICENSE.txt`; the two notices have separate
provenance and are not interchangeable.
