# 原始資料摘要：遞迴演算法的時間複雜度 (Recursive Time Complexity)

> **原始文章標題**：通过一道面试题目，讲一讲递归算法的时间复杂度！  
> **原始連結**：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/03-recursive-time-complexity.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/03-recursive-time-complexity.md)

---

## 1. 核心主題概述
本篇透過大廠經典面試題「計算數值的整數次方 $x^n$（快速冪演算法）」，系統性闡明求解遞迴演算法時間複雜度的通用法則。揭示了初學者誤用二分遞迴卻未達到對數時間的根本原因，確立了以「遞迴呼叫次數」為核心的分析架構。

## 2. 涵蓋演算法與核心知識點
- **遞迴時間複雜度核心定理**：
  $$\text{遞迴時間複雜度} = \text{遞迴次數} \times \text{每次遞迴內部的操作次數}$$
- **快速冪問題的三種實作對比**：
  1. **直覺線性遞迴**：每次呼叫 `function1(x, n-1) * x`，共遞迴 $n$ 次，時間複雜度為 $O(n)$。
  2. **偽二分遞迴（常見陷阱）**：寫成 `function2(x, n/2) * function2(x, n/2)`。雖然指數減半，但每一層都會分裂成 2 個分支，展開成高度為 $\log n$ 的滿二元樹，節點總數依然為 $2^{\log n} = n$，時間複雜度仍為 $O(n)$。
  3. **正統優化二分遞迴**：先計算 `int t = function3(x, n/2);` 並儲存變數，再依奇偶性返回 `t * t * x` 或 `t * t`。只呼叫一次遞迴，遞迴樹為單鏈結構，遞迴次數為 $\log n$，時間複雜度降為 $O(\log n)$。

## 3. 重要複雜度數據
- 線性遞迴求次方：時間複雜度 $O(n)$
- 雙分支重複遞迴求次方：時間複雜度 $O(n)$
- 單分支優化快速冪：時間複雜度 $O(\log n)$

## 4. 關聯核心概念頁面
- [遞迴複雜度分析 (Recursive Complexity Analysis)](../concepts/recursive-complexity.md)
- [分治法 (Divide-and-Conquer Method)](../concepts/divide-and-conquer.md)
- [遞迴法與迭代法 (Recursion and Iteration)](../concepts/recursion-and-iteration.md)
- [遞迴法 vs 迭代法比較](../syntheses/recursion-vs-iteration.md)
