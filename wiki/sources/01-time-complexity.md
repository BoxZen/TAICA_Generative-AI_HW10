# 原始資料摘要：時間複雜度 (Time Complexity)

> **原始文章標題**：关于时间复杂度，你不知道的都在这里！  
> **原始連結**：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/01-time-complexity.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/01-time-complexity.md)

---

## 1. 核心主題概述
本篇深入剖析演算法領域中最基礎且關鍵的指標——**時間複雜度（Time Complexity）**與**大 O 符號（Big-O Notation）**。澄清了初學者常見的觀念盲點，指出時間複雜度並非指執行程式碼的絕對精確秒數，而是衡量演算法隨著輸入規模 $n$ 增長時，運算時間的「漸近增長趨勢」。

## 2. 涵蓋演算法與核心知識點
- **時間複雜度的本質**：漸近時間複雜度（Asymptotic Time Complexity），關注輸入資料規模趨近於無窮大時的趨勢。
- **大 O 符號的數學定義**：表示演算法執行的漸近上界（Upper Bound），但在演算法面試與工程溝通中，通常指漸近緊確界（Tight Bound）。
- **複雜度化簡原則**：
  1. 省略常數項（如 $O(2n+1) \to O(n)$）。
  2. 省略低階項（如 $O(n^2 + n) \to O(n^2)$）。
- **對數底數的本質**：由換底公式可知不同底數之間僅差一個常數倍數，因此統一記為 $O(\log n)$。
- **不同數據規模下的成長差異**：說明常數項在數據規模極小時可能佔主導，但隨 $n$ 增長，高階項必然主導演算法執行效能。

## 3. 重要複雜度量級排序
根據文中所列，常見複雜度量級增長率由低到高排序如下：
$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)$$

## 4. 關聯核心概念頁面
- [時間複雜度 (Time Complexity & Big-O)](../concepts/time-complexity.md)
- [超時判定與硬體運算限制 (Algorithm Timeout)](../concepts/algorithm-timeout.md)
- [時間與空間權衡 (Time-Space Tradeoff)](../syntheses/time-space-tradeoff.md)
