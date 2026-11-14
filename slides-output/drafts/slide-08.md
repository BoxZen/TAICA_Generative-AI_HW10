# 局部最佳的豪賭：貪婪演算法與適用陷阱

- **貪婪哲理**：今朝有酒今朝醉。每步只搶眼下最優選擇，單向推進、絕不回頭。
- **極速優勢**：免除遍歷狀態，時間常為 $O(n \log n)$ 或 $O(n)$，空間低至 $O(1)$。
- **翻車陷阱**：非標準面額（1, 4, 5 元湊 8 元），貪婪選 4 枚，DP 僅需 2 枚！
- **適用鐵律**：唯有嚴謹證明具備「貪婪選擇性質」，局部最優才能真正導向全域最優。

來源出處：wiki/concepts/greedy-algorithm.md , raw/07-algorithm-design.md , https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
