# Index

pandas의 `index 객체`는 <u>Series의 경우에는 각 요소에 대한 ID 역할</u>을 하고, <u>DataFrame의 경우에는 각 행에 대한 ID 역할</u>을 합니다.



앞서 살펴본 것과 같이, `index 기능`을 통해 <u>Series와 DataFrame의 인덱스를 추출</u>할 수 있습니다.

```python
import pandas as pd
series = pd.Series([10, 20, 30, 40], index = ['A', 'B', 'C', 'D'])
print(series.index) # Index(['A', 'B', 'C', 'D'], dtype='object')
```



**Index 객체는 순서가 있는 집합처럼 작동**합니다. 당연히 교집합과 합집합 등의 집합 연산도 지원합니다.

```python
import pandas as pd

Series_A = pd.Series([10, 20, 30, 40], index = ['A', 'B', 'C', 'D'])
Series_B = pd.Series([30, 20, 10, 40], index = ['C', 'D', 'E', 'F'])

index_A = Series_A.index
index_B = Series_B.index

print('교집합:', index_A & index_B)
# 교집합: Index(['C', 'D'], dtype='object')

print('합집합:', index_A | index_B)
# 합집합: Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
```



`Series`와 `DataFrame`에 데이터를 <u>추가하거나 삭제</u>하고, <u>Index를 이용해서 이를 확인해 볼 수 있습니다.</u>

**데이터를 추가하거나 삭제하는 함수**는 실습에서 자세히 다루겠습니다.

```python
import pandas as pd

# Series 생성
series = pd.Series([10, 20, 30, 40], index = ['A', 'B', 'C', 'D'])

# 삭제
series = series.drop('A')
print(series.index) # ['B', 'C", 'D']

# 생성
series['A'] = 50
print(series) # B: 20, C: 30, D: 40, A: 50

# DataFrame 생성
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index = [1, 2, 3])

# index 삭제
df = df.drop(2)
print(df.index) # [1, 3]

```





## 1. 실습 - Series의 인덱스 추출 및 연산

- Series의 `인덱스(index)`를 **추출/연산하는 방법 실습**

```python
# Series의 인덱스가 추출되어 출력 확인

import pandas as pd
series = pd.Series([10, 20, 30, 40], index = ['A', 'B', 'C', 'D'])

print(series.index) # Index(['A', 'B', 'C', 'D'], dtype='object')
```



- 생성된 두개의 Series의 index들의 `교집합과 합집합` 구하는 코드

```python
import pandas as pd
series1 = pd.Series([10, 20, 30, 40], index = ['A', 'B', 'C', 'D'])
series2 = pd.Series([50, 60, 70, 80], index = ['C', 'D', 'E', 'F'])

print('합집합=', series1.index | series2.index)
# 합집합= Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

print('교집합=', series1.index & series2.index)
# 교집합= Index(['C', 'D'], dtype='object')
```



## 2. 실습 - Series의 데이터 추가/삭제

**데이터를 추가하거나 삭제**하는 함수를 실습하고, <u>Index 기능을 이용하여 이를 확인하는 방법</u> 학습



- 데이터 추가

```python
series['E'] = 50
```



- 데이터 삭제

```python
series = series.drop('B') # drop 은 리턴값이 있음
```

`drop()` 함수의 경우에는 **지정된 Index의 값이 삭제된 Series를 복제하여 리턴**하기 때문에 series변수에 갱신해주어야 합니다.



- 실습

```python
import pandas as pd
series = pd.Series([10, 20, 30, 40], index = ['A', 'B', 'C', 'D'])

print('생성 직후=',series.index) 
# 생성 직후= Index(['A', 'B', 'C', 'D'], dtype='object')

series['E'] = 50
print('데이터 추가 후=',series.index) 
# 데이터 추가 후= Index(['A', 'B', 'C', 'D', 'E'], dtype='object')

series = series.drop('B')
print('B의 값 삭제 후=',series.index) 
# B의 값 삭제 후= Index(['A', 'C', 'D', 'E'], dtype='object')
```



___



## 3. DataFrame 인덱스 추출 및 연산

- DataFrame 인덱스 추출 출력

```python
import pandas as pd
df = pd.DataFrame(
	[
        [1, 10],
        [2, 20],
        [3, 30],
        [4, 40]
    ],
    columns = ['A', 'B'],
    index = ['a', 'b', 'c', 'd']
)

print(df.index) # Index(['a', 'b', 'c', 'd'], dtype='object')
```



- 두 개의 DataFrame의 index들의 `교집합 & 합집합` 구하기

```python
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index = [1, 2, 3])
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]}, index = [2, 3, 4])

print('합집합=', df1 .index | df2 .index)
# 합집합= Int64Index([1, 2, 3, 4], dtype='int64')

print('교집합=', df1 .index & df2 .index)
# 교집합= Int64Index([2, 3], dtype='int64')
```



## 4. DataFrame 데이터 추가/삭제

- 행 데이터 추가

```python
df.loc['d'] = [7, 8]
```



- 데이터 삭제

```python
# 인덱스 b의 행을 삭제
df = df.drop('b', axis = 0)

# 컬럼 A의 열을 삭제
df = df.drop('A', axis = 1)
```

axis 를 통해 행을 삭제할 지, 열을 삭제할 지 지정 `( axis = )  생략가능`하므로 `df=df.drop('b',0)` 형태가능

`drop() 함수`는 지정된 index의 행이 삭제된 df 복제하여 리턴하기 때문에 df변수에 갱신해줘야함



- 실습

```python
import pandas as pd

df = pd.DataFrame(
	[
		[1, 10], 
	  	[2, 20], 
	  	[3, 30], 
	  	[4, 40]
	], 
  	columns = ['열1', '열2'], 
  	index = ['행A', '행B', '행C', '행D']
)
print('생성 직후=',df .index) 

df.loc['행E'] = [5,50]
print('행 데이터 추가 후=',df.index) 

df= df.drop('행B',axis=0)
print('행B의 행 삭제 후=',df.index) 
```

