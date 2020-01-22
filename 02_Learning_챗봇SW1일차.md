# 0115

> 교육 프로그램 플랫폼
>
> 	https://www.udacity.com/
> 	https://www.edx.org/
> 	https://www.coursera.org/

___

# 챗봇SW 퀘스트 1일차

- python의 문법
  1. 저장
  2. 조건
  3. 반복



### 저장

- 저장의 개념? save...
  - dust = 60  >>> 60을 'dust' 라는 변수에 저장



- 무엇을 저장하는가
  - 숫자 : 현실세계에 존재하는 모든 숫자
  - 글자 : 현실세계에 존재하는 존재하는 모든 글자. 
    - **따옴표**로 둘러싼 글자 or 숫자
  - 참/거짓 ( True / False )
    - 조건/반복에 사용됨 
    - ex) 300 > 200     =>  True
    - ex) 150 == 161   =>  False



- 어떻게 저장하는가

  - 변수(variable)

    - 저장된 값을 변경 할 수 있는(variable) 박스.

    - 숫자, 글자, 참거짓을 담을 수 있다.

    - ```python
      dust = 58
      dust = 60
      print(dust)
      ```

  - 리스트(List) , 배열

    - 박스가 순서대로 여러 개가 붙어있다.

    - ```python
      location = ['영등포구','구로구']
      print(location[1])
      ```

  - 딕셔너리(dictionary)

    - 궁극의 박스 "견출지 붙인 박스들의 묶음"

    - ```python
      dust = {'영등포구':58, '강남구':49}
      print(dust['영등포구'])
      ```



| ""       | 저장하는법               | 불러오는법       | 출력값    |
| -------- | ------------------------ | ---------------- | --------- |
| 변수     | a = 1                    | print(a)         | 1         |
| 리스트   | a = [1, 2, 3]            | print(a)         | [1, 2, 3] |
| 딕셔너리 | a = {'서울':1, '인천':2} | print(a['서울']) | 1         |



- 점심메뉴 실습예제

  - ```python
    # menu 리스트를 만들어주세요.
    import random
    
    menu = ['스테이크', '성게알밥', '트러플그라탕', '참치회']
    
    phone_book = {
      '스테이크':'010-1234-5678',
      '성게알밥':'010-1111-2222',
      '트러플그라탕':'070-1234-4444',
      '참치회':'080-1212-1515',
                 }
    
    food = random.choice(menu)
    
    # print(food + '입니다. ' + '전화번호는 ' + phone_book[food] + ' 입니다.')
    # print(f'{food}입니다. 전화번호는 {phone_book[food]}입니다.') # f 스트링 3.7버전이상부터 지원
    print('{}입니다. 전화번호는 {}입니다.'.format(food, phone_book[food]))
    
    ```



### 조건(if/else)

- ```python
  dust = 60
  
  if dust > 50:
  	print('50초과')
  else:
  	print('50이하')
      
  50초과
  ```

- 미세먼지 실습예제

  - ```python
    import requests
    from bs4 import BeautifulSoup
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'.format(key)
    request = requests.get(url).text
    soup = BeautifulSoup(request,'xml')
    item = soup('item')[5]
    time = item.dataTime.text
    dust = int(item.pm10Value.text)
    
    # dust 변수에 들어 있는 내용을 출력해보세요.
    print('{} 기준 미세먼지 농도는 {}입니다.'.format(time, dust))
    
    # dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
    if dust > 150 :
      print("매우나쁨")
    elif 80 < dust <= 150 :
      print("나쁨")
    elif 30 < dust <= 80 :
      print("보통")
    elif 0 <= dust <= 30 :
      print("좋음")
    ```



### 반복

> while 은 무한반복하고, 종료조건이 필요하지만
>
> for 은 한번 순회반복하고, 종료조건이 따로 필요치 않다.



- While

  - while 에 해당하는 조건일 동안 계속 반복.

    - ```python
      n = 0
      while n < 3 :
      	print('출력')
      	n = n+1
      ```

- for 

  - 순회 : 한번씩 들르고 가는것

    - ```python
      for i in List :
      	print('정해진 범위 안에서 계속')
      ```

  



## API (Application Programming Interface)

> 응용 프로그램에서 사용할 수 있도록,
>
> 운영 체제나 프로그래밍 언어가 제공하는 기능을
>
> 제어할 수 있게 만든 인터페이스를 뜻한다.

~~코드는 일단 돌아가게 짜고, 그뒤에 `최적화` 를 통해 수행속도를 개선하자...~~



### 웹(WEB)에서의 커뮤니케이션 방식

> 대부분의 서비스는 요청(request)과 응답(response)으로 이루어져 있다.

​						

   요청               >>>>           응답

(사용자)						   (XML, JSON)



**오픈 소스 기술 + API 통신 = 쉬워진 프로그래밍**





### 로또 실습예제

```python
# 아래에 코드를 작성하세요.
import random

list = range(1, 46)
a = random.sample(list, 6)

print(sorted(a))
```







