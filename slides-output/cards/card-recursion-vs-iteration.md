# 證據卡：綜合比較：遞迴法 vs 迭代法 (Recursion vs Iteration)
> **來源 Wiki 頁面**：`wiki/syntheses/recursion-vs-iteration.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
在電腦程式設計中，重複性計算主要透過兩種控制流實現：
- **遞迴法（Recursion）**：函式自我呼叫，自頂向下（Top-Down）拆解問題，依賴執行階段的**呼叫堆疊（Call Stack）**隱式維護計算狀態與返回位址 [來源: raw/07-algorithm-design.md §recursive method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **迭代法（Iteration）**：利用迴圈結構（`for`、`while`）自底向上（Bottom-Up）累積推進，直接顯式更新局部變數，不產生額外的函式呼叫框架 [來源: raw/07-algorithm-design.md §iterative method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與關鍵性質
| 比較項目 | 遞迴法 (Recursion) | 迭代法 (Iteration) |
| :--- | :--- | :--- |
| **思維邏輯** | 符合數學歸納法，直觀定義問題與終止邊界 | 狀態機思維，需要明確設計狀態如何循序推進 |
| **推演方向** | 自頂向下（Top-Down）：原問題 $\to$ 子問題 $\to$ 邊界 | 自底向上（Bottom-Up）：邊界初始值 $\to$ 規模累積 $\to$ 目標 [來源: raw/07-algorithm-design.md §iterative method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **記憶體消耗** | **需消耗 $O(\text{樹高})$ 的堆疊記憶體**；每一層呼叫均需建立 Stack Frame [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md) | **$O(1)$ 常數空間**；僅重複使用固定暫存變數 [來源: raw/04-space-complexity.md §来看一下例子 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md) |
| **執行效率** | 每次函式調用均涉及暫存器壓棧（Push）、彈棧（Pop）與跳轉開銷，常數耗時較大 [來源: raw/06-memory-consumption.md §C++的内存管理 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md) | 純指令跳轉，CPU 管線與分支預測友好，速度極快 |
| **崩潰風險** | 若遞迴深度過深（通常大於 $10^4 \sim 10^5$），會直接觸發**堆疊溢位（Stack Overflow）**導致程式崩潰 [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md) | 不受呼叫堆疊大小限制，只要迴圈終止條件正確絕不會堆疊溢位 |

---

## 3. 重要數據與複雜度證據
- **遞迴實作**：
  每次將搜尋區間折半後遞迴自我呼叫。雖然時間複雜度為 $O(\log n)$，但呼叫堆疊深度同樣達到 $\log_2 n$，空間複雜度為 $O(\log n)$ [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
- **迭代實作**：
  僅透過 `left`、`right` 與 `mid` 三個整數指標在迴圈中更新區間，時間複雜度同樣為 $O(\log n)$，但空間複雜度徹底降為 $O(1)$ [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/07-algorithm-design.md §iterative method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
2. [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)
3. [來源: raw/07-algorithm-design.md §iterative method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
4. [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)
5. [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)
6. [來源: raw/07-algorithm-design.md §recursive method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
7. [來源: raw/06-memory-consumption.md §C++的内存管理 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)
8. [來源: raw/04-space-complexity.md §来看一下例子 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)

