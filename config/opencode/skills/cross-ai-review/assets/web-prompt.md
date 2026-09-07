<!--
這份檔案是給「使用者」貼到另一個 AI(通常沒有 direct local repo/source-of-truth access 的 web 版 AI,例如瀏覽器聊天視窗)用的可攜式 prompt。
OpenCode 不會載入、解析或執行這個檔案。

用法:
1. 把下方「貼上區塊開始」到「貼上區塊結束」之間的內容,連同你與本機端 AI 的完整對話 export(建議雙方訊息都包含,不要只截另一個 AI 最後一則回答),一起貼給另一個 AI。
2. 之後若有 export 裡沒有、且會實質影響後續工作的新需求、限制、決定或證據,在這段之後另外用文字補充即可,不需要重貼一次完整 prompt。
3. 如果有要提供的正式檔案、patch、log 或其他測試證據,依下方檔案交換規則封裝成 `.tar.zst` 後一併上傳,讓它可以直接查核實際內容,而不是只憑摘要判斷。
-->

<!-- 貼上區塊開始 -->

這是我與另一個 AI 的對話 export。請閱讀我和另一個 AI 雙方的完整內容,而不是只看另一個 AI 最後一則回答,並據此了解目前需求、討論脈絡、既有判斷、實作及測試結果。

你可以把 export 內的 user messages 與 AI responses 視為目前已知 context。若我另外補充了 export 中沒有、且會實質影響另一個 AI 後續工作的需求、限制、決定、證據或其他重要資訊,請在回答中明確帶出。我的較新需求、限制或決定優先於較早內容。

需要另一個 AI review 或知道的判斷、證據、問題或實作結果,直接寫在回答中即可;不要另外重複整理一份內容相同的 relay message,除非另行整理能明顯提升可讀性。

另一個 AI 不一定正確。若目前已提供相關專案、檔案、artifact、patch、程式碼、repo 或 git 狀態、指令輸出、log、build、測試結果或其他可查核內容,請直接檢查實際內容,不要只根據另一個 AI 的摘要推測。若要反駁,請提供可驗證的依據。不要摳字眼,也不要用不影響結論的低機率、無關或過度假設情境阻礙進度;小例外、額外證據或風險可以順帶說明。

不要假設另一個 AI 已經看過目前這個對話中曾出現的 prompt、檔案或 artifact。若 review、判斷或實作依賴某份精確原文,而目前提供的 export、附件或 archive 沒有包含它,請明確要求取得原文;若你這一端持有而另一端沒有,則在需要交叉 review 時直接帶出原文,或依檔案交換規則封裝。不要用摘要、記憶或相近版本重建精確 artifact。若精確原文已經在目前提供的 export 或附件裡,直接使用,不要多問一次。

我希望你和另一個 AI 對每一個會實質改變 implementation 的新判斷進行交叉 review。Diagnosis 與 remediation direction 是不同的命題;同意問題成立只代表 diagnosis consensus,不代表尚未提出及 review 的 remediation 已有共識。Remediation direction 不必規定每一行 code,但必須足以界定預期行為、主要修改邊界,以及會實質影響 scope、observable behavior、interface、資料處理、相容性、風險處置或驗收方式的決定。

開始查核或提出修改建議之前,請先把每一項 artifact 分成三類:named formal deliverable(正式交付項目)、required validation evidence(必要驗證證據),以及 optional migration、deployment 或 helper tooling(非必要的搬遷/部署/輔助工具)。只有 named formal deliverable 才能被正式修改。我提供給你的 archive,不代表裡面的東西全部自動算進 formal scope——archive 內容要分開分類;一支 migration/helper script 可以被你當成 evidence 或 tooling 來 review,但不會因此變成 implementation scope 的一部分。我最新的 explicit scope 決定,優先於較早的 workflow 假設、另一個 AI 提出的 remediation,以及「implementation defect 可以直接修」這類通用規則。如果你發現 out-of-scope 的 helper 或 evidence artifact 有 defect:回報實際 defect 與證據;不要直接建議修改它、不要要求重新封裝它,也不要把它當成 completion blocker,回到 named formal deliverable 繼續處理。Review 一項 artifact,不代表你取得修改它的授權。當所有 named formal deliverable 都通過 implementation review 與驗證後,就回到它們的 commit/deployment gate;除非我明確擴大 scope,否則不要重新打開 optional helper 或 deployment tooling。

一旦確認出現尚未經另一個 AI review 的新實質判斷,這一輪就停止所有進一步的正式修改,不再改動 source-of-truth 或 tracked source files,整理判斷與證據後交另一個 AI review。仍可繼續為了把問題查清楚所必要的查閱、分析、測試或其他不構成正式實作的驗證;這些查證自然產生的 cache、temporary files 或 generated artifacts 不算正式修改。如果有會實質影響後續工作的問題必須先由另一個 AI 回答,也適用同一規則。

當你正在 review 另一個 AI 新提出、尚未形成共識的 diagnosis 或 remediation direction 時,請獨立查核。若不同意,或產生新的實質判斷,就停止正式修改並交另一個 AI review。若所需的 diagnosis 與 remediation 都已由雙方 review 並接受,而且沒有新的實質判斷,只要目前檔案與環境足以可靠實作,就直接修改、測試與驗證,不要只回覆「我同意」後再做一次純確認。上一輪若是你提出其中一項判斷,另一個 AI 已獨立接受且沒有新分歧,該命題也已形成共識;是否能正式實作,仍以所需 diagnosis 與 remediation 是否都已有共識為準。

單純要求你 review,不代表這一輪只能評論。若 review 後形成足夠共識,而且目前條件足以可靠實作,就在同一輪繼續 implementation。只有 review 產生新的實質判斷時才因 protocol 停止;但如果我明確要求本輪僅限 review、禁止修改或不要產出 implementation,請遵守這個較新的限制。

如果另一個 AI 只提出「X 是 bug」,你也同意 X,但尚未有人提出 remediation direction,即使你認為修法很 obvious、很簡單或只有一種合理方向,也不能直接正式實作。請先提出最低限度但足以 review 的 remediation direction 與理由,交另一個 AI review。

增加支持相同結論的證據、補充測試、進一步解釋理由,或選擇不改變既有共識的等價 code-level 寫法,不算新的實質判斷。只要不需要新增或改變尚未 cross-review 的 remediation judgment,就屬於 routine implementation detail,可以直接處理。

正式實作、測試與 implementation review 都使用同一個 substantive-judgment gate。如果 implementation 只是沒有忠實完成既有 remediation,例如漏改、condition 寫反或漏掉已約定的 validation,而修正不需要新增或改變實質 remediation judgment,就留在 implementation／implementation-review loop。若目前有足夠檔案與可靠環境,直接修正並驗證,再把修正後的 implementation 交另一個 AI review,不要自行宣告 DONE。

如果目前不能可靠修改,請具體指出 implementation defect、證據以及偏離既有共識之處,交給能實作的一方。接手方應獨立查核;若同意且不需要新的 remediation judgment,就修正、驗證並再次送 implementation review;若不同意,請附上證據交回,不要盲目修改。只有既有 remediation 本身錯誤、不完整,或必須新增或改變會實質影響結果的 remediation judgment 時,才停止所有進一步正式修改並回到 remediation cross-review。

你沒有 direct local repo/source-of-truth access,不代表你只能做 read-only review。如果 named formal deliverable 已經透過附件或 `.tar.zst` 提供給你,而且你目前的工具足以可靠編修,就直接解包、修改工作副本、完成你這邊能做的初步驗證,再重新封裝 `.tar.zst`,交給有本機環境的一端套用並完成只有那個環境才能做的驗證。不要只因為沒有 direct repo access 就直接跳到下面這種 environment handoff——先確認 deliverable 本身是不是已經在你手上。只有真正缺少必要檔案、project state、驗證證據,或修改/驗證確實依賴你這裡拿不到的 repo/git 狀態、工具鏈或執行環境時,才需要具體指出缺什麼,請對方依檔案交換規則補上。

完成實作後,請提供實際修改內容與足以查核的驗證結果。Implementation review 的目的,是檢查 implementation 是否忠實符合既有共識以及是否引入新問題,不是重新做沒有資訊增量的 diagnosis 或 remediation confirmation。若 implementation 正確符合共識、驗證足夠且沒有新問題,就直接進入 DONE,不要再要求實作者確認一次 review 結果。

如果另一個 AI 有問問題,請回答。若判斷、修改或測試需要目前無法取得的檔案、專案資訊、repo 或 git 狀態、指令輸出、log、build、測試結果、工具鏈或執行環境,請具體說明需要另一個 AI 提供或執行什麼,不要只籠統要求更多資訊,也不要把「已完成」或「測試通過」當成足夠證據。若正式修改只能在另一個 AI 能可靠取得的環境中完成,不要假裝已經實作;清楚說明已形成共識的方向與需要完成的工作。這是 environment handoff,不代表既有共識需要再次 review。

正式 implementation-review round 的 handoff gate 如下：

- 每一個 formal implementation-review round 最後都必須是 verified current `.tar.zst` handoff，或 explicit direct-access exemption；final response 不得對 handoff status silent。
- 如果本輪建立或修改 formal deliverable、peer AI 必須對它做 implementation review、且 peer AI 無法直接存取 exact current files 或 exact current commit，就必須產生 current `.tar.zst`。
- 在 required-exchange case，pasted diff、`git diff`、commit summary、`git show` output、commit hash，或「檔案已經 committed」的說法，都不能取代 `.tar.zst`。
- 如果 peer 確實可以直接 access 並 review exact current files 或 exact current commit，archive 可以不產生；但 final response 必須明確寫出：
  ```text
  Handoff archive: not required
  Reason: <why the peer has exact current direct access>
  ```
- diagnosis/remediation-only round 尚未有 formal implementation 時，不需要新的 archive。已有 archive 若包含 exact unchanged current formal deliverables，可以 reuse；但 formal deliverable 在 archive 建立後有任何變更，舊 archive 就是 stale，必須重新產生 current archive。

需要 file exchange 時一律使用 `.tar.zst`。如果環境不能可靠產生 `.tar.zst`，要明確說明 blocker，不要靜默替換格式。本輪為完成工作、正式修改、正式交付或提供必要 review 證據而新增或修改的檔案要封裝;另一個 AI 明確要求的檔案即使本輪未修改,也要依需求封裝。純調查、build 或 test 自動產生,而且未被要求、無須交付、不是正式實作必須更新的檔案,也不是必要 review 證據的 cache、temporary files 或 generated garbage 不要封裝;generated artifact 若是正式交付、正式實作需要更新、必要證據或被明確要求,仍要納入。

請先完成本輪依照上述規則能合理完成的工作,再交換檔案,不要在處理途中要求我轉交已修改檔案。封裝時保留必要相對路徑;若目前能存取工作區,將 `.tar.zst` 放在工作區根目錄,否則集中提供下載,並在回答最後提醒我要傳給另一個 AI review,同一句提醒要直接寫出實際檔名或路徑,不要只靠我往上翻才找得到是哪一份。如果我已提供另一個 AI 傳來的 archive,請直接使用;除非內容更新、另一個 AI 重新要求或本輪產生新修改,否則不要要求重傳同一份 `.tar.zst`。

<!-- 貼上區塊結束 -->
