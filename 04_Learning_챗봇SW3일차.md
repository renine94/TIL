# 0117

# 챗봇서비스SW 3일차

##### 1. 앱을 실행하면 자동 서버 재부팅 (오토 로딩)

- app.py 맨아래에 추가

  - ```python
    if __name__ == '__main__' :
        app.run(debug=True)
    ```

- cmd 실행 후

  - ```
    cd flask
    python app.py
    ```

- 홈페이지 접속

  - `127.0.0.1:5000` 은 `localhost:5000` 로 대체 가능



##### 2. 메인화면 변경

- 글자를 띄워주는게 아니라 index.html 문서로 응답

  - templates 폴더에 index.html 추가

    - ```python
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>잡동사니</title>
      </head>
      <body>
          <h1>다양한 서비스</h1>
          <a href="/pastlife">당신의 전생은?!</a>
          <a href="/html">검색 다모아</a>
      </body>
      </html>
      ```



## 공공데이터 포털

> www.data.go.kr

##### 1. 회원가입

##### 2. 키발급

- API 사용

  - 주소창에 `API주소`  넣고 발급받은 `KEY` 를 `{}` 에 넣어주면 `XML 또는 Json`  파일 형식 볼 수 있음

    - ```
      미세먼지 api
      http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6
      
      키 key ( 공공데이터 포털에서 개인적으로 받아옴 )
      Q1tzJ3HGeYfiUk2yVBLLSxToVyyCncSr2BMo9rRGTv1S0hx%2FDHBfWreugEi7VIizNWpdf9aK9025wCpby40MsA%3D%3D
      ```





## 챗봇만들기

#### 1. 텔레그램 데스크탑 버전 설치

- 봇파더를 통해 봇 만들기

  - /newbot

  - ```
    메이킹 리퀘스트
    https://api.telegram.org/bot1052992854:AAHPTYxtXMaRZWkPtvoKgZsA8aURju6Vyko/getMe
    ```

  - ```
    key = 비밀
    
    https://api.telegram.org/bot[TOKEN]
    /sendMessage?chat_id=812493852&text=펭하
    ```

- 봇파더를 통해 발급받은 키를 api 사용법과 같이 활용하여 다양한 기능 수행

  



#### 2. 파이썬을 통해 request 받고 보내기

- 코드

  - ```python
    import requests
    from pprint import pprint
    
    base_url = 'https://api.telegram.org'
    key = '비밀' # 나의 개인 키
    update_url =f'{base_url}/bot{key}/getUpdates' # f 스트링
    
    '''
    url 에 요청을 보내서 받아온 json 파일을 response 변수에 넣는다.
    json 파일을받기 때문에 뒤에 .json() 함수를 써준다.
    '''
    # 1. chat_id 1개만 받아오기
    # response = requests.get(update_url).json()
    # chat_id = response['result'][0]['message']['chat']['id']
    # print(chat_id)
    
    '''
    보기좋게 프린트 해주는 라이브러리 pprint
    pprint.pprint(response)
    '''
    ## - chat_id 전부 가져오기
    response = requests.get(update_url).json()
    chat_ids = []
    for result in response['result']:
        chat_ids.append( result['message']['chat']['id'] )
       
    print( chat_ids )
    
    # set() 함수를 실행한 결과를 다시 abab 변수에 넣어줘야 반영이 된다.
    abab = set(chat_ids)
    print( abab )
    
    # 2. 받아온 chat_id로 메시지 보내기. ( 입력값을 보내기 )
    text = input('텍스트를 입력하세요.')
    for chat_id in set(chat_ids):
        message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(message_url)
    ```

- getUpdates 를 계속안하고, 텔레그램에게 일을 시키기

  - **Webhook** ( 웹훅 )

    - 누군가가 `특정단어` 를 보내면 챗봇이 나에게 알려준다...

    - 텔레그램이 나에게 요청(상태변화)가 있어요 라고 알려줌

    - 나는 서버를 열어두고 텔레그램이 알림을 보내면 그걸 처리해서 다시 챗봇에게 보내줌

    - setWebhook(URL) : 챗봇에게 갈고리를 걸때 어디로(url) 요청을 받을건지 명시해줘야함

      - URL 은 우리의 서버 주소를 적는것

    - ```
      [setWebhook] 웹훅 설정하기
      인터넷 주소창에 입력 ( ngrok 프록시 서버 경유함 )
      
      [ ngrok 에 웹훅 걸기 ]
      https://api.telegram.org/bot[TOKEN]/setWebhook?url=https://61260667.ngrok.io/telegram
      
      [ pythonanywhere 에 웹훅 걸기 ]
      https://api.telegram.org/bot[TOKEN]
      /setWebhook?url=http://kjaegu9771.pythonanywhere.com/telegram
      ```

      

  

  - **ngrok** ( 요청을 대신 받아주는 친구 ) `프록시` `대리인` 
    - 서버가 로컬호스트에서 열려있기 때문에 챗봇(텔레그램)이 멀캠을 뚫고 이 서버로 들어올수없기때문
    - ngrok 이라는 프록시 서버를 두고 요청을 대신 받게 만든다
    - 설치파일(.zip) 을 홈디렉토리(user/multicampus) 로 옮긴다.
    - cmd 에서 `ngrok http 5000` 이라고 입력하여 실행 ( cmd 는 ngrok 서버 열음 )
      - git bash 는 나의 서버를 돌릴 예정
      - `https://61260667.ngrok.io` ngrok 프록시서버
    - ![image-20200124130900392](C:\Users\kjaeg\TIL\img\image-20200124130900392.png)
    - 
    - 
    - setWebhook 을 설정하게되면, getUpdates 는 멈춘다. ( 챗봇이 알아서 공지를 주기 때문에 )
    - 



requests 는 .json()

flask 의 request 는 get_json()



#### 3. 챗봇에 파파고API 붙이기

> Header 에 문서정보가 들어간다.
>
> <meta> 정보라고도 함

- post 방식으로 요청보내기

  - ```python
    requests.post(url, 헤더정보, 데이터) 
    ```

  - ```python
    import requests
    from pprint import pprint
    
    client_id = '비밀'
    client_secret = '비밀'
    
    text ='안녕'
    papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
    
    # 네이버 API 는 대부분 post 방식으로 요청을 보내달라고 명시해놓음
    # requests.post(url, {헤더정보}, {데이터}) 
    
    headers = {
        'X-Naver-Client-Id' : client_id,
        'X-Naver-Client-Secret' : client_secret,
    }
    data = {
        'source' : 'ko',
        'target' : 'en',
        'text' : text,
    }
    response = requests.post(papago_url, headers=headers, data=data)
    
    # get_json() 은 플라스크꺼.
    pprint(response.json())
    
    ```



### Git bash 한글설정

- 우클릭 - Option - Text - Locale - ko_KR - eucKR



### Python decouple 

> 깃허브에 파일을 올릴때 인증키와 같은 중요한 정보는 숨겨서 올려야할때 쓰는 라이브러리

- `pip install python-decouple` 

- `.env`  파일 만들어주기

  - ```python
    from decouple import config
    
    client_id = config('NAVER_CLIENT_ID')
    ```

  - .env 파일에 대문자(상수) 로 키(TOKEN) 같은것들을 다 모아둔다.

    - ```
      NAVER_CLIENT_ID='인증키부분'
      ```

  - 



___

