# 核心概念：遞迴法與迭代法 (Recursion and Iteration)

---

## 1. 一句話白話定義（初學者生活化類比）
**迭代法就像是「一步一腳印踩著階梯拾級而上」，而遞迴法就像是「俄羅斯娃娃一層層打開，看到最核心的微型娃娃後，再一層層套回包好」。**  
計算機中兩種最基礎的反覆計算控制結構：迭代法（Iterative Method）透過迴圈機制自底向上推進；遞迴法（Recursive Method）則透過函式自我呼叫自頂向下展開 [來源: raw/07-algorithm-design.md §iterative method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與哲學對照
1. **迭代法（Iterative Method）**：  
   「道生一，一生二，二生三，三生萬物。《老子》」由最簡單的已知初值（$n=0$ 或 $1$）出發，透過迴圈變數的更新，一步步推導至目標規模 $n$（自底向上 Bottom-Up）[來源: raw/07-algorithm-design.md §iterative method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
2. **遞迴法（Recursive Method）**：  
   「易有大恒，是生兩檥。兩檥生四馬，四馬生八卦。《易傳》」假設規模更小的子問題已經可解，將當前問題化簡為一個或多個自我呼叫，直到觸及基底終止條件（Base Case），再逐層將結果回傳整合（自頂向下 Top-Down）[來源: raw/07-algorithm-design.md §recursive method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 3. 時空複雜度與底層資源消耗對比

| 評估維度 | 迭代法 (Iteration) | 遞迴法 (Recursion) |
| :--- | :--- | :--- |
| **控制結構** | `for` / `while` 迴圈 | 函式自我呼叫（Self-Calling Function） [來源: raw/07-algorithm-design.md §recursive method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **推演方向** | 自底向上（Bottom-Up） | 自頂向下（Top-Down） [來源: raw/07-algorithm-design.md §iterative method \| 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html) |
| **時間複雜度** | $O(n)$（循序迴圈操作） | $O(n)$（單鏈遞迴）至 $O(2^n)$（多分支展開） [來源: raw/05-recursive-complexity-analysis.md §时间复杂度分析 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md) |
| **空間複雜度** | **$O(1)$ 常數空間**（僅需少數迴圈變數） | **$O(\text{樹高})$ 呼叫堆疊空間** [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md) |
| **底層硬體開銷** | 無額外呼叫開銷，速度極快 | 每次呼叫需建立 Stack Frame，保存暫存器與返回位址 [來源: raw/06-memory-consumption.md §C++的内存管理 \| 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md) |

---

## 4. 適用場景與常見誤區
- **遞迴的致命弱點：堆疊溢位（Stack Overflow）**  
  在作業系統中，執行緒的呼叫堆疊容量通常極為有限（例如 Linux 預設 8MB，Windows 預設 1MB）。若遞迴深度達到 $10^5 \sim 10^6$ 次，即便時間充足，程式也會因為堆疊記憶體用盡而崩潰閃退 [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
- **二分搜尋法對比**：  
  二分搜尋使用迭代寫法只需兩個指針變數，空間為 $O(1)$；而遞迴寫法需要消耗 $O(\log n)$ 的堆疊空間。在極致效能要求下優先選擇迭代版 [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

---

## 5. 關聯主題與延伸閱讀
- [遞迴複雜度分析](recursive-complexity.md)
- [空間複雜度](space-complexity.md)
- [程式記憶體配置與對齊](memory-management.md)
- [遞迴法 vs 迭代法比較](../syntheses/recursion-vs-iteration.md)
- [原始文獻摘要: 07-algorithm-design](../sources/07-algorithm-design.md)
