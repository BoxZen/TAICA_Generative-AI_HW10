# 核心概念：遞迴複雜度分析 (Recursive Complexity Analysis)

---

## 1. 一句話白話定義（初學者生活化類比）
**分析遞迴的時間就像是「計算整棵家族樹所有成員的總人數」，而分析遞迴的空間則是看「家族樹中最長的那一脈單傳路徑有多深」。**  
遞迴演算法（Recursive Algorithm）的複雜度分析核心在於將函式自我呼叫的過程視覺化為一棵「遞迴樹（Recursion Tree）」，以樹的總節點數決定時間，以樹的最大深度決定空間 [來源: raw/03-recursive-time-complexity.md §本篇通过一道面试题 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 2. 核心運作步驟與關鍵性質

### (1) 遞迴時間複雜度黃金公式
$$\text{遞迴時間複雜度} = \text{遞迴呼叫次數} \times \text{每次遞迴內部的操作次數}$$
[來源: raw/03-recursive-time-complexity.md §总结 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)

### (2) 遞迴空間複雜度核心定律
$$\text{遞迴空間複雜度} = \text{遞迴樹的最大深度} \times \text{每次呼叫所需的輔助空間}$$
因為每一次函式呼叫都會在呼叫堆疊（Call Stack）上建立一個堆疊訊框（Stack Frame），保存參數與返回點。由於深度優先走訪特性，同一時間存在於堆疊中的訊框數量上限即等於樹的最大深度 [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

---

## 3. 典型案例時空複雜度深度剖析

### 案例一：計算整數次方 $x^n$（快速冪）
- **直覺遞迴法**：
  ```cpp
  int function1(int x, int n) {
      if (n == 0) return 1;
      return function1(x, n - 1) * x;
  }
  ```
  遞迴樹為單鏈，呼叫次數為 $n$，每次常數相乘，時間複雜度為 $O(n)$，空間複雜度為 $O(n)$ [來源: raw/03-recursive-time-complexity.md §同一道题目 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
- **偽二分遞迴陷阱**：
  ```cpp
  int function2(int x, int n) {
      if (n == 0) return 1;
      if (n % 2 == 1) return function2(x, n / 2) * function2(x, n / 2) * x;
      return function2(x, n / 2) * function2(x, n / 2);
  }
  ```
  雖然指數除以 2，但每一層都會裂變成 2 個分支，展開成高度為 $\log n$ 的滿二元樹，總節點數為 $2^{\log n} = n$。因此時間複雜度**仍為 $O(n)$** [來源: raw/03-recursive-time-complexity.md §看代码 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)！
- **真·優化快速冪**：
  ```cpp
  int function3(int x, int n) {
      if (n == 0) return 1;
      int t = function3(x, n / 2); // 關鍵：暫存單次呼叫結果
      if (n % 2 == 1) return t * t * x;
      return t * t;
  }
  ```
  只遞迴一條路徑，呼叫次數為 $\log n$，時間複雜度降為 $O(\log n)$，空間複雜度為 $O(\log n)$ [來源: raw/03-recursive-time-complexity.md §依然感觉没有达到极致 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

### 案例二：斐波那契數列（Fibonacci）
- **雙分支樹狀遞迴**：
  ```cpp
  int fibonacci(int i) {
      if (i <= 0) return 0;
      if (i == 1) return 1;
      return fibonacci(i - 1) + fibonacci(i - 2);
  }
  ```
  - **時間複雜度**：展開為二元樹，樹高為 $n$。節點總數為 $2^0 + 2^1 + \dots + 2^{n-1} = 2^n - 1$。時間複雜度為恐怖的指數級 $O(2^n)$ [來源: raw/05-recursive-complexity-analysis.md §时间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。
  - **空間複雜度**：雖然節點高達 $2^n$ 個，但走訪方式為深度優先搜尋，堆疊中同時存在的最大訊框數等於樹高 $n$，因此空間複雜度僅為線性 $O(n)$ [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

---

## 4. 適用場景與常見誤區
- **常見誤區 1：以為寫了 `n/2` 就一定是 $O(\log n)$**  
  二分切割若伴隨著多重複制呼叫（如上述 `function2`），每個子問題都重複計算兩遍，依然會退化為線性甚至指數複雜度 [來源: raw/03-recursive-time-complexity.md §看代码 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
- **常見誤區 2：忽略遞迴帶來的呼叫堆疊溢位（Stack Overflow）**  
  在深度較大的遞迴（例如 $n = 10^5$ 的線性遞迴）中，即便時間不超時，也極易因超過預設堆疊記憶體（通常僅數 MB）而崩潰 [來源: raw/05-recursive-complexity-analysis.md §空间复杂度分析 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md)。

---

## 5. 關聯主題與延伸閱讀
- [時間複雜度](time-complexity.md)
- [空間複雜度](space-complexity.md)
- [分治法 (Divide-and-Conquer Method)](divide-and-conquer.md)
- [遞迴法 vs 迭代法比較](../syntheses/recursion-vs-iteration.md)
- [原始文獻摘要: 03-recursive-time-complexity](../sources/03-recursive-time-complexity.md)
- [原始文獻摘要: 05-recursive-complexity-analysis](../sources/05-recursive-complexity-analysis.md)
