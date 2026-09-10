# OpenCode satellites

這個目錄保存 OpenCode 周邊工具的 source checkout。每個子目錄都是**獨立的 Git repository**，不是 root repository 的 vendored content。

## Layout invariant

```text
~/local-ai/opencode-satellites/
├── README.md                   # tracked by the root repository
└── <satellite>/                # independent Git repository, ignored by the root repository
```

Root `.gitignore` 只保留這個 `README.md`，其餘 `opencode-satellites/` 下的內容一律排除：

```gitignore
/opencode-satellites/*
!/opencode-satellites/README.md
```

因此 root repository 永遠不會吸收 satellite 的 source、history、build output 或 working tree 狀態。

Core OpenCode 不是 satellite。它固定位於 `../opencode`，由它自己的 repository 與 release 流程負責，不放進這個目錄。

## Ownership boundary

- Root repository 只負責這個 layout 文件與 ignore rule。
- 每個 satellite 的 branch、commit、build、release 與 publication policy 由該 satellite 自己的 repository 與其 maintenance documentation 決定。
- Root repository 的 policy 不取代 satellite repository 的 policy；反之亦然。
- Credential 不屬於任何一層 Git，包含 satellite repository。

## Lifecycle authority

- 每個 satellite 自行追蹤它的 upstream；upstream 關係屬於該 satellite，不由 root repository 集中管理。
- baseline 優先採用 upstream 的官方 release，而不是任意 upstream commit。
- branch model：以 upstream release tag `vX.Y.Z` 為基礎，開出 `sky/vX.Y.Z` 作為該 release line 的本地 branch。
- 本地 delta 應保持小、generic、可 upstream；不放 machine-specific、帳號相關或不可公開的內容。
- upstream 出新 release 時，建立新的 release-line branch，並只重新套用仍然需要的 patch；已被 upstream 吸收或已不需要的 patch 不再帶入。
- 當 upstream 的支援已足夠時，satellite 可以退場；退場屬於正常結果，不是失敗。

## Rules

- 進入 satellite 目錄前，先用 `git rev-parse --show-toplevel` 確認 Git root，避免把 mutation 下在錯誤的 repository。
- 絕不把 satellite 的檔案 stage 或 commit 進 root repository。
- 新增 satellite 時，直接在這個目錄建立獨立 checkout；不需要修改 root `.gitignore`，既有 ignore rule 已涵蓋。
