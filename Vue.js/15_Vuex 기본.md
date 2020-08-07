# Vuex 기본

> - 참조
>   - [티스토리](https://uxgjs.tistory.com/149)
>   - [Module 더 최소화하기](https://blog.woolta.com/categories/10/posts/132)





## 1. Vuex 구성

- State
- Mutations
- Actions
- Getters



### State

- Project에서 **공통으로 사용할 변수** 를 정의
- 프로젝트 내의 모든 곳에서 참조 및 사용이 가능합니다.
- state를 통해 각 컴포넌트에서 동일한 값을 사용할 수 있습니다.

```js
export const state = () => ({
    account: null,
    isAdmin: null,
    item: null
})
```



### Mutations

- **State를 변경시키는 역할** 을 합니다. ( mutations 을 통해서만 state를 변경해야함 )
- 비동기 처리가 아니라 **동기처리**를 합니다. 위의 함수가 실행되고 종료된 후 그 다음 아래 함수 실행됨
- `commit('함수명', '전달인자')` 으로 실행 시킬 수 있습니다.
- mutations 내에 **함수 형태** 로 작성합니다.

```js
export const mutations = {
    currentUser(state, account) {
        state.account = account; // state의 account 변수에 넘겨 받은 account 값을 입력함
    }
}
```



### Actions

- **Mutations를 실행시키는 역할** 을 합니다.
  - Mutations이 실행되면 state도 변경이 되겠지요.
- **비동기 처리**를 합니다. 순서에 상관없이 먼저 종료된 함수의 피드백을 받아 후속 처리를 합니다.
- `dispatch('함수명', '전달인자')` 으로 실행 시킬 수 있습니다.
- actions 내에 **함수 형태**로 작성합니다.
- 비동기 처리이기 때문에 콜백함수로 주로 작성합니다.

```js
export const actions = {
    setAccount({ commit, dispatch }, account) {
        commit('currentUser', account);
        dispatch('setIsAdmin', account.uid);
    }
}

dispatch('setAccount', account);
```



**Components에서 then() 으로 콜백함수 실행**

```js
dispatch('setAccount', account)
	.then( () => { } );

export const actions = {
    setAccount({ commit }, account) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                commit('currentUser', account);
                resolve()
            }, 1000)
        })
    }
}
```



### Getters

- 각 Components의 계산된 속성(computed)을 공통 사용 정의라고 보면 된다.
- 여러 Components에서 동일한 computed가 사용 될 경우 Getters에 정의하여 공통으로 쉽게 사용가능
- 하위 모듈의 getters를 불러오기 위해서는 특이하게 `this.$store.getters["경로명/함수명"];` 을 사용

```js
export const getters = {
    isAuthenticated(state) { // 현재 로그인 상태인지 확인 (true/false)
        return !!state.user;
    },
    
    getAccount(state) { // 회원정보 불러오기
        return state.account;
    },
};
```





## 2. Vuex Module

- 모듈별로 관리하기



**ex) store/index.js**

```js
import Vue from 'vue';
import Vuex from 'vuex';
import appointment from '@/store/modules/appointment';
import bookmark from '@/store/modules/bookmark.js';
import map from '@/store/modules/map';
import place from '@/store/modules/place';
import review from '@/store/modules/review';
import snackbar from '@/store/modules/snackbar';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    appointment,
    bookmark,
    map,
    place,
    review,
    snackbar,
  },
});
```



**ex) store/modules/bookmark.js**

```js
export default {
  state: {
    bookmark: false,
  },
    
  getters: {
    bookmark(state) {
      return state.bookmark;
    },
  },
    
  mutations: {
    trueBookmark(state) {
      state.bookmark = true;
    },
    falseBookmark(state) {
      state.bookmark = false;
    },
  },
    
  actions: {
    visibleBookmark({ commit }) {
      commit('trueBookmark');
    },
    invisibleBookmark({ commit }) {
      commit('falseBookmark');
    },
  },
    
};
```



#### rootState 는 actions 와 getters 에서만 사용가능

vuex 를 모듈형으로 개발할 때, 기본적으로 state 변수 값은 동일 모듈에 있는 state만 참조하게 됩니다.

만약 내가 최상위에 있는 `state` 변수나 다른 모듈의 변수 값을 활용하기 위해서는 `rootState` 를 활용해야 한다 하지만 이 rootState는 actions과 getters의 인자로만 사용될 수 있습니다.

만약 mutations에서 사용하기를 원한다면 actions 에서 받아서 mutations쪽으로 commit해서 활용해야 합니다.



#### Mutations와 Actions의 사용가능 인자

- Mutations
  - mutations내에 있는 함수의 인자는 state 와 payload 입니다.
  - **기본 인자는 state만 사용**할 수 있고 **commit으로 넘어온 전달 인자는 payload**만 있습니다.

```js
// 방법1 - 제일 많이 쓰임
mutationA(state, payload) {
    
}

// 방법2 - 이렇게도 가능
mutationA(state, {data1, data2}) {
    
}
```



- Actions

```js
// 방법1 - 제일 많이 쓰임
actionsA({ rootState, state, commit, dispatch }, payload) {
    
}
```





## 3. 접근방법

`Components`에서 store에 있는 state, mutations, actions, getters 에 접근하는 방법은 아래와 같다



- #### state에 접근하는 방법

  - state에 접근하기 위해서는 Components의 **computed** 내에 작성해야 합니다.



1. `this.$store.state.items`

2. mapState 활용방법

```js
computed: {
    ...mapState({
        items: state => state.items,
    }),
}
```



- #### mutations에 접근하는 방법

  - mutations을 실행하기 위해서는 **components의 methods 영역 내에 작성**해야 한다.



1. `this.$store.commit('경로명/함수명')`
2. mapMutaions 활용방법

```js
methods: { // methods 영역에서 호출해야 함
    ...mapMutations({
        add: 'item/increment' // this.add() 를 this.$store.commit('item/increment') 에 매핑
    })
}
```



- #### Actions에 접근하는 방법

  - actions을 실행하기 위해서는 **Components의 methods 영역 내에 작성**해야 한다.



1. `this.$store.dispatch['경로명/함수명']`
2. mapActions 활용방법

```js
methods: { // methods 영역에서 호출해야 함
    ...mapActions({
        add: 'item/increment' // this.add()를 this.$store.dispatch('item/increment')
    })
}
```



- Getters에 접근하는 방법
  - getters을 실행하기 위해서는 components의 computed 영역에 작성해야 한다.



1. `this.$store.getters['경로명/함수명']`
2. mapGetters 활용방법

```js
computed: {
    ...mapGetters({
        doneCount: 'item/doneTodosCount'
    })
}
```





## 4. 모듈로 구성된 vuex에서 상위모듈 dispatch, commit 실행

모듈로 구성할 경우 하위 모듈에서 **형제 또는 부모 모듈의 state**에 접근하기 위해서는 **rootState**를 사용하면 됩니다.
그러면 형제 또는 부모 모듈의 **Mutations나 Actions**를 실행시킬 경우는 어떻게 해야 하느냐!!!
세번쨰 인자에 `{ root: true }`를 지정해 주면 됩니다

```
dispatch("path1/actionA", payload, { root: true });
```

