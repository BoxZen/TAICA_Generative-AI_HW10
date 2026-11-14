# 以空間換時間的極致：記憶化與動態規劃

- **重疊危機**：純遞迴算斐波那契樹節點達 $2^n - 1$，時間呈爆炸級 $O(2^n)$。
- **動態規劃本質**：分治法結合記憶表，隨時記錄中間解，杜絕重複走冤枉路。
- **維度躍遷**：藉由 $O(n)$ 陣列空間，將龐大運算從指數級驟降為線性級 $O(n)$。
- **極致壓縮**：若僅保留前兩項滾動變數，空間更可大幅壓制在常數 $O(1)$。

來源出處：wiki/concepts/dynamic-programming.md , raw/05-recursive-complexity-analysis.md , https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md
