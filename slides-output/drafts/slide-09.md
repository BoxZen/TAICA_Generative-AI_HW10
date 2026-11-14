# 決策十字路口：常見演算法設計典範選擇矩陣

- **決策分水嶺**：獨立子問題選分治，重疊子問題選 DP，證明無後效性才選貪婪。
- **測資反推法則**：
  - $n \le 20 \implies O(2^n)$（回溯枚舉）
  - $n \le 10^4 \implies O(n^2)$（雙重迴圈 / 二維 DP）
  - $n \le 10^5 \implies O(n \log n)$（高效排序 / 分治）
  - $n \ge 10^7 \implies O(n)$ 或 $O(\log n)$（線性掃描 / 二分搜尋）
- **工程防禦**：超深層運算優先選用迭代結構，杜絕堆疊溢位崩潰。

來源出處：wiki/syntheses/algorithm-design-strategies.md , raw/02-algorithm-timeout.md , https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md
