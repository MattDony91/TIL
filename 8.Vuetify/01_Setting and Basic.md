2020년 1월 16일

---

## \<Index>

1. Vue - Review (Vue CLI install, setting)
2. Vuetify - Install
3. Vuetify - Basic
4. 

---

### 1. Vue - Review (Vue CLI install, setting)

>  CLI 를 이용해 vue 개발 환경 구축하기

​	`$ npm i -g @vue/cli` : vue-cli 설치

​	`$ vue create 프로젝트이름` : 새로운 프로젝트 생성

   - (create 명령어 입력후 Vue에 대해 아무것도 기억나지 않을 경우 아래와 같이 만들자)

        - `> Manually select features` 선택
          			- `Babel, Router, Linter / Formatter` 체크(spacebar) 후 선택(enter)
          			- `Use history mode for router?(Y/n)` => Y
          			- `Pick a linter / formatter config:` => `ESLint with error prevention only`
          			- `Pick additional lint features:` => `Lint on save`
          			- `Where do you prefer placing config for Babel, ESLint, etc.?` => `> In package.json`
          			- `Save this as a preset for future projects?(y/N)` => N

     `$ npm run serve` : 실행 명령어

---

### 2. Vuetify  - Install

- Vuetify 설치하기
  - (터미널 창에) `$ vue add vuetify` 입력 후 `> Default` 선택
  - `src/plugins/vuetify.js` 폴더가 추가된 것을 확인
- v-icon 태그에 material desing icon 이 바로 적용되게 하기 위한 설정은 v-button 태그에서 설명

---

### 3. Vuetify - Basic

> Vuetify 는 UI component framework 이다.

- v-app : Vuetify의 root component 로 'v-' 로 시작하는 vuetify의 모든 component는 v-app 안에서만 사용 할 수 있다.

