#### 2019년 7월 31일

# Web

### 1. bootstrap

> CSS 를 클래스안에 !import 속성으로 미리 정의해 놓아 사용하기 편하게 만들어 놓은 웹개발 도구

- 사용하기 위한 사전 준비
  - [https://getbootstrap.com](https://getbootstrap.com/) 페이지에서 `get start` 버튼을 클릭해 접속
  
  - Quick start 밑에 CSS와 JS 부분의 영역을 복사해서 html 안에 붙여 넣는다.(붙여 넣는 영역을 잘 읽어보자.)
  
    ```html
    <!-- CSS 는 head 안에 붙여넣는다. -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    ```
  
    ```html
    <!-- JS 는 body 태그 닫기 직전에 붙여 넣는다. -->
    <!-- 아무대나 붙여 넣어도 정상적으로 동작하지만 응답속도 면에서 차이가 난다. -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    ```
  
    
- __bootstrap__ 을 적용해 보자
  - Margin and padding
  
    ```css
    /* bootstarp 에서는 아래와 같이 이미 선언되어 있는 클래스를 지정해 css를 적용시킨다. */
    .mt-1 {
        margin-top: 1rem !important;
    }
    ```
  
  - 종류 및 사용방법
  
    - 종류
  
      | 속성 종류  | 적용범위 | 단위 |
    | --------- | -------- | ---- |
      | m (margin) | t (윗쪽에 적용) | 1 (rem) |
      | p (padding) | b (아랫쪽에 적용) | 2 (rem) |
      |           | l (왼쪽에 적용) | 3 (rem) |
      |           | r (오른쪽에 적용) | 4 (rem) |
      |           | x (왼쪽, 오른쪽에 적용) | 5 (rem) |
      |           | y (윗쪽, 아랫쪽 적용) | 6 (rem) |
      |           | auto (자동적용) |         |
      | | (아무것도 적지 않을시 모든방향 적용) | |
      
    - 사용방법
    
      - '(속성종류 + 적용범위)-단위' 꼴로 사용
    
      - margin 또는 padding 을 주고 싶은 태그의 class에 위의 형태를 추가
    
        ``` html
        <!-- 사용예시 -->
        <div class="mt-3 mb-2">Margin 적용 예시</div>
        ```
    
  - 이 외에 많은 기능들은 필요할때마다 공식 홈페이지의 __Documentation__에서 찾아보고 사용하자.



### 2. Flask

> python web framework 중 하나로 수업에선 클라이언트의 요청을 받은 서버가 응답을 주기 위해 동작해야할 부분을 코딩한다.

- 사용하기 위한 사전준비

  - Flask는 외부 패키지 이므로 설치가 되어있지 않을시 터미널 환경에 아래와 같은 명령어를 입력해 설치하자(설치되었는지 확인하기 위한 명령어:  `pip list` / __19년 8월 기준 Flask 버전 1.1.1__)
    - 설치하기 위한 명령어: `pip install Flask`

- app.py 파일을 생성하고 그 안에 아래와 같은 코드를 복사해 붙여 넣는다.

  ```python
  from flask import Flask, escape, request
  
  app = Flask(__name__)
  
  # 페이지에 요청을 주고 받을때의 동작과 경로 값들을 설정하는 부분
  @app.route('/')
  def hello():
      name = request.args.get("name", "World")
      return f'Hello, {escape(name)}!'
  ```

- 터미널 환경에서 아래와 같은 명령어로 Flask를 실행할 수 있다.(pwd 는 app.py 파일이 있는 폴더에 위치해야한다.)

  ```
  둘 다 flask를 실행시키는 명령어 이다.
  $ env FLASK_APP=.py flask run
  $ flask run
  ```

- python 파일 실행만으로도 flask가 동작하도록 app.py 파일의 가장 밑에 코드를 추가해 보자.

  ```python
  from flask import Flask, escape, request
  
  app = Flask(__name__)
  
  @app.route('/')
  def hello():
      name = request.args.get("name", "World")
      return f'Hello, {escape(name)}!'
  
  # 새롭게 추가된 부분 (app.py 파일을 실행하는 것만으로 flask를 실행시킬 수 있다.)
  if __name__ == '__main__':
      app.run(debug=True)
  ```

- 여러 html 파일들을 관리하기 위해 app.py 파일과 같은 위치에 `templates 폴더` 를 생성한다.(폴더의 이름은 무조건 templates 여야 한다.)

- templates 폴더 안의 html 파일들을 접근하기위해 flask 패키지에서 render_template을 추가해준다.

  ```python
  from flask import Flask, escape, request, render_template # 추가된 모듈
  
  app = Flask(__name__)
  
  @app.route('/')
  def hello():
      name = request.args.get("name", "World")
      return f'Hello, {escape(name)}!'
  
  if __name__ == '__main__':
      app.run(debug=True)
  ```

- 랜덤으로 6개의 번호를 보여주는 페이지(lotto.html)와 랜덤으로 점심메뉴를 추천해주는 페이지(lunch.html)를 기능으로 추가해보자.

- 먼저 `app.py` 파일 안에 위에서 언급한 페이지들에서 해야할 기능들을 만들어주자.

  ```python
  import random # 랜덤으로 숫자를 뽑기 위해 추가된 부분
  from flask import Flask, escape, request, render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def home():
      return f'Welcome flask test homepage!'
  
  # 6개의 번호를 뽑아주는 페이지
  @app.route('/lotto')
  def lotto():
      numbers = random.sample(range(1, 46), 6)
      return render_template('lotto.html', numbers=numbers)
  	# numbers=numbers 에서 앞의 numbers는 lotto.html 파일 안에서 쓰기 위한 변수명이고
      # 이 때 들어 있는 값은 윗줄에서 생성한 numbers 변수에 들어있는 난수 6개 이다.
  
  # 랜덤으로 점심메뉴를 추천해주는 페이지
  @app.route('/lunch')
  def lunch():
      menu = ['짜장면', '볶음밥', '라면', '치킨']
      my_lunch = random.choice(menu)
      return render_template('lunch.html', my_lunch=my_lunch)
  
  if __name__ == '__main__':
      app.run(debug=True)
  ```

- 다음으로 `templates 폴더` 안에 `lotto.html`, `lunch.html` 을 생성하고 html을 작성해 보자.

- `app.py`에서 넘겨줬던 변수를 __`{{변수이름}}` 형태(jinja 문법)__로 사용할 수 있음을 주의하자.

  ```html
  <!-- lotto.html 파일의 내용 -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
    <div class="container">
      <!-- 여기부터 -->
      <p>로또 번호: {{lotto}}</p>
      <!-- 여기까지 -->
    </div>
  </body>
  </html>
  ```

  ```html
  <!-- lunch.html 파일의 내용 -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
    <div class="container">
      <!-- 여기부터 -->
      <p>오늘의 추천 점심메뉴: {{my_lunch}}</p>
      <!-- 여기까지 -->
    </div>
  </body>
  </html>
  ```

- 위의 두 html 파일을 보면 body 태그 안에 주석 처리된 부분 이외에는 완전히 똑같은 것을 확인 할 수 있다.

- 페이지의 기능이 늘어 날수록 중복되는 코드가 계속해서 늘어나므로 __jinja 문법__으로 중복을 제거하는 방법을 살펴보자.

- `templastes 폴더` 안에 `base.html` 파일을 생성하고 중복되는 html 코드를 작성하자.

- 바뀌는 부분만 jinja 문법을 이용해 동적으로 변하는 공간을 생성해 준다.

  ```html
  <!-- base.html 파일의 내용 -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
    <div class="container">
      <!-- 여기부터 -->
      {% block body %}
      {% endblock %}
      <!-- 여기까지 jinja 문법으로 동적으로 변하는 부분만 지정해준다. -->
    </div>
  </body>
  </html>
  ```

- 다음으로 `lotto.html`, `lunch.html` 파일의 내용을 수정해 보자.

  ```html
  <!-- 수정된 lotto.html 파일의 내용 -->
  {% extends 'base.html' %} <!-- base.html 에 접근 -->
  <!-- 그 안에 선언한 공간을 써주고 그 사이에 내용을 채워 넣는다. -->
  {% block body %}
  <p>로또 번호: {{lotto}}</p> <!-- 실제 적용될 내용 -->
  {% endblock %}
  ```

  ```html
  <!-- 수정된 lunch.html 파일의 내용 -->
  {% extends 'base.html' %}
  {% block body %}
  <p>오늘의 추천 점심메뉴: {{my_lunch}}</p> <!-- 실제 적용될 내용 -->
  {% endblock %}
  ```

- 위에서 배운 bootstrap 등으로 html을 꾸미고 crawling 등을 사용해 페이지를 추가하며 복습하자.