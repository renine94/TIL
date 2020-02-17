# 모듈(module)

2020/02/17

> 모듈은 파이썬 정의와 문장들을 담고 있는 파일
>
> 파일의 이름은 모듈 이름에 확장자 `.py` 를 붙인다.

- 모듈
  - 특정 기능을 .py 파일 단위로 작성한 것.
- 패키지
  - 특정 기능과 관련한 **여러 모듈들의 집합**. 
  - 패키지 안에는 또다른 서브 패키지를 포함할 수 있음
  - 인터넷에 있는 패키지를 설치해서 사용 (bs4)
- 파이썬 표준 라이브러리
  - 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서 파이썬 표준 라이브러리라 함
- pip (패키지 관리자)
  - `pyPI` 에 저장된 외부 패키지들을 설치하도록 도와줌





### 버전관리

![semantic versioning 이미지 검색결과](https://miro.medium.com/max/524/1*c2lrK2Bqvntq1p-frD2KcQ.png)



ex) 파이썬 3.7.3

앞에 3버전대가 바뀌어버리면 하위호환성이 깨지는 경우가 있음.





### 다양한 모듈 사용법

```python
import module
import pakage1.module1, pakage2.module2
from module import var
from module import function
from module import Class
from module import *  # 변수명이 겹칠 위험이 존재함, 지양바람, 공간 상의 비효율
from pakage.module import var, function, Class
```



