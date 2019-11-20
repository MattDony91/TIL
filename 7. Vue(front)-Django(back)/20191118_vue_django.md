#### 2019년 11월 18일

#  Vue-Django

> - Vue-Django 사이에 올바른 사용자의 요청인지 확인하기 위해 JWT(JSON Web Token)을 사용
> - JWT의 Header, Payload, Signature 로 이뤄져 있다.
> - Header 에는 토큰 타입과 해싱 알고리즘을 지정
> - Payload 토큰에 담을 정보가 들어 있음
> - Signater 해쉬값으로 시크릿키로 사용

#### 시작하기

- 폴더 안에 Vue 프로젝트와 Django 프로젝트를 각각 생성
  - `$npm create front-end` : Vue  프로젝트 생성(프론트 엔드)
  - `$mkdir back-end`
  - back-end 폴더 안에 `$django-admin startproject todoback .` : Django 프로젝트 생성(백엔드)



### 1. Vue

- router : 하나의 싱글페이지 안에서는 다른 url 경로를 설정할 수 없기 때문에 router 를 사용해 페이지를 나눠준다.

  - `$vue ui` -> 메뉴에서 `Plugins` -> `+Add plugin` -> router 검색 ->  `@vue/cli-plugin-router` 체크 후 설치

- `src/views/새로운파일.vue` 생성

- router 안의 `index.js` 파일의 routes안에 아래와 같이 추가

  ```vue
  const routes = [
    {
      paht: '/login',
      name: 'login',
      component: Login,
    },
  ]
  ```

- App.vue 파일에서 router-link 태그를 달아 추가해 준다.

  `<router-link to="/login">Login</router-link>`
  
- `npm install vue-session` : session 공간을 사용하기 위해 필요한 라이브러리 설치

- 로그인 검증을 위해 vue validation  라이브러리를 찾아 사용해 보기

- `npm install jwt-decode` : 암호화 되어 있는 jwt 를 복호화 해주는 라이브러리

- `vue ui`에서 `vuex` 설치(로그인 된 상태인지 확인하기 위한 token 같은 경우 vue 안의 거의 모든 영역에서 확인되어야 할 사항이므로 이를 모든 .vue 파일에 선언해 확인하는 것보다 vuex라는 라이브러리를 통해 하나의 공용 공간을 만들어 놓고 그때마다 확인하는 방식으로 사용하는게 효율적이다.)

  - store 폴더 안에 새로운 폴더 생성 modules
  - modules 폴더 안에 기능별로 js 파일을 따로 만들어 관리

  ```js
  // ex) auth.js - 사용자의 접근 권한과 관련된 사항들을 정리
  // index.js에서 modules를 제외한 state, mutations, actions에 대해 정의해준다.
  const state = { // data 에 해당
    token: null
  }
  
  const mutations = { // methods 에 해당
    setToken (state, token) {
      state.token = token
    }
  }
  
  const actions = { // 실행시킬 함수들의 묶음
    login (options, token) {
      options.commit('setToken', token)
    },
    logout (options) {
      options.commit('setToken', null)
    }
  }
  
  export default { // auth.js 파일을 불러오는 곳에서 사용할 수 있도록 내보내 주기
    state,
    mutations,
    actions,
  }
  
  //-------------------------------------------------------------------------
  // store 폴더 안의 index.js 파일에 auth.js 를 불러와 modules에 추가해주기
  import Vue from 'vue'
  import Vuex from 'vuex'
  import auth from './modules/auth.js' // auth.js 불러오기
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
      state: { // vue에서 data
    },
    mutations: { // vue에서 methods
    },
    actions: { // vue에서 methods들을 묶어 놓음(비동기적으로 처리함)
    },
    modules: {
      auth, // 추가하기
    }
  })
  ```

  - store 폴더 안의 `index.js` 파일에 `auth.js 추가하기`

- Vue  Lifecycle(찾아서 공부하기)

  - Create -> Mount -> Update -> Destroy

  




### 2. Django

- 설치하기

  - `$pip install djangorestframework`
  - `$pip install djangorestframework-jwt`
  - `$pip install django-cors-headers`

- `settings.py` 파일에 아래와 같이 추가

  ```python
  INSTALLED_APPS = [
      'todos',
      'rest_framework',
      'corsheaders',
  ]
  ```

-  https://jpadilla.github.io/django-rest-framework-jwt/,   https://pypi.org/project/django-cors-headers/  두 사이트를 참고해 설정하기