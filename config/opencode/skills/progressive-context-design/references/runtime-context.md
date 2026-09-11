# Runtime Context, Reachability, and Reference Routing

Use this reference for runtime-loaded instructions, skills, reference triggers, guaranteed reachability, and progressive loading. `../SKILL.md` owns the minimum obligations; this file owns loading topology and validation method.

## Separate execution platform from receiving platform

Record the current execution platform, receiving platform, artifact type, available tools, and the receiver's actual loading mechanism. Authoring in one environment does not imply the target repository, OpenCode runtime, or user machine has the same tools, files, or permissions.

## Loading layers

| Layer | Question it must answer |
| --- | --- |
| skill ID/name/description or equivalent selection metadata | Should this method be selected for the task? |
| guaranteed runtime entry | What minimum behavior, boundary, stop condition, and deeper trigger must always be known? |
| triggered reference | How is this branch executed correctly, including exceptions and validation? |
| README/rationale/maintenance background | Why is the design this way and how is it maintained? |

Keep short always-needed rules in the guaranteed entry. Do not hide mandatory behavior behind paths the agent must guess, and do not infer automatic loading from special-looking filenames.

## OpenCode-specific loading evidence

For OpenCode, distinguish skill advertisement/discovery, permission, skill-body loading, supporting-file path advertisement, and actual reference-content reading. A supporting file appearing in a sampled file list does not prove its contents were read.

Treat `AGENTS.md` or another instruction file as guaranteed only when the effective OpenCode version, working-directory/project lookup, config, or other runtime evidence establishes that it is loaded for the relevant task. Do not infer nested `AGENTS.md` loading solely from path nesting.

## Guaranteed reachability

Mandatory local information requires a complete path:

`guaranteed entry -> observable trigger/routing condition -> exact target -> read-before decision/action`.

File existence and README links do not establish reachability. If the platform does not automatically load nested instructions, use a routing mechanism that the actual platform supports.

## Reference-trigger contract

Every execution reference needs:

1. an observable trigger from task/artifact/state;
2. an exact resolvable relative path;
3. a read-before point;
4. a content boundary sufficient to include constraints and exceptions that can change the action;
5. missing/inaccessible behavior.

A filename, directory listing, title, or search hit is not evidence that required content was read.

## Splitting must not disconnect capability

Before moving a method into a reference, map the original observable condition, how the runtime entry recognizes it after the split, when the reference is read, and what happens if it is unavailable.

A trigger such as "when needed" or "if useful" is not sufficient when the method can change behavior. Fix routing or cancel the split. Do not create forwarding-only reference chains without independent information value.

## Multiple references may trigger together

Reference triggers are not a mutually exclusive menu. Documentation, placement, runtime loading, and change impact can all apply to one task. Read every required reference before its dependent decision. If one judgment is a prerequisite for another, follow dependency order; when no dependency exists, the required references may be loaded in the same stage.

## Reread when context changes

Previously read content may be reused only while it remains in context, is unchanged, and the triggering conditions remain the same. Reread when the reference/version changes, necessary content leaves context, a new branch becomes active, or target platform/artifact/scope changes.

## Validate loading topology proportionately

Choose cases according to the changed behavior: a clear trigger, a nearby case that should stop before an unrelated deeper reference, simultaneous triggers, uncertain trigger applicability, missing/denied required reference, and version/context changes when relevant.

Evidence must show the required reference was read before the dependent judgment and unrelated references were not unconditionally preloaded. If the runtime cannot expose actual loading, report the validation gap; static topology is not runtime-loading proof.
