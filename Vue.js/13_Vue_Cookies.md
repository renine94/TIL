# Vue-Cookies

> [공식문서](https://www.npmjs.com/package/vue-cookies)
>
> 비동기요청으로 Django 서버에 로그인하여 보내서 받은 Token 값을
>
> 브라우저 Cookie 에 저장을 편리하게 하기 위해서 사용하는 라이브러리이다.

`route53` 에서 domain 구입 추천 ( AWS )



- 현재상태
  - `vue create [프로젝트명]`
  - `vue add router` 







:cupid: 설치

```shell
$ npm i vue-cookies --save
```



:cupid: 설정

```js
// main.js

import Vue from 'vue'
import App from './App.vue'
import router from './router'

// 이 부분 추가 vue-cookies 사용하겠다.
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```



:cupid: 사용

- App.vue
- [native 쓰는이유](https://eddie2yim.tistory.com/47)
  - .vue컴포넌트에서 **Vue객체의 이벤트를 바인딩** 하고자 한다면, **.native**를 사용해 연결한다
  - 즉, 자기 컴포넌트에서 정의한 이벤트가 아니고 App.vue 에서 정의한걸 다른 컴포넌트가
    쓰고 있기때문???????

```html
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/accounts/login">Login</router-link> |
      <!-- native 옵션을 줘야함 -->
      <router-link @click.native="logout" to="/accounts/logout">Logout</router-link>
    </div>
    
    <router-view @submit-login-data="login" />
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8090'

export default {
  // 전달받은 데이터 Django 보내줌 -> token 받아 로그인 상태 유지
  name: 'App',
  data() {
    return {
      isLoggedIn: false
    }
  },
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },

    login(loginData) {
      axios.post('http://localhost:8090/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key) // res.data.key => token
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err))
    },

    logout() {
      const requestHeaders = {
        header: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }

      axios.post(SERVER_URL + '/rest-auth/logout/', null, requestHeaders)
        .then((res) => {
          console.log(res.data)
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response))
    },
  }
}
</script>
```