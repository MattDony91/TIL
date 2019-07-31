#### 2019년 7월 30일

# Web

### 1. CSS (Cascading Style Sheet)

- CSS 적용하는 방법 3 가지

  - __Inline__: html 태그 안에 `style` 속성을 이용해 css 적용(사용하지 않는 것을 권장함)

    ```html
    <!-- 사용예시 -->
    <h1 style="color: orangered;">CSS_Inline</h1>
    ```

  - __Embedding (내부 참조)__: 

    ```html
    <!-- 사용예시 -->
    <head>
        <style>
            h2{
                color:skyblue;
                font-size: 100px;
            }
        </style>
    </head>
    <body>
        <h2>CSS_Embedding</h2>
    </body>
    </html>
    ```

  - __link file (외부 참조)__:

    ```html
    <!-- 사용예시 -->
    <head>
        <link rel="stylesheet" href="00_intro.css">
    </head>
    <body>
        <p>link file</p>
    </body>
    
    
    
    <!-- 00_intro.css 파일 -->
    p {
        color: olivedrab;
        font-size: 50px;
    }
    ```



- 절대크기와 상대크기
  - %: 단위는 부모에 대해 상대적인 사이즈
  - em: 배수를 표현하며 부모에 따르는 단위
  - rem: 배수로 표현하는  독자적인 단위
  - px: 독자적인 단위
  - viewport(vw, vh): 화면의 비율에 따라 실시간으로 바뀌는 반응형 단위



- __색상 표현 단위__
  - HEX: #ffffff
  - RGB: rgb(0, 0, 0)
  - RGBA: rgb(0, 0, 0, 0.5)



- __선택자(selector)__
  - __\*__  (전체선택자):  모든 element를 선택
  - __tag name__  (태그 선택자):  해당하는 모든 tag를 선택
  - __#__  (아이디 선택자): id 를 선택
  - __.__  (클래스 선택자): class를 선택
  - __선택자 우선순위__: __id > class > tag__



- __display 속성__
  - block
    - 항상 새로운 라인에서 시작
    - 화명 크기 전체의 가로폭을 차지한다.
    - Inline 요소를 포함 할 수 있다.
    - 기본으로 block 속성 값을 갖는 태그
      - div, ol, ul, li, form, table, hr, p, h1 ~ h6
  - inline
    - 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.
    - content의 너비만큼 가로폭을 차지한다.
    - 기본으로 inline 속성 값을 갖는 태그
      - span, input, a
  - inline - block
    - 기본적으로 inline 속성은 margin 값을 가질 수 없지만 inline-block 을 사용하면 가능하다.
  - none
    - 데이터를 사라지게 하는 속성
    - visibility: hidden 속성과 다르게 데이터 자체가 사라지므로 차지하고 있는 공간도 없다.



- __visibility__
  - hidden
    - display: none 속성과 다른점은 hidden 으로 숨겨놓고 값 자체는 남아있기 때문에 공간은 남아있다.



- font & text
  - font-size
  - font-family
  - letter-spacing
  - text-align



- __position__
  - static
    - 기본값(default)
  - relative
    - 원래 있던 위치에 대한 상대적인 위치
  - absolute
    - 절대값 위치
    - 부모 - 자식 관계에서 자식은  부모 안에서의 절대값으로 움직인다
  - fixed
    - 고정된 위치값으로 스크롤에 내리거나 올려도 사용자가 보는 화면상에서 항상 같은 위치에 고정