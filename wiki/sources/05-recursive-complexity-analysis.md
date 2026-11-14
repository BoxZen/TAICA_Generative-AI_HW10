# 原始資料摘要：遞迴演算法時空複雜度深度分析

> **原始文章標題**：递归算法的时间与空间复杂度分析！  
> **原始連結**：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/05-recursive-complexity-analysis.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/05-recursive-complexity-analysis.md)

---

## 1. 核心主題概述
本篇透過兩大經典演算法案例——「求斐波那契數列（Fibonacci）」與「二分搜尋法（Binary Search）」，全方位剖析遞迴呼叫在「時間維度（遞迴樹節點總數）」與「空間維度（呼叫堆疊最大深度）」上的本質行為。

## 2. 涵蓋演算法與核心知識點
- **遞迴空間複雜度核心定律**：
  $$\text{遞迴演算法空間複雜度} = \text{遞迴樹的最大深度} \times \text{每次遞迴所需的輔助空間}$$
  因為電腦透過呼叫堆疊（Call Stack）保存每一層函數呼叫的區域變數與返回位址，同時存在於記憶體中的呼叫幀（Stack Frame）數量最多等於當前路徑的最大深度。
- **斐波那契數列遞迴效能剖析**：
  - **樹狀遞迴**：`fib(n) = fib(n-1) + fib(n-2)`。
    - 時間複雜度：展開為高度為 $n$ 的二元樹，節點總數約 $2^0 + 2^1 + \dots + 2^{n-1} = 2^n - 1$，時間複雜度為恐怖的指數級 $O(2^n)$。
    - 空間複雜度：雖然整棵樹節點極多，但系統採取深度優先走訪（DFS），在任意時刻堆疊中僅保留從根到葉的一條路徑，最大深度為 $n$，因此空間複雜度為線性 $O(n)$。
  - **線性遞迴優化**：改為單向傳遞前兩項數值 `fib(prev, curr, count)`，遞迴深度為 $n$，時間降為 $O(n)$，空間為 $O(n)$。
- **二分搜尋法（遞迴版）效能剖析**：
  - 每次問題規模減半，形成單鏈遞迴樹，樹高為 $\log_2 n$。
  - 時間複雜度：遞迴 $\log n$ 次，每次常數操作，時間為 $O(\log n)$。
  - 空間複雜度：呼叫堆疊深度為 $\log n$，空間為 $O(\log n)$。

## 3. 重要複雜度對比數據
- 樹狀遞迴求斐波那契數：時間 $O(2^n)$，空間 $O(n)$
- 單向遞迴求斐波那契數：時間 $O(n)$，空間 $O(n)$
- 遞迴版二分搜尋法：時間 $O(\log n)$，空間 $O(\log n)$

## 4. 關聯核心概念頁面
- [遞迴複雜度分析 (Recursive Complexity Analysis)](../concepts/recursive-complexity.md)
- [空間複雜度 (Space Complexity)](../concepts/space-complexity.md)
- [記憶化 (Memoization)](../concepts/memoization.md)
- [動態規劃 (Dynamic Programming)](../concepts/dynamic-programming.md)
- [遞迴法 vs 迭代法比較](../syntheses/recursion-vs-iteration.md)
