# Commit Message Guide

把 commit message 視為「一個 logical change 的 durable historical document」。

未來的 AI 或人類應該能快速判斷這個 change 是否應該：

- keep
- revert
- migrate
- cherry-pick
- replace
- 因 underlying need 已不存在而 drop

## Subject

描述 semantic result，不要只描述 migration mechanics。

偏好：

```text
feat(config): define provider-neutral OpenCode agent policy
feat(skills): add progressive context design guidance
docs(maintenance): document stable tag archive workflow
fix(command-guard): preserve native permission matching
```

避免：

```text
merge old config
copy files
migration changes
update stuff
```

只有 transition 本身就是 meaningful behavior 時，才讓 `merge` / `restore` / `migrate` 成為 subject 重點。

## Opening paragraph

第一段用最少文字回答：

- 這顆 commit 建立或改變了什麼？
- 為什麼需要？

讀者不應該先讀完整 bullet list 才知道目的。

## Deeper detail

只在有助於理解時加入 section，例如：

```text
Context:
Rationale:
Compatibility:
Validation:
Deferred:
```

不要為了模板完整而硬塞 heading。

## Rationale

保留 future maintainer 可能誤刪的 deliberate choice，例如：

- public/private responsibility boundary
- compatibility constraint
- 為什麼一個看似更簡單的 alternative 被拒絕
- 為什麼某項 integration 刻意 deferred
- 為什麼某設定屬於 machine profile 而不是 shared config

## Validation

只記錄真的執行過的驗證。

可以寫：

```text
- OpenCode loaded the home profile successfully.
- A real `generalL` subtask ran on the expected model and returned the expected smoke-test result.
```

不要沒有 evidence 就寫：

```text
fully tested
safe
works perfectly
```

## Current policy versus history

Commit message 回答：

> 為什麼這個 logical change 當初進入 history？

Current documentation 回答：

> 現在適用什麼？

如果一個 change 建立了 durable active rule，不能只把 rule 留在 commit message。

## Logical boundary

一顆 commit 應該能獨立被 review、revert、migrate 與 explain。

不要只因為同一個 session 做了很多事，就把無關 subsystem 塞成一顆 commit。
