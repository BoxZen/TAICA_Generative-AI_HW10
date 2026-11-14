# 為什麼需要演算法？從超時 (TLE) 與硬體極限談起

- **超時本質**：線上評測限時 1 秒，總運算量超越硬體承載極限即判定超時。
- **硬體基準**：現代 CPU 實測 1 秒內僅能完成約 $10^7 \sim 10^8$ 次基本操作。
- **實機數據**：$O(n)$ 在 $n=10^8$ 順利通過；但在 $n=10^9$ 時耗時超標必然崩潰。
- **實戰心法**：動筆前務必觀察測資規模，總操作次數嚴禁突破 $10^8$ 警戒線。

來源出處：wiki/concepts/algorithm-timeout.md , raw/02-algorithm-timeout.md , https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md
