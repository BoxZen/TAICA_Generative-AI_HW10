# 證據卡：核心概念：時間複雜度與大 O 標記 (Time Complexity & Big-O Notation)
> **來源 Wiki 頁面**：`wiki/concepts/time-complexity.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
**時間複雜度就像是衡量一趟旅程「耗時隨距離拉長而暴增的走勢圖」，而不是拿碼錶測量某一輛車開了幾分幾秒。**  
它衡量的是當輸入資料規模 $n$ 膨脹時，演算法操作次數的「成長倍率與趨勢」，讓我們能超越特定硬體的限制，客觀評估演算法的優劣 [來源: raw/01-time-complexity.md §究竟什么是时间复杂度 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 2. 核心運作步驟與關鍵性質
1. **漸近分析（Asymptotic Analysis）**：關注輸入規模 $n$ 趨近於無窮大時的運算次數主導項，而非具體的執行指令條數 [來源: raw/01-time-complexity.md §究竟什么是时间复杂度 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
2. **大 O 符號（Big-O Notation）的本質**：數學上大 $O$ 表示演算法執行的「漸近上界（Upper Bound）」，即最壞情況下的成長速度；但在演算法工程與面試交流中，通常用來代表緊確界（Tight Bound）的運算趨勢 [來源: raw/01-time-complexity.md §什么是大O | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
3. **複雜度化簡兩大黃金法則**：
   - **省略常數項**：例如 $O(2n + 10) \implies O(n)$，因為當 $n$ 巨大時常數倍率不改變成長曲線的本質量級 [來源: raw/01-time-complexity.md §复杂表达式的化简 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
   - **省略低階項**：例如 $O(n^2 + 5n + 100) \implies O(n^2)$，最高次項將決定整體的增長極限 [來源: raw/01-time-complexity.md §复杂表达式的化简 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
4. **對數底數的等價性**：由對數換底公式 $\log_a n = \frac{\log_b n}{\log_b a}$，不同底數之間僅相差常數項 $\frac{1}{\log_b a}$，依照化簡規則忽略常數，因此演算法中一律統寫為 $O(\log n)$ [來源: raw/01-time-complexity.md §O(logn)中的log是以什么为底？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 3. 重要數據與複雜度證據
### 常見複雜度量級排行榜（成長速度由快到慢 / 效率由高到低）：
$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)$$
[來源: raw/01-time-complexity.md §不同数据规模的差异 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)

- **$O(1)$ 常數階**：操作次數與資料規模 $n$ 完全無關（如存取陣列指定索引）。
- **$O(\log n)$ 對數階**：每次操作將問題規模減半（如二分搜尋法、快速冪）。
- **$O(n)$ 線性階**：單層遍歷資料（如陣列循序尋找最大值）。
- **$O(n \log n)$ 線性對數階**：高效排序法（如合併排序、快速排序的平均情況）。
- **$O(n^2)$ 平方階**：雙層巢狀迴圈（如選擇排序法、泡沫排序法）。
- **$O(2^n)$ 指數階**：每增加一個輸入規模，運算量翻倍（如未經剪枝的斐波那契遞迴）。

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/01-time-complexity.md §不同数据规模的差异 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
2. [來源: raw/01-time-complexity.md §O(logn)中的log是以什么为底？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
3. [來源: raw/01-time-complexity.md §究竟什么是时间复杂度 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
4. [來源: raw/01-time-complexity.md §什么是大O | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
5. [來源: raw/01-time-complexity.md §复杂表达式的化简 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)

