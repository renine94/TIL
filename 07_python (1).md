# 파이썬 (1) - 0120

### 1.깃허브(Github)

> https://backlog.com/git-tutorial/kr/intro/intro1_1.html 블로그 참조
>
> 통합 버전 관리 시스템,  소스코드 관리도구
>
> 폴더 중심. ( 폴더를 기점으로 관리하게 됨 )

- 개요

  - ![image-20200122173613289](C:\Users\multicampus\Desktop\미래의 TIL\07_python (1).assets\image-20200122173613289.png)
  - 
  - 이렇게 버전관리가 안되기 때문에 git 을 사용함
  

  
  - SCM : 소스 코드 매니지먼트 (what)
  - VCS : 버전 컨트롤 시스템 (how)



- 버전 확인
  - `git bash` 에서 `git --version` 입력



- TIL ( Today I Learned )
  - 오늘 내가 배운 내용을 폴더로 관리



- **깃만들기 순서** ( git bash 에서 진행 )
  1. 폴더를 만들고 `git init` 이라고 치면 `master` 가 생긴다.
  2. `master` 가 있으면 `git` 으로 관리되는 폴더이다.
  3. `ls -a` 명령어를 치면 숨어있는 .git 파일을 볼 수 있다.



- **git bash 명령어**

  1.  파일 내용 보기

     - `cat 파일명` 

  2.  파일 지우기

     - `rm -r .git`  .git 폴더를 지우겠다는 뜻

  3.  상태확인 명령어

     - `git status` 

  4.  git 에 파일 추가하기 ( 파일을 커밋 준비를 시킨 것 )

     - `git add 파일 또는 폴더명` 

  5. git 에 사진찍기 ( 파일을 저장하기 )

     - `git config --global user.name "Jaegu Kang"` 메타정보 집어넣기

     - `git config --global user.email "kjaegu9771@gmail.com"`  gitgub 이메일 넣기

     - `git config --global --list` 메타정보 확인하기 

     - ```shell
       git commit -m "first commit"  첫번째 커밋, first commit 은 변경내용 적어주는게 좋음
       ```

  6.  commit 들의 모음을 보고싶다.

     - `git log` 
     - `git log --oneline` "메시지" 들의 모임 ( 뭘 했는지에 대한 정보만 볼 수 있음 )

  7.  파일 추가하기 ( 00_markdown_basic 추가한것처럼 )

     - `touch 파일or폴더명` 

       - ```shell
         *순서*
         
         touch a.txt
         git status
         git add a.txt
         git status
         git commit -m "Add a.txt"
         git log
         git log --oneline
         ```

  8.  이전 버전 시점으로 돌아가기 ( checkout )

     - `git checkout fa9f3ad`  고유시점으로 돌아가기 `fa9f3ad` "first commit" 시점으로 돌아가기
     - 다시 되돌아가기
       - `git checkout master` master 시점으로 다시 되돌아간다.

  9.  git remote (로컬저장소에서 원격저장소에 올리는 명령어 모음)

     - 추가하기

       - `git remote add 저장소의 이름(별명) 저장소의 주소` 

         - ```shell
           git remote add origin https://github.com/94incheon/TIL.git
           ```

         - 저장소의 이름 : origin

     - 버전 확인하기

       - `git remote -v` 더 많은 정보 보기

     

     - **git push ( 모심기 )** 앞으로 1년동안 매일매일 해야됨 하루도 빠짐없이......
       - `git push origin master` 깃허브의 TIL 폴더에 올라갔음

  10. bit.do/01_TIL 실습 따라하기
  
  11.  수정이력넣기
  
      - `git add -u` 
        -  rm a.txt 한 내용도 반영시킴..





## 집에서 원격저장소(github) 접속해서 코드 받아오기

- git bash 실행후 `clone` 명령어 실행

  - ```shell
    $ git clone https://github.com/94incheon/TIL.git
    ```



- 파일 생성하고,

```shell
$ touch "파일명"
```



- 파일 추가 (add) 하고

```shell
$ git add "파일명"
```



- 파일 저장 (commit) 하고

```shell
$ git commit -m "커밋 메시지 주석"
```



- 파일 푸쉬 (push) 해서 원격저장소로 보내기

```shell
$ git push origin master
```



- 순서

  - ![image-20200122173659944](C:\Users\multicampus\Desktop\미래의 TIL\07_python (1).assets\image-20200122173659944.png)
  - 

- 홈 디렉토리 가기

  - ```
    cd ~
    ```

- 깃허브

  1. 디렉토리 추가
  2. 셋팅 - 콜라보레이션 탭
  3. 이메일 or 닉네임 으로 협업동료 추가
  4. 해당 동료는 이메일에서 수락누르면 그때부터 push 가능해짐





### Github (용어)

___

(1) Pull Requests

> 포크 앤 플릭.. 방식..?
>
> 협업 권한이 없는사람이 원격저장소 주인에게 코드에러있다고 코드수정한거 요청하는곳..??

- 순서
  1. 강동주쌤 백일장을 `fork` 해서 내 원격저장소에 복제?? 한다.. (브랜치)
     - fork 한뒤에 `git clone [가져온주소]` 으로 내 로컬저장소로 가져옴
  2. `git bash` 에서 해당 코드를 수정하고 내 원격저장소에 다시 `push` 해서 올린다.
  3. `github` 홈페이지에서 `pull requests` 을 눌러서 동주쌤에게 반영해달라고 요청한다.
- ![image-20200122173720816](C:\Users\multicampus\Desktop\미래의 TIL\07_python (1).assets\image-20200122173720816.png)
- 



- 클론 받아올때 이름 지정하기

  - ```shell
    $ git clone https://github.com/edu-john/python.git [master-python]
    ```

- 파일 복사하기 ( cp )

  - ```shell
    $ cp [복사할파일의 주소] [복사할위치]
    
    $ cp ~/master-python/01_python_intro.ipynb .
    ```



## 주피터 노트북 설치

> `jupyter notebook` 은 데이터 사이언스 파트에서 많이 활용한다.
>
> 머신러닝, 딥러닝, 인공지능, 빅데이터 등등.. 

### (1) 설치

- 설치하기

  - ```shell
    $ pip install jupyter
    ```

- 실행하기

  - ```shell
    $ jupyter notebook
    ```

  - `Ctrl + Enter` 실행하기
  
- 셀 삭제

  - 셀을 선택한후 `esc` 를눌러서 코드편집에서 나온후에,
  - 셀 선택 후 `dd` 를 누르면 된다.
  - `z` 를 누르면 되돌리기







## 라이브러리

### Keyword

- 키워드 들을 볼 수 있는 라이브러리

  - ```python
    import keyword
    
    print(keyword.kwlist)
    ```




`TypeError` : `callable` 은 함수라고 보면된다.



`함수명.__doc__` 은 함수의 멀티주석 내용을 볼 수 있다.



### Sys

- 





## 파이썬

> 파이썬 돌릴 때 **'python tutor'** 꼭 실행해서 컴퓨터 동작원리 이해할 것



- 할당

  - `=` 으로 변수에 자료를 할당한다

- 자료형

  - 숫자형(Numbers)

    - int (정수)
    - float(실수)
    - complex(복소수)

  - 문자형(String)

    - 

  - **블리언(bool)**

    - True / False 

    - Flase = 0 이거나 [] 비어있거나, None

      - ```python
        홀수 판별
        
        if a % 2 :
        
        나머지가 1 이면 조건이 True 이므로 if문이 실행된다. ( 홀수 라는 얘기 )
        ```

- 





## HW & WS

```shell
$ git credential reject
$ protocol=https
$ host=lab.ssafy.com 

엔터 2번하면 초기화됨.
```



### (1) gitlab .....

