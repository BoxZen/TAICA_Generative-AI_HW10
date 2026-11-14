# 原始資料摘要：空間複雜度分析 (Space Complexity)

> **原始文章標題**：空间复杂度分析  
> **原始連結**：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/04-space-complexity.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/04-space-complexity.md)

---

## 1. 核心主題概述
本篇建立了演算法**空間複雜度（Space Complexity）**的評估標準。釐清了空間複雜度與執行檔實體大小的區別，強調空間複雜度是衡量演算法執行期間記憶體動態消耗的漸近成長量度，並透過典型程式碼範例解析 $O(1)$、$O(n)$ 到 $O(\log n)$ 的物理意涵。

## 2. 涵蓋演算法與核心知識點
- **空間複雜度的定義**：記作 $S(n) = O(f(n))$，表示演算法在運算過程中所需佔用之暫存記憶體空間的漸近量度。
- **初學者兩大核心盲點釐清**：
  1. **不等於執行檔（Binary）大小**：空間複雜度衡量的是執行期動態佔用之記憶體（堆疊與堆積空間），而非編譯產出的二進位程式檔磁碟體積。
  2. **不等於精確位元組數**：實際記憶體用量受編譯器記憶體對齊、變數邊界填充與底層容器實作等硬體與環境因素影響；空間複雜度僅提供大體規模的漸近估計。
- **典型空間複雜度範例**：
  - 常數空間 $O(1)$：變數數量固定，不隨輸入規模 $n$ 成長。
  - 線性空間 $O(n)$：動態分配長度為 $n$ 的動態陣列。
  - 對數空間 $O(\log n)$：主要出現在特定遞迴結構（如樹高為 $\log n$ 的遞迴呼叫堆疊）。

## 3. 重要複雜度數據
- 固定計數迴圈：空間複雜度 $O(1)$
- 動態陣列配置 `new int(n)`：空間複雜度 $O(n)$
- 二分遞迴呼叫堆疊：空間複雜度 $O(\log n)$

## 4. 關聯核心概念頁面
- [空間複雜度 (Space Complexity)](../concepts/space-complexity.md)
- [程式記憶體配置與對齊 (Memory Management)](../concepts/memory-management.md)
- [時間與空間權衡 (Time-Space Tradeoff)](../syntheses/time-space-tradeoff.md)
