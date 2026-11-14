# 不可忽視的代價：空間複雜度與記憶體管理

- **空間定義**：衡量執行期動態記憶體規模 $S(n)$，絕非編譯產出之執行檔大小。
- **底層分區**：涵蓋程式碼區、常數資料區、函式堆疊區（Stack）與動態堆積區（Heap）。
- **硬體對齊**：CPU 區塊存取規範促使編譯器填充位元組，結構體大小往往大於各欄位總和。
- **邊界警訊**：動態開闢表格防範記憶體超限（MLE），深層呼叫防範堆疊溢位。

來源出處：wiki/concepts/space-complexity.md , raw/04-space-complexity.md , https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md
