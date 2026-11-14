# 演算法 LLM Wiki 全站總目錄

歡迎查閱演算法主題 LLM Wiki。本知識庫作為教學型簡報與演算法知識的唯一可信來源，所有內容均嚴格基於收錄之原始資料（`raw/`）編譯而成。

---

## 1. 總覽 (Overview)
- [演算法 LLM Wiki 全站總覽](overview.md)：全站知識架構總覽、單向事實防線說明與初學者演算法五站式學習地圖。

---

## 2. 原始資料摘要 (Sources)
- [原始資料摘要：時間複雜度](sources/01-time-complexity.md)：解析漸近時間複雜度與大 O 符號的本質，建立複雜度增長等級排序。
- [原始資料摘要：演算法超時與運算效能](sources/02-algorithm-timeout.md)：以硬體運算基準建立 1 秒內約 $10^7 \sim 10^8$ 次操作的安全資料規模邊界。
- [原始資料摘要：遞迴演算法的時間複雜度](sources/03-recursive-time-complexity.md)：透過快速冪問題揭示「遞迴次數 $\times$ 單次操作」的計算核心與二分拆解陷阱。
- [原始資料摘要：空間複雜度分析](sources/04-space-complexity.md)：釐清執行期動態記憶體開銷與二進位執行檔體積的本質差別。
- [原始資料摘要：遞迴演算法時空複雜度深度分析](sources/05-recursive-complexity-analysis.md)：以斐波那契數列與二分搜尋剖析遞迴樹節點總數（時間）與最大深度（空間）。
- [原始資料摘要：程式記憶體消耗與底層管理](sources/06-memory-consumption.md)：解析 C++ 記憶體四分區、資料型態大小與硬體記憶體對齊規則。
- [原始資料摘要：演算法設計典範與思維策略](sources/07-algorithm-design.md)：師大資工經典演算法設計策略總覽，涵蓋遞增、枚舉、分治、DP 與貪婪法。

---

## 3. 核心概念 (Concepts)
- [時間複雜度與大 O 標記](concepts/time-complexity.md)：演算法操作次數隨輸入規模 $n$ 增長的漸近走勢評估與化簡原則。
- [超時判定與電腦運算能力估算](concepts/algorithm-timeout.md)：現代評測系統 1 秒極限與根據輸入規模 $n$ 反推演算法複雜度指南。
- [空間複雜度分析](concepts/space-complexity.md)：衡量演算法執行期額外動態記憶體配置的漸近量度與常見誤區。
- [遞迴複雜度分析](concepts/recursive-complexity.md)：將自我呼叫視覺化為遞迴樹，計算總節點數與呼叫堆疊最大深度。
- [程式記憶體配置與對齊](concepts/memory-management.md)：探討堆疊與堆積架構、資料型態長度與 CPU 對齊填充機制。
- [遞增法](concepts/incremental-method.md)：化整為零、逐一納入元素更新狀態的單步推進策略。
- [記憶化與預先計算](concepts/memoization.md)：以空間換取時間，透過即時查表或常數預建表格消除重複計算。
- [分治法](concepts/divide-and-conquer.md)：將大問題分割為互相獨立的子問題，各個擊破後縫合解答。
- [動態規劃](concepts/dynamic-programming.md)：分治法輔以記憶法，專治重疊子問題並確保全域最優解。
- [貪婪演算法](concepts/greedy-algorithm.md)：每一步做出局部最優決策，追求極致速度並探討貪婪選擇性質。
- [遞迴法與迭代法](concepts/recursion-and-iteration.md)：對比自頂向下展開與自底向上迴圈推進的效能與堆疊開銷。

---

## 4. 綜合比較 (Syntheses)
- [動態規劃 vs 貪婪演算法](syntheses/dp-vs-greedy.md)：全域最佳與局部貪婪的決策機制對比、找零問題案例與選型原則。
- [遞迴法 vs 迭代法](syntheses/recursion-vs-iteration.md)：呼叫堆疊開銷、執行效率與 Stack Overflow 風險深度對比。
- [時間與空間的權衡藝術](syntheses/time-space-tradeoff.md)：探討以空間換取時間的典型應用與極致狀態壓縮技巧。
- [常見演算法設計典範選擇指南](syntheses/algorithm-design-strategies.md)：全景決策流程圖、策略適用邊界與資料規模對照速查表。
