# 核心概念：遞增法 (Incremental Method)

---

## 1. 一句話白話定義（初學者生活化類比）
**遞增法就像是「排隊進場時驗票員一位一位依序檢驗放行」，不急著一口氣處理所有人，而是化整為零、穩健推進。**  
「不積跬步，無以至千里。不積小流，無以成江海。《荀子》」遞增法是最符合電腦運作特性的經典思維：電腦執行程式一次只做一個動作，當問題龐大時，透過一次納入一個新元素、更新當前狀態，逐步累積至最終解答 [來源: raw/07-algorithm-design.md §incremental method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與關鍵性質
1. **初始狀態設定**：先建立基礎解或空結果（例如累加總和初始化為 0）[來源: raw/07-algorithm-design.md §範例：加總數字 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
2. **單步納入與局部更新**：每一次迴圈處理一個新資料項，並將其與既有累積結果結合（例如 `sum += array[i]`）[來源: raw/07-algorithm-design.md §範例：加總數字 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
3. **就地處理（In-place）節省空間**：遞增法常常能搭配就地更新技巧，避免額外申請空間。例如對調兩條陣列時，透過一次交換一對元素（one-pass），而不需要額外建立暫存陣列 [來源: raw/07-algorithm-design.md §範例：對調陣列 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 3. 典型演算法與時空複雜度分析

### (1) 數值累加（Summation）
```cpp
int sum = 0;
for (int i = 0; i < n; i++)
    sum += array[i];
```
- 時間複雜度：單層迴圈掃描 $n$ 個元素，為 $O(n)$ [來源: raw/07-algorithm-design.md §範例：加總數字 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- 空間複雜度：僅使用變數 `sum`，空間複雜度為常數 $O(1)$ [來源: raw/07-algorithm-design.md §範例：加總數字 | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

### (2) 選擇排序法（Selection Sort）
每次從未排序區間中挑出最小值，交換至已排序區間末尾：
```cpp
for (int i = 0; i < 5; i++) {
    int min = i;
    for (int j = i + 1; j < 5; j++)
        if (array[j] < array[min])
            min = j;
    int temp = array[i]; array[i] = array[min]; array[min] = temp;
}
```
- 時間複雜度：雙層迴圈比較次數為 $\frac{n(n-1)}{2}$，時間複雜度為 $O(n^2)$ [來源: raw/07-algorithm-design.md §範例：選擇排序法（selection sort） | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- 空間複雜度：就地交換，額外空間為 $O(1)$ [來源: raw/07-algorithm-design.md §範例：選擇排序法（selection sort） | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 4. 適用場景與常見誤區
- **適用場景**：串流資料讀取、單遍掃描統計、原地資料轉換與基礎排序 [來源: raw/07-algorithm-design.md §incremental method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **常見誤區：忽略演算法整體效能上限**  
  遞增法雖然直觀簡練且省記憶體，但若未結合更高級的資料結構（如二元搜尋樹或堆積），在排序等問題上容易停留於 $O(n^2)$ 的低效瓶頸 [來源: raw/07-algorithm-design.md §範例：選擇排序法（selection sort） | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 5. 關聯主題與延伸閱讀
- [記憶化 (Memoization)](memoization.md)
- [迭代法與遞迴法 (Recursion and Iteration)](recursion-and-iteration.md)
- [貪婪演算法 (Greedy Method)](greedy-algorithm.md)
- [常見演算法設計典範選擇指南](../syntheses/algorithm-design-strategies.md)
- [原始文獻摘要: 07-algorithm-design](../sources/07-algorithm-design.md)
