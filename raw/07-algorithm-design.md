> **原始文章標題**：algorithm design - 演算法筆記
> **原始連結**：https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
> **擷取日期**：2026-11-14

# algorithm design - 演算法筆記

## incremental method

> 不積跬步，無以至千里。不積小流，無以成江海。《荀子》

### incremental method

「遞增法」是符合電腦運作特性的方法。電腦執行程式，一次只做一個動作，完成了一件事才做下一件事。當一個問題太大太多時，化整為零、一個一個解決吧！

合抱之木，生於毫末；九層之臺，起於累土；千里之行，始於足下。謹以此句與大家共勉。

### 範例：加總數字

無論電腦再怎麼強，還是得一個一個累加數字。

![Incremental1.png](https://web.ntnu.edu.tw/~algo/Incremental1.png)

```cpp
void summation()
{
	int array[5] = {3, 6, 9, -8, 1};

	int sum = 0;
	for (int i=0; i<5; i++)
		sum += array[i];

	cout << "總和是" << sum;
}
```

```cpp
int summation(int array[], int n)
{
	int sum = 0;
	for (int i=0; i<n; i++)
		sum += array[i];
	return sum;
}
```

### 範例：複製字串

無論電腦再怎麼強，還是得逐字複製。

![Incremental2.png](https://web.ntnu.edu.tw/~algo/Incremental2.png)

```cpp
void copy()
{
	char s[15] = "incremental";
	char t[15];

	int i;
	for (i=0; s[i] != '\0'; i++)
		t[i] = s[i];
	t[i] = '\0';

	cout << "原本字串" << s;
	cout << "複製之後的字串" << t;
}
```

```cpp
void copy(char* s, char* t)
{
	int i;
	for (i=0; s[i]; i++)
		t[i] = s[i];
	t[i] = '\0';
}
```

### 範例：選擇排序法（selection sort）

找到第一小的數字，放在第一個位置；再找到第二小的數字，放在第二個位置。一次找一個數字，如此下去就會把所有數字按照順序排好了。

![Incremental3.png](https://web.ntnu.edu.tw/~algo/Incremental3.png)

```cpp
void selection_sort()
{
	int array[5] = {3, 6, 9, -8, 1};

	for (int i=0; i<5; i++)
	{
		// 從尚未排序的數字當中，找到第i小的數字。
		int min_index = i;
		for (int j=i+1; j<5; j++)
			if (array[j] < array[min_index])
				min_index = j;

		// 把第i小的數字，放在第i個位置。
		swap(array[i], array[min_index]);
	}

	// 印出排序結果。
	for (int i=0; i<5; i++)
		cout << array[i];
}
```

```cpp
void selection_sort(int array[], int n)
{
	for (int i=0; i<n; i++)
	{
		// 從尚未排序的數字當中，找到第i小的數字。
		int min_index = i;
		for (int j=i+1; j<n; j++)
			if (array[j] < array[min_index])
				min_index = j;

		// 把第i小的數字，放在第i個位置。
		swap(array[i], array[min_index]);
	}
}
```

### 範例：印出直角三角形

多字成行，多行成直角三角形。由細微的東西開始，一件一件組起來。

![Incremental4.png](https://web.ntnu.edu.tw/~algo/Incremental4.png)

```cpp
// 多字成行
void print_line(int n)	// n 是一行的長度
{
	for (int i=1; i<=n; i++) cout << '@';
	cout << '\n';
}

// 多行成直角三角形
void print_triangle(int n)	// n 是行數
{
	for (int i=n; i>=1; i--) print_line(i);
}
```

### 範例：人潮最多的時段（interval partitioning problem）

一群訪客參加宴會，我們詢問到每一位訪客的進場時刻與出場時刻，請問宴會現場擠進最多人的時段。

換個視角。想像會場門口裝著一支監視器。有訪客進入，會場就多一人；有訪客離開，會場就少一人。如此就很容易統計會場人數。遞增的標的是時刻，而不是訪客。

【註：這個技巧在中文網路稱作「離散化」。】

![Incremental5.png](https://web.ntnu.edu.tw/~algo/Incremental5.png)

```cpp
struct Guest {int arrival, leave;} g[10];

bool cmp(int i, int j)
{
	return abs(i) < abs(j);
}

void maximum_guest()
{
	vector<int> time;
	for (int i=0; i<10; i++)
	{
		time.push_back(+g[i].arrival);
		time.push_back(-g[i].leave);
	}

	sort(time.begin(), time.end(), cmp);

	int n = 0, maximum = 0;
	for (int i=0; i<time.size(); i++)
	{
		if (time[i] >= 0)
			n++;
		else
			n--;

		maximum = max(maximum, n);
	}
	cout << "人潮最多的時段有" << maximum << "人";
}
```

此處僅找出人數。找出人潮最多的時段，就留給各位自行嘗試吧。

### 範例：儲存座標

遞增的標的，主為點，次為座標軸。

![Incremental6.png](https://web.ntnu.edu.tw/~algo/Incremental6.png)

```cpp
struct Point {float x, y;} p[5] =
{
	{0, 1}, {1, 2}, {3, 0}, {2, 2}, {3, 1}
};
```

遞增的標的，主為座標軸，次為點。

![Incremental7.png](https://web.ntnu.edu.tw/~algo/Incremental7.png)

```cpp
float x[5] = {0, 1, 3, 2, 3};
float y[5] = {1, 2, 0, 2, 1};
```

### 範例：印出轉換成小寫的字串

![Incremental8.png](https://web.ntnu.edu.tw/~algo/Incremental8.png)

有需要改變的，只有大寫字母──如果是大寫字母，就轉換成小寫字母並且印出；如果不是大寫字母，就直接印出。

```cpp
void print_lowercase()
{
	char s[15] = "Hello World!";

	for (int i=0; s[i]; i++)
		if (s[i] >= 'A' && s[i] <= 'Z')
			cout << (char)(s[i] - 'A' + 'a');
		else
			cout << s[i];
}
```

也可以一步一步進行：（一）複製一份字串（二）字串轉換成小寫（三）印出字串。

```cpp
void print_lowercase()
{
	char s[15] = "Hello World!";
	char t[15];

	// 第一波：複製一份字串
	for (int i=0; s[i]; i++)
		t[i] = s[i];

	// 第二波：字串轉換成小寫
	for (int i=0; s[i]; i++)
		if (t[i] >= 'A' && t[i] <= 'Z')
			t[i] = t[i] - 'A' + 'a';

	// 第三波：印出字串
	cout << t;
}
```

```cpp
void print_lowercase()
{
	char s[15] = "Hello World!";
	char t[15];

	// 每一波的程式碼可以自行包裝成為函式，
	// 亦可套用標準函式庫。
	my_copy(s, t);		// 複製字串
	my_lowercase(t);	// 換成小寫
	cout << t;			// 印出字串
}
```

第一種解法稱作one-pass，資料只會讀取一遍。讀取資料的同時，也一口氣處理掉所有事情。

第二種解法稱作multi-pass，資料會重複讀取許多遍。所有事情劃分成數個階段，逐步處理，每個階段只專心處理一件事情。

one-pass的優點是：程式碼簡短、執行時間也短。缺點是：程式碼不易編修。

multi-pass的優點是：程式碼一目了然，容易編修、測試、除錯；程式碼可以包裝成為函式，也有機會套用標準函式庫。缺點是：需要額外的暫存記憶體。

這兩種方式各有利弊。程式員必須自行取捨。

### 範例：對調數字

利用一個變數，暫存其中一個數字，以便對調。

![Incremental9.png](https://web.ntnu.edu.tw/~algo/Incremental9.png)

```cpp
void swap_int()
{
	int a = 0, b = 1;

	// 交換a與b
	int temp = a;
	a = b;
	b = temp;

	cout << a << ' ' << b;
}
```

```cpp
void swap_int(int& a, int& b)
{
	int temp = a;
	a = b;
	b = temp;
}
```

### 範例：對調陣列

節省記憶體的方法：採用遞增法，逐一對調數字。

![Incremental10.png](https://web.ntnu.edu.tw/~algo/Incremental10.png)

```cpp
void swap_int_array()
{
	int a[5] = {3, 6, 9, -8, 1};
	int b[5] = {9, 8, 7, 6, 5};

	// one-pass
	for (int i=0; i<5; i++)
	{
		int temp = a[i];
		a[i] = b[i];
		b[i] = temp;
	}
}
```

浪費記憶體的方法：建立一條陣列，暫存其中一條陣列。

![Incremental11.png](https://web.ntnu.edu.tw/~algo/Incremental11.png)

```cpp
void swap_int_array()
{
	int a[5] = {3, 6, 9, -8, 1};
	int b[5] = {9, 8, 7, 6, 5};

	// multi-pass
	int temp[5];
	for (int i=0; i<5; i++) temp[i] = a[i];
	for (int i=0; i<5; i++) a[i] = b[i];
	for (int i=0; i<5; i++) b[i] = temp[i];
}
```

```cpp
void swap_int_array()
{
	int a[5] = {3, 6, 9, -8, 1};
	int b[5] = {9, 8, 7, 6, 5};

	// multi-pass
	int temp[5];
	my_copy(a, temp);
	my_copy(b, a);
	my_copy(temp, b);
}
```

## memoization

> 惟事事，乃其有備，有備無患。《書經》

### memoization

「記憶法」是符合電腦運作特性的方法。電腦擁有大量儲存空間。只要將計算過的數值，儲存於記憶體，往後就能直接使用記憶體儲存的資料，不必再浪費時間重複計算一遍。

```
memoization（tabulation）
演算法執行過程之中，即時更新數值，儲存於記憶體。
例如堆疊的大小。

precomputation（precalculation）（preprocessing）
演算法開始之時，預先計算數值，儲存於記憶體。
例如圓周率、字串的長度、質數的表格。
```

如果要儲存大量的、同性質的數值，我們可以將這些數值整理成一個表格（通常是陣列），以方便查閱──稱作「查詢表lookup table」。例如質數表便是一個「查詢表」。

### 範例：陣列大小

使用一個變數，記錄資料數量，以便迅速地增加資料。

![Memoization1.png](https://web.ntnu.edu.tw/~algo/Memoization1.png)

```cpp
void array_size()
{
	int array[100];
	int n = 0;		// 使用一個變數，記錄資料數量。
	array[n++] = 3;	// 以便迅速地增加資料。
	array[n++] = 6;
	array[n++] = 9;
	cout << n;
}
```

C++標準函式庫的stack，事實上也額外隱含了一個變數，記錄資料數量。當堆疊塞入資料、彈出資料的時候，也就是呼叫push函式、呼叫pop函式的時候，就默默更新資料數量。

```cpp
void stack_size()
{
	stack<int> s;		// C++標準函式庫的stack
	s.push(1);			// 默默地n++
	s.pop();			// 默默地--n
	cout << s.size();	// 把n印出來
}
```

### 範例：加總數字

利用一個變數，累計數字的總和。

![Memoization2.png](https://web.ntnu.edu.tw/~algo/Memoization2.png)

```cpp
void summation()
{
	int array[5] = {3, 6, 9, -8, 1};

	int sum = 0;
	for (int i=0; i<5; i++)
		sum += array[i];

	cout << "總和是" << sum;
}
```

```cpp
int summation(int array[], int n)
{
	int sum = 0;
	for (int i=0; i<n; i++)
		sum += array[i];
	return sum;
}
```

### 範例：統計字母數量

建立26格的陣列，讓字母a到z依序對應陣列的每一格，作為lookup table。一邊讀取字串，一邊累計字母出現次數。

![Memoization3.png](https://web.ntnu.edu.tw/~algo/Memoization3.png)

```cpp
void count_letter_frequency()
{
	char s[15] = "Hello World!";
	int c[26] = {};

	// 字母一律換成小寫
	for (int i=0; s[i]; i++)
		if (s[i] >= 'A' && s[i] <= 'Z')
			s[i] = s[i] - 'A' + 'a';

	// 統計字母數量
	for (int i=0; s[i]; i++)
		if (s[i] >= 'a' && s[i] <= 'z')
			c[s[i] - 'a']++;

	// 印出統計結果
	for (int i=0; i<26; i++)
		cout << char('a'+i) << ':' << c[i] << '\n';
}
```

### 範例：統計數字數量

當數字範圍太大，無法建立那麼大的陣列，可以改用hash table、binary search tree等等資料結構作為lookup table。

![Memoization4.png](https://web.ntnu.edu.tw/~algo/Memoization4.png)

```cpp
void histogram()
{
	int array[10] =
	{
		1, 3, 4, 10, 11,
		1000000000, 23, 99, 123, 514
	};
//	int c[1000000000] = {};
	map<int, int> c;	// binary search tree

	// 統計數字數量
	for (int i=0; i<10; i++)
		c[array[i]]++;

	// 印出統計結果
	for (auto i: c)
		cout << i.first << ':' << i.second << '\n';
}
```

### 範例：計數排序法（counting sort）

建立足夠長的陣列，讓數字對應陣列的每一格，作為lookup table。統計每個數字的出現次數。由小到大讀取lookup table，順便排序數字。

![Memoization5.png](https://web.ntnu.edu.tw/~algo/Memoization5.png)

```cpp
void counting_sort()
{
	int array[5] = {3, 6, 9, 9, 1};
	int c[9 + 1] = {};

	// 統計數字數量
	for (int i=0; i<5; i++)
		c[array[i]]++;

	// 由小到大讀取lookup table，順便排序數字。
	for (int j=0, i=0; j<10 && i<5; j++)
		while (c[j] > 0)
		{
			c[j]--;
			array[i++] = j;
		}
}
```

### 範例：求1到n的全部整數的立方和，n的範圍由1到10。

![Memoization6.png](https://web.ntnu.edu.tw/~algo/Memoization6.png)

以直接的方式，累加每個立方數。（儘管這個問題有公式解，但是為了方便舉例，所以這裡不採用公式解。）

```cpp
int sum_of_cubes(int n)
{
	int sum = 0;
	for (int i=1; i<=n; i++)
		sum += i * i * i;
	return sum;
}

void print_sum_of_cubes()
{
	int n;
	while (cin >> n && n > 0)
		cout << sum_of_cubes(n);
}
```

使用memoization。建立11格的陣列，每一格依序對應0到10的立方數，作為lookup table。一旦計算完畢，就儲存至表格；往後就直接讀取表格，不需重複計算。

```cpp
int sum_of_cubes(int n)
{
	// 其值為 0 表示沒有存入答案
	static int answer[10 + 1] = {};

	// 如果已經計算過，就直接讀取表格的答案。
	if (answer[n] != 0) return answer[n];

	// 如果不曾計算過，就計算一遍，儲存答案。
	int sum = 0;
	for (int i=1; i<=n; i++)
		sum += i * i * i;
	return answer[n] = sum;
}

void print_sum_of_cubes()
{
	int n;
	while (cin >> n && n > 0)
		cout << sum_of_cubes(n);
}
```

使用preprocessing。

```cpp
void print_sum_of_cubes()
{
	// 預先建立立方數表格
	int cube[10 + 1];
	for (int i=1; i<=10; i++)
		cube[i] = i * i * i;

	int n;
	while (cin >> n && n > 0)
	{
		// 直接讀取表格的立方數
		int sum = 0;
		for (int i=1; i<=n; i++)
			sum += cube[i];
		cout << sum;
	}
}
```

preprocessing當然也可以直接算答案啦。

```cpp
int sum_of_cubes(int n)
{
	int sum = 0;
	for (int i=1; i<=n; i++)
		sum += i * i * i;
	return sum;
}

void print_sum_of_cubes()
{
	// 預先計算所有答案
	int answer[10 + 1];
	for (int i=1; i<=10; i++)
		answer[i] = sum_of_cubes(i);

	// 直接讀取表格的答案
	int n;
	while (cin >> n && n > 0)
		cout << answer[n];
}
```

最後是preprocessing的極致。

```cpp
void print_sum_of_cubes()
{
	// 預先計算答案，寫死在程式碼裡面。
	int answer[10 + 1] =
	{
		0, 1, 9, 36, 100, 225,
		441, 784, 1296, 2025, 3025
	};

	// 直接讀取表格的答案
	int n;
	while (cin >> n && n > 0)
		cout << answer[n];
}
```

### 範例：印出方框

建立二維陣列：陣列的格子，依序對應視窗的文字。

![Memoization7.png](https://web.ntnu.edu.tw/~algo/Memoization7.png)

不直接印出方框，而是間接填至陣列。不必數空白鍵，只需兩條水平線和兩條垂直線。

```cpp
void print_square_border()
{
	// 建立記憶體
	char array[5][5];

	// 預先填入空白鍵
	for (int i=0; i<5; i++)
		for (int j=0; j<5; j++)
			array[i][j] = ' ';

	// 填入方框：兩條水平線、兩條垂直線
	// 即便相互重疊也無所謂
	for (int i=0; i<5; i++) array[0][i] = '@';
	for (int i=0; i<5; i++) array[4][i] = '@';
	for (int i=0; i<5; i++) array[i][0] = '@';
	for (int i=0; i<5; i++) array[i][4] = '@';

	// 印出方框
	for (int i=0; i<5; i++)
	{
		for (int j=0; j<5; j++)
			cout << array[i][j];
		cout << '\n';
	}
}
```

### 範例：拆開迴圈（loop unrolling）

![Memoization8.png](https://web.ntnu.edu.tw/~algo/Memoization8.png)

迴圈語法的功能是：一段指令，重覆實施數次，但是每次都稍微變動一點點。

事實上，我們可以反璞歸真，拆開迴圈，還原成數行指令。如此一來，就節省了迴圈每次累加變數的時間，也節省了迴圈每次判斷結束條件的時間。

拆開迴圈是一種preprocessing，預先計算迴圈變量、預先計算迴圈結束條件。

拆開迴圈之後，雖然降低了程式的執行時間，但是也降低了程式可讀性。程式員必須自行取捨。

## enumeration

> 愚者千慮，必有一得。《史記》

### enumeration

「枚舉法」利用了電腦無與倫比的計算速度。找到不確定的變數，枚舉所有可能性，逐一判斷正確性。

```
enumerate
一筆一筆列出所有資料。
對應到程式語言的for。

search
瀏覽所有資料，找出需要的部份。
對應到程式語言的for加if。
```

收集充分資訊，就能解決問題。

![Enumeration1.png](https://web.ntnu.edu.tw/~algo/Enumeration1.png)

### 範例：枚舉一百個平方數

採用直接法：依序枚舉數字1到100；枚舉過程當中，將數字平方得到平方數。

![Enumeration2.png](https://web.ntnu.edu.tw/~algo/Enumeration2.png)

```cpp
void generate_squares()
{
	for (int i=1; i<=100; i++)
		cout << i*i << "是平方數";
}
```

採用試誤法：依序枚舉數字1到∞；枚舉過程當中，判斷數字是不是平方數。

![Enumeration3.png](https://web.ntnu.edu.tw/~algo/Enumeration3.png)

```cpp
void generate_squares()
{
	for (int i=1; i<=100*100; i++)
	{
		int sqrt_i = sqrt(i);
		if (sqrt_i * sqrt_i == i)
			cout << i << "是平方數";
	}
}
```

### 範例：尋找陣列裡的最小值

由小到大枚舉陣列索引值，逐一比較陣列元素。

![Enumeration4.png](https://web.ntnu.edu.tw/~algo/Enumeration4.png)

```cpp
void find_minimum()
{
	int array[5] = {3, 6, 9, -8, 1};

	int min = 2147483647;
	for (int i=0; i<5; i++)	// 枚舉索引值
		if (array[i] < min)	// 比較元素
			min = array[i];	// 隨時記錄最小值

	cout << "最小的數字是" << min;
}
```

```cpp
int find_minimum(int array[], int n)
{
	int min = 2147483647;
	for (int i=0; i<n; i++)	// 枚舉索引值
		if (array[i] < min)	// 比較元素
			min = array[i];	// 隨時記錄最小值
	return min;
}
```

### 範例：尋找陣列裡的特定數字（sequential search）

找到所有特定數字：瀏覽一遍所有數字。

![Enumeration5.png](https://web.ntnu.edu.tw/~algo/Enumeration5.png)

```cpp
void find_all_number()
{
	int array[5] = {3, 6, 9, -8, 1};

	for (int i=0; i<5; i++)	// 枚舉
		if (array[i] == 6)	// 搜尋
			cout << i << ':' << array[i] << '\n';
}
```

找到其中一個特定數字：一旦找到，立即停止瀏覽，以節省時間。

![Enumeration6.png](https://web.ntnu.edu.tw/~algo/Enumeration6.png)

```cpp
void find_number()
{
	int array[5] = {3, 6, 9, -8, 1};

	for (int i=0; i<5; i++)	// 枚舉
		if (array[i] == 6)	// 搜尋
		{
			cout << i << ':' << array[i];
			break;
		}
}
```

```cpp
int find_number(int array[], int n, int num)
{
	for (int i=0; i<n; i++)
		if (array[i] == num)
			return i;
	return -1;
}
```

### 範例：尋找二維陣列裡的特定數字

![Enumeration7.png](https://web.ntnu.edu.tw/~algo/Enumeration7.png)

多個元素成為一個橫條、多個橫條成為一個陣列。內層先枚舉元素，外層再枚舉橫條，就能枚舉所有元素。

方才是由內而外、由小到大進行思考，其實也可以由外而內、由大到小進行思考：外層先枚舉每一個橫條，內層再枚舉一個橫條的每一個元素，就能枚舉所有元素。

```cpp
bool find_number(int n)
{
	int array[3][5] =
	{
		{3, 6, 9, -8, 1},
		{2, 4, 6, 8, 10},
		{11, 7, 5, 3, 2}
	};

	// 外層枚舉每一個橫條
	for (int i=0; i<3; i++)
		// 內層枚舉一個橫條的每一個元素
		for (int j=0; j<5; j++)
			// 就能枚舉所有元素
			if (array[i][j] == n)
				return true;
	return false;
}
```

此處再介紹一種特別的思考方式：第一層枚舉每一個橫條，第二層枚舉每一個直條，就能枚舉所有直條與橫條的交錯之處。

雖然前後兩個思考方式完全不同，但是前後兩支程式碼卻完全相同。

```cpp
bool find_number(int n)
{
	int array[3][5] =
	{
		{3, 6, 9, -8, 1},
		{2, 4, 6, 8, 0},
		{7, 5, 3, 2, 1}
	};

	// 第一層枚舉每一個橫條
	for (int i=0; i<3; i++)
		// 第二層枚舉每一個直條
		for (int j=0; j<5; j++)
			// 就能枚舉所有橫條與直條交錯之處
			if (array[i][j] == n)
				return true;
	return false;
}
```

### 範例：平面上距離最近的兩個點（closest pair）

![Enumeration8.png](https://web.ntnu.edu.tw/~algo/Enumeration8.png)

第一層枚舉第一個點，第二層枚舉第二個點。為了避免重複枚舉相同的一對點，第二層只枚舉索引值更高的點。

```cpp
void closest_pair()
{
	float point[10][2] =
	{
		{3, 3}, {1, 5}, {4, 6}, {2, 8}, {9, 9},
		{2, 1}, {7, 2}, {6, 5}, {9, 4}, {5, 9}
	};

	// 距離最近的兩個點的距離
	float d = 1e9;

	// 枚舉第一點
	for (int i=0; i<10; i++)
		// 枚舉第二點
		for (int j=i+1; j<10; j++)
		{
			// 計算第一點到第二點的距離
			float dx = point[i][0] - point[j][0];
			float dy = point[i][1] - point[j][1];
			float dij = sqrt(dx * dx + dy * dy);

			// 記錄最短的距離
			if (dij < d) d = dij;
		}
	cout << "距離是" << d;
}
```

可以把計算距離的程式碼，抽離出來成為一個函式。好處是程式碼變得清爽許多，增加程式碼可讀性。壞處是大量呼叫函式，導致執行時間變長。

```cpp
struct Point {float x, y;};

// 計算兩點之間的距離
float dist(Point a, Point b)
{
	float dx = a.x - b.x;
	float dy = a.y - b.y;
	return sqrt(dx * dx + dy * dy);
}

void closest_pair()
{
	Point point[10] =
	{
		{3, 3}, {1, 5}, {4, 6}, {2, 8}, {9, 9},
		{2, 1}, {7, 2}, {6, 5}, {9, 4}, {5, 9}
	};

	float d = 1e9; 
	for (int i=0; i<10; i++) 
		for (int j=i+1; j<10; j++)
			// 記錄最短的距離
			d = min(d, dist(point[i], point[j]));

	cout << "距離是" << d;
}
```

魚與熊掌不可兼得，這兩種程式碼各有優缺點，沒有絕對的好壞。程式員必須自行取捨。

### 範例：字串搜尋（string searching）

從長字串之中，找到短字串的出現位置。

![Enumeration9.png](https://web.ntnu.edu.tw/~algo/Enumeration9.png)

第一層先枚舉所有可以對齊的位置，第二層再枚舉所有需要對齊的字元。

```cpp
void string_searching()
{
	char text[15] = "It's a pencil.";
	char pattern[6] = "a pen";

	// 枚舉所有可以對齊的位置
	for (int i=0; i<15; i++)
	{
		// 枚舉所有需要對齊的字元
		bool find = true;
		for (int j=0; j<5; j++)
			if (text[i+j] != pattern[j])
				find = false;

		if (find)
			cout << "短字串出現在第" << i << "個字元";
	}
}
```

因為短字串不會超出長字串末段，所以第一層枚舉範圍可以再略微縮小。

因為只要一個相異字元，就足以表明對齊位置錯誤，所以第二層的枚舉過程可以提早結束。

```cpp
void string_searching()
{
	char text[15] = "It's a pencil.";
	char pattern[6] = "a pen";

	// 仔細估量枚舉範圍
	for (int i=0; i<15-6+1; i++)
	{
		bool find = true;
		for (int j=0; j<5; j++)
			if (text[i+j] != pattern[j])
			{
				find = false;
				break;
			}

		if (find)
			cout << "短字串出現在第" << i << "個字元";
	}
}
```

### 範例：統計字母數量

![Enumeration10.png](https://web.ntnu.edu.tw/~algo/Enumeration10.png)

第一層先枚舉26種英文字母，第二層再枚舉字串的所有字元，計算一種字母的數量。

```cpp
void count_letter()
{
	char s[15] = "Hello World!";

	// 字母統一換成小寫
	for (int i=0; s[i]; i++)
		if (s[i] >= 'A' && s[i] <= 'Z')
			s[i] = s[i] - 'A' + 'a';

	// 枚舉26種英文字母
	for (int i=0; i<26; i++)
	{
		// 枚舉字串的所有字元
		int c = 0;
		for (int j=0; s[j]; j++)
			if (s[j] == 'a' + i)
				c++;

		// 印出一種字母的數量
		cout << (char)('a' + i) << ':' << c;
	}
}
```

先前曾經介紹過統計字母數量的範例。先前範例當中，雖然耗費記憶體空間，但是執行時間短──簡單來說就是空間大、時間小。此處範例當中，則是空間小，時間大，恰恰相反。這兩種方式各有優缺點，程式員必須自行取捨。

### 範例：反轉字串

![Enumeration11.png](https://web.ntnu.edu.tw/~algo/Enumeration11.png)

兩個枚舉，一個從頭到尾，一個從尾到頭，步調相同，逐步對調字元。雖然是兩個枚舉，卻只有一個迴圈。

```cpp
void reverse_string()
{
	char s[15] = "Hello World!";

	// 兩個枚舉，一個從頭到尾，一個從尾到頭。
	for (int i=0, j=12; i<j; i++, j--)
		swap(s[i], s[j]);

	cout << "反轉之後的字串是" << s;
}
```

```cpp
void reverse(char* s)
{
	int n = strlen(s);
	for (int i=0; i<n/2; i++)
		swap(s[i], s[n-1-i]);
}
```

### 範例：尋找總和為10的區間

假設陣列元素只有正數。

![Enumeration12.png](https://web.ntnu.edu.tw/~algo/Enumeration12.png)

兩個枚舉，枚舉區間左端以及枚舉區間右端，都是從頭到尾，保持一左一右，視情況輪流枚舉。雖然是兩個枚舉，卻只有一個迴圈。

```cpp
void find_interval()
{
	int array[5] = {3, 6, 1, 7, 2};

	int sum = 0;
	for (int i=0, j=-1; j<5; )	// 枚舉區間[i, j]
	{
		if (sum > 10)
		{
			// 總和太大，區間左端往右縮短。
			sum -= array[i];
			i++;
		}
		else if (sum < 10)
		{
			// 總和太小，區間右端往右伸長。
			j++;
			sum += array[j];
		}
		else if (sum == 10)
		{
			// 總和剛好，
			// 區間左端往右縮短，
			// 亦得區間右端往右伸長。
			// 任選一種皆可。
//			sum -= array[i];
//			i++;
			j++;
			sum += array[j];
		}

		if (sum == 10)
			cout << '[' << i << ',' << j << ']';
	}
}
```

```cpp
void find_interval(int array[], int n, int num)
{
	int sum = 0;
	for (int i=0, j=0; j<=n; )	// 枚舉區間[i, j)
	{
		if (sum > num)
			sum -= array[i++];
		else
			sum += array[j++];

		if (sum == num)
			cout << '[' << i << ',' << j-1 << ']';
	}
}
```

讀者可以想想看：陣列元素若有零、有負數，是否要調整枚舉方式？

### 範例：尋找陣列之中的最小值，陣列已經由小到大排序

找到其中一個最小值：經常整理房間，尋找東西就快；預先排序資料，搜尋速度就快。

![Enumeration13.png](https://web.ntnu.edu.tw/~algo/Enumeration13.png)

```cpp
void find_minimum()
{
	int array[5] = {3, 3, 6, 6, 9};
	cout << "最小的數字是" << array[0];
}
```

找到所有最小值：讀者請自行嘗試。

### 範例：尋找陣列之中的特定數字，陣列已經由小到大排序

找到其中一個特定數字：首先找到陣列中央的數字，依其數字大小，繼續搜尋左半段或者右半段。

![Enumeration14.png](https://web.ntnu.edu.tw/~algo/Enumeration14.png)

```cpp
void find_number()
{
	int array[15] =
	{
		2, 3, 5, 7, 11,
		13, 17, 19, 23, 29,
		31, 37, 41, 43, 47
	};

	int left = 0, right = 15-1;
	while (left <= right)
	{
		int mid = left + (right - left) / 2;
		if (array[mid] < 29)
			left = mid + 1;		// 繼續搜尋剩下的右半段
		else if (array[mid] > 29)
			right = mid - 1;	// 繼續搜尋剩下的左半段
		else if (array[mid] == 29)
		{
			// 找到了其中一個數字
			cout << mid << ':' << array[mid];
			return;
		}
	}

	cout << "找不到29";
}
```

找到所有特定數字：讀者請自行嘗試。

### 範例：平面上距離最近的兩個點（closest pair）

![Enumeration15.png](https://web.ntnu.edu.tw/~algo/Enumeration15.png)

找到距離最近的其中一對點：預先依照X座標排序所有點，搜尋得以略過大量情況。

```cpp
struct Point {float x, y;};

// 計算兩點之間的距離
float dist(Point a, Point b)
{
	float dx = a.x - b.x;
	float dy = a.y - b.y;
	return sqrt(dx * dx + dy * dy);
}

bool cmp(Point a, Point b)
{
	return a.x < b.x;
}

void closest_pair()
{
	Point point[10] =
	{
		{3, 3}, {1, 5}, {4, 6}, {2, 8}, {9, 9},
		{2, 1}, {7, 2}, {6, 5}, {9, 4}, {5, 9}
	};

	// 依照X座標排序所有點
	sort(point, point+10, cmp);

	float d = 1e9; 
	for (int i=0; i<10; i++)
		for (int j=i+1; j<10; j++)
		{
			// 兩個點的X座標已經相距太遠，直接略過，
			// 繼續枚舉下一個左端點。
			if (point[j].x - point[i].x > d) break;
			d = min(d, dist(point[i], point[j]));
		}

	cout << "距離是" << d;
}
```

找到距離最近的每一對點：讀者請自行嘗試。

### 範例：英文單字從單數變複數

枚舉各種情況，寫成大量判斷式。

![Enumeration16.png](https://web.ntnu.edu.tw/~algo/Enumeration16.png)

```cpp
void plural(string s)
{
	int n = s.length();
	if (s.back() == 'y')
		cout << s.substr(0, n-1) << "ies";
	else if (s.back() == 's' || s.back() == 'x')
		cout << s << "es";
	else if (s.substr(n-2) == "sh" || s.substr(n-2) == "ch")
		cout << s << "es";
	else if (s.substr(n-3) == "man")
		cout << s.substr(0, n-3) << "men";
	else
		cout << s << 's';
}
```

### 範例：小畫家倒墨水（flood fill algorithm）

電腦圖片可以想成是一張方格紙，每個方格都填著一種顏色。現在要實現小畫家倒墨水的功能：以某一格為起點，只要相鄰方格顏色一樣，就染成同一個顏色。

![Enumeration17.png](https://web.ntnu.edu.tw/~algo/Enumeration17.png)

運用大量指令，枚舉上下左右四個方向；運用遞迴，枚舉相鄰同色方格。

必須避免已經枚舉過的方格又重複枚舉，否則程式在有生之年都不會結束。

```cpp
int image[10][10];	// 圖片的大小為 10x10

void flood(int x, int y, int new_color, int old_color)
{
	if (x>=0 && x<10 && y>=0 && y<10)	// 不能超出邊界
		if (image[x][y] == old_color)	// 同色方格才枚舉
		{
			// 染色
			image[x][y] = new_color;
			// 枚舉上下左右四個方向
			flood(x+1, y, new_color, old_color);
			flood(x-1, y, new_color, old_color);
			flood(x, y+1, new_color, old_color);
			flood(x, y-1, new_color, old_color);
		}
}

void ink()
{
	// 在座標(7,6)的方格，淋上1號顏色。
	flood(7, 6, 1, image[7][6]);
}
```

大量指令，亦得寫成一個迴圈。

```cpp
void flood(int x, int y, int new_color, int old_color)
{
	if (x>=0 && x<10 && y>=0 && y<10)
		if (image[x][y] == old_color)
		{
			image[x][y] = new_color;

			// 寫成一個迴圈
			for (int i=0; i<4; i++)
			{
				static int dx[4] = {1, -1, 0, 0};
				static int dy[4] = {0, 0, 1, -1};
				flood(x + dx[i], y + dy[i], new_color, old_color);
			}
		}
}
```

多層判斷式，亦得拆解成一層一層的判斷式。

```cpp
void flood(int x, int y, int new_color, int old_color)
{
	if (!(x>=0 && x<10 && y>=0 && y<10)) return;
	if (image[x][y] != old_color) return;

	image[x][y] = new_color;

	for (int i=0; i<4; i++)
	{
		static int dx[4] = {1, -1, 0, 0};
		static int dy[4] = {0, 0, 1, -1};
		flood(x + dx[i], y + dy[i], new_color, old_color);
	}
}
```

### 範例：三維函數繪圖

當問題太過困難，就增加限制，將部分變數改成常數。

一、固定X值，計算Y值Z值；嘗試各種X值。

二、固定Y值，計算X值Z值；嘗試各種Y值。

三、固定Z值，計算X值Y值；嘗試各種Z值。

![Enumeration18.gif](https://web.ntnu.edu.tw/~algo/Enumeration18.gif)

### straightforward method / trial and error

「直接法」，直接算出答案。例如按照流程進行得到答案、套用公式計算答案、直接印出答案。

「嘗試錯誤法」、「試誤法」，針對答案進行enumerate與search。有些困難的問題，難以直接推導答案，既然推導不出來，就慢慢測試答案、慢慢驗算吧──確立答案的範圍，窮舉所有可能的答案，再從中搜尋正確答案。

直接法和試誤法剛好相反。直接法是由題目本身下手，推導答案；試誤法則是從答案下手，讓答案迎合題目需求。

![Enumeration19.png](https://web.ntnu.edu.tw/~algo/Enumeration19.png)

### 範例：印出直角三角形

![Enumeration20.png](https://web.ntnu.edu.tw/~algo/Enumeration20.png)

先前介紹直接法，現在介紹試誤法。

窮舉一個正方形的所有位置，一一判斷是否屬於三角形區域。

```cpp
void print_triangle(int n)
{
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
			if (i + j < n)
				cout << '@';

		cout << '\n';
	}
}
```

### 範例：印出方框

![Memoization7.png](https://web.ntnu.edu.tw/~algo/Memoization7.png)

先前介紹直接法，現在介紹試誤法。

窮舉一個正方形的所有位置，一一判斷是否屬於方框區域。

```cpp
void print_square_border(int n)
{
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
			if (i == 0 || i == n-1 || j == 0 || j == n-1)
				cout << '@';
			else
				cout << ' ';

		cout << '\n';
	}
}
```

## backtracking

### backtracking

「回溯法」。枚舉多維度數值的方法。

由於內容較多較雜，另以專門頁面介紹。

## iterative method

> 道生一，一生二，二生三，三生萬物。《老子》

### iterative method

繁中「疊代法」、簡中「迭代法」、本站「迭代法」。不斷利用目前求得的數值，再求得新數值。

### 範例：字串變整數

![Iterative1.png](https://web.ntnu.edu.tw/~algo/Iterative1.png)

直覺的方式是遞增法。個、十、百、千、萬、……，每個位數分別乘上10的次方，通通加起來。此處按照高位數到低位數的順序進行處理，以符合字串的儲存順序。

![Iterative2.png](https://web.ntnu.edu.tw/~algo/Iterative2.png)

```cpp
// 計算字串長度
int string_length(char* s)
{
	int n = 0;
	while (s[n]) n++;
	return n;
}

// 計算10的exp次方
int pow10(int exp)
{
	int n = 1;
	for (int i=0; i<exp; i++)
		n *= 10;
	return n;
}

void string_to_integer()
{
	char s[10] = "26962869";

	// 預先計算字串長度。
	int length = string_length(s);

	// 依序處理高位數到低位數。
	int n = 0;
	for (int i=0; i<length; i++)
		n += (s[i] - '0') * pow10(length - 1 - i);

	cout << n;
}
```

更好的方式是迭代法！由高位數到低位數、也就是由左到右讀取字串，每讀取一個字元，就將數值乘以十、加上當前字元的對應數字。

![Iterative3.png](https://web.ntnu.edu.tw/~algo/Iterative3.png)

```cpp
void string_to_integer()
{
	char s[10] = "26962869";

	int n = 0;
	for (int i=0; s[i]; i++)
		n = n * 10 + s[i] - '0';

	cout << n;
}
```

同一個問題，有著不同的解法。有著程式碼很長、執行時間很長的方法，也有著程式碼很短，執行時間很短的方法。一支程式的好壞，除了取決於正確性和可讀性之外，同時也取決於計算方法。

### 範例：多項式函數求值（Horner's rule）

多項式函數，代入數值。一乘一加，不斷更迭，求得函數值。完全不需要次方運算。

![Iterative4.png](https://web.ntnu.edu.tw/~algo/Iterative4.png)

### 範例：除法

不斷乘以十、除以除數，就是一種迭代。

![Iterative5.png](https://web.ntnu.edu.tw/~algo/Iterative5.png)

### 範例：牛頓法（Newton's method）

找到連續函數等於零的位置。一開始隨便設定一個位置，不斷利用斜率求出下一個位置，就是一種迭代。

```
xₙ₊₁ = xₙ - f(xₙ) / f′(xₙ)
```

![Iterative6.png](https://web.ntnu.edu.tw/~algo/Iterative6.png)

### 範例：3n+1猜想（Collatz conjecture）

猜想的內容是這樣的：有一個整數，如果是偶數，就除以2；如果是奇數，就乘以3再加1。一個整數不斷這樣操作下去，最後一定會變成1。這個操作的過程就是一種迭代。

![Iterative7.png](https://web.ntnu.edu.tw/~algo/Iterative7.png)

至今尚未有人能夠證明其正確性。有趣的是，目前也尚未檢查出任何反例。

### 範例：生命遊戲（cellular automaton）

一個二維的方格平面，每個格子都有一個細胞，可能是活的，可能是死的。細胞的生命狀況，隨時間變動，變動規則如下：

```
復活：一個死細胞，其八個鄰居，有三個活細胞，則下一刻復活。
存活：一個活細胞，其八個鄰居，有兩個或三個活細胞，則下一刻存活。
死於孤單：一個活細胞，其八個鄰居，只有零個或一個活細胞，則下一刻死亡。
死於擁擠：一個活細胞，其八個鄰居，有四個以上活細胞，則下一刻死亡。
```

![Iterative8.png](https://web.ntnu.edu.tw/~algo/Iterative8.png)

實作時，我們可以弄兩張地圖，第一張地圖儲存現在這個時刻的狀態，第二張地圖儲存下一個時刻的狀態。兩張地圖交替使用，以節省記憶體空間。

實作時，我們可以切割概念、包裝成函式，讓程式碼易讀。

至今尚未有人能夠預測細胞最終會滅亡或延續。

```cpp
// 印出狀態
void print_board(bool board[5][5])
{
	for (int x=0; x<5; ++x)
	{
		for (int y=0; y<5; ++y)
			cout << (board[x][y] ? '@' : ' ');
		cout << '\n';
	}
	cout << '\n';
}

// 八個鄰居中，還活著的細胞數目。
int count_neighbor(int x, int y, bool board[5][5])
{
	static const int dx[8] = {-1,-1,-1,0,0,1,1,1};
	static const int dy[8] = {-1,0,1,-1,1,-1,0,1};

	int n = 0;
	for (int i=0; i<8; ++i)
	{
		int mx = x + dx[i];
		int my = y + dy[i];
		if (mx >= 0 && mx < 5 && my >= 0 && my < 5)
			n += board[mx][my];
	}
	return n;
}

// 判斷細胞死活
void go(int x, int y, bool board[5][5], bool next[5][5])
{
	int n = count_neighbor(x, y, board);
	if (!board[x][y])
		if (n == 3)					// 復活
			next[x][y] = true;
		else						// 仍舊死亡
			next[x][y] = board[x][y];
	else
		if (n == 2 || n == 3)		// 存活
			next[x][y] = true;
		else if (n == 0 || n == 1)	// 死於孤單
			next[x][y] = false;
		else if (n >= 4)			// 死於擁擠
			next[x][y] = false;
}

// 清空細胞
void clear_board(bool board[5][5])
{
	for (int x=0; x<5; ++x)
		for (int y=0; y<5; ++y)
			board[x][y] = false;
}

// 預先設定一些活的細胞
void load_board(bool board[5][5])
{
	board[3][1] = true;
	board[3][2] = true;
	board[3][3] = true;
	board[2][3] = true;
	board[1][2] = true;
}

void cellular_automaton()
{
	bool board[2][5][5] = {};
	clear_board(board[0]);
	load_board(board[0]);
	print_board(board[0]);

	// 迭代四回合
	for (int t=0; t<4; ++t)
	{
		for (int x=0; x<5; ++x)
			for (int y=0; y<5; ++y)
				go(x, y, board[t%2], board[(t+1)%2]);

		print_board(board[(t+1)%2]);
	}
}
```

### 範例：蘭頓的螞蟻（Langton's ant）

跟生命遊戲相似，不過這個遊戲更神奇。

```
一、格子有黑與白兩種顏色。
二、螞蟻走入白格則右轉，走入黑格則左轉。
三、螞蟻離開格子時，格子顏色顛倒。
```

驚人的是，乍看完全沒有規律的路線，卻在10647步之後開始循環。原因至今不明。

![Iterative9.gif](https://web.ntnu.edu.tw/~algo/Iterative9.gif)

### 範例：數學歸納法（mathematical induction）

數學歸納法的第二步驟，就是證明可不可以迭代！第二步驟的證明過程中一定會用到迭代！

```
1. 先證明 n = 1 成立。（有時候不見得要從1開始。）
2. 假設 n = k 成立，證明 n = k+1 也會成立。

當 1. 2. 得證，就表示 n = 1 ... ∞ 全部都成立。
```

### 範例：插入排序法（insertion sort）

從表面上來看，這是遞增法與枚舉法：第一層是遞增法，逐一把每個數字插入到左方已排序的陣列。第二層是枚舉法，搜尋插入位置；再將大量數字往右挪，以騰出空間插入數字。

但是從另一個視角來看，利用目前排序好的陣列，再求出更長的陣列，其實就是迭代法。

![Iterative10.png](https://web.ntnu.edu.tw/~algo/Iterative10.png)

### 範例：以試除法建立質數表

從表面上來看，這是兩層的枚舉法：第一層先枚舉正整數，一一試驗是否為質數；第二層再枚舉所有已知質數，一一試除。

但是從另一個視角來看，利用目前求得的質數，再求出更多質數，其實就是迭代法。

### 範例：十分逼近法

數線分割成十等份區間，從中找出正確區間，把對應的小數位數添到答案末端，然後不斷十等分下去。

利用目前求得的小數，再求出更多的小數，其實就是迭代法。

![Iterative11.png](https://web.ntnu.edu.tw/~algo/Iterative11.png)

### 範例：書塔（book stacking problem）

將書本一本一本疊起來，成為一座斜塔，越斜越好。

![Iterative12.png](https://web.ntnu.edu.tw/~algo/Iterative12.png)

對於任何一本書來說，其上方所有書本的整體重心，必須落在這本書上，這本書才能平穩地支撐住上方所有書本。

將書本插入到書塔底部，讓書塔的重心落在書本邊緣，就可以讓書塔最斜。插入書本到書塔底部之後，就更新書塔的重心位置，以便稍後插入下一本書本。

不斷插入書本到書塔底部、更新書塔重心，運用先前的書塔求得新的書塔──這段過程就是一種迭代。

### 範例：交卷

考試結束了，學生要交卷，老師要收卷。大家將手上的考卷，不斷傳遞給其他人，不斷匯集給老師。一個人不能同時交卷和收卷，一個人不能同時交卷給多人（搗亂），一個人不能同時向多人收卷（手忙腳亂）。假設每個人交卷速度一致，請讓整個過程越短越好。

![Iterative13.png](https://web.ntnu.edu.tw/~algo/Iterative13.png)

每個人隨時都在收卷交卷，一定最省時。老師亦然，一直處於收卷狀態，一定最省時。

遞增的標的，選定為老師。老師每次收卷，直接複製貼上前面幾次收卷的部屬方式，是最好的──這段過程就是一種迭代。

## recursive method

> 易有大恒，是生兩檥。兩檥生四馬，四馬生八卦。《易傳》

### recursive method

繁中「遞迴法」、簡中「递归法」、本站「遞迴法」。重複運用相同手法，縮減問題範圍，直到釐清細節。

### 範例：碎形（fractal）

利用相同手法繪圖，繪圖範圍越來越精細。

圖中的碎形稱作Sierpinski triangle。凡是尖端朝上的正三角形，就在當中放置一個尖端朝下的正三角形；放置之後，圖形就變得更細膩，範圍就變得更小了。

![Recursive1.png](https://web.ntnu.edu.tw/~algo/Recursive1.png)

圖中的碎形稱作Kosh snowflake。一條邊三等分，去除中段，朝外補上兩段，形成尖角。

![Recursive2.png](https://web.ntnu.edu.tw/~algo/Recursive2.png)

圖中的碎形稱作Pythagoras tree。不斷繪製正方形、直角三角形，看起來像是一棵茂密的樹。

## divide-and-conquer method

> 凡治眾如治寡，分數是也。鬥眾如鬥寡，形名是也。《孫子》

### divide-and-conquer method

「分治法」。分割問題、各個擊破。將一個大問題，分割成許多小問題。如果小問題還是很難，就繼續分割成更小的問題，直到問題變得容易解決。

分割出來的小問題，稱作「子問題subproblem」。解決一個問題，等價於解決所有子問題。

用樹狀圖表達原問題與子問題的關係，最好不過！

![DivideAndConquer1.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer1.png)

分治法著重分割問題的方式──要怎麼分割問題，使得子問題簡單又好算？各位讀者可以藉由本文的範例，體會分割問題的方式。

### 範例：分解動作

想要學習「從中場帶球上籃」，我們可以將此動作分割為「跑步運球」、「跑步收球」、「單手將球放入籃框」等動作，分別學習。每一項動作都熟練之後，組合起來便是帶球上籃了。

如果覺得「跑步運球」還是太難，可以更細分成「原地運球」、「走動運球」、「運球時護球」等動作，克服了之後便能夠順利解決「跑步運球」的問題了。

![DivideAndConquer2.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer2.png)

### 範例：方格法求面積

左邊為原問題，右邊放大並細分的圖是其中一個子問題。

![DivideAndConquer3.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer3.png)

### 範例：分類數數

左邊最大的框框是原問題，將原問題的數字進行分類後再統計，分類後的每一個框框都是一個子問題。

![DivideAndConquer4.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer4.png)

### recursive method

在分治法當中，亦得遞迴地分割問題，其實就是遞迴法。

![DivideAndConquer5.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer5.png)

程式碼細分為三個階段：divide、conquer、combine。divide階段是把原問題分割成小問題，conquer階段是解決小問題，combine階段是運用小問題的解答，整理出原問題的解答。

![DivideAndConquer6.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer6.png)

```cpp
divide_and_conquer(原問題)
{
	/* divide */
	先將原問題分割成許多小問題;

	/* conquer */
	遞迴呼叫函式，求得子問題的解;
	解答1 = divide_and_conquer(子問題1);
	解答2 = divide_and_conquer(子問題2);
	......

	/* combine */
	用小問題的解答，算出原問題的解答;
	原問題解答 = 解答1 + 解答2 + ......;

	return 原問題解答;
}
```

### 範例：合併排序法（merge sort）

![DivideAndConquer7.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer7.png)

divide階段：資料分割成兩堆。

conquer階段：兩堆資料各自從事merge sort。

combine階段：兩堆已排序過的資料，合併成一堆。

```cpp
void merge(int array[], int left, int right, int mid)
{
	int n = right - left + 1;
	int* x = new int[n];

	int i = left, j = mid + 1;
	for (int k=0; k<n; k++)
	{
		if      (i == mid + 1)         x[k] = array[j++];
		else if (j == right + 1)       x[k] = array[i++];
		else if (array[i] <= array[j]) x[k] = array[i++];
		else                           x[k] = array[j++];
	}

	for (int k=0; k<n; k++)
		array[left + k] = x[k];
	delete[] x;
}

void merge_sort(int array[], int left, int right)
{
	if (left >= right) return;

	/* divide */
	int mid = left + (right - left) / 2;

	/* conquer */
	merge_sort(array, left, mid);
	merge_sort(array, mid+1, right);

	/* combine */
	merge(array, left, right, mid);
}

void merge_sort(int array[], int n)
{
	merge_sort(array, 0, n-1);
}
```

### 範例：快速排序法（quicksort）

![DivideAndConquer8.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer8.png)

divide階段：任意挑選一個數字當作基準（例如最右端），把資料分割成左右兩堆。左堆數字小於等於基準，右堆數字大於基準。

conquer階段：左右兩堆資料各自從事quicksort。

combine階段：不做任何事。

```cpp
int partition(int array[], int left, int right)
{
	int pivot = array[right];	// 基準

	int i = left;
	for (int j = left; j < right; ++j)
		if (array[j] <= pivot)
		{
			swap(array[i], array[j]);
			i++;
		}

	swap(array[i], array[right]);
	return i;	// pivot的位置
}

void quicksort(int array[], int left, int right)
{
	if (left >= right) return;

	/* divide */
	int k = partition(array, left, right);

	/* conquer */
	quicksort(array, left, k-1);	// 左堆
	quicksort(array, k+1, right);	// 右堆

	/* combine */
}

void quicksort(int array[], int n)
{
	quicksort(array, 0, n-1);
}
```

### prune-and-search method

「修剪搜尋法」是分治法的特例。去除不重要的子問題，只搜尋重要的子問題。

![DivideAndConquer9.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer9.png)

### 範例：二元搜尋法（binary search）

![DivideAndConquer10.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer10.png)

在已排序陣列裡面，尋找特定數字。

陣列由中央切成兩邊，一邊數字較小、一邊數字較大。這兩邊一定有一邊不是我們所要的，可以去除，只需要繼續尋找其中一邊。

```cpp
int binary_search(int array[], int n, int key)
{
	int left = 0, right = n-1;
	while (left <= right)
	{
		int mid = left + (right - left) / 2;
		if      (array[mid] < key)  left = mid + 1;
		else if (array[mid] > key)  right = mid - 1;
		else if (array[mid] == key) return mid;
	}
	return -1;	// 找不到
}
```

### 範例：快速選擇法（quickselect）

![DivideAndConquer11.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer11.png)

在未排序陣列裡面，尋找第k小數字。

運用quicksort 的分割手法，把陣列切成兩邊，一邊數字較小、一邊數字較大。這兩邊一定有一邊不是我們所要的，可以去除，只需要繼續尋找其中一邊。

```cpp
int quickselect(int array[], int n, int k)
{
	int left = 0, right = n-1;
	while (left <= right)
	{
		int i = partition(array, left, right);
		if      (k < i)  right = i - 1;
		else if (k > i)  left = i + 1;
		else if (k == i) return array[i];
	}
	return -1;	// 找不到
}
```

### 範例：尋找假幣（counterfeit coin problem）

一堆硬幣，當中一枚硬幣是假幣，重量比真幣輕，肉眼無法分辨差異。手邊的工具僅有一台天平，但沒有砝碼，該如何藉由天平判斷假幣？

當硬幣總數為一，那麼該幣就是假幣。當硬幣總數為二，則兩枚硬幣分別放在天平兩端秤重，較輕的一端就是假幣。當硬幣總數為三以上，一定有辦法找出假幣，以下介紹兩種策略。

採用遞增法。每次取兩枚硬幣，放在天平兩端秤重。當天平平衡，表示這兩枚硬幣都是真幣，接著繼續處理剩餘硬幣。當天平傾斜，比較輕的硬幣就是假幣。

![DivideAndConquer12.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer12.png)

採用分治法。兩枚硬幣放在天平兩端秤重，當天平平衡，表示這兩枚硬幣都是真幣。接著只剩下N-2枚硬幣要尋找假幣──問題遞迴縮小了！

剩下N-2枚，太多了一點。一次取多一點硬幣，同時放在天平兩端秤，問題就能縮小更多了！

把所有硬幣平均分成三份，取兩份放在天平兩端秤重。當天平平衡，表示剩下的一份含有假幣，問題一次便縮小為1/3。當天平傾斜，表示比較輕的一份含有假幣，問題一次便縮小為1/3。

![DivideAndConquer13.png](https://web.ntnu.edu.tw/~algo/DivideAndConquer13.png)

讀者可以想想看：如果硬幣數量不是三的倍數怎麼辦？如果一開始不知道假幣與真幣孰輕孰重怎麼辦？

## dynamic programming

### dynamic programming

「動態規劃」。分治法輔以記憶法。當分治法分割出來的問題，一而再、再而三出現，就運用記憶法儲存這些問題的答案，避免重複求解，以空間換取時間。

由於內容較多較雜，另以專門頁面介紹。

## greedy method

> 今朝有酒今朝醉，明日愁來明日愁。《羅隱．自遣》

### greedy method

「貪心法」。以incremental method或iterative method製造答案的方法，大致上分為兩類：

一、填答案：從沒有答案開始，逐步填滿答案。

二、改答案：先隨便弄個答案，逐步修飾答案。

觀察問題特徵，擬定一個看似最好的原則，依照原則填答案、改答案。

### 範例：找零錢

你去商店買東西，你掏出了一張一百元，買了一包23元的零食。店員須找零錢給你，但是你希望店員找給你的硬幣數目越少越好，如此口袋會輕一點。那麼店員會給你幾個硬幣呢？

![Greedy1.png](https://web.ntnu.edu.tw/~algo/Greedy1.png)

填答案的原則是：先找給你面額較高的硬幣。

金額越少，找給你的硬幣數目也就越少。先找給你面額較高的硬幣，金額下降的最多──如此一來，往後找給你的硬幣數目就一定是最少了。

注意到：當錢幣面額很特別時，這個方法才正確。詳情請參考「[change-making problem](KnapsackProblem.html)」。

### 範例：文章換行（word wrap）

一大段的英文段落，適當的將文章換行，讓文字不超過紙張邊界，盡量節省紙張空間。

![Greedy2.png](https://web.ntnu.edu.tw/~algo/Greedy2.png)

填答案的原則是：字儘量往前擠，擠不下就換行。

### 範例：騎士周遊問題（knight's tour）

西洋棋盤上，請找到一條路線，讓騎士恰好經過棋盤上每一格各一次。

![Greedy3.gif](https://web.ntnu.edu.tw/~algo/Greedy3.gif)

填答案的原則是：走向出路選擇較少的格子。如果遇到出路選擇一樣多的格子，就走向位於下方的格子。如果又遇到一樣低的格子，就走向位於左方的格子。

![Greedy4.png](https://web.ntnu.edu.tw/~algo/Greedy4.png)

這種填答案的方式，耗盡死路，保留活路，將來走入死胡同的機會就變少了。有一種「置之死地而後生」的味道。

注意到：這個方法不一定會成功。我們根本無法證明這個方法會成功，只是乍看起來比較容易成功。

我們當下所做的最佳決定，以長遠的眼光來看，不一定是最佳決定。儘管貪心法不見得得到正確的、最好的答案，卻是個快速得到答案的好方法。

### 範例：活動選擇問題（activity selection problem）

暑假到了，有好多好多有趣的營隊可以參加囉！攀岩、潛水、單車環島團、吉他營、電腦營、……，每個營隊都好有趣，好想每個營隊都參加──可是卻有好多營隊的活動期間都互相卡到，沒辦法同時參加。到底要參加哪些營隊活動才好呢？當然是越多種越好！

![Greedy5.png](https://web.ntnu.edu.tw/~algo/Greedy5.png)

填答案的原則很簡單：優先選擇最早結束的活動，就能剩下最多時間來安排其他活動。

仔細分成兩種情況進行討論：一、最早結束的活動，與其他活動的時間不重疊；二、最早結束的活動，與某些活動的時間重疊。

一的狀況下，參加最早結束的活動，顯然是最理想的──憑空多參加了一個活動，又不耽誤到其他活動。

此觀念可以用recursive method詮釋：去除最早結束的活動、遞迴縮小問題。

![Greedy6.png](https://web.ntnu.edu.tw/~algo/Greedy6.png)

二的狀況下，最早結束的活動、以及時間與之重疊的活動當中，只能選擇其中一個參加。此時參加最早結束的活動，得以剩下比較多的時間，仍是最理想的。

此觀念可以用recursive method詮釋：去除最早結束的活動、去除因而無法參加的活動，遞迴縮小問題。

![Greedy7.png](https://web.ntnu.edu.tw/~algo/Greedy7.png)

填答案的原則是：所有活動按照結束時間排序，依序參加活動。如果時間允許就參加，如果時間衝突就不參加。

![Greedy8.png](https://web.ntnu.edu.tw/~algo/Greedy8.png)

### 範例：函數的局部極小值

![Greedy9.png](https://web.ntnu.edu.tw/~algo/Greedy9.png)

改答案的原則是：一開始x隨意設定一個數值，例如設定x = 0。微調x值，並且計算f(x)──如果f(x)減少，就更新x；如果f(x)沒減少，就不更新x。不斷修改x值，最後就到達局部極小值。

### 範例：交換相鄰數字的排序法

![Greedy10.png](https://web.ntnu.edu.tw/~algo/Greedy10.png)

改答案的原則是：每當發現相鄰兩個數字，左邊數字大於右邊數字，兩個數字就交換位置。

不斷交換位置，導致大數字逐漸往右端移動、小數字逐漸往左端移動，最後一定能完成排序。

讀者可以想想看：交換任意兩個數字的排序法，成立嗎？

順帶一提，排序過程反向操作，可以得到一個結論：排序過的陣列，經由兩兩相鄰交換，一定可以得到各種排列方式。

### 範例：平面上距離最近的兩個點（closest pair）

採用遞增法，逐次增加一個點；採用枚舉法，計算新點到其他點的距離。每當發現更近的兩個點，下次即可減少橫向搜尋範圍。

運用目前得到的答案，藉此得到更好的答案！可以看作是間接地、改答案的原則。

![Greedy11.png](https://web.ntnu.edu.tw/~algo/Greedy11.png)

另外，還可以減少縱向搜尋範圍。除了新點以外，兩點之間的距離，至少都是上次的最短距離，不能太密太擠。在橫向搜尋範圍之內，進行縱向排序（採用即時排序的資料結構，效率較佳），只需檢查新點的上兩點、下兩點，就一定能檢查到半圓內所有點！

儘管無法直接得到正確的點，但是只需檢查少數幾點！可以看作是間接地、填答案的原則。

![Greedy12.png](https://web.ntnu.edu.tw/~algo/Greedy12.png)

## scaling algorithm

> 古之欲明明德於天下者，先治其國。

### scaling algorithm

「縮放演算法」。將數值拆解為不同數量級，每個數量級分別計算一次答案，並且累計每次計算成果。

### 範例：乘法

數量級從小到大：乘數拆解為不同數量級，先以個位數相乘一次，再以十位數相乘一次，……，再以最高位數相乘一次，累加起來，得到正確結果。

![Scaling1.png](https://web.ntnu.edu.tw/~algo/Scaling1.png)

### 範例：基數排序法（radix sort）

數量級從小到大：所有數字先以個位數排序一次，再以十位數排序一次，……，再以最高位數排序一次，得到正確結果。

![Scaling2.png](https://web.ntnu.edu.tw/~algo/Scaling2.png)

數量級從大到小：所有數字先以最高位數排序一次，再以前兩高位數排序一次，……，再以全部位數排序一次，得到正確結果。

![Scaling3.png](https://web.ntnu.edu.tw/~algo/Scaling3.png)

改善計數排序法的效率，不必建立一長串陣列。

### 範例：多重解析度字串搜尋（multiscale string searching）

從宏觀到微觀，從粗糙到細膩。短字串跳N格實施比對。若足夠相似，才跳N/2格實施比對。……。若足夠相似，才跳1格實施比對。

![Scaling4.png](https://web.ntnu.edu.tw/~algo/Scaling4.png)

改善字串搜尋的效率，不必每次都比對一大串字元。

### 範例：Shell排序法（Shell sort）

從宏觀到微觀，從粗糙到細膩。跳N個數字為同一組，每組分別實施插入排序法。跳N/2個數字為同一組，各組分別實施插入排序法。……。跳1個數字為同一組，所有數字實施插入排序法。

![Scaling5.png](https://web.ntnu.edu.tw/~algo/Scaling5.png)

改善插入排序法的效率，不必每次都挪動一大串數字。

## I/O-efficient algorithm

> 巇始有朕，可抵而塞，可抵而卻，可抵而息，可抵而匿，可抵而得。《鬼谷子》

### I/O-efficient algorithm（external memory algorithm）

儲存容量大，存取時間長；儲存容量小，存取時間短。魚與熊掌不可兼得。自然而然形成階層架構：暫存器、快取、記憶體、硬碟，儲存容量越來越大，存取時間越來越久。

需要計算的變數，儲存在暫存器；不在暫存器，就找快取；不在快取，就找記憶體；不在記憶體，就找硬碟。

簡中譯作寄存器、缓存、内存、硬盘。

![IO1.png](https://web.ntnu.edu.tw/~algo/IO1.png)

實務上，硬碟可以換成光碟、隨身碟、雲碟、顯示器、揚聲器。

簡中譯作光盘、闪存盘、云盘、显示器、扬声器。

![IO2.png](https://web.ntnu.edu.tw/~algo/IO2.png)

對電腦來說，最花時間的動作，不是運算，而是讀寫：從硬碟讀入資料到記憶體、從記憶體寫出資料到硬碟。

每當資料不在記憶體，就從硬碟讀入資料到記憶體。根據硬碟運轉速率，等待硬碟籌備資料；根據傳輸通道大小，讀入一堆資料。

![IO3.png](https://web.ntnu.edu.tw/~algo/IO3.png)

異地資料，讀寫時間約是計算時間的一千倍！此時我們關心讀寫時間，不太關心計算時間。「輸入輸出效率演算法」或者「外部記憶體演算法」目的是減少讀寫時間。或者簡單來說，減少讀寫次數。

順帶一提，I/O-efficient algorithm是新興詞彙，目前較少見；external memory algorithm是原始詞彙，目前仍常見。

### 範例：動態陣列（dynamic array）

![IO4.png](https://web.ntnu.edu.tw/~algo/IO4.png)

不知資料多寡，只好準備一塊記憶體空間，暫存資料。每當空間滿了，才擴充空間。

C++標準函式庫的vector，即是動態陣列。

```cpp
void dynamic_array()
{
	vector<int> v;
	v.push_back(3);
	v.push_back(6);
	v.push_back(9);
	v.push_back(-8);
	v.push_back(1);
}
```

### 範例：緩衝區（buffer）

![IO5.png](https://web.ntnu.edu.tw/~algo/IO5.png)

不知資料生成時刻，只好準備一塊記憶體空間，暫存資料。每當資料夠了，才處理資料。

printf/scanf、cin/cout，內含緩衝區。

```cpp
void print()
{
	printf("It's a pencil.");
	fflush(stdout);			// 立即清空緩衝區
	setbuf(stdout, NULL);	// 不使用緩衝區

	cout << "It's a pencil.";
	cout << flush;			// 立即清空緩衝區
	cout << endl;			// 等同 cout << '\n' << flush;
	cout << unitbuf;		// 每次都清空緩衝區（不使用緩衝區）
};
```

### 範例：合併排序法（merge sort）

排序硬碟資料。

一、資料分段排序：每段資料符合記憶體容量，假設分成了k段。k段資料分別讀入、排序、寫出。

![IO6.png](https://web.ntnu.edu.tw/~algo/IO6.png)

二、資料合併排序：記憶體配置k塊輸入、1塊輸出緩衝區。k段資料合併成排序資料。

![IO7.png](https://web.ntnu.edu.tw/~algo/IO7.png)

在步驟一，當資料分段太多，則遞迴處理。

![IO8.png](https://web.ntnu.edu.tw/~algo/IO8.png)

### 範例：桶子排序法（bucket sort）

排序硬碟資料。

![IO9.png](https://web.ntnu.edu.tw/~algo/IO9.png)

一、資料分類排序：記憶體配置1塊輸入、k塊輸出緩衝區。一段資料分散於k個桶子，依照數字大小。

二、資料分段排序：k段資料分別讀入、排序、寫出。

在步驟二，當一段資料太長，則遞迴處理。

### 範例：選擇排序法暨二元搜尋法（selection sort & binary search）

不排序硬碟資料，不使用其他硬碟空間，直接輸出排序結果。

![IO10.png](https://web.ntnu.edu.tw/~algo/IO10.png)

篩選最小的數字們、排序、輸出。以二元搜尋法，調整篩選範圍。如果硬碟未讀完、緩衝區已滿溢，則減少篩選範圍，重新來過；如果硬碟已讀完，緩衝區未滿溢，則排序、輸出、更新篩選範圍。

小心處理同一數字數量非常多的情況。

```cpp
int MIN = -1000000000;	// 數字的最小值
int MAX = +1000000000;	// 數字的最大值
const int M = (1 << 18);
const int N = (1 << 19);
int in[M];				// 篩選前的數字
int out[N];				// 篩選後的數字

// 讀取檔案裡面所有數字，篩選大於等於L、小於等於R的數字。
int read(ifstream& fin, int L, int R)
{
	int n = 0;
	fin.clear();			// 回復讀寫狀態
	fin.seekg(0, fin.beg);	// 回到檔案開頭

	while (true)
	{
		// 讀取檔案裡面的數字
		fin.read((char*)in, sizeof(int)*M);
		int c = fin.gcount() / sizeof(int);
		if (c <= 0) break;	// 沒有數字就結束

		// 篩選數字
		for (int i = 0; i < c; i++)
			if (in[i] >= L && in[i] <= R)
				if (L == R)
				{
					if (n < N) out[n++] = in[i];
					else n++;	// 同一數字出現許多次
				}
				else
				{
					if (n < N) out[n++] = in[i];
					else return -1;	// 存不下
				}
	}
	return n;
}

// 選擇排序法暨二元搜尋法
// 屢次從檔案裡面篩選最小的數字們、排序、輸出。
// 如果記憶體滿溢，則將篩選範圍減半，重新來過。
void sort_file()
{
	ifstream fin("number.in", ios::binary);
	ofstream fout("number.out", ios::binary);

	// 選擇排序法暨二元搜尋法
	for (int L = MIN, R = MAX; L <= R; )
	{
		int M = (L + R) / 2;
		int n = read(fin, L, M);

		if (n < 0)			// 記憶體滿溢。篩選範圍減半。
			R = M;
		else if (n == 0)	// 查無數字。處理另一半範圍。
			L = M + 1;
		else				// 記憶體未滿溢。排序。輸出。
		{
			if (L == M)
			{
				for ( ; n > N; n -= N)
					fout.write((char*)out, sizeof(int)*N);
				if (n > 0)
					fout.write((char*)out, sizeof(int)*n);
			}
			else
			{
				sort(out, out + n);
				fout.write((char*)out, sizeof(int)*n);
			}

			// 處理其餘範圍
			L = M + 1;
			R = MAX;
		}
	}

	fin.close();
	fout.close();
}
```

## cache-efficient algorithm

> 士農工商四民者，國之石，民也。

### cache-efficient algorithm

方才討論了記憶體與硬碟的讀寫。「快取效率演算法」則是考慮快取與記憶體的讀寫。

對中央處理器來說，最花時間的動作，不是運算，而是讀寫：從記憶體讀入資料到快取、從快取寫出資料到記憶體。

每當資料不在快取，就從記憶體讀入資料到快取，讀入資料所在的那一個區塊。區塊大小等於通道大小。快取大小是其倍數。

![Cache1.png](https://web.ntnu.edu.tw/~algo/Cache1.png)

資料不在快取，稱作cache miss。「快取效率演算法」目的是減少cache miss、減少讀入次數。

順帶一提，cache-efficient細分為cache-aware和cache-oblivious。前者充分瞭解硬體規格，知道區塊大小、快取大小。後者無視硬體規格，不知道詳細數據。

### 範例：陣列與串列

陣列在記憶體裡是連續的。串列在記憶體裡通常不是連續的。

![Cache2.png](https://web.ntnu.edu.tw/~algo/Cache2.png)

枚舉陣列元素，偶爾載入區塊，不會重複載入，速度快。

![Cache3.png](https://web.ntnu.edu.tw/~algo/Cache3.png)

枚舉串列元素，經常載入區塊，甚至重複載入，速度慢。

![Cache4.png](https://web.ntnu.edu.tw/~algo/Cache4.png)

### 範例：變數型態

int = 4 byte，short = 2 byte，雖然儲存空間不一樣大，但是加法運算卻一樣快，都是一單位時間。

雖然兩數加法一樣快，但是多數總和就不一樣快。short array空間小，區塊少，速度快。

![Cache5.png](https://web.ntnu.edu.tw/~algo/Cache5.png)

```cpp
short summation()
{
	short array[1000] = {};

	// short array，空間小，區塊少，速度快。
	short sum = 0;
	for (int i=0; i<1000; i++)
		sum += array[i];
	return sum;
}
```

```cpp
int summation()
{
	int array[1000] = {};

	// int array，空間大，區塊多，速度慢。
	int sum = 0;
	for (int i=0; i<1000; i++)
		sum += array[i];
	return sum;
}
```

### 範例：二維陣列的總和

依序枚舉二維陣列的所有元素，累計總和。

![Cache6.png](https://web.ntnu.edu.tw/~algo/Cache6.png)

枚舉橫條元素，偶爾載入區塊，速度快。

枚舉直條元素，不斷載入區塊，速度慢。

```cpp
int summation()
{
	int array[1000][1000] = {};

	// 橫條為主，速度快。
	// 外層枚舉每一個橫條，內層枚舉一個橫條的每一個元素。
	int sum = 0;
	for (int i=0; i<1000; i++)
		for (int j=0; j<1000; j++)
			sum += array[i][j];
	return sum;
}
```

```cpp
int summation()
{
	int array[1000][1000] = {};

	// 直條為主，速度慢。
	// 外層枚舉每一個直條，內層枚舉一個直條的每一個元素。
	int sum = 0;
	for (int j=0; j<1000; j++)
		for (int i=0; i<1000; i++)
			sum += array[i][j];
	return sum;
}
```

### 範例：矩陣轉置（matrix transpose）

矩陣轉置：沿著左上右下對角線翻轉矩陣。

輸入矩陣偶爾載入區塊，輸出矩陣不斷載入區塊。

![Cache7.png](https://web.ntnu.edu.tw/~algo/Cache7.png)

```cpp
void matrix_transpose()
{
	int a[1000][1000] = {};
	int b[1000][1000] = {};

	for (int i=0; i<1000; i++)
		for (int j=0; j<1000; j++) 
			b[j][i] = a[i][j];
}
```

```cpp
void matrix_transpose(int a[], int b[], int x, int y)
{
	for (int i=0; i<x; i++)
		for (int j=0; j<y; j++) 
			b[x*j+i] = a[y*i+j];
}
```

分塊矩陣轉置：基本單位從元素變成分塊。

調整枚舉順序，優先枚舉分塊。雖然輸入矩陣載入區塊略增，但是輸出矩陣載入區塊驟減。

![Cache8.png](https://web.ntnu.edu.tw/~algo/Cache8.png)

```cpp
void block_transpose(int _a[], int _b[], int _x, int _y, int x, int y)
{
	for (int i=0; i<_x; i++)
		for (int j=0; j<_y; j++)
			_b[x*j+i] = _a[i*y+j];
}

void matrix_transpose(int a[], int b[], int x, int y)
{
	int xblock = sqrt(x);			// 分塊數量
	int yblock = sqrt(y);
	int xq = x / xblock;			// 分塊寬度
	int yq = y / yblock;
	int xr = x - (xblock - 1) * xq;	// 最後一個分塊寬度
	int yr = y - (yblock - 1) * yq;

	for (int i=0; i<xblock; i++)
		for (int j=0; j<yblock; j++)
		{
			int* _a = a + y*(xq*i) + (yq*j);
			int* _b = b + x*(yq*j) + (xq*i);
			int _x = (i < xblock-1) ? xq : xr;
			int _y = (j < yblock-1) ? yq : yr;
			block_transpose(_a, _b, _x, _y, x, y);
		}
}
```

### 範例：小畫家倒墨水（flood fill algorithm）

建立二維陣列或者一維陣列，盤面格子依序對應陣列索引值，區塊形成橫條。一個格子，左右通常是相同區塊，上下通常是不同區塊。墨水填充過程，經常載入區塊。

![Cache9.png](https://web.ntnu.edu.tw/~algo/Cache9.png)

建立一維陣列，盤面格子重新對應陣列索引值，區塊從橫條變方塊。墨水填充過程，不常載入區塊。

![Cache10.png](https://web.ntnu.edu.tw/~algo/Cache10.png)

## parallel algorithm

> 眾心成城，眾口鑠金。《國語》

### parallel algorithm

循序（sequential）就是逐一，平行（parallel）就是一齊，兩者是相對概念。

![Parallel1.png](https://web.ntnu.edu.tw/~algo/Parallel1.png)

「平行演算法」。當多個數值需要計算，就可以使用多個計算器一齊計算。優點是減少計算時間，缺點是增加硬體、增加電力。

計算器有兩種類型：SIMD與MIMD。

SIMD：多個計算器只能一齊執行相同指令。

MIMD：多個計算器可以分頭執行不同指令。

SIMD富含巧思，MIMD缺乏變化，所以我們只談SIMD。

當每一輪迴圈之間的變數不互相使用，就可以讓每一個計算器一齊計算。

![Parallel2.png](https://web.ntnu.edu.tw/~algo/Parallel2.png)

平行計算的架構：記憶體傳遞資料給多個計算器，多個計算器一齊計算，多個計算器傳遞資料給記憶體。

籌備規劃平行計算，需要額外時間空間。因此平行計算不一定比循序計算好。程式員必須自行取捨。

### parallel algorithm補充說明

平行計算的經典弱點：

```
kernel launch overhead：籌備規劃平行計算，需要額外時間空間。
shared memory bank conflict：共享記憶體，需要排隊等待，需要額外時間。
barrier synchronization overhead：結束平行計算，需要等待執行最久的計算器，需要額外時間。
branch divergence overhead：if敘述，後續指令略有不同，難以一齊計算。
```

平行計算的層級與稱呼：

```
層級       計算器                平行計算
---------+---------------------+-----------------------------------
微處理器 | 實體 processor core | 多行程、多进程（multiprocessing）
作業系統 | 虛構 thread         | 多執行緒、多线程（multithreading）
異質系統 | 實體 processor      | 異構計算（heterogeneous computing）
網際網路 | 實體 computer       | 分散式計算（distributed computing）
```

平行計算的程式語言與函式庫：

```
類型   語言   函式庫             標頭檔         備註
-----+------+------------------+-------------+----------------------
SIMD |      | OpenMP           | <omp.h>     | GCC、MSVC編譯器已內建
SIMD | CUDA |                  |             | 僅適用NVIDIA公司的產品
MIMD | C++  | standard library | <thread>    |
MIND | C    | C POSIX library  | <pthread.h> | 僅適用類UNIX作業系統
```

平行計算的組合語言與指令集：

```
類型   語言   指令集   備註
-----+------+-------+--------------------------
SIMD | x86  | SSE   | 各種基本運算
SIMD | x86  | AVX   | SSE增加輸入輸出的位元長度
SIMD | x86  | FMA   | 形如a = b × c + d的運算
```

### 範例：複製字串

理論：各個字元分頭複製。n步變1步。

![Parallel3.png](https://web.ntnu.edu.tw/~algo/Parallel3.png)

實務：籌備n個執行緒，需要額外時間空間，跟循序計算沒兩樣，弄巧成拙。因此，字串切成數段，分頭複製。

![Parallel4.png](https://web.ntnu.edu.tw/~algo/Parallel4.png)

```cpp
void copy()
{
	char s[15] = "incremental";
	char t[15];

	// 必須預先知道字串長度，才能明確訂定平行計算範圍。
	int n = 11;

	// 分段數量交由編譯器決定
	#pragma omp parallel for
	for (int i=0; i<n; i++)
		t[i] = s[i];
	t[n] = '\0';

	cout << "原本字串" << s;
	cout << "複製之後的字串" << t;
}
```

```cpp
void copy(char* s, char* t, int n)
{
	#pragma omp parallel for
	for (int i=0; i<n; i++)
		t[i] = s[i];
	t[n] = '\0';
}
```

### 範例：加總數字

理論：數字雙雙相加。n步變log₂n步。

![Parallel5.png](https://web.ntnu.edu.tw/~algo/Parallel5.png)

實務：陣列切成數段，分頭計算總和。最後累加各段總和。

![Parallel6.png](https://web.ntnu.edu.tw/~algo/Parallel6.png)

```cpp
void summation()
{
	int array[5] = {3, 6, 9, -8, 1};

	// 陣列切成兩段，分頭計算總和。
	int sum = 0;
	#pragma omp parallel for num_threads(2) reduction(+:sum)
	for (int i=0; i<5; i++)
		sum = sum + array[i];

	cout << "總和是" << sum;
}
```

```cpp
int summation(int array[], int n)
{
	int sum = 0;
	#pragma omp parallel for num_threads(2) reduction(+:sum)
	for (int i=0; i<n; i++)
		sum += array[i];
	return sum;
}
```

### 範例：生命遊戲（cellular automaton）

理論：兩層的平行化，外層是地圖的每一個細胞，內層是八個鄰居細胞數量總和。8⋅x⋅y步變log₂8步。

實務：只平行化每一個細胞，放棄平行化細胞數量總和。

![Parallel7.png](https://web.ntnu.edu.tw/~algo/Parallel7.png)

```cpp
void cellular_automaton()
{
	// 包裝成函式，讓程式碼易讀！
	bool board[2][5][5] = {};
	clear_board(board[0]);
	load_board(board[0]);
	print_board(board[0]);

	// 迭代四回合
	for (int t=0; t<4; ++t)
	{
		// 只平行化每一個細胞，放棄平行化細胞數量總和。
		#pragma omp parallel for collapse(2)
		for (int x=0; x<5; ++x)
			for (int y=0; y<5; ++y)
				go(x, y, board[t%2], board[(t+1)%2]);

		print_board(board[(t+1)%2]);
	}
}
```

### 範例：矩陣乘法（matrix multiplication）

理論：兩層的平行化，外層是輸出矩陣的每一個元素，內層是數列點積。x⋅y⋅z步變1+log₂y步。

實務：只平行化每一個元素，放棄平行化數列點積。

![Parallel8.png](https://web.ntnu.edu.tw/~algo/Parallel8.png)

```cpp
void matrix_multiply()
{
	const int x = 3, y = 3, z = 3;
	int a[x][y] = {{1,0,0},{0,1,0},{0,0,1}};
	int b[y][z] = {{1,2,3},{4,5,6},{7,8,9}};
	int c[x][z];

	// 只平行化每一個元素
	#pragma omp parallel for collapse(2) schedule(static)
	for (int i=0; i<x; i++)
		for (int j=0; j<z; j++) 
		{
			// 放棄平行化數列點積
			c[i][j] = 0;
			for (int k=0; k<y; k++)
				c[i][j] += a[i][k] * b[k][j];
		}

	cout << "矩陣是" << '\n';
	for (int i=0; i<x; i++)
	{
		for (int j=0; j<z; j++)
			cout << c[i][j] << ' ';
		cout << '\n';
	}
}
```

```cpp
void multiply_matrix(int a[], int b[], int c[], int x, int y, int z)
{
	// 只平行化每一個元素
	#pragma omp parallel for collapse(2) schedule(static)
	for (int i=0; i<x; i++)
		for (int j=0; j<z; j++) 
		{
			// 放棄平行化數列點積
			c[z*i+j] = 0;
			for (int k=0; k<y; k++)
				c[z*i+j] += a[y*i+k] * b[z*k+j];
		}
}
```

進一步考慮I/O-efficient algorithm。

矩陣乘法：各個執行緒重複讀寫相同元素。x⋅z個執行緒，各自讀取2⋅y個元素。總共讀取2⋅x⋅y⋅z個元素。

分塊矩陣乘法：矩陣切割為b⋅b個分塊，每次計算一個輸出矩陣分塊，減少讀寫時間。b⋅b⋅b個執行緒，每b個執行緒共享(x/b + z/b)⋅y個元素。總共讀取b⋅(x+z)⋅y個元素。

註：此層級的平行計算，無法讓部分執行緒共享部分記憶體。但是分塊矩陣乘法起碼有cache-efficient algorithm的效果。

![Parallel9.png](https://web.ntnu.edu.tw/~algo/Parallel9.png)

```cpp
void clear_block(int* _c, int _x, int _z, int z)
{
	for (int i=0; i<_x; i++) 
		for (int j=0; j<_z; j++)
			_c[z*i+j] = 0;
}

void multiply_block(int* _a, int* _b, int* _c, int _x, int _y, int _z, int y, int z)
{
	for (int i=0; i<_x; i++)
		for (int j=0; j<_z; j++)
		{
			// c[i][j] += a[i][k] * b[k][j];
			int t = 0;
			for (int k=0; k<_y; k++)
				t += _a[y*i+k] * _b[z*k+j];
			_c[z*i+j] += t;
		}
}

void multiply_matrix(int* a, int* b, int* c, int x, int y, int z)
{
	const int block = 1;			// 分塊數量（單邊）
	int xq = x / block;				// 分塊寬度
	int yq = y / block;
	int zq = z / block;
	int xr = x - (block - 1) * xq;	// 最後一個分塊寬度
	int yr = y - (block - 1) * yq;
	int zr = z - (block - 1) * zq;

	#pragma omp parallel for collapse(2) schedule(static)
	for (int i=0; i<block; i++)
		for (int j=0; j<block; j++)
		{
			// c[i][j] = 0;
			int* _c = c + (xq * z * i) + (zq * j);
			int _x = (i < block-1) ? xq : xr;
			int _z = (j < block-1) ? zq : zr;
			clear_block(_c, _x, _z, z);

			// c[i][j] = a[i][k] * b[k][j];
			#pragma omp parallel for schedule(static)
			for (int k=0; k<block; k++)
			{
				int* _a = a + (xq * y * i) + (yq * k);
				int* _b = b + (yq * z * k) + (zq * j);
				int _y = (k < block-1) ? yq : yr;
				multiply_block(_a, _b, _c, _x, _y, _z, y, z);
			}
		}
}
```

## pipelined algorithm

> 使人各得其所長，天下事當；均其分職，天下事得；

### pipelined algorithm

「流水線演算法」。原理如同工廠的裝配線、生產線。

不同功能的計算器，各自負責專門指令。一連串指令，依序交給每一種計算器。每一輪迴圈當中的一連串指令，接連交給計算器。

![Pipelined1.png](https://web.ntnu.edu.tw/~algo/Pipelined1.png)

當每一輪迴圈之間的變數不互相使用、且迴圈之中的指令不重複，就可以讓每一種計算器不停計算。

CPU已經內建流水線功能，程式員不必親自設計流水線演算法。因此流水線演算法目前不是顯學。

## randomized algorithm

> 有過物者必濟，故受之以既濟。《易傳》

### randomized algorithm

「隨機化演算法」。隨便的計算數值、計算順序。難得糊塗。

### 範例：隨機數字（random number）

隨機數字又稱亂數。亂七八糟、毫無章法、什麼都有可能。

![Randomized1.png](https://web.ntnu.edu.tw/~algo/Randomized1.png)

如何製造亂數呢？沒人知道！數學家尚未釐清「亂」是什麼。計算學家則創造了形形色色的算式，偽造亂數，聊勝於無。

簡易算式：乘上一數、加上一數，迭代下去。

```cpp
int rand()
{
	// 使用unsigned int，即便溢位也不會當機。
	static unsigned int seed = 0;
	// 乘上一數、加上一數。
	seed = seed * 1103515245U + 12345U;
	// 符合int上限範圍，得到[0, 2³¹-1]之間的亂數。
	return int(seed % 2147483648U);
}
```

C標準函式庫，已經有亂數了。

```cpp
void random_number()
{
	// 設定亂數表，之後才能使用rand()。
	srand(time(0));

	// 印出10個亂數，範圍是整數0到整數4。
	for (int i=0; i<10; i++)
		cout << rand() % 5;
}
```

### 範例：雜湊函數（hash function）

一種特別的函數：數字變成特定範圍數字。

![Randomized2.png](https://web.ntnu.edu.tw/~algo/Randomized2.png)

雜湊函數應用廣泛，衍生許多變化，其中一種經典變化是：數字變成特定範圍亂數。隨便導致分散──亂數四散，不會太集中。

```cpp
int hash(int num, int range)
{
	// 以給定的資料，製造一個亂數，位於[0, range-1]。
	unsigned int hash = num;	// num是負數也沒關係
	hash = hash * 1103515245U + 12345U;
	return int(hash % 2147483648U) % range;
}
```

C++標準函式庫，已經有雜湊函數了，但是不是亂數版本。不會變成亂數，而是變成原本數字，喜感十足。

```cpp
void hash_function()
{
	// 印出數字0到9的雜湊值，位於[0, 2³¹-1]。
	hash<int> int_hash;
	for (int i=0; i<10; i++)
		cout << int_hash(i);

	// 印出數字0到9的雜湊值，位於[0, 2³¹-1]。
	for (int i=0; i<10; i++)
		cout << hash<int>{}(i);
}
```

### 範例：雜湊表（hash table）

以簡短陣列儲存資料，以雜湊函數決定儲存位置。隨便導致分散──資料四散，不會太集中。

![Randomized3.png](https://web.ntnu.edu.tw/~algo/Randomized3.png)

優點是搜尋迅速，只需瀏覽少數資料，不必瀏覽全部資料。

```cpp
const int range = 5;

void add_number(vector<int> table[range], int num)
{
	// 以雜湊函數決定存放位置
	int h = hash(num, range);
	// 儲存至陣列
	table[h].push_back(num);
}

bool find_number(vector<int> table[range], int num)
{
	// 只需瀏覽少數資料，不必瀏覽全部資料。
	int h = hash(num, range);
	for (auto x: table[h])	// 窮舉
		if (x == num)		// 搜尋
			return true;
	return false;
}
```

### 範例：均勻隨機數字（uniform random number）

亂數雖分散，卻不見得均勻。於是計算學家另行創造算式，偽造均勻亂數。由於需要背景知識，此處不多提。

又亂、又均勻，很匪夷所思吧！譯作亂數真的沒問題嗎？

![Randomized4.png](https://web.ntnu.edu.tw/~algo/Randomized4.png)

C++標準函式庫，已經有均勻亂數了。

```cpp
void random_number()
{
	// 亂數生成器
	default_random_engine g;
 
	// 均勻亂數，範圍[0, 5)。
	uniform_int_distribution<int> rand(0, 4);
 
	// 印出10個亂數，範圍是整數0到整數4。
	for (int i=0; i<10; i++)
		cout << rand(g);
}
```

### 範例：隨機抽樣（simple random sampling）

隨機挑選一物，機率均等。

![Randomized5.png](https://web.ntnu.edu.tw/~algo/Randomized5.png)

```cpp
// 差勁的做法。不均勻。
int simple_random_sampling(int array[], int n)
{
	srand(time(0));
	return array[rand() % n];
}

// 比較優秀的做法。比較均勻。
int simple_random_sampling(int array[], int n)
{
	default_random_engine g;
	uniform_int_distribution<int> rand(0, n-1);
	return array[rand(g)];
}
```

### 範例：隨機混洗（random shuffle）

隨機排列，打亂順序，機率均等。

![Randomized6.png](https://web.ntnu.edu.tw/~algo/Randomized6.png)

```cpp
void random_shuffle(int array[], int n)
{
	srand(time(0));

	// 數字0到n-1
	int permutate[n];
	for (int i=0; i<n; i++) permutate[i] = i;

	// 逐次挑出一個數字
	for (int i=0; i<n-1; i++)
	{
		// 剩下的數字，隨機挑出一個數字（的位置）。
		int j = i + rand() % (n - i);
		// 挑出的數字，挪至前面。
		swap(permutate[i], permutate[j]);
	}

	// 重新排列
	int temp[n];
	for (int i=0; i<n; i++) temp[i] = array[i];
	for (int i=0; i<n; i++) array[permutate[i]] = temp[i];
}
```

與其先排列再交換，不如直接交換。

![Randomized7.png](https://web.ntnu.edu.tw/~algo/Randomized7.png)

```cpp
void random_shuffle(int array[], int n)
{
	srand(time(0));

	// 逐次挑出一個數字
	for (int i=0; i<n-1; i++)
	{
		// 剩下的數字，隨機挑出一個數字（的位置）。
		int k = i + rand() % (n - i);
		// 挑出的數字，挪至前面。
		swap(array[i], array[k]);
	}
}
```

### 範例：隨機化搜尋法（randomized search）

隨便挑一個位置，直到找到為止、直到無處可尋為止。程式可能永不結束。

![Randomized8.png](https://web.ntnu.edu.tw/~algo/Randomized8.png)

```cpp
int randomized_search(int array[], int n, int num)
{
	srand(time(0));

	// 建立表格，記錄已經找過的位置。
	// 一開始所有位置皆未找過。
	bool visit[n] = {};

	// 錯誤的實作方式。
	// 程式可能永不結束，儘管機率趨近0。
	for (int i=0; i<n; i++)
	{
		int j;
		do j = rand() % n; while (visit[j]);
		if (array[j] == num) return j;
		visit[j] = true;
	}
	return -1;
}
```

從其餘位置當中隨便挑一個位置，直到找到為止、直到無處可尋為止。程式一定結束。

![Randomized9.png](https://web.ntnu.edu.tw/~algo/Randomized9.png)

```cpp
int randomized_search(int array[], int n, int num)
{
	srand(time(0));

	for (int i=0; i<n-1; i++)
	{
		// 從其餘位置當中隨便挑一個位置
		int j = i + rand() % (n - i);
		if (array[j] == num) return j;
		// 已經找過的數字，挪至前面，永不再找。
		swap(array[i], array[j]);
	}
	return -1;
}
```

綜觀過程，是以一種順序讀取各個數字。因此隨機的計算順序，可以等價交換成隨機的輸入順序、循序的計算順序。

![Randomized10.png](https://web.ntnu.edu.tw/~algo/Randomized10.png)

```cpp
int randomized_search(int array[], int n, int num)
{
	// 隨機排列
	random_shuffle(array, array+n);

	// 循序搜尋
	for (int i=0; i<n; i++)
		if (array[i] == num)
			return i;
	return -1;
}
```

```cpp
int randomized_search(int array[], int n, int num)
{
	// 額外建立索引值、指標，避免改變陣列內容。
	int index[n];
	for (int i=0; i<n; i++)
		index[i] = i;

	// 隨機的計算順序
	random_shuffle(index, index+n);

	for (int i=0; i<n; i++)
		if (array[index[i]] == num)
			return i;
	return -1;
}
```

搜尋次數的期望值是(n+1)/2。

```
正確數字在每個位置的出現機率都一樣多，都是1/n。
正確數字出現在第1個位置，讀取第1個數字就能找到。
正確數字出現在第i個位置，讀取第i個數字才能找到。
  (1/n) × 1 + (1/n) × 2 + ... + (1/n) × n
= (1/n) × (1 + ... + n)
= (1/n) × (1+n)n/2
= (1+n)/2
```

### 範例：隨機化排序法（randomized sort）

隨便挑兩個位置，若數字順序不對則交換，直到無處可尋為止。

![Randomized11.png](https://web.ntnu.edu.tw/~algo/Randomized11.png)

交換次數的期望值是多少呢？

只挑相鄰位置，期望值會比較少嗎？

儘管缺乏實用價值，但是如果你會分析，麻煩教我。

### 範例：矩陣乘法驗算（matrix product verification）

矩陣乘法，通盤檢查太久，抽樣檢查較快。

第二個矩陣，隨機挑選一個向量來驗算。驗算一次，僥倖通過機率是(n-1)/n；驗算k次，僥倖通過機率是(n-k)/n。

![Randomized12.png](https://web.ntnu.edu.tw/~algo/Randomized12.png)

第二個矩陣，隨機挑選多個向量，以向量總和來驗算。驗算一次，僥倖通過機率是1/2；驗算k次，僥倖通過機率是(1/2)ᵏ。效果好多了。

![Randomized13.png](https://web.ntnu.edu.tw/~algo/Randomized13.png)

```cpp
const int N = 10;
typedef int Matrix[N][N];

// Freivalds's algorithm
bool verify_matrix_product(Matrix A, Matrix B, Matrix C)
{
	srand(time(0));

	// 驗算5次
	for (int t=0; t<5; t++)
	{
		// 第二個矩陣，隨機挑選多個向量。
		// 0是沒選中，1是選中。
		bool column[N] = {};
		for (int i=0; i<N; ++i)
			column[i] = rand() % 2;

		// 計算向量總和
		int sumB[N] = {};
		for (int k=0; k<N; k++)
			for (int j=0; j<N; j++)
				if (column[j])
					sumB[k] += B[k][j];

		// 以向量總和來驗算
		// 逐次檢查各個元素
		for (int i=0; i<N; i++)
		{
			int sumAB = 0;
			for (int k=0; k<N; k++)
				sumAB += A[i][k] * sumB[k];

			int sumC = 0;
			for (int j=0; j<N; j++)
				if (column[j])
					sumC += C[i][j];

			if (sumAB != sumC) return false;
		}
	}
	return true;
}
```

### 範例：集合相似度（set similarity）

此處將集合相似度設為交聯比：交集大小除以聯集大小。

交集與聯集，通盤計算需額外記憶體，抽樣計算以節省記憶體。

![Randomized14.png](https://web.ntnu.edu.tw/~algo/Randomized14.png)

集合有兩種資料結構：循序儲存、索引儲存。

如果是循序儲存，隨機挑選一個數字，判斷是不是交集元素、聯集元素。大量抽樣，統計比例。累計越多次，答案越準確。

![Randomized15.png](https://web.ntnu.edu.tw/~algo/Randomized15.png)

陣列還可以改成雜湊表，節省搜尋時間。

```cpp
const int range = 10;

double set_similarity(vector<int> A[range], vector<int> B[range])
{
	srand(time(0));

	int c = 0;	// 交集大小
	int d = 0;	// 聯集大小

	for (int i=0; i<5; i++)	// 抽樣5次
	{
		int x = rand();
		bool inA = find_number(A, x);	// 搜尋雜湊表
		bool inB = find_number(B, x);
		if (inA && inB) c++;
		if (inA || inB) d++;
	}

	return (double)c / d;
}
```

如果是索引儲存，隨機抽樣改成隨機排列，然後挑選首個標記位置來比對。

![Randomized16.png](https://web.ntnu.edu.tw/~algo/Randomized16.png)

隨機排列還可以改成雜湊函數，節省排列時間。

```cpp
// MinHash
double set_similarity(bool A[], bool B[], int range)
{
	int c = 0;	// 交集大小
	int d = 0;	// 聯集大小（和抽樣次數一樣，其實可以省略。）

	for (int i=0; i<5; i++)	// 抽樣5次
	{
		// 創造新的雜湊函數（此處沒有實作，這是虛擬碼。）
		int (*hash)(int,int) = new_hash_function();

		int headA = 2147483647;
		for (int j=0; j<range; j++)
			if (A[j])
				headA = min(headA, hash(j, range));

		int headB = 2147483647;
		for (int j=0; j<range; j++)
			if (B[j])
				headB = min(headB, hash(j, range));

		if (headA == headB) c++;
		d++;
	}

	return (double)c / d;
}
```

### 範例：快速排序法（quicksort）

挑選一個數字當作基準，所有數字分成大的一邊和小的一邊，遞迴下去。

無論挑選哪一個數字當作基準，最終都會得到正確結果。

![Randomized17.png](https://web.ntnu.edu.tw/~algo/Randomized17.png)

然而，隨機挑選基準，不是最好的方式。挑選中位數當作基準，讓數字對半分，讓遞迴次數最少，才是最好的方式。

中位數無法預測。實務上是將陣列三等份，以三個中央數的中位數當作基準。因為上一層遞迴已經數字分成兩邊、大致排序過了，所以這種方式更容易接近中位數。

### 範例：平面上距離最近的兩個點（closest pair）

挑選一個點對距離當作方格寬度，建立方格紙。最近點對只會在相同方格、相鄰方格。窮舉田字，窮舉田字裡面所有點對，取距離最小者。

無論挑選哪一個距離當作寬度，最終都會得到正確結果。

![Randomized18.png](https://web.ntnu.edu.tw/~algo/Randomized18.png)

然而，隨機挑選距離，不是最好的方式。實務上是挑選最近距離三倍以下的距離當作方格寬度。做法請參考：

[](https://www.cs.cmu.edu/~ckingsf/class/02713/lectures/lec31-random.pdf)

## streaming algorithm

> 臣不能以喻臣之子，臣之子亦不能受之於臣，是以行年七十而老斲輪。《莊子》

### streaming algorithm

現在是資訊爆炸的年代，資料不斷增加。「串流演算法」就是處理源源不絕的輸入資料。大家關注的有：

```
online：隨時處理資料，甚至隨時計算正確答案。
one-pass：只讀取一次資料，盡量計算正確答案。
memory-bounded：資料無法盡數儲存，盡量計算正確答案。
```

### 範例：統計數字數量

先排序，再統計。

![Streaming1.png](https://web.ntnu.edu.tw/~algo/Streaming1.png)

```cpp
void histogram(int array[], int n)
{
	sort(array, array+n);

	int c = 1;
	for (int i=1; i<n; i++)
		if (array[i] == array[i-1])
			c++;
		else
		{
			// 印出統計結果
			cout << array[i-1] << ':' << c << '\n';
			// 重新計數
			c = 1;
		}
	// 印出統計結果
	cout << array[n-1] << ':' << c << '\n';
}
```

變成串流。建立陣列，根據數值大小，累計至對應位置。

![Streaming2.png](https://web.ntnu.edu.tw/~algo/Streaming2.png)

```cpp
void histogram(istream& in)
{
	int c[1000000] = {};

	int num;
	while (in >> num)
	{
		c[num]++;
		cout << c[num];
	}
}
```

減少記憶體。格子少於數值範圍，只好使用雜湊函數。相異數字可能存入相同格子，無法精確統計。

![Streaming3.png](https://web.ntnu.edu.tw/~algo/Streaming3.png)

```cpp
int hash(int num, int range)
{
	return num % range;
}

void histogram(istream& in)
{
	// 統計表格，範圍0到9。
	int c[10] = {};

	int num;
	while (in >> num)
	{
		// 以雜湊函數決定累計位置。
		int h = hash(num, 10);
		c[h]++;
		cout << c[h];
	}
}
```

建立多個統計表格，使用不同雜湊函數，分散風險。推定最小值為統計結果。

![Streaming4.png](https://web.ntnu.edu.tw/~algo/Streaming4.png)

```cpp
int hash1(int num) {return num % 10;}
int hash2(int num) {return num % 9;}
int hash3(int num) {return num * num % 10;}

// count–min sketch
void histogram(istream& in)
{
	// 3個統計表格
	int c[3][10] = {};
	// 3種雜湊函數
	int (*hash[3])(int) = {hash1, hash2, hash3};

	int num;
	while (in >> num)
	{
		int count_min = 2147483647;
		for (int i=0; i<3; i++)
		{
			// 以雜湊函數決定累計位置，分散風險。
			int h = hash[i](num);
			c[i][h]++;
			// 取最小值
			count_min = min(count_min, c[i][h]);
		}
		cout << count_min;
	}
}
```

### 範例：相異數字個數

先排序，再統計。

![Streaming5.png](https://web.ntnu.edu.tw/~algo/Streaming5.png)

```cpp
int count_distinct(int array[], int n)
{
	sort(array, array+n);

	int x = 0;
	if (n > 0) x = 1;
	for (int i=1; i<n; i++)
		if (array[i] != array[i-1])
			x++;
	return x;
}
```

變成串流。建立陣列，根據數值大小，累計至對應位置。

```cpp
void count_distinct(istream& in)
{
	int c[1000000] = {};

	int x = 0;
	int num;
	while (in >> num)
	{
		if (!c[num]) x++;
		c[num]++;
		cout << x;
	}
}
```

減少記憶體。格子少於數值範圍，只好使用雜湊函數。相異數字可能存入相同格子，無法精確統計。

```cpp
void count_distinct(istream& in)
{
	// 統計表格，範圍0到9。
	int c[10] = {};

	int x = 0;
	int num;
	while (in >> num)
	{
		// 以雜湊函數決定累計位置。
		int h = hash(num, 10);
		if (!c[h]) x++;
		c[h]++;
		cout << x;
	}
}
```

再減少記憶體。任意一個二進位數字，最低的位元1，不存在的機率差不多是0，位於第一低位數的機率是1/2，位於第二低位數的機率是1/4，……，位於第i低位數的機率是1/2ⁱ。

更進一步，任意2ⁱ個相異二進位數字，最低的位元1，涵蓋前i低位數的機率差不多是1。邏輯有點奇怪，姑且當作是這樣吧。

每讀一個數字，先套用雜湊函數得到新數字，再找到最低位元1，並紀錄其位置。若涵蓋前i低位數，則推定2ⁱ是相異數字個數。

雜湊函數宛如隨機排列。重新打亂數字，讓位元1均勻分布，以便迎合上述機率。重新打亂數字，不影響相異數字個數。

```cpp
// Flajolet–Martin sketch
void count_distinct(istream& in)
{
	// 統計表格，總共32位元，僅使用其中31位元。
	// 範圍0到2147483647。
	unsigned int mask = 0;

	int num;
	while (in >> num)
	{
		int h = hash(num, 2147483647);

		// 找到最低位元1
		int lsb1 = 31;
		for (int i=0; i<31; i++)
			if (h & (1 << i) == 1)
			{
				lsb1 = i;
				break;
			}

		// 並紀錄其位置
//		mask |= (1U << lsb1);
		if (h > 0) mask |= (1U << lsb1);	// 避免之後溢位

		// 找到連續的位元1
		// 換句話說，找到最低位元0。
		int lsb0 = 31;
		for (int i=0; i<31; i++)
			if (mask & (1U << i) == 0)
			{
				lsb0 = i;
				break;
			}

		// 推定2ⁱ是相異數字個數
		cout << (1U << lsb0);
	}
}
```

```cpp
// Flajolet–Martin sketch
void count_distinct(istream& in)
{
	unsigned int mask = 0;

	int num;
	while (in >> num)
	{
		int h = hash(num, 2147483647);

		// 利用內建函式，得到最低的位元1。
		if (h > 0) mask |= (1U << __builtin_ctz(h));

		// 利用內建函式，得到最低的位元0。
		unsigned int x = 1U << __builtin_ctz(mask + 1U);

		// 經實驗發現，除以0.77351，答案更精準。
		cout << floor(double(x) / 0.77351);
	}
}
```

### 範例：尋找陣列裡的最小值

趁早找到最小值，不想看遍全部數字。

![Streaming6.png](https://web.ntnu.edu.tw/~algo/Streaming6.png)

前n/e個，記錄最小值。第n/e + 1個以後，如果小於最小值，就推定為答案。

實際應用：找伴侶、買水果、炒短線。

```cpp
// Gilbert–Mosteller strategy
int find_minimum(int array[], int n)
{
	int k = floor((double)n / exp(1));
	int min = 2147483647;
	for (int i=0; i<k; i++)
		if (array[i] < min)
			min = array[i];

	for (int i=k; i<n; i++)
		if (array[i] < min)
			return array[i];
	return min;
}
```

### 範例：隨機抽樣（random sampling）

隨機挑選一物，機率均等。

![Streaming7.png](https://web.ntnu.edu.tw/~algo/Streaming7.png)

```cpp
int random_sampling(int array[], int n)
{
	srand(time(0));
	return array[rand() % n];
}
```

變成串流。使用動態陣列。

```cpp
void random_sampling(istream& in)
{
	vector<int> array;	// 動態陣列

	int num;
	for (int i=0; in >> num; i++)
	{
		array.push_back(num);
		cout << array[rand() % (i+1)];
	}
}
```

節省記憶體，只需儲存一物。從1開始編號，遭遇第i物時，儲存機率1/i，捨棄機率1 - 1/i。

最終得到第i物的條件是：保留第i物，捨棄第i+1物到第n物。機率恰是1/n：

```
   1           1             1                   1
  ⎯⎯⎯ × ( 1 - ⎯⎯⎯ ) × ( 1 - ⎯⎯⎯ ) × ... × ( 1 - ⎯⎯⎯ )
   i          i+1           i+2                  n 

   1     i    i+1         n-1    1
= ⎯⎯⎯ × ⎯⎯⎯ × ⎯⎯⎯ × ... × ⎯⎯⎯ = ⎯⎯⎯
   i    i+1   i+2          n     n
```

最終得到各物的機率，推導過程如法炮製，機率均是1/n。

```cpp
// reservoir sampling
void random_sampling(istream& in)
{
	srand(time(0));

	int result = 0, num;
	for (int i=0; in >> num; i++)
	{
		if (rand() % (i+1) < 1)
			result = num;
		cout << result;
	}
}
```

### 範例：隨機混洗（random shuffle）

遭遇第i物時，第i物與後面挑一物對調。

![Randomized7.png](https://web.ntnu.edu.tw/~algo/Randomized7.png)

```cpp
// 產生[0,x)的隨機整數。
inline int rand(int x) {return rand() % x;}

// 產生[x,y)的隨機整數。
inline int rand(int x, int y) {return x + rand(y - x);}

// Fisher–Yates shuffle
void random_shuffle(int array[], int n)
{
	srand(time(0));

	for (int i=0; i<n-1; i++)
		swap(array[i], array[rand(i, n)]);
}
```

隨機混洗可以串流嗎？我也不知道。哎喲隨便啦。
