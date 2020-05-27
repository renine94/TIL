# Vue.js

**더미데이터 제공 사이트**

[JSONPlaceholder](https://jsonplaceholder.typicode.com/)

[KoreanJSON](https://koreanjson.com/)



**메서드**

> 객체안에 들어있는 함수
>
> 메서드는 function 키워드로 정의

**에로우 함수**

> 콜백함수 정의할때는 에로우로 쓰자.



메서드 정의할땐 function 키워드

`콜백함수는 Arrow 키워드`





## :one: js - 배열 붙이는 방법

> .concat()
>
> spread
>
> push + spread

- 방법1 (concat)

```js
const arr1 = [1,2,3]
const arr2 = [4,5,6]

arr1.concat(arr2) // [1,2,3,4,5,6]
```

- 방법2 (spread)

```js
const arr1 = [1,2,3]
const arr2 = [4,5,6]

const arr3 = [...arr1, ...arr2] // 스프레드
```

- 방법3 (push + spread)

```js
const arr1 = [1,2,3]
const arr2 = [4,5,6]

arr1.push(...arr2)
```







## :two: Vue 객체의 라이프사이클

![생애주기](https://cdnsite1.assist.ro/sites/default/files/styles/big/public/images/blog/Vue-instance-lifecycle-Page-1.png?itok=OdC8TOWx)

**Life Cycle Hook**

- Declarative (선언형)

  - 유산슬을 만들어줘(대신해서 절차를 수행 => 프레임워크)

  - Vue.js (데이터의 변화에 맞춰 UI를 변경)

  - **UI 단계(Hook)**
    `== url('/articles/') -> views (list_article())`

    `== JS코드가 처음 생성되었을 때(hook) -> function()`

  

- Imperative (명령형)

  - 직접 요리(언제 무엇을)
  - 레시피(절차적)
  - Vanilla JS (DOM, 이벤트리스너)

  



:cupid:**무한 스크롤 구현하기**

- [스크롤 모니터 CDN](https://cdnjs.com/libraries/scrollmonitor)
  - [js 라이브러리](https://github.com/stutrek/scrollMonitor) 깃허브











## :three: Computed

> 함수인데, Data 를 Create Update Delete 하지 않고, Read(return) 하고 싶을 때.
>
> Python의 Property 같은 느낌 => 캐싱됨.
>
> 함수지만 실제로는 값으로 쓰이기 때문에 {{ bankrrupedPeople }} 네이밍 주의



- 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Computed</title>
</head>
<body>
    
    
  <!-- 코드 작성 -->
  <div id="app">
    <h1>Bankrruped</h1>
    {{ bankrrupedPeople }}
  </div>

    
    
  <!-- Vue.js & Script -->
  <script src="vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',

      data: {
        // accounts 라는 Table 을 만든다고 생각 (모델링 부분)
        accounts: [
          {name: 'neo', balance: 500, isBankrruped: true},
          {name: 'tak', balance: 700, isBankrruped: false},
          {name: 'john', balance: 350, isBankrruped: false},
          {name: 'justin', balance: 200, isBankrruped: true},
        ],
      },

      methods: {

      },

      // 함수인데, Data 를 Create Update Delete 하지 않고, Read(return) 하고 싶을 때.
      // Python의 Property 같은 느낌 => 캐싱됨.
      // 함수지만 실제로는 값으로 쓰이기 때문에 {{ bankrrupedPeople }} 네이밍 주의
      // 함수지만, 명사형으로 작성한다.
      computed: {
        bankrrupedPeople: function() {
          // filter 는 새로운 배열을 리턴한다.
          const newArr = this.accounts.filter((account) => {
            return account.isBankrruped
          })
          return newArr
        },
      },
    })
  </script>
</body>
</html>
```

