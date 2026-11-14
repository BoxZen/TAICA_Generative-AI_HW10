# 證據卡：核心概念：記憶化與預先計算 (Memoization & Precomputation)
> **來源 Wiki 頁面**：`wiki/concepts/memoization.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
**記憶化就像是「在隨身小筆記本上記下做過題目的答案」，下次再遇到一模一樣的考題時，翻開筆記直接抄，不必重新計算半天。**  
「惟事事，乃其有備，有備無患。《書經》」記憶法是演算法中「以空間換取時間（Space-Time Tradeoff）」的經典手法。透過在記憶體中建立表格記錄計算結果，避免重複計算相同的子問題 [來源: raw/07-algorithm-design.md §memoization | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與關鍵性質
根據資料快取的時間點，可分為兩大形態：
1. **即時記憶化（Memoization / Tabulation）**：  
   在演算法執行過程中，即時更新數值並儲存於記憶體變數或陣列中。下次需要時直接讀取，例如即時維護堆疊大小、計數排序法中的頻率統計表格 [來源: raw/07-algorithm-design.md §memoization | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
2. **預先計算（Precomputation / Preprocessing）**：  
   在演算法開始執行前，預先計算好可能用到的數據表格並常駐記憶體。例如預先建構 1 到 10 的立方和對照表、圓周率常數或質數表，當查詢請求抵達時能在 $O(1)$ 時間內直接返回解答 [來源: raw/07-algorithm-design.md §memoization | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 3. 重要數據與複雜度證據
### (1) 計數排序法（Counting Sort）
利用陣列下標作為數值鍵值，以額外記憶體統計每個數值出現的次數：
```cpp
int count[10] = {0};
for (int i = 0; i < n; i++)
    count[array[i]]++; // 記錄頻率
```
- 時間複雜度：只需掃描資料兩遍，時間複雜度為線性 $O(n + k)$，其中 $k$ 為數值範圍 [來源: raw/07-algorithm-design.md §範例：計數排序法（counting sort） | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- 空間複雜度：需要配置大小為 $k$ 的計數陣列，空間複雜度為 $O(k)$ [來源: raw/07-algorithm-design.md §範例：計數排序法（counting sort） | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

### (2) 預先計算立方和（Table Lookup）
若需頻繁查詢 1 到 $n$ 的立方和，預先建立靜態陣列：
```cpp
const int cube_sum[11] = {0, 1, 9, 36, 100, 225, 441, 784, 1296, 2025, 3025};
// 查詢時直接回傳
return cube_sum[n];
```
- 時間複雜度：單次查詢只需 $O(1)$ [來源: raw/07-algorithm-design.md §範例：求1到n的全部整數的立方和 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- 空間複雜度：消耗預建表格的常數空間 $O(k)$ [來源: raw/07-algorithm-design.md §範例：求1到n的全部整數的立方和 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/07-algorithm-design.md §範例：計數排序法（counting sort） | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
2. [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
3. [來源: raw/07-algorithm-design.md §範例：求1到n的全部整數的立方和 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
4. [來源: raw/07-algorithm-design.md §memoization | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)

