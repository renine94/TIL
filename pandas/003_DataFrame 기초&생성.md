# DataFrame

`DataFrame`은 **두 개 이상의 Series로 구성된 자료형**으로, <u>2차원 배열 혹은 행렬으로 볼 수 있습니다.</u>

행 ID인 `인덱스` 와 `컬럼`으로 구성되는 <u>DataFrame은 잘 정의되어 있는 엑셀시트와 매칭</u>됩니다.

| 인덱스 | 컬럼1 | 컬럼2 |
| :----: | :---: | :---: |
|   A    |   1   |  10   |
|   B    |   2   |  20   |
|   C    |   3   |  30   |
|   D    |   4   |  40   |



DataFrame은 pandas의 `DataFrame()함수` 를 사용하여 만들 수 있습니다.

중첩된 배열로부터 DataFrame을 만드는 방법과 사전(Dictionary)으로부터 DataFrame을 만드는방법이 있습니다.

- DataFrame 만드는 방법
  - 중첩된 배열로부터 DataFrame 생성
  - Dict 로 DataFrame 생성

```python
import pandas as pd
df = pd.DataFrame(
	{
        '컬럼1': [1, 2, 3, 4],
        '컬럼2': [10, 20, 30, 40]
    },
    index = ['A', 'B', 'C', 'D']
)

df = pd.DataFrame(
	[[1, 10], [2, 20], [3, 30], [4, 40]],
    columns = ['컬럼1', '컬럼2'],
    index = ['A', 'B', 'C', 'D']
)
```





- `.values, .index, .columns` 함수를 사용하여 DataFrame의 구성요소를 확인할 수 있습니다.

```python
import pandas as pd
df = pd.DataFrame(
    			[[1, 10], [2, 20], [3, 30], [4, 40]],
                columns = ['컬럼1', '컬럼2'],
                index = ['A', 'B', 'C', 'D']
)

print(df.values) # [[1, 10], [2, 20], [3, 30], [4, 40]]
print(df.index) # ['A', 'B', 'C', 'D']
print(df.columns) # [컬럼1, 컬럼2]
```





## 1. DataFrame 생성

본 실습에서는 `컬럼별로 데이터를 정의` 하고, `인덱스를 따로 부여하는 방법`으로 DataFrame을 생성해 보겠습니다.



- 생성1

```python
import pandas as pd

df1 = pd.DataFrame(
	{
        '컬럼1': [1, 2, 3, 4],
        '컬럼2': [10, 20, 30, 40]
    },
    index = ['A', 'B', 'C', 'D']
)

# print(df1.to_html())
print(df1)
```



- 생성2

```python
import pandas as pd
df2 = pd.DataFrame(
	[
        [1, 10],
        [2, 20],
        [3, 30],
        [4, 40]
    ],
    columns = ['컬럼1', '컬럼2'],
    index = ['A', 'B', 'C', 'D']
)

print(df2)
print(df2.to_html())
```

