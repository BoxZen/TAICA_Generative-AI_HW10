# 證據卡：核心概念：超時判定與電腦運算能力估算 (Algorithm Timeout & Execution Limits)
> **來源 Wiki 頁面**：`wiki/concepts/algorithm-timeout.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
**演算法超時就像是在廚房接了一張要求 1 秒內必須出菜的急單，你必須提前算出自己的切菜手速（硬體每秒運算上限）到底裝得下多少份食材（輸入資料規模 $n$）。**  
超時（Time Limit Exceeded, TLE）是線上評判系統（Online Judge）用來阻擋低效演算法的安全閥，提示工程師該演算法的運算次數超過了硬體每秒能承受的極限 [來源: raw/02-algorithm-timeout.md §超时是怎么回事 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)。

---

## 2. 核心運作步驟與關鍵性質
1. **評測系統時間限制**：線上平台（如 LeetCode、ACM OJ）通常對單一測試案例設有 1 秒（部分題目 2 秒）的時間紅線 [來源: raw/02-algorithm-timeout.md §超时是怎么回事 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)。
2. **硬體處理速度基準**：
   - 以現代主流伺服器或 4.0GHz CPU 為例，理論時脈每秒震盪次數達 $4 \times 10^9$ 次 [來源: raw/02-algorithm-timeout.md §从硬件配置看计算机的性能 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)。
   - 然而，考量到 CPU 指令週期、記憶體讀寫、快取分頁（Cache Miss）與系統調度開銷，**C++ 程式在 1 秒內能完成的基本操作（如加減賦值）次數約為 $10^7 \sim 10^8$ 次** [來源: raw/02-algorithm-timeout.md §从硬件配置看计算机的性能 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)。
3. **實機實驗驗證**：
   - 執行 $O(n)$ 運算：當 $n = 10^8$ 時，耗時約數十至幾百毫秒，安全通過；但當 $n = 10^9$ 時，耗時大幅飆升突破 1 秒甚至達數秒，必定觸發超時 [來源: raw/02-algorithm-timeout.md §做个测试实验 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)。
   - 執行 $O(n^2)$ 運算：若 $n = 10^5$，總操作次數達 $10^{10}$ 次，耗時可達數十秒，必死無疑 [來源: raw/02-algorithm-timeout.md §做个测试实验 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)。

---

## 3. 重要數據與複雜度證據
在解題與設計系統時，應先觀察題目給定的輸入範圍 $n$，反推可接受的時間複雜度：

| 題目輸入資料規模 $n$ | 允許採用的最高時間複雜度 | 典型解題演算法策略 |
| :--- | :--- | :--- |
| $n \le 10 \sim 11$ | $O(n!)$ | 全排列枚舉（Permutation）、暴力回溯搜尋 [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md) |
| $n \le 20 \sim 25$ | $O(2^n)$ | 子集枚舉、回溯搜尋法（Backtracking） [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md) |
| $n \le 10^3 \sim 10^4$ | $O(n^2)$ | 雙層迴圈、動態規劃二維表格、簡單排序 [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md) |
| $n \le 10^5 \sim 10^6$ | $O(n \log n)$ | 合併排序、快速排序、二分搜尋結合遍歷 [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md) |
| $n \le 10^7 \sim 10^8$ | $O(n)$ | 單層迴圈遍歷、雙指針、遞增法、滑動窗口 [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md) |
| $n \ge 10^9$ | $O(\log n)$ 或 $O(1)$ | 二分搜尋法、快速冪、數學公式解 [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md) |

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/02-algorithm-timeout.md §总结 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)
2. [來源: raw/02-algorithm-timeout.md §从硬件配置看计算机的性能 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)
3. [來源: raw/02-algorithm-timeout.md §超时是怎么回事 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)
4. [來源: raw/02-algorithm-timeout.md §做个测试实验 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md)

