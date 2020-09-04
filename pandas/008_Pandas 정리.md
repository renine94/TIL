# 학습정리



## 1. Pandas 자료형

- **Series**
  - Pandas의 기본이 되는 자료형
  - 인덱스와 값으로 구성
  - 각 요소에 대한 이름이 있는 배열 자료형
- **DataFrame**
  - 두 개 이상의 Series로 구성된 자료형
  - 2차원 배열 혹은 행렬
  - 행ID인 인덱스와 열ID인 컬럼으로 구성됨
  - 엑셀시트와 매칭됨
- **Index**
  - Series - 각 요소에 대한 ID 역할
  - DataFrame - 각 행에 대한 ID 역할



## 2. 데이터 인덱싱과 슬라이싱

- DataFrame에서 열 선택하기
  - `df['컬럼명']`



- 인덱스 참조
  - 명시적인 인덱스 참조
    - `loc()`
  - 암묵적인 인덱스 참조
    - `iloc()`





## 3. 데이터 불러오기

- CSV 파일
  - `read_csv()`



- xlsx, xls 파일
  - `read_excel()`



인터넷 상에 있는 데이터도 불러올 수 있습니다. 이때는 인자로 URL경로 넣어주면 됩니다.

```python
import pandas as pd
df = pd.read_csv('http://~~~')
```





## 4. 데이터 확인하기

**DF**

|    함수    |      설명       |
| :--------: | :-------------: |
|   shape    |  행과 열 개수   |
|   head()   |   앞 5개 확인   |
|   tail()   |   뒤 5개 확인   |
|   mean()   |      평균       |
|   var()    |      분산       |
|   min()    |     최소값      |
|   max()    |     최대값      |
| describe() | 기초통계량 확인 |
|   corr()   |  상관계수 확인  |

