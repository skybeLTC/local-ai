# local-ai Repository Rules

Apply these rules when working in the `~/local-ai` management repository.

- Keep `README.md` files tracked by this repository AI-friendly and human-readable; write prose in Taiwan Traditional Chinese by default while preserving technical identifiers, paths, commands, code, and necessary technical terms.
- Keep `AGENTS.md` files tracked by this repository in English and limited to execution-time rules, invariants, safety boundaries, and precise navigation.
- When `README.md` and `AGENTS.md` coexist at the same scope, keep the minimum actionable form of mandatory execution rules in `AGENTS.md` and deeper rationale or architecture in `README.md`; do not use a forwarding-only `AGENTS.md` rule that hides mandatory policy exclusively in README.

- Treat `~/local-ai`, `~/local-ai/opencode`, and `~/local-ai/private` as separate Git repositories.
- Never stage or commit `opencode/` or `private/` into the root repository.
- Keep public shared behavior under `config/opencode/`; keep machine-specific provider/model mappings in the private repository.
- Never place credentials, authentication tokens, private keys, or `auth.json` in Git, including private Git.
- Before a Git mutation whose repository scope is not obvious, verify the target with `git rev-parse --show-toplevel`.
- When changing shared OpenCode configuration or documentation, use `config/opencode/README.md` as the subsystem entry point.
- When changing the OpenCode source fork, follow the maintenance documentation inside `opencode/`; root-repository policy does not replace source-repository policy.
