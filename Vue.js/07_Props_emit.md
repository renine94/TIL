# Vue.js - Props_emit

[컴포넌트가 무엇인가요?]([https://kr.vuejs.org/v2/guide/components.html#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EC%9E%91%EC%84%B1](https://kr.vuejs.org/v2/guide/components.html#컴포넌트-작성))



## :one: Props

> 부모에서 자식으로 데이터를 넘겨준다.
>
> 단방향 데이터 흐름



- Parent
  - Child 자식에게 props 를 내려줌

```html
<template>
  <div class="parent">
    <h1>부모 컴포넌트</h1>
    <!-- 1. prop 이름="내용" -->
    <Child @hungry="parentMsg = '밥먹어라.'"  :propFromParent="parentMsg" />
  </div>
</template>

<script>
import Child from '../components/Child.vue'

export default {
  name: 'Parent',
  data() {
    return {
      parentMsg: '부모에서 내리는 메시지'
    }
  },
  components: {
    Child, // 'Child': Child
  }
}
</script>

<style>
  .parent {
    border: 3px solid red;
    margin: 3px;
    padding: 3px;
  }
</style>

```



- Child
  - `this.$emit('커스텀이벤트이름')`
    - 부모에게 이벤트를 알리는 것.
    - 부모의 데이터에는 접근 불가능

```html
<template>
  <div class="child">
    <h2>자식 컴포넌트</h2>
    <!-- 3. 사용한다 -->
    {{ propFromParent }}
    <button @click="hungrySignal">배고파요!</button>
  </div>
</template>

<script>
export default {
  name: 'Child',
  // 2. props 등록(반드시 Object를 써야지 Validation 가능)
  props: {
    propFromParent: String,
  },
  methods: {
    hungrySignal() {
      // 부모한테 이벤트(시그널) 방출
      this.$emit('hungry') // 커스텀 이벤트
    }
  }
}
</script>

<style>
  .child {
    border: 3px solid blue;
    margin: 3px;
    padding: 3px;
  }
</style>
```

