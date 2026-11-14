# 原始資料摘要：演算法設計典範與思維策略 (Algorithm Design)

> **原始文章標題**：algorithm design - 演算法筆記  
> **原始連結**：https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/07-algorithm-design.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/07-algorithm-design.md)

---

## 1. 核心主題概述
本篇彙整臺灣師範大學資工系演算法筆記之「演算法設計（Algorithm Design）」經典教學文獻。系統化梳理了計算機科學中解決複雜問題的核心思維策略（Paradigms），從基礎的遞增、枚舉、記憶化，到分治法、動態規劃、貪婪法等，並提供了豐富的 C++ 程式碼範例與生活化哲理對照。

## 2. 涵蓋演算法與核心知識點
1. **遞增法（Incremental Method）**：
   - 「不積跬步，無以至千里」。循序處理資料，完成一步再做下一步，符合計算機一次執行一條指令的特性。
   - 範例：陣列累加求和、選擇排序法（Selection Sort）、單遍掃描找區間、就地對調數字以節省記憶體。
2. **記憶化（Memoization & Precomputation）**：
   - 「有備無患」。演算法執行中即時記錄或事前預先計算已知數值（Tabulation），以記憶體儲存換取運算速度。
   - 範例：字串長度暫存、統計字母與數字數量、計數排序法（Counting Sort）、迴圈展開（Loop Unrolling）。
3. **枚舉法（Enumeration）**：
   - 「愚者千慮，必有一得」。窮舉所有可能性並驗證。
   - 範例：平方數枚舉、循序搜尋（Sequential Search）、平面最近點對（Closest Pair）、區間和搜尋。
4. **回溯法（Backtracking）**：
   - 枚舉多維度數值的方法，透過樹狀走訪尋找滿足約束條件的解，遇到死胡同即回溯。
5. **迭代法（Iterative Method）與遞迴法（Recursive Method）**：
   - 迭代法：狀態由已知逐步向前推演（Bottom-Up），控制結構為迴圈，記憶體常數開銷。
   - 遞迴法：自我呼叫展開，將大問題推演至基底條件（Top-Down），依賴呼叫堆疊。
6. **分治法（Divide-and-Conquer Method）**：
   - 「凡治眾如治寡，分數是也」。將大問題分割為互相獨立且結構相同的子問題，分別求解後合併。
7. **動態規劃（Dynamic Programming, DP）**：
   - 「分治法輔以記憶法」。當分治法分割出來的子問題高度重疊、一再重複出現時，利用記憶法儲存答案，避免重複計算，以空間換取時間。
8. **貪婪演算法（Greedy Method）**：
   - 「今朝有酒今朝醉」。在每個決策點上只做出當下局部最佳（Locally Optimal）的選擇，期望以此逼近或達到全域最佳（Globally Optimal）解。

## 3. 重要演算法關係矩陣
- **分治法 + 記憶化 $\to$ 動態規劃（DP）**
- **遞增法 + 局部最佳評估 $\to$ 貪婪演算法（Greedy）**
- **枚舉法 + 深度優先搜尋 + 剪枝 $\to$ 回溯法（Backtracking）**

## 4. 關聯核心概念頁面
- [遞增法 (Incremental Method)](../concepts/incremental-method.md)
- [記憶化 (Memoization)](../concepts/memoization.md)
- [分治法 (Divide-and-Conquer Method)](../concepts/divide-and-conquer.md)
- [動態規劃 (Dynamic Programming)](../concepts/dynamic-programming.md)
- [貪婪演算法 (Greedy Method)](../concepts/greedy-algorithm.md)
- [遞迴法與迭代法 (Recursion and Iteration)](../concepts/recursion-and-iteration.md)
- [動態規劃 vs 貪婪演算法比較](../syntheses/dp-vs-greedy.md)
- [時間與空間權衡](../syntheses/time-space-tradeoff.md)
- [常見演算法設計典範選擇指南](../syntheses/algorithm-design-strategies.md)
