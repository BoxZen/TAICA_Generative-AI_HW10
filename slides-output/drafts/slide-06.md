# 化整為零的藝術：分治法與遞迴複雜度剖析

- **分治三步**：切分大問題 $\to$ 遞迴解決獨立子問題 $\to$ 縫合局部成果拼湊全解。
- **時空公理**：遞迴時間為「呼叫總次數 $\times$ 單次運算」；空間為「遞迴樹最大深度」。
- **快速冪陷阱**：未暫存之雙遞迴節點達 $n$，退化為 $O(n)$；暫存單次呼叫方達 $O(\log n)$。
- **核心假設**：各子問題必須完全獨立；若高度重複，則必須進化為動態規劃。

來源出處：wiki/concepts/divide-and-conquer.md , raw/03-recursive-time-complexity.md , https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md
