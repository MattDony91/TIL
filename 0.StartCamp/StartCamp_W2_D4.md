#### 2019년 7월 11일

# StartCamp_W2_D4



### Flask

#### 기본 사용 방법


- 터미널 창에서 'pip install flask' 를 입력해 flask 설치
- 'pip list'를 입력해 설치 목록을 확인 할 수 있다.
- http://flask.pocoo.org/ 에서 아래와 같은 코드를 복사해 app.py 파일에 붙여 넣는다.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/") # route => 경로를 받아 줌, '/' => 최상단의 위치(root)를 표시
def hello():
    return "Hello World!"
```

- 터미널 창에서 아래와 같은 명령어를 입력하면 실행

```
student@DESKTOP MINGW64 ~/startcamp/04.first_app (master)
$ FLASK_APP=app.py flask run
```

- 실행결과 아래와 같은 화면이 나온다.

```
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

- 주소를 클릭해 들어가 보면 hello()에 정의된 "Hello World!" 를 볼 수 있다.
- app.py 밑에 새로운 route 를 추가해 보자.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/") 
def hello():
    return "Hello World!"

@app.route("/hi") # 새로 추가된 route
def hi():
    return "안녕하세요!"
    
if __name__ == '__main__': # 터미널 창에서 'python app.py' 명령어로 실행 가능하게 된다.
    app.run(debug=True)
```

- 'python app.py' 로 실행시켜 서버로 접속한 후 주소를 '127.0.0.1:5000/hi' 로 변경하면 "안녕하세요!" 를 볼 수 있다.



#### 외부에서 파일을 불러와 html 완성하기(Rendering)

> Rendering 이란 불완전한 어떤것을 완전한 것으로 만들어가는 것을 말함(뇌피셜)
>
> (아재...의 학창시절 pmp에 만화 랜더링해서 저장하고 야자 내내 만화만 보던 기억...)

- 먼저 app.py와 같은 위치에 'templates' 의 폴더를 생성한다.(폴더 이름 절대 중요!! 무조건 templates)
- templtes 폴더 안에 'index.html' 파일을 생성한다.
- return 에서 render_template('index.html') 을 반환해준다.

```python
from flask import Flask, render_template # render_template 추가
app = Flask(__name__)

@app.route("/") 
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "안녕하세요!"
    
@app.route("/html_file") # 새로 추가된 route
def html_file():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
```



#### 문제점!!

> 만약 만들어야하는 페이지가 100개, 200개, 300개.. 수 없이 많아 진다면 어떻게 해야 할까?
>
> 정답은 : variable routing

- 동적인 URL주소를 할당해서 해결할 수있다.(route 설정을 변수화 시킬 수 있다!!)

```python
@app.route("/greeting/<string:name>") 	# 새로운 route를 추가해보자.
def greeting(name):					# greeting/ 다음에 올 주소를 string타입의 name 변수로 지정
    return f"안녕하세요 {name}님!!"
```

- '127.0.0.1:5000/greeting/홍길동' 을 접속해 보자.
- 주소에 '홍길동' 을 아무 이름이나 바꿔가며 변화되는 것을 확인해 보자.



#### 응용하기(variable routing & rendering)

> variable routing 과 rendering을 같이 사용해 보자

- 아래와 같은 코드 추가

```python
@app.route("/cube_html/<int:num>") # 새로운 route 생성
def cube_html(num):
    cube_num = num ** 3
    return render_template('cube.html', num_html=num, cube_num_html=cube_num)
# 'num_html=num' 에서 왼쪽에 있는 'num_html'은 cube.html 파일에서 사용할 변수이다.
# 'cube_num_html=cube_num' 도 위와 마찬가지로 왼쪽에 있는 변수는 html 파일에서 사용할 변수
```

- 'templates' 폴더 안에 'cube.html' 파일 생성

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <strong>{{num_html}}</strong>의 세제곱은 <i>{{cube_num_html}}</i>입니다.
    <!-- 중괄호 두개 사이에 render_template 에서 선언한 변수를 사용할 수 있다. -->
</body>

</html>
```

- 실행시켜 결과를 확인해 보자.



#### form 태그 을 이용한 데이터 전달

- 새로운 route 두 개 'ping' 과 'pong'을 생성

``` python
@app.route('/ping')
def ping():
	return render_template('ping.html')

@app.route('/pong')
def pong():
    return render_template('pong.html')

```

- ping.html 파일을 만들고 body 태그 안에 'form 태그'와 'input 태그'를 작성해 보자.

```html
<!-- ping.html 파일 -->

<body>
    <h1>Ping 페이지 입니다.</h1>
    <!-- form 태그를 통해 데이터를 넘겨줄 주소를 결정 -->
    <form action="/pong">
        <!-- input 태그를 통해 사용자로부터 데이터를 입력 받음 -->
        <input type="text" name="test">
        <!-- submit 타입은 데이터전송 버튼을 만들어줌 -->
        <input type="submit">
    </form>
</body>
```

- 'input 태그'는 사용자에게 입력값을 받기 위한 태그로 'type 속성'으로 입력받을 데이터를 강제할 수 있다.

  (다양한 데이터를 입력 받을 수 있음. 궁금하면 w3schools 에서 찾아보기)

- 'form 태그'는 'action 속성' 을 이용해 input 태그를 이용해 사용자게 입력받은 데이터를 어디로 넘겨줄지 결정한다. 이 때, 데이터를 구분하기 위해 'input 태그' 안에 'name 속성'을 이용한다.

- 'input 태그'의 'submit 타입'을 통해 버튼을 클릭할때 'form 태그'에 'action 속성' 에서 정해준 곳으로 데이터를 넘긴다.

- app.py 파일에 돌아와 'pong 라우트' 에서 입력 받은 데이터를 조작해 보자.

```python
from flask import Flask, render_template, request # flask 안에 request 를 추가해주자

@app.route('/pong')
def pong():
    user_input = request.args.get('test')
    # 위의 코드는 'ping.html' 에서 'input 태그'에 입력한 값을 가져와 user_input 변수는 코드
    return render_template('pong.html', user_input=user_input)
```

- ping 에서 입력한 값을  pong 에서 사용자에게 보여주자.

```html
<!-- pong.html 파일 -->

<body>
    <h1>PongPongPong</h1>
    사용자가 입력한 데이터 : <strong>{{user_input}}</strong>
    <!-- ping.html 에서 넘겨 받은 user_input 데이터를 출력해주는 것을 볼 수 있다.-->
</body>
```



### Json 형식

> dictionary 처럼 key와 value 로 구성되어 있음 (아래 예시)

```
{
  "totSellamnt": 81961886000,
  "returnValue": "success",
  "drwNoDate": "2019-07-06",
  "firstWinamnt": 2240409000,
  "drwtNo6": 39,
  "drwtNo4": 34,
  "firstPrzwnerCo": 9,
  "drwtNo5": 37,
  "bnusNo": 12,
  "firstAccumamnt": 20163681000,
  "drwNo": 866,
  "drwtNo2": 15,
  "drwtNo3": 29,
  "drwtNo1": 9
}
```

#### 사용해보기

``` python
@app.route('/lotto')
def lotto_result():
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    lotto_numbers = res.json()
    
    # 위의 url에 접속하면 위의 예시와 같은 json 형식의 값을 볼 수 있다.
    # 당첨번호는  drwtNo1 ~ drwtNo6 의 키값을 가지고 있는 것을 확인할 수 있다.
    
    winning_numbers = [] # 당첨번호를 가져와 담기위한 List
    for i in range(1, 7):
        winnig_numbers.append(lotto_numbers[f'drwtNo{i}'])
    bonum_number = lottor_numvers['bnusNo']
    
    return render_template('lotto.html', w=winning_numbers, b=bonus_number)
```

- lotto.html 파일 생성

```html
<!-- lotto.html 파일 -->

<body>
    <h1>로또 당첨번호 확인</h1>
    <strong>{{w}}</strong><br>
    보너스 번호 : {{b}}
</body>
```

