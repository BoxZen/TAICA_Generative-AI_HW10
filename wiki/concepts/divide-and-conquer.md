# 核心概念：分治法 (Divide-and-Conquer Method)

---

## 1. 一句話白話定義（初學者生活化類比）
**分治法就像是「將一場千人大合唱拆成各部聲樂各自練唱，大家把各自的段落唱熟後，最後在舞台上合奏成一首磅礴交響曲」。**  
「凡治眾如治寡，分數是也。鬥眾如鬥寡，形名是也。《孫子》」分治法是演算法中最重要的分治哲理：當一個問題規模太過龐大難以直接攻克時，將其拆解為數個相互獨立、結構相同但規模較小的子問題，各個擊破後再將成果合併 [來源: raw/07-algorithm-design.md §divide-and-conquer method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 2. 核心運作步驟與三步曲
分治法在執行時嚴格遵循三大步驟：
1. **分割（Divide）**：將大問題分割成兩個或多個子問題。理想情況下子問題規模大致均等，且子問題之間互相獨立（不互相依賴）[來源: raw/07-algorithm-design.md §divide-and-conquer method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
2. **克服（Conquer）**：遞迴求解各個子問題。若子問題規模已縮小至基底條件（Base Case），則直接計算解答 [來源: raw/07-algorithm-design.md §divide-and-conquer method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。
3. **合併（Combine）**：將各子問題的局部解答黏合、匯流，拼湊出原問題的最終全局解 [來源: raw/07-algorithm-design.md §divide-and-conquer method | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 3. 典型演算法與時空複雜度分析

### (1) 二分搜尋法（Binary Search）
將排序陣列一分為二，判斷目標值在左半部或右半部，捨棄另一半：
- 時間複雜度：每次規模減半，遞迴深度為 $\log_2 n$，時間複雜度為 $O(\log n)$ [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
- 空間複雜度：遞迴實作佔用呼叫堆疊 $O(\log n)$；迭代實作僅需指標變數，空間為 $O(1)$ [來源: raw/05-recursive-complexity-analysis.md §二分法（递归实现）的性能分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

### (2) 快速冪運算（Power $x^n$）
計算 $x^n = x^{n/2} \times x^{n/2}$，藉由只呼叫一次遞迴並平方：
- 時間複雜度：樹高 $\log n$，時間複雜度為 $O(\log n)$ [來源: raw/03-recursive-time-complexity.md §依然感觉没有达到极致 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
- 空間複雜度：呼叫堆疊深度為 $O(\log n)$ [來源: raw/03-recursive-time-complexity.md §依然感觉没有达到极致 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 4. 適用場景與常見誤區
- **獨立性前提**：分治法最關鍵的假設在於「子問題之間互相獨立」。若子問題大量重複（例如求斐波那契數時 `fib(n-1)` 與 `fib(n-2)` 均包含 `fib(n-3)`），純分治將引發指數級的重複運算災難 [來源: raw/05-recursive-complexity-analysis.md §时间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
- **升級分水嶺**：當子問題高度重疊時，必須引入記憶化，轉化為**動態規劃（Dynamic Programming）** [來源: raw/07-algorithm-design.md §dynamic programming | 原始連結](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)。

---

## 5. 關聯主題與延伸閱讀
- [動態規劃 (Dynamic Programming)](dynamic-programming.md)
- [遞迴複雜度分析](recursive-complexity.md)
- [記憶化 (Memoization)](memoization.md)
- [動態規劃 vs 貪婪演算法比較](../syntheses/dp-vs-greedy.md)
- [原始文獻摘要: 07-algorithm-design](../sources/07-algorithm-design.md)
