# 證據卡：核心概念：貪婪演算法 (Greedy Method)
> **來源 Wiki 頁面**：`wiki/concepts/greedy-algorithm.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
**貪婪演算法就像是「在自助餐夾菜時永遠先搶當下看起來最昂貴的大菜」，每一步都只貪圖眼前最巨大的利益，絕不瞻前顧後。**  
「今朝有酒今朝醉，明日愁來明日愁。《羅隱．自遣》」貪婪演算法（Greedy Method）的核心思維是在問題的每一個決策階段，都毫不猶豫地做出當前看起來最好的選擇（局部最佳解 Locally Optimal Choice），並期盼透過局部最佳的堆疊，最終達到全域最佳（Globally Optimal Solution）[來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與關鍵性質
要讓貪婪法能夠獲取「真正全域最優解」，問題必須嚴格滿足兩大條件：
1. **貪婪選擇性質（Greedy Choice Property）**：  
   全局最佳解可以透過一系列局部最佳（貪婪）的選擇來達成，且先前做出的選擇絕不因後續決策而推翻或回溯 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
2. **最佳子結構（Optimal Substructure）**：  
   執行一次貪婪選擇後，剩下的子問題依然是一個最佳化問題，其子問題的最優解與當前選擇結合仍為全局最優 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

### 運作步驟：
- 建立候選集合（Candidates）。
- 依據貪婪策略排序或選出當前最具優勢的元素。
- 檢查該元素是否滿足約束條件，若滿足則納入解集合。
- 轉入下一階段，直至問題解決。

---

## 3. 重要數據與複雜度證據
- **時間複雜度**：  
  因為貪婪法採取「單向推進、永不回頭」的決策模式，不需要遍歷所有狀態或維護複雜轉移矩陣。其時間瓶頸通常落在**初始排序**或**優先佇列維護**上，常見複雜度為 **$O(n \log n)$** 或 **$O(n)$** [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **空間複雜度**：  
  通常只需維護當前選擇的結果或排序後的陣列，空間複雜度多為 **$O(1)$** 或 **$O(n)$**，遠比動態規劃節省空間 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)
2. [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)

