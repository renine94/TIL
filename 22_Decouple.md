# decouple 

> 

## .env

> 프로젝트에서 키 숨기는 방법
>
> db 를 숨기거나 코드에 드러내고싶지 않은 부분을 처리 해준다.

### 1. 패키지 설치

- `pip install python-decouple`



### 2. 사용법

- `.env`

  - 프로젝트 최상단에 파일을 만들어준다.

  - ```python
    ACCESS_KEY=공개키
    ```

- 사용하는 `.py` 에서

  - ```python
    from decouple import config
    
    access_key = config('ACCESS_KEY')
    ```

- `.gitignore` 

  - `.gitignore` 에다가 `.env` 를 추가시킨다.



### 3. 사진  설명

#### 	1. Env 파일을 폴더의 루트에다가 만들어준다.

![image-20200331133524359](img/image-20200331133524359.png)

#### 	2.  사용해야하는 `.py` 파일 내에서 사용한다.

​	![image-20200331133850554](img/image-20200331133850554.png)

