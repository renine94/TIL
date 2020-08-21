# Series

- `Series`는 <u>Pandas의 가장 기본이 되는 자료형</u>으로, **인덱스**와 **값**으로 구성됩니다. 즉,
  Series는 각 요소에 대한 이름이 있는 배열 자료형이라고 해석할 수 있습니다.

| 인덱스 |  값  |
| :----: | :--: |
|   A    |  10  |
|   B    |  20  |
|   C    |  30  |
|   D    |  40  |
|   E    |  50  |
|   F    |  60  |



## 1. Series 생성방법 (3가지)

- `Series`는 pandas의 `Series()` 함수를 사용하여 만들 수 있습니다. 인데긋와 값을 바탕으로 Series를 만드는 방법과 사전(dictionary)이라는 자료형을 바탕으로 Series를 만드는 방법이 있습니다.

```python
import pandas as pd
import numpy as np

# 첫번째 방법
series = pd.Series([10, 20, 30, 40, 50, 60],
                  index=['A','B','C','D','E','F'])

# 두번째 방법
series = pd.Series({
    'A':10,
    'B':20,
    'C':30,
    'D':40,
    'E':50,
    'F':60
})

# 세번째 방법
series = pd.Series(np.random.random(10))

print(series)
```



- `.values`와 `.index` 기능을 사용하여 <u>series의 구성 요소를 확인</u>할수 있습니다. 결과에서 보다시피, Series는 <u>index와 numpy의 ndArray로 구성</u>되는 것을 확인할 수 있습니다.

```python
import pandas as pd
series = pd.Series([10, 20, 30],
                  index = ['A', 'B', 'C'])

print(series.index) # Index(['A', 'B', 'C'], dtype='object')
print(series.values) # [10 20 30]
print(type(series.values)) # numpy.ndArray
```





## 2. Series 연산

- `Series의 값은 ndArray 자료형`이므로, numpy가 지원하는 <u>ndArray에 대한 연산을 Pandas의 Series에 대해서도 똑같이 지원</u>합니다.
- 유니버셜 함수의 경우, <u>ndArray는 위치가 같은 요소끼리 연산이 되지만,</u> **Series는 인덱스가 같은 요소끼리 연산**이 됩니다.

```python
import pandas as pd
S_A = pd.Series([10, 20, 30], index = [1, 2, 3])
S_B = pd.Series([5, -3, 10], index = [3, 2, 1])

print(S_A + S_B) # {1: 20, 2: 17, 3: 35}
```



- Numpy의 **브로드캐스팅도 지원**이 됩니다. 다만, <u>Series는 기본적으로 1차원 배열이므로 1차원 배열과 상수 간 연산만 지원되는 것처럼 보일 수 있습니다.</u>

```python
import pandas as pd
series = pd.Series([10, 20, 30], index = ['A', 'B', 'C'])

print(series + 1) # {A: 11, B: 21, C: 31}
print(series * 2) # {A: 20, B: 40, C: 60}
```



- .str에 속한 문자열 관련 함수를 사용한다면, **Series에 속한 문자열 자료형에 일괄적으로 함수를 적용**할수 있습니다.

```python
import pandas as pd
series = pd.Series(['17:30', '21:15', '22:00'])
series.str.split(':') # {0: [17, 30], 1: [21, 15], 2: [22, 00]}

series = pd.Series(['abc', 'def', 'hi'])
series.str.capitalize() # {0: Abc, 1: Def, 2: Hi}
```





## 3. 연산 실습

- 두 개의 Series를 각각 더하고 곱해보자

```python
import pandas as pd
S_A = pd.Series([10, 20, 30], index = ['A', 'B', 'C'])
S_B = pd.Series([30, 20, 10, 50], index = ['A', 'B', 'C', 'D'])

print(S_A + S_B)
# A 40.0
# B 40.0
# C 40.0
# D NaN
# dtype: float64

print(S_A * S_B)
# A 300.0
# B 400.0
# C 300.0
# D NaN
# dtype: float64
```



- **Series의 문자열함수 적용**

본 실습에서는 Series에 문자열 함수를 적용해 보겠습니다.



아래의 코드를 실행하여 생성된 Series의 값인 `small`과 `very small` 에 대문자로 변환하는 문자열함수인 `upper()` 가 적용되는 것을 확인해 봅시다.

```python
import pandas as pd
S_C = pd.Series(['small', 'very small'])

print(S_C.str.upper())
# 0 SMALL
# 1 VERY SMALL
# dtype: object
```



