# 原始資料摘要：演算法超時與運算效能 (Algorithm Timeout)

> **原始文章標題**：On的算法居然超时了，此时的n究竟是多大？  
> **原始連結**：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/02-algorithm-timeout.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/02-algorithm-timeout.md)

---

## 1. 核心主題概述
本篇探討在線上評判系統（Online Judge, 如 LeetCode）中程式遭遇**超時（Time Limit Exceeded, TLE）**的根本機制。透過硬體架構剖析與實機測試，建立了程式設計者對「電腦 1 秒鐘能跑多少次基本操作」的直觀量化概念，並給出不同複雜度演算法所允許的最大輸入資料規模。

## 2. 涵蓋演算法與核心知識點
- **超時（TLE）的成因**：線上評判平台通常將單題執行時間限制在 1 秒（部分題目為 2 秒）。若計算量超過硬體每秒處理能力即判定超時。
- **硬體效能基準**：
  - 現代主流個人電腦與評測機（如 4.0GHz CPU），理論時脈單核每秒震盪約 $4 \times 10^9$ 次。
  - 考量指令管線、記憶體存取、快取未命中與指令週期，實際上 C++ 程式 1 秒內能完成的簡單操作次數約為 $10^7 \sim 10^8$ 次。
- **實機驗證數據**：
  - $O(n)$ 迴圈在 $n=10^8$ 時耗時約數十至數百毫秒；在 $n=10^9$ 時耗時超過 1 秒甚至數秒。
  - $O(n^2)$ 迴圈在 $n=10^5$ 時總操作達 $10^{10}$ 次，耗時可達數十秒，必超時。

## 3. 資料規模與複雜度選擇速查表
依據評測系統 1 秒（約 $10^7 \sim 10^8$ 次運算）限制，給出安全資料規模上限：
- $O(n)$：$n \le 10^7 \sim 10^8$
- $O(n \log n)$：$n \le 10^5 \sim 10^6$
- $O(n^2)$：$n \le 10^3 \sim 10^4$
- $O(2^n)$：$n \le 20 \sim 25$
- $O(n!)$：$n \le 10 \sim 11$

## 4. 關聯核心概念頁面
- [超時判定與硬體運算限制 (Algorithm Timeout)](../concepts/algorithm-timeout.md)
- [時間複雜度 (Time Complexity & Big-O)](../concepts/time-complexity.md)
- [常見演算法設計典範選擇指南](../syntheses/algorithm-design-strategies.md)
