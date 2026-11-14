# 核心概念：動態規劃 (Dynamic Programming)

---

## 1. 一句話白話定義（初學者生活化類比）
**動態規劃就像是「用一張表格隨時記錄爬樓梯的最佳路線」，每踏上一階新台階，都直接利用前面台階算好的最少步數累加，絕不浪費時間回頭重複走冤枉路。**  
動態規劃（Dynamic Programming, DP）本質上就是**「分治法輔以記憶法」**。當分治法拆解出來的子問題一而再、再而三重複出現時，運用記憶表儲存這些問題的解答，避免重複求解，以空間換取時間 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與兩大黃金性質
一個問題能採用動態規劃解決，必須具備以下兩大關鍵性質：
1. **重疊子問題（Overlapping Subproblems）**：  
   在問題遞迴分解的過程中，相同的子問題會被重複調用多次（例如計算 $fib(5)$ 需要 $fib(3)$，計算 $fib(4)$ 同樣需要 $fib(3)$）[來源: raw/05-recursive-complexity-analysis.md §时间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
2. **最佳子結構（Optimal Substructure）**：  
   大問題的全局最佳解，可以嚴格由局部子問題的最佳解組合推導而得 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

### 實作路徑兩大分支：
- **自頂向下記憶化搜尋（Top-Down Memoization）**：保留遞迴外觀，但在進入計算前先查表，若已有答案則直接返回 [來源: raw/07-algorithm-design.md §memoization | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **自底向上動態規劃表格（Bottom-Up Tabulation）**：利用迴圈由最小規模的已知基底出發（如 `dp[0], dp[1]`），依序遞推填滿表格 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 3. 典型演算法與時空複雜度分析

### 斐波那契數列效能躍遷對比：
- **純樹狀遞迴**：
  時間複雜度 $O(2^n)$，空間複雜度 $O(n)$（呼叫堆疊）[來源: raw/05-recursive-complexity-analysis.md §时间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
- **動態規劃表格化（DP Array）**：
  ```cpp
  int dp[n + 1];
  dp[0] = 0; dp[1] = 1;
  for (int i = 2; i <= n; i++)
      dp[i] = dp[i - 1] + dp[i - 2];
  ```
  - 時間複雜度：單層迴圈迭代 $n$ 次，大幅驟降至 **$O(n)$** [來源: raw/05-recursive-complexity-analysis.md §时间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
  - 空間複雜度：配置大小為 $n$ 的表格，空間為 **$O(n)$**；若進行「滾動變數空間壓縮」，僅維護前兩項數值，空間可進一步降至 **$O(1)$** [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

---

## 4. 適用場景與常見誤區
- **適用場景**：存在重疊子結構的最值問題（如最短路徑、背包問題、最長共同子序列）[來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **與貪婪演算法的本質差別**：  
  貪婪法每一步只盲目挑選當下最好的選擇，不作回溯或全面權衡；而動態規劃會完整記錄與評估所有可能的子狀態轉移，確保最終獲得全局全域最優解 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 5. 關聯主題與延伸閱讀
- [分治法 (Divide-and-Conquer Method)](divide-and-conquer.md)
- [記憶化 (Memoization)](memoization.md)
- [貪婪演算法 (Greedy Method)](greedy-algorithm.md)
- [動態規劃 vs 貪婪演算法比較](../syntheses/dp-vs-greedy.md)
- [時間與空間權衡](../syntheses/time-space-tradeoff.md)
- [原始文獻摘要: 07-algorithm-design](../sources/07-algorithm-design.md)
