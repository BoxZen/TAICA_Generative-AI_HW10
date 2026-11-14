# 原始資料摘要：程式記憶體消耗與底層管理 (Memory Consumption)

> **原始文章標題**：刷了这么多题，你了解自己代码的内存消耗么？  
> **原始連結**：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md  
> **擷取日期**：2026-11-14  
> **對應本地檔案**：[raw/06-memory-consumption.md](file:///d:/Code/Antigravity/TAICA_Generative-AI_HW10/raw/06-memory-consumption.md)

---

## 1. 核心主題概述
本篇從計算機系統與程式語言底層視角，深入解析軟體執行時的記憶體分配機制。涵蓋常見語言（C/C++、Java、Python）記憶體管理差異、C++ 程式執行期記憶體四/五大分區、基礎資料型態大小以及**記憶體對齊（Memory Alignment）**的硬體原因與計算規則。

## 2. 涵蓋演算法與核心知識點
- **程式語言記憶體管理模式差異**：
  - C/C++：堆疊與堆積空間明確區分，堆積空間（`malloc`/`free` 或 `new`/`delete`）完全由程式設計師手動管理。
  - Java / Python / Go：具備垃圾回收機制（Garbage Collection, GC），執行期自動追蹤並釋放無用物件。
- **C/C++ 記憶體分區模型**：
  1. **程式碼區（Text Segment）**：存放編譯後的 CPU 二進位機器指令，通常為唯讀。
  2. **資料區 / 常數區（Data & BSS Segment）**：存放已初始化與未初始化的全域變數、靜態變數及常數字串。
  3. **堆疊區（Stack）**：由編譯器自動分配與釋放，儲存函式參數、區域變數與返回位址，生長方向由高位址往低位址。
  4. **堆積區（Heap）**：由工程師動態申請與釋放，空間較大，生長方向由低位址往高位址。
- **基礎資料型態長度基準（64 位元架構常見配置）**：
  - `char`：1 Byte
  - `short`：2 Bytes
  - `int`：4 Bytes
  - `long`：4 或 8 Bytes（視作業系統資料模型而定）
  - `long long`：8 Bytes
  - 指標型態（`T*`）：8 Bytes（64 位元定址空間）
- **記憶體對齊（Memory Alignment）**：
  - **硬體原因**：現代 CPU 以特定寬度（如 4 Bytes 或 8 Bytes）的記憶體區塊進行存取。若資料跨越對齊邊界，CPU 必須進行兩次記憶體讀取與移位拼湊，造成效能耗損。
  - **對齊規則**：結構體變數首位址必須是對齊數的倍數，成員變數偏移量為該成員大小的整數倍，結構體總大小必須為其最大成員大小的整數倍（透過編譯器自動 Padding 填充）。

## 3. 重要實例數據
- 結構體範例：
  ```cpp
  struct Example {
      char a;   // 1 byte
      // 填充 3 bytes padding
      int b;    // 4 bytes
  }; // 總大小為 8 bytes，而非 5 bytes！
  ```

## 4. 關聯核心概念頁面
- [程式記憶體配置與對齊 (Memory Management)](../concepts/memory-management.md)
- [空間複雜度 (Space Complexity)](../concepts/space-complexity.md)
- [時間與空間權衡 (Time-Space Tradeoff)](../syntheses/time-space-tradeoff.md)
