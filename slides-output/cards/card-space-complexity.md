# 證據卡：核心概念：空間複雜度分析 (Space Complexity)
> **來源 Wiki 頁面**：`wiki/concepts/space-complexity.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
**空間複雜度就像是在廚房料理時「料理台上臨時擺放碗盤與備料盆的最大佔地面積」，而不是看這家餐廳整棟建築物有多大。**  
空間複雜度（Space Complexity）記作 $S(n) = O(f(n))$，用來評估演算法在運算過程中，需要向電腦申請多少動態記憶體空間隨輸入規模 $n$ 成長的趨勢 [來源: raw/04-space-complexity.md §什么是空间复杂度呢？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 2. 核心運作步驟與關鍵性質
1. **空間複雜度的計算法則**：
   - 關注演算法在執行期間「額外輔助空間（Auxiliary Space）」與「輸入資料所延伸之暫存結構」的記憶體開銷 [來源: raw/04-space-complexity.md §什么是空间复杂度呢？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
2. **兩大關鍵認知防線**：
   - **防線一：不考慮編譯後執行檔（Binary）的大小**  
     許多初學者常混淆程式本體體積與執行期耗費記憶體。空間複雜度嚴格只看「執行期佔用之動態記憶體（堆疊與堆積）」，完全不計入可執行檔本身的磁碟大小 [來源: raw/04-space-complexity.md §关注空间复杂度有两个常见的问题 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。
   - **防線二：非精確位元組數計算**  
     空間複雜度是大體預估，因為編譯器的記憶體對齊（Memory Alignment）、底層容器內部容量擴展機制（如 `std::vector` 的容量倍增策略）等因素，都會讓實際記憶體大小產生差異 [來源: raw/04-space-complexity.md §关注空间复杂度有两个常见的问题 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 3. 重要數據與複雜度證據
### (1) 常數空間 $O(1)$
僅使用固定數量的輔助變數，不論輸入規模 $n$ 多大，配置空間均維持不變：
```cpp
int j = 0;
for (int i = 0; i < n; i++) {
    j++;
}
```
隨 $n$ 增長，所需開闢的記憶體空間為常量，表示為 $O(1)$ [來源: raw/04-space-complexity.md §来看一下例子 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

### (2) 線性空間 $O(n)$
配置的記憶體隨輸入規模 $n$ 呈線性比例增長：
```cpp
int* a = new int(n);
for (int i = 0; i < n; i++) {
    a[i] = i;
}
```
定義了一個佔用大小為 $n$ 的動態陣列，其開闢之記憶體大小隨 $n$ 線性增加，記作 $O(n)$ [來源: raw/04-space-complexity.md §什么时候的空间复杂度是O(n)？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

### (3) 對數空間 $O(\log n)$
在遞迴演算法中，若遞迴樹的最大深度為 $\log n$（如二分搜尋法），呼叫堆疊（Call Stack）所佔用的空間即為 $O(\log n)$ [來源: raw/04-space-complexity.md §什么时候空间复杂度是 O(logn)呢？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)。

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/04-space-complexity.md §什么时候的空间复杂度是O(n)？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
2. [來源: raw/04-space-complexity.md §来看一下例子 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
3. [來源: raw/04-space-complexity.md §关注空间复杂度有两个常见的问题 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
4. [來源: raw/04-space-complexity.md §什么时候空间复杂度是 O(logn)呢？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
5. [來源: raw/04-space-complexity.md §说到空间复杂度 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
6. [來源: raw/04-space-complexity.md §同样在工程实践中 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)
7. [來源: raw/04-space-complexity.md §什么是空间复杂度呢？ | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md)

