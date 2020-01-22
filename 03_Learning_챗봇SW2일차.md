# 0116

# 파이썬 챗봇SW 2일차

### 컴퓨터 조작하기

##### 1. **git bash** ( 리눅스랑 닮은 cmd 창 깔기 ) 

> git 사이트에서 2.25버전 다운로드 ( 깃배쉬 )
>
> > git bash 실행시키기
> >
> > > 환경변수에서 vs코드 path 추가하기 (2개 경로 모두)

- 명령어

  > 접속하자마자 나오는 ~ 은 홈디렉토리를 뜻함
  >
  > 어느정도 명령어 치고 Tab 누르면 자동완성됨

  - pwd : 현재 작업중인 디렉토리 ( print working directory )
  - ls : 폴더명 리스트로 뽑아보기
  - cd : 폴더 이동하기 ( change directoty )
    - `cd 폴더명` 폴더로 이동		`cd ..` 상위폴더이동		 `cd ~` 홈디렉토리 이동 `cd .` 현재 디렉토리
  - mkdir : 폴더만들기 ( make directory )
    - `mkdir [codes]` codes 라는폴더 생성 
  - clear : 화면 클리어 // cls
  - python [실행할파일]



### 웹 브라우저를 조작하기

##### 1. webbrowser 라이브러리 import

- 브라우저 열기
  - webbrowser.opne(url)



##### 2. 개발자 도구

- 크롬 - F12  
  - 네트워크
    - 헤더 - **Remote Address** : 네이버의 ip주소를 확인할 수 있음
  - 요소
    - `Ctrl + shift + C` 로 해당 소스 찾아서 우클릭  `Copy Selector`  



##### 3. 요청받기

- pip install requests
  - requests.get(url)
  - requests.get(url).text --> html 문서 출력된다.
- pip list
  - pip 에 깔려있는 패키지들 리스트들을 볼 수 있다.



##### 4. BeautifulSoup

> 웹크롤링에 사용되는 라이브러리

- bs4.Beautifulsoup(html문서넣기)

  - ```python
    # 심화 실습 : 네이버 실시간 검색어 가져오기
    # 총 10개 가져와 출력
    
    import requests
    import bs4
    from datetime import datetime
    
    url = 'https://www.daum.net/'
    now = datetime.now()
    
    
    # requests 라이브러리를 이용해서 요청 응답 받아오기
    response = requests.get(url).text
    
    # lxml 이라는 parser 를 통해 파서할것..
    data = bs4.BeautifulSoup(response, 'lxml')
    
    # id = #??? 인 태그만 가져온다.
    query = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li')
    
    
    print ("%s년 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute))
    
    for i in query :
        print(       
            i.select_one('.ir_wa').get_text() + ' : ' +
            i.select_one('.link_issue').get_text()
            )
    
    
    
    ```

  - select_one()

  - select()



##### 5. lxml

> Parser 의 한 종류



##### 6. 크롬 확장프로그램

- Json 뷰어 ( json viewer chrome extension )

  - ```shell
    https://chrome.google.com/webstore/detail/json-viewer/aimiinbnnkboelefkjlenlgimcabobli
    ```

  - 



### 플라스크

> 경량형 웹/서버 프레임워크

- 설치

  - `pip install Flask` 

- 실행

  - app.py 만들기

    - ```python
      from flask import Flask, render_template, request
      from datetime import datetime
      from faker import Faker
      
      app = Flask(__name__)
      fake = Faker('ko_KR')
      
      
      @app.route('/')
      def home():
          return 'happy hacking!'
      
      @app.route('/ssafy')
      def ssafy():
          return 'This is SSAFY'
      
      @app.route('/hello/<name>')
      def hello(name):
          return 'Hello ' + name
      
      # /cube/1 => 1
      # /cube/2 => 8
      # /cube/3 => 27
      
      @app.route('/cube/<int:num>')
      def cube(num):
          return str(num ** 3) 
      
      # datetime
      @app.route('/newyear')    
      def newyear():
          if datetime.today().month == 1 and datetime.today().day == 1 :
              return '예'
          else :
              return '아니오'
      
      @app.route('/html')
      def html():
          return render_template('home.html')
      
      @app.route('/pastlife')
      def pastlife():
          return render_template('pastlife.html') 
      
      @app.route('/result')
      def result():
          # pastlife 로부터 넘겨진 사용자의 이름을 받아온다. (result?user=강재구)
          user = request.args.get('user')
          job = fake.job()
          # render_template(a, b, c) a 화면을 렌더링해주고, b,c라는 데이터를 보내준다.
          return render_template('result.html', user=user, job=job)
      ```

  - 코드에 변경이 있을때마다 `ctrl + c` 로 서버를끄고 다시 `flask run` 으로 서버를 킨다.

  - `@app.route('cube/<num>')` 에서 num 은 기본적으로 str 취급함

    - 그래서 `@app.route('/cube/<int:num>')` 로 입력해줘서 들어오는 num 을 int 처리시킴



### HTML

- /home

  - ```html
    <!DOCTYPE html>
    
    <html>
        <head>
            <title>Jaegu Kang</title>
        </head>
        <body>
            <h1>Jaegu Kang</h1>
            <hr>
            <p>SAFFY 서울 1반 교육생 강재구입니다.</p>
            <a href="https://www.ssafy.com">SAFFY</a>
            <ul>
                <li>Java</li>
                <li>Python</li>
                <li>HTML</li>
            </ul>
    
            <h2>검색 다모아</h2>
    
            <h3>네이버</h3>
            <form action="https://search.naver.com/search.naver">
                <input type="text" name="query">
                <input type="submit">
            </form>
    
            <h4>다음</h4>
            <form action="https://search.daum.net/search">
                <input type="text" name="q">
                <input type="submit">
            </form>
    
            <h5>구글</h5>
            <form action="https://www.google.com/search">
                <input type="text" name="q">
                <input type="submit">
            </form>
        </body>
    </html>
    ```

- <from>

  - action="보내는곳"  >  url 창 결과로 나옴
  - `name="aa"`   =>   ?aa=.......  데이터를 보낼때는 박스에 담아서 보내야함 input 태그에 name



- /pastlife

  - ```html
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>당신의 전생은?!</title>
        </head>
        <body>
            <h1>당신의 전생은?!</h1>
            <p>당신의 전생을 알려드립니다.</p>
    
            <form action="/result">
                <input name="user" placeholder="이름을 입력해주세요." type="text">
                <input type="submit">
            </form>
        </body>
    </html>
    ```

- /result

  - ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>당신의 전생은!!</title>
    </head>
    <body>
        <h1>{{ user }}님의 전생은 {{ job }}입니다.</h1>
    </body>
    </html>
    ```



- 확인

> https://www.kjaegu9771.pythonanywhere.com/
> https://www.kjaegu9771.pythonanywhere.com/home
> https://www.kjaegu9771.pythonanywhere.com/newyear
> https://www.kjaegu9771.pythonanywhere.com/pastlife

[전생확인](https://www.kjaegu9771.pythonanywhere.com/pastlife)





### Deploy (배포)

> https://www.pythonanywhere.com/ 회원가입

1. app.py 와 templates 파일 업로드
2. 배쉬에서 pip3.7 install Faker
3. Web 탭에서 리로드
4. kjaegu9771.pythonanywhere.com/pastlife 접속