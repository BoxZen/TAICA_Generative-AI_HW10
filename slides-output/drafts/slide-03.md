# 衡量效率的尺：時間複雜度與大 O 標記

- **白話定義**：衡量操作次數隨輸入規模 $n$ 增長的走勢圖，標記最壞漸近上界。
- **化簡原則**：忽略常數項（$2n \to n$），捨棄低階項（$n^2 + n \to n^2$）。
- **對數等價**：因換底公式相差常數倍，不同底數在大 O 中一律統稱 $O(\log n)$。
- **速度天平**：$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n)$。

來源出處：wiki/concepts/time-complexity.md , raw/01-time-complexity.md , https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md
