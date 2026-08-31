# local-ai Repository Rules

Apply these rules when working in the `~/local-ai` management repository.

- Treat `~/local-ai`, `~/local-ai/opencode`, and `~/local-ai/private` as separate Git repositories.
- Never stage or commit `opencode/` or `private/` into the root repository.
- Keep public shared behavior under `config/opencode/`; keep machine-specific provider/model mappings in the private repository.
- Never place credentials, authentication tokens, private keys, or `auth.json` in Git, including private Git.
- Before a Git mutation whose repository scope is not obvious, verify the target with `git rev-parse --show-toplevel`.
- When changing shared OpenCode configuration or documentation, use `config/opencode/README.md` as the subsystem entry point.
- When changing the OpenCode source fork, follow the maintenance documentation inside `opencode/`; root-repository policy does not replace source-repository policy.
