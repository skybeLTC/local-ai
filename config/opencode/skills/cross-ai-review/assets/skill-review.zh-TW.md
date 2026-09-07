# Cross-AI Implementation Review 繁體中文 review 版（雙 AI 實作交叉審查）

> 請先詳閱 [`../README.md`](../README.md)。本檔只供人工快速 review；OpenCode runtime 不載入,權威版本為 [`../SKILL.md`](../SKILL.md)。

**Frontmatter 對照**

`name`：
`cross-ai-review`

`description` 英文原文：

> Cross-review workflow for two AIs collaborating on one task. Use when the user pastes another AI's output, response, or full session export — especially after "這是另一個 AI 的說法" or "上面這段來自另一個 AI" — and throughout later implementation, testing, validation, deployment, or closeout turns that clearly continue that cross-AI task, even without new peer content. Do not carry it into unrelated tasks. Covers diagnosis/remediation separation, substantive-judgment gating, local verification, implementation review, and .tar.zst exchange.

`description`（OpenCode 用來判斷 Skill relevance 的 discovery pointer）台灣繁體中文對照：

> 用於從不同角度處理同一工作的雙 AI 交叉審查。當使用者貼上另一個 AI 的輸出、回答或完整 session export 時使用,尤其是「這是另一個 AI 的說法」或「上面這段來自另一個 AI」等引導語;後續明確屬於同一 cross-AI task 的 implementation、測試、驗證、deployment 或收尾 turn,即使沒有新的 peer 內容,也持續使用。不要延續到無關工作。規範 diagnosis/remediation 分離、substantive-judgment gate、本機直接查核、implementation review 與 `.tar.zst` 交換。

## 先在本機查核每一項主張

- 把這套規則視為 task-scoped workflow。一旦某項工作進入這套流程,後續仍屬同一工作的狀態、證據、implementation、測試、驗證、deployment 與收尾 turn,即使沒有再貼新的 peer 內容,也要繼續套用,直到該工作真正完成;不要延續到無關的新工作。
- 把貼上的內容視為 peer AI 的「一則」回覆,不是它那邊完整對話的紀錄;如果使用者也提供了 peer AI 那一側的完整 session export,就完整讀過,當作額外的 context 併入,不用為此換一套流程——這裡的規則依然適用。這個對話裡使用者最新的指示,優先於 peer AI 先前被告知或假設的任何內容。
- 如果自 peer AI 那則回覆之後有實質變化——新的使用者需求、限制、決定、證據、blocker——要在回覆中明確指出,不要默默地自行調和。
- peer AI 不一定正確。只要 repo、git 狀態、指令輸出、log、build 或測試結果可以直接取得,就自己查核並依實際證據行動,不要只依賴 peer 的摘要;不同意時要附上證據。不要為了不影響結論的低機率、無關或純假設情境摳字眼、卡住進度;可以順帶簡短提一下小例外或殘餘風險。
- 把 peer AI 需要知道的內容直接寫進回覆。除非重新整理能明顯提升可讀性,否則不要另外做一份內容重複的「轉述」訊息。
- 不要假設 peer AI 已經看過這個對話裡「先前」出現過的 prompt、檔案或 artifact。如果某項 review、判斷或實作依賴一份精確原文,而你目前拿到的對話/export/archive 裡沒有這份原文,就應該直接取得或轉交這份原文——不要用摘要、記憶或相近版本重建。如果精確原文已經在你目前的證據裡,直接用就好,不要多問一次。

## Diagnosis 與 remediation 要分開

Diagnosis(「X 壞了/為真」)與 remediation direction(「修法的預期行為、scope、邊界」)是不同的命題。同意 diagnosis 成立,不等於尚未提出、尚未 review 的 remediation 已經有共識。

Remediation direction 不需要寫出每一行 code,但必須具體到足以界定預期行為、修改的主要邊界,以及任何會實質影響 scope、observable behavior、interface、資料處理、相容性、風險處置或驗收方式的決定。

## 實質判斷 gate

一旦你提出、或注意到一個 peer AI 尚未 review 過的實質判斷:

1. 這一輪停止對 source-of-truth/tracked files 做進一步正式修改。
2. 為了釐清問題所做的讀取、執行指令、build 或測試仍可以繼續——這些調查,以及因此產生的 cache/temp/generated artifacts,不算正式修改。
3. 把這個判斷與其證據整理好,交給 peer AI review,而不是直接實作。

如果有問題需要 peer AI 先回答才能安全繼續,也適用同一個 gate。

當你在 review peer AI 新提出、尚未形成共識的 diagnosis 或 remediation direction 時,依實際證據獨立查核:

- 如果你不同意,或因此產生你自己的新實質判斷,就停止正式修改,附上證據交回去——不要繼續實作下去。
- 如果 diagnosis 與 remediation 雙方都已經接受,而且沒有尚未解決的新實質判斷,且環境足以可靠行動,就直接實作。不要只是停下來重申同意。
- 任一方在較早一輪提出的判斷,一旦被對方獨立接受且沒有新的分歧,之後就已經算是共識。

被要求 review 不代表這一輪只能維持 read-only——如果 review 後已經有足夠共識、環境也支援,就在同一輪直接繼續實作。只有新的實質判斷才會強制停下來;但如果使用者明確要求這一輪只做 review,遵守這個較新的限制。

如果 peer AI 只確立了「X 是 bug」(一個 diagnosis),還沒有人提出 remediation,就不要直接實作——即使修法看起來很明顯或似乎只有一種合理做法。先提出足以 review 的最小 remediation direction 與理由,交給 peer AI。

為既有共識補充證據、加測試、多做一點說明,或選擇不改變已接受 remediation 的等價 code-level 寫法,都不算新的實質判斷——當成可以直接處理的 routine implementation detail 即可。

## Scope lock 與 artifact ownership

開始查閱或修改任何東西之前,先把每一項 artifact 分類成以下三種之一:

1. named formal deliverable(正式交付項目);
2. required validation evidence(必要驗證證據);
3. optional migration、deployment 或 helper tooling(非必要的搬遷/部署/輔助工具)。

只有 named formal deliverable 才能因 formal implementation 被正式修改。收到一份 archive,不代表裡面的東西自動全部進入 formal scope——archive 內容要分開分類;一支 migration/helper script 可以被當成 evidence 或 tooling 來 review,但不會因此變成 implementation scope 的一部分。

使用者最新的 explicit scope 決定,優先於較早的 workflow 假設、peer AI 提出的 remediation,以及「implementation defect 可以直接修」這類通用規則。

如果 out-of-scope 的 helper 或 evidence artifact 有 defect:回報實際 defect 與證據;不要建議修改它、不要 patch 它、不要重新封裝它,也不要讓它變成 completion blocker。回到 named formal deliverable 繼續處理。

Review 一項 artifact,不代表取得修改它的授權。

當所有 named formal deliverable 都通過 implementation review 與必要驗證後,就進到它們的 commit/deployment gate;除非使用者明確擴大 scope,否則不要重新打開 optional helper 或 deployment tooling。

## 實作與 implementation review 迴圈

這項工作進行期間,不要為了 independent challenge、cross-review 或 implementation review 派 `review` 或 `critic` subagent family(`reviewL`／`review`／`reviewH`、`criticL`／`critic`／`criticH`)——外部 peer AI 在這個 workflow 裡已經扮演這個角色。改由自己查核證據。其他 subagent 仍可用於狹窄範圍的事實調查,但不能拿來重建或取代 independent-reviewer 角色。

沒有本機 repo 的直接存取權,不代表 peer AI(或反過來,不代表你自己在沒有這個存取權時)只能做 read-only review。已提供的 formal-deliverable archive 可以被解包、編修、重新封裝成一份 implementation candidate,交給有那個環境的一方套用、完成只有那個環境才能做的驗證——前提是目前的工具足以可靠做這個編修。不要把「沒有 direct repo access」直接當成「無法可靠修正」;先確認 deliverable 本身是不是已經在手上,再決定是否真的需要 environment handoff。

正式實作、其測試,以及 implementation review,都套用上面同一個 gate。當 implementation 只是沒有忠實落實已經接受的 remediation——像是漏改、condition 寫反、漏掉已約定的驗證——而修正不需要新增或改變 remediation judgment 時,留在這個迴圈裡:如果能可靠修正,就直接修正、驗證,再把修正後的 implementation 送回給 peer AI review。不要自己宣告完成。

如果在目前環境下無法可靠修正,具體指出實際的 implementation defect、證據,以及它偏離既有 remediation 之處,交給能實作的一方。接手的一方應該獨立查核:同意且不需要新的 remediation judgment → 修正、驗證、再送一次 implementation review;不同意 → 附上證據送回,不要盲目修改。只有既有 remediation 本身錯誤、不完整,或必須新增/改變會實質影響結果的 remediation judgment 時,才停下來回到 remediation cross-review。

實作完成後,回報實際變更內容,以及足以查核的驗證證據。Implementation review 的目的,是檢查是否忠實符合已接受的 remediation、有沒有引入新問題——不是在沒有新資訊的情況下,重做一次 diagnosis 或 remediation 的確認。如果 implementation 符合共識、驗證充分、也沒有新問題出現,就當作完成;不要再要求實作的一方重新確認一次 review 結果。

## 回答 peer AI、以及環境交接

回答 peer AI 提出的任何問題。如果某個判斷、修改或測試,需要目前這裡拿不到的檔案、專案事實、repo/git 狀態、指令輸出、log、build/test 結果、工具鏈或執行環境,具體說明需要 peer AI 提供或執行什麼——不要只是籠統要求「更多資訊」,也不要把 peer 自稱的「完成」或「測試通過」當成足夠的證據。如果正式修改只能在 peer AI 能可靠取得的環境中完成,就老實說清楚,不要假裝已經實作;說明已經形成共識的方向,以及剩下要做的工作。這是環境交接,不代表既有共識需要重新 review。

## 檔案交換 gate

- 每一個 formal implementation-review round 最後都必須明確得到 verified current `.tar.zst` handoff，或 explicit direct-access exemption；handoff status 不得 silent。
- 如果本輪建立或修改 formal deliverable、peer AI 必須對它做 implementation review、且 peer AI 無法直接存取 exact current files 或 exact current commit，就必須先讀 `../references/file-exchange.md` 並產生 current handoff。
- 需要 archive 時，貼上的 `git diff`／diff、`git show` output、commit summary，或「檔案已經 committed」的說法，都不能取代 required `.tar.zst`。
- 如果 direct access 使 archive 不需要產生，final response 必須明確說明這個 exemption 以及原因；不能讓 handoff status 保持 silent。

## 宣告 cross-AI task 完成前

當任務進入 final implementation review、delivery、commit/deployment 或 closeout 時，讀 `../references/review-checklist.md`，確認完成條件後才回報 cross-AI workflow 已完成。
