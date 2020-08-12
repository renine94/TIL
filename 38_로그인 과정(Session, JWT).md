# :key:로그인이 이루어지는 과정



## 1. 세션 `id` 를 이용하는 방식

이 방식에서는 서버는 특정 유저의 정보를 담은 세션을 생성한다.

1. 유저가 로그인할 때
2. 서버는 세션을 생성한 후
3. 그 세션의 `id`를 클라이언트에 보내주고
4. 클라이언트는 이 `id`를 클라이언트에 저장해두었다가
5. 인증이 필요한 데이터를 가져올 때 서버에 `id` 값을 보내면
6. 서버는 그 `id`를 통해 세션을 불러와 유효한지 확인하는 방식으로 인증

![](https://media.vlpt.us/images/yaytomato/post/0a2cbabb-4ba8-4325-91e1-e0efc992dfd2/%E1%84%89%E1%85%A6%E1%84%89%E1%85%A7%E1%86%AB%20%E1%84%8B%E1%85%B2%E1%84%8C%E1%85%A5%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC.png)





## 2. JWT 을 이용하는 방식

비슷한 방식으로

1. 유저가 로그인할 때
2. 서버가 인증 정보를 보내주는데, 암호화나 시그니처 추가가 가능한 데이터 패키지안에 인증정보를 담아 보내준다.(이 패키지가 JSON Web Token 즉 JWT 이다.)
3. 담기는 정보 중 `accessToken` 과 `refreshToken`이 이후 유저인증에 사용되는데
4. 이 정보를 클라이언트에 저장해준다.

```
좀 더 자세히 설명하면 실질적인 인증 정보는 accessToken 인데 일정 시간이 지나면 만료하는 구조를 가지고 있다.(로그인 후 며칠 뒤 로그인이 만료돼서 다시 로그인해야 했던 경험이 있는가?) refreshToken을 이용해 로그인을 지속적으로 유지할 수도 있다. refreshToken을 서버에 보내면 그때마다 새로운 accessToken을 발급해 돌려주는 거다. refreshToken 사용은 옵션이다.
```

5. 이 `accessToken`을 유저에게만 보여줄 수 있는 정보에 접근할 때 서버에 보내면
6. 서버는 그 토큰이 유효한지 확인하는 방식으로 인증한다.

![](https://media.vlpt.us/images/yaytomato/post/94ff189f-46fb-4901-bb7f-06d7b2154834/JWT%20%E1%84%8B%E1%85%B2%E1%84%8C%E1%85%A5%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC.png)





## 3. react 또는 vue에 적용하기

#### 준비물

로그인 API를 호출할 때 백엔드는 HTTP 응답 `Set-Cookie` 헤더에 `refreshToken` 값을 설정하고 `accessToken`을 Json payload에 담아 보내줘야 한다.



##### 클라이언트에서 처리하기

```js
onLogin = (email, password) => {
  const data = {
      email,
      password,
  };

  axios.post('/login', data)
    .then(res => {
      const { accessToken } = res.data;
      
      // API 요청하는 콜마다 헤더에 accessToken 담아 보내도록 설정
      axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;
      
      // accessToken을 localStorage, cookie 등에 저장하지 않는다!
    })
    .catch(err => console.err(err));
}
```





## 4. 로그인 만료, 로그인 연장 처리하기

JWT 인증 방식에서 실질적으로 인증되었나를 결정하는 것은 `accessToken` 이다.
하지만 우리가 택한 구조에서 브라우저에 저장된 값은 쿠키에 저장된 `refreshToken` 뿐이기에
로컬에 저장된 `accessToken` 은 브라우저 창이 꺼지거나 페이지가 리프레시 되는 등 페이지가 리로드 되면 사라진다. 또한, `accessToken` 은 일정 시간이 지나면 만료된다. 그래서

1. 이메일, 비밀번호를 입력해서 `accessToken` 을 받아오는 보통 로그인 처리뿐만 아니라 보다 완성도 있는 사이트를 만들기 위해
2. `accessToken` 이 만료됐을 때 어떻게 처리할 지(예를 들어 은행 사이트같이 보안이 중요한 서비스라면 아예 다시 로그인하도록 로그인 페이지로 이동시킬 수도 있고, 아니면 유저 모르게 서버에서 새로운 accessToken을 받아와서 로그인이 연장되도록 할 수도 있음)
3. 페이지 리로드 될 때 어떻게 처리할 지도 결정해야 한다.



이 예제에서는 유저가 다시 직접 로그인하도록 유도하지 않고 조용히 자동으로 로그인 연장하는 기능을 구현해보겠다. (영어로 silent refresh 라고 부른다.)



#### 처리할 "로그인" 케이스들

1. 이메일, 비밀번호를 체크하는 보통 로그인

![](https://media.vlpt.us/images/yaytomato/post/19ef3dde-c7a4-495f-97bc-8411bd59a17c/%E1%84%87%E1%85%A9%E1%84%82%E1%85%A5%E1%84%89%E1%85%B3_%20JWT%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB.png)

2. `accessToken` 이 만료됐을 때 로그인 연장 처리
3. 페이지 리로드 될 때 로그인 연장 처리

![](https://media.vlpt.us/images/yaytomato/post/adc86cfd-188a-4423-bf7c-9dcc8d0950fa/%E1%84%87%E1%85%A9%E1%84%82%E1%85%A5%E1%84%89%E1%85%B3_%20JWT%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%8C%E1%85%A1%E1%86%BC.png)



#### 준비물

위에서 이야기한 3가지 케이스에 대응하기 위해 API가 2개 필요하다.

1. `POST /login` : 이메일, 비밀번호를 보내면 `refreshToken`과 `accessToken`을 리턴한다.
2. `POST /silent-refresh` : 쿠키에 담긴 `refreshToken`이 자동으로 보내지면 새로운 `refreshToken`과 `accessToken`을 리턴한다.



두 API 모두 HTTP 응답 `Set-Cooke` 헤더에 `refreshToken`값을 설정하고 `accessToken`을 Json payload에 담아 보내줘야 한다.



#### 클라이언트에서 처리하기

1. 로그인
2. 로그인 만료되기 전에 연장

```js
const JWT_EXPIRY_TIME = 24 * 3600 * 1000; // 만료시간 (24시간 밀리 초로 표현)

onLogin = (email, password) => {
    const data = {
        email,
        password,
    };
    axios.post('/login', data)
      .then(onLoginSuccess)
      .catch(err => console.err(err))
}

onSilentRefresh = () => {
    axios.post('/silent-refresh', data)
      .then(onLoginSuccess)
      .catch(err => console.err(err))
}

onLoginSuccess = res => {
    const { accessToken } = res.data;
    
    // accessToken 설정
    axios.defaults.headers.common['Autorization'] = `Bearer ${accessToken}`;
    
    // accessToken 만료하기 1분 전에 로그인 연장
    setTimeout(onSilentRefresh, JWT_EXPIRY - 60000);
}
```



3. 페이지 리로드 될 때 로그인 연장

```js
// 어플리케이션이 실행될 때마다 다시 로그인 시도
class App extends Component {
    componentDidMount() {
        onSilentRefresh();
    }
    // ...
}
```



## 마치며...



