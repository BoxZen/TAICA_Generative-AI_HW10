# 簡報工作流節點 1：檢索 Wiki 來源清單與覆蓋率評估

本文件記錄教學型簡報從 Wiki 知識庫中檢索之所有相關頁面與核心知識點，作為後續抽取證據卡（Evidence Cards）與規劃教學大綱的依據。

---

## 1. 覆蓋率關卡檢查結果
- **關卡要求門檻**：至少檢索到 3 篇以上相關 Wiki 概念頁。
- **實際檢索成果**：共檢索到 **11 篇核心概念頁**、**4 篇綜合比較頁** 與 **7 篇原始文獻摘要**。
- **關卡判定**：✅ **覆蓋率充分（11 / 3），通過覆蓋率關卡，准予進入節點 2**。

---

## 2. 檢索頁面清單與核心重點摘要

### (1) 基礎效能與度量衡模組
1. `wiki/concepts/time-complexity.md`
   - **核心重點**：時間複雜度定義、漸近分析、大 O 符號上界本質、常數與低階項化簡法則、對數換底常數忽略、常見複雜度排序 $O(1) \sim O(n!)$。
2. `wiki/concepts/algorithm-timeout.md`
   - **核心重點**：線上評判平台 1 秒時限機制、CPU 理論時脈與實測 $10^7 \sim 10^8$ 次/秒 運算基準、數據規模 $n$ 反推複雜度安全上限表。
3. `wiki/concepts/space-complexity.md`
   - **核心重點**：空間複雜度定義、排除可執行檔磁碟體積誤區、非精確位元組特性、記憶體限制（MLE）、$O(1)$ 到 $O(n)$ 實例。
4. `wiki/concepts/memory-management.md`
   - **核心重點**：C++ 執行期 Text/Data/Stack/Heap 分區、基本型態位元組大小、CPU 對齊步長與編譯器 Padding 填充機制。

### (2) 遞迴與結構思維模組
5. `wiki/concepts/recursive-complexity.md`
   - **核心重點**：遞迴時間核心公式（遞迴次數 $\times$ 單次操作）、遞迴空間核心定律（樹的最大深度）、快速冪 $x^n$ 三種遞迴寫法、斐波那契指數級 $O(2^n)$ 遞迴樹分析。
6. `wiki/concepts/recursion-and-iteration.md`
   - **核心重點**：自頂向下 vs 自底向上、呼叫堆疊開銷、Stack Overflow 崩潰風險、二分搜尋遞迴 $O(\log n)$ 與迭代 $O(1)$ 空間對比。

### (3) 經典演算法設計典範模組
7. `wiki/concepts/incremental-method.md`
   - **核心重點**：化整為零、單步累積、選擇排序法、單遍掃描與原地交換節省記憶體。
8. `wiki/concepts/memoization.md`
   - **核心重點**：以空間換取時間、即時查表（Tabulation）與預先計算（Precomputation）、計數排序法線性複雜度。
9. `wiki/concepts/divide-and-conquer.md`
   - **核心重點**：分割、克服、合併三步曲、子問題互相獨立性前提、二分搜尋與快速冪的分治模型。
10. `wiki/concepts/dynamic-programming.md`
    - **核心重點**：分治法輔以記憶法、重疊子問題與最佳子結構、自頂向下記憶化與自底向上表格法、斐波那契 $O(2^n) \to O(n)$ 降維奇蹟。
11. `wiki/concepts/greedy-algorithm.md`
    - **核心重點**：局部最佳決策、貪婪選擇性質與最佳子結構、極致速度與空間節省、非標準找零失效陷阱。

### (4) 綜合決策與對比模組
12. `wiki/syntheses/dp-vs-greedy.md`
    - **核心重點**：全域最優決策 vs 局部貪婪推進、硬幣找零對照案例、貪婪性質數學證明指引。
13. `wiki/syntheses/recursion-vs-iteration.md`
    - **核心重點**：時空複雜度、呼叫堆疊深層風險、工程選型分水嶺。
14. `wiki/syntheses/time-space-tradeoff.md`
    - **核心重點**：以空間換時間（DP、計數排序）vs 以時間換空間（原地對調、DP 狀態壓縮）。
15. `wiki/syntheses/algorithm-design-strategies.md`
    - **核心重點**：全景決策流程圖、資料規模 $n$ 避坑選型對照表。
