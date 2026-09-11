# Repository Navigation

`../SKILL.md` owns the core authority, placement, and change-impact contract; this file handles navigation methods only.

Use this reference for repository/subsystem entry points, source-of-truth discovery, directory navigation, forwarding locations, and nested-repository boundaries. It answers how an unfamiliar agent reliably finds the natural owner; it does not decide source-module or service architecture.

## Separate navigation from placement

Placement decides who owns information. Navigation decides how a consumer reaches that owner from a known entry. Correct placement does not guarantee discoverability, and navigation convenience does not justify duplicating authority.

## Repository and subsystem entries

An entry should state purpose, scope, responsibility boundary, and natural next locations rather than reproducing a complete file tree. Each navigation item should say when to enter it, what root the path is relative to, and what authority/evidence is expected there.

A subsystem layer should exist only for independent scope, lifecycle, maintenance responsibility, or navigation value. If an intermediate layer merely forwards to another layer without new decision value, merge or remove it.

## Source-of-truth discovery

When similar files, mirrors, generated artifacts, or historical copies coexist, navigation must identify current authority. Do not use "looks newest", directory height, or modification time as the sole authority test.

A mirror may appear in navigation only with a clear authoritative/derived relation so agents do not maintain the mirror backward as authority.

## Nested repositories

State which repository owns each path, which configuration/docs are shared versus repository/environment-specific, whether cross-repository links are reachable by the recipient, and whether edit authorization crosses repository boundaries.

Adjacency, nesting, parent ignore rules, and matching filenames do not prove shared Git history, authority, or authorization.

## Navigation changes

When an entry or owner moves, update actual navigation dependents. Keep only minimal forwarding information at the old location when it still improves discovery; do not leave a second current policy.

Navigation changes can also trigger placement, runtime-loading, and change-impact references.
