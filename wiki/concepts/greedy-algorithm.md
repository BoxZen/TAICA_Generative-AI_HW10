# 核心概念：貪婪演算法 (Greedy Method)

---

## 1. 一句話白話定義（初學者生活化類比）
**貪婪演算法就像是「在自助餐夾菜時永遠先搶當下看起來最昂貴的大菜」，每一步都只貪圖眼前最巨大的利益，絕不瞻前顧後。**  
「今朝有酒今朝醉，明日愁來明日愁。《羅隱．自遣》」貪婪演算法（Greedy Method）的核心思維是在問題的每一個決策階段，都毫不猶豫地做出當前看起來最好的選擇（局部最佳解 Locally Optimal Choice），並期盼透過局部最佳的堆疊，最終達到全域最佳（Globally Optimal Solution）[來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與兩大支柱
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

## 3. 時間與空間複雜度分析
- **時間複雜度**：  
  因為貪婪法採取「單向推進、永不回頭」的決策模式，不需要遍歷所有狀態或維護複雜轉移矩陣。其時間瓶頸通常落在**初始排序**或**優先佇列維護**上，常見複雜度為 **$O(n \log n)$** 或 **$O(n)$** [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **空間複雜度**：  
  通常只需維護當前選擇的結果或排序後的陣列，空間複雜度多為 **$O(1)$** 或 **$O(n)$**，遠比動態規劃節省空間 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 4. 適用場景與常見誤區
- **經典適用場景**：活動選擇問題（區間排程）、霍夫曼編碼（Huffman Coding）、最小生成樹（Kruskal / Prim）[來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **致命陷阱：短視近利導致全局劣解**  
  貪婪法最大的盲點在於「並非所有問題都具備貪婪選擇性質」。例如在非標準面額找零問題中（若面額有 1, 4, 5 元，要湊 8 元）：
  - 貪婪策略：先選最大的 5 元，剩下 3 元只能用三個 1 元湊，共需 4 枚硬幣（$5 + 1 + 1 + 1$）。
  - 真實全域最優解：選兩個 4 元，僅需 2 枚硬幣（$4 + 4$）。  
  在此類場景下，貪婪法徹底失效，必須改由**動態規劃（DP）**窮盡最佳轉移路徑 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 5. 關聯主題與延伸閱讀
- [動態規劃 (Dynamic Programming)](dynamic-programming.md)
- [遞增法 (Incremental Method)](incremental-method.md)
- [動態規劃 vs 貪婪演算法比較](../syntheses/dp-vs-greedy.md)
- [常見演算法設計典範選擇指南](../syntheses/algorithm-design-strategies.md)
- [原始文獻摘要: 07-algorithm-design](../sources/07-algorithm-design.md)
