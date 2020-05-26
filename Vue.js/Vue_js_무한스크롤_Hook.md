# Vue.js





## :one: 무한스크롤 (Life Cycle Hook )

> - 필요 라이브러리
>   - [Vue.js](https://kr.vuejs.org/v2/guide/installation.html)
>   - [Axios Github](https://github.com/axios/axios)
>   - [ScrollMonitor Github](https://github.com/stutrek/scrollMonitor) / [CDN](https://cdnjs.com/libraries/scrollmonitor)

- 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .button-bottom {
      position: fixed;
      right: 10vw;
      bottom: 10vh;
    }
  </style>
  <title>Scroller</title>
</head>
<body>

    
  <div id="app">
    <div v-for="photo in photos">
      <h5>{{ photo.title }}</h5>
      <img :src="photo.thumbnailUrl" :alt="photo.title"> <!-- v-bind:표준속성  -->
    </div>
    <button @click="scrollToTop" class="button-bottom">^</button>
    <!-- HTML 이 Vue 인스턴스와 연결된 순간부터, Life cycle hook 의 영향을 받는다. -->
    <div id="bottomSensor"></div>
  </div>




  <!-- Vue & 비동기 & 스크롤모니터 -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/scrollmonitor/1.2.0/scrollMonitor.js"></script>
    
    
    
    
  <!-- 사용자 정의 js -->
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        photos: [],
        page: 1,
      },
      methods: {
        getPhotos: function() {
          const options = {
            params: {
              _page: this.page++,
              _limit: 3,
            }
          }
          axios.get('https://jsonplaceholder.typicode.com/photos', options)
            .then(res => {
              // console.log('>>> GET PHOTOS <<<')
              // spread 배열합치기(Python / JS는 방법이 다름)
              this.photos = [...this.photos, ...res.data]
            })
            .catch(err => console.err(err))
        },

        addScrollWatcher: function() {
          const bottomSensor = document.querySelector('#bottomSensor')
          const watcher = scrollMonitor.create(bottomSensor)
          // watcher 가 화면에 들어오면, 콜백(cb) 하겠다.
          // 콜백함수는 Arrow 함수 표기법 사용
          watcher.enterViewport(() => {
            setTimeout(() => {
              this.getPhotos()
            }, 500) // 0.5초
          })
        },

        scrollToTop: function() {
          scroll(0, 0)
        },

        loadUntilViewportIsFull: function() {
          const bottomSensor = document.querySelector('#bottomSensor')
          const watcher = scrollMonitor.create(bottomSensor)
          if (watcher.isFullyInViewport) {
            this.getPhotos()
          }
        },
      },

      // LifeCycleHook
      // https://assist-software.net/blog/how-use-vue-instance-lifecycle-hooks

      // created: 초기화 이후 Ajax 요청 보내기 좋은 시점(Data, Methods 접근가능)
      created: function() {
        this.getPhotos()
      },

      // mounted: DOM 과 Vue 인스턴스가 연동이 완료되고 난 이후에 실행할 일들
      mounted: function() {
        this.addScrollWatcher()
      },

      // updated: data({}) 가 바뀌고 나서, 화면이 다시 렌더된 이후,
      updated: function() {
        this.loadUntilViewportIsFull()
      },

    })

  </script>
</body>
</html>
```





**해당 코드를 이해하기 위해서는 Life Cycle Hook 의 개념을 알아야 한다.**

![생애주기](https://cdnsite1.assist.ro/sites/default/files/styles/big/public/images/blog/Vue-instance-lifecycle-Page-1.png?itok=OdC8TOWx)

