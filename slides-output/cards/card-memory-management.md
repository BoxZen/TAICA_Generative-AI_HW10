# 證據卡：核心概念：程式記憶體配置與對齊 (Memory Layout & Memory Alignment)
> **來源 Wiki 頁面**：`wiki/concepts/memory-management.md`
> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定

## 1. 關鍵定義與白話類比
**記憶體配置就像是在圖書館依照書本性質分區上架，而記憶體對齊則是規定書本只能放在整數尺度的格子裡，避免管理員借一本書還得抽兩次抽屜。**  
了解程式碼的記憶體消耗必須深入電腦底層的記憶體分區模型與硬體對齊規範，它是跨越演算法理論與硬體實踐的關鍵內功 [來源: raw/06-memory-consumption.md §不同语言的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。

---

## 2. 核心運作步驟與關鍵性質
### (1) 程式執行期記憶體四大分區
在 C/C++ 體系中，程式載入執行時會被劃分為以下邏輯區域：
1. **程式碼區（Text Segment）**：儲存編譯後的二進位機器指令，為唯讀區以防誤改 [來源: raw/06-memory-consumption.md §C++的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。
2. **資料區 / 常數區（Data & BSS Segment）**：儲存全域變數、靜態變數與常數 [來源: raw/06-memory-consumption.md §C++的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。
3. **堆疊區（Stack）**：由編譯器自動分配與釋放，儲存函式區域變數、參數與返回位址，記憶體由高位址向低位址生長，速度極快但容量有限 [來源: raw/06-memory-consumption.md §C++的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。
4. **堆積區（Heap）**：由工程師透過 `new` / `malloc` 動態申請，由低位址向高位址生長，容量大但若未釋放易導致記憶體洩漏（Memory Leak）[來源: raw/06-memory-consumption.md §C++的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。

### (2) 基礎型態記憶體長度基準（64 位元架構常見配置）
- `char`：1 Byte
- `short`：2 Bytes
- `int`：4 Bytes
- `long`：4 或 8 Bytes
- `long long`：8 Bytes
- 指標型態（`T*`）：8 Bytes（64 位元定址空間）  
[來源: raw/06-memory-consumption.md §如何计算程序占用多大内存 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)

### (3) 記憶體對齊（Memory Alignment）原理與規則
- **硬體物理成因**：現代 CPU 並非以單一位元組為單位隨意讀取記憶體，而是以特定區塊大小（例如 4 Bytes 或 8 Bytes）為對齊步長。如果一個 4-byte 整數放在非 4 的倍數位址上，CPU 必須執行兩次記憶體存取、移位與拼接才能取回資料，嚴重降低效能 [來源: raw/06-memory-consumption.md §内存对齐 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。
- **編譯器填充（Padding）**：
  編譯器會在結構體成員之間自動塞入填充位元組，使變數偏移量為其自身大小的整數倍，結構體總大小亦為最大成員大小的整數倍 [來源: raw/06-memory-consumption.md §内存对齐 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。

---

## 3. 重要數據與複雜度證據
考慮以下結構體：
```cpp
struct Example {
    char a;   // 佔 1 byte
              // 編譯器自動填充 3 bytes padding
    int b;    // 佔 4 bytes（位址必須是 4 的倍數）
};
```
- 初學者直覺計算：$1 + 4 = 5$ Bytes。
- 實際記憶體佔用：經過對齊後為 **8 Bytes** [來源: raw/06-memory-consumption.md §内存对齐 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)。

---

## 4. 嚴格收錄之雙重出處清單
1. [來源: raw/06-memory-consumption.md §如何计算程序占用多大内存 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)
2. [來源: raw/06-memory-consumption.md §C++的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)
3. [來源: raw/06-memory-consumption.md §不同语言的内存管理 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)
4. [來源: raw/06-memory-consumption.md §内存对齐 | 原始連結](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md)

