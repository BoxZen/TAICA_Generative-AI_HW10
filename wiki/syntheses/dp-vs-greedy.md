# 綜合比較：動態規劃 vs 貪婪演算法 (Dynamic Programming vs Greedy Algorithm)

---

## 1. 核心決策機制本質對比
在解決最佳化問題（Optimization Problems）時，動態規劃（Dynamic Programming, DP）與貪婪演算法（Greedy Method）是最常被拿來並列對比的兩大設計典範：

- **動態規劃（DP）**：以「全局宏觀」視角出發，本質是「分治法輔以記憶法」。它會窮盡並保留所有潛在有用的子狀態，透過狀態轉移方程式在各子解之間權衡比較，確保最終獲得全局全域最優解 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **貪婪演算法（Greedy）**：「今朝有酒今朝醉」。在每一個決策點上只專注於眼前當下看起來利益最大的選擇（局部最佳解），一旦選定便絕不回溯、不反悔，期盼局部的最優能夠串聯成全域的最優 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 全方位特性對比矩陣

| 比較維度 | 動態規劃 (Dynamic Programming) | 貪婪演算法 (Greedy Method) |
| :--- | :--- | :--- |
| **思維哲學** | 謹慎籌劃、步步為營、記憶已知 | 眼前至上、短視進取、永不回頭 [來源: raw/07-algorithm-design.md §greedy method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **子問題關係** | 具有**重疊子問題**與**最佳子結構** [來源: raw/07-algorithm-design.md §dynamic programming \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) | 必須具備**貪婪選擇性質**與**最佳子結構** [來源: raw/07-algorithm-design.md §greedy method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **決策方式** | 綜合評估所有可能轉移路徑後做決策 | 僅依據預設規則挑選當前最優候選項 [來源: raw/07-algorithm-design.md §greedy method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **時間複雜度** | 通常為多項式階，如 $O(n^2)$ 或 $O(n \cdot W)$ | 通常極快，多為 $O(n)$ 或 $O(n \log n)$（主要耗費在排序） [來源: raw/07-algorithm-design.md §greedy method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **空間複雜度** | 需配置狀態表格，通常為 $O(n)$ 或 $O(n^2)$（以空間換取時間） [來源: raw/07-algorithm-design.md §dynamic programming \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) | 通常為 $O(1)$ 或 $O(n)$，記憶體消耗極低 [來源: raw/07-algorithm-design.md §greedy method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **最優性保證** | 只要狀態轉移完整，保證獲得全域最優解 [來源: raw/07-algorithm-design.md §dynamic programming \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) | 僅在嚴格滿足貪婪選擇性質時才正確；否則易陷入局部陷阱 [來源: raw/07-algorithm-design.md §greedy method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |

---

## 3. 經典場景判別案例：硬幣找零問題
以「湊出特定金額所需的最少硬幣枚數」為例：
- **標準法定貨幣面額（如 1, 5, 10, 50 元）**：  
  由於大面額均為小面額的倍數關係，具備貪婪選擇性質，直接採用貪婪法（每次優先挑選最大面額）即可得到最少硬幣數，時間只需 $O(n)$ [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
- **特殊設計面額（如 1, 4, 5 元，目標金額 8 元）**：  
  - **貪婪法選擇**：先挑 5 元，剩餘 3 元只能挑三個 1 元，共需 $1 + 3 = 4$ 枚硬幣。
  - **動態規劃選擇**：透過 $dp[8] = \min(dp[7], dp[4], dp[3]) + 1$ 評估，發現挑選兩枚 4 元只需 $2$ 枚硬幣。  
  此時貪婪法徹底失效，必須以動態規劃為準 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 4. 決策選型指引
1. **先嘗試證明貪婪選擇性質**：若能透過數學歸納法或反證法證明「局部最優必然包含在全域最優解中」，優先採用貪婪演算法，以換取極致的執行速度與超低記憶體消耗 [來源: raw/07-algorithm-design.md §greedy method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
2. **若存在後效性或反例**：只要後續的決策會受到當前選擇的牽制，或者找不到局部最優的絕對保證，應果斷改採動態規劃，透過建立狀態矩陣消除後效性 [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 5. 關聯概念頁面
- [動態規劃 (Dynamic Programming)](../concepts/dynamic-programming.md)
- [貪婪演算法 (Greedy Method)](../concepts/greedy-algorithm.md)
- [分治法 (Divide-and-Conquer Method)](../concepts/divide-and-conquer.md)
- [時間與空間權衡 (Time-Space Tradeoff)](time-space-tradeoff.md)
