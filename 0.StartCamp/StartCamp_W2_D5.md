#### 2019년 7월 12일

# StartCamp_W2_D5

-----------

#### 저장 안해서 날려먹은 부분...

------------------------



### Telegram API 사용하기

##### 1. Telegram API를 사용하기 위한 준비

   - 먼저 [https://web.telegram.org](https://web.telegram.org/) 사이트에 접속해 로그인 한다.
   
   - BotFather 를 검색해 팔로잉하고 대화창에 '/newbot'을 입력해 새로운 챗봇을 생성한다.
   
     (챗봇의 이름(name)과  유저이름(username)을 설정해 준다. / 유저이름은 ID와 같은 개념 고유식별값)
   
   - 생성이 완료되면 API 사용을 위한 'token' 값이 주어진다. 



##### 2. Python 에서 Telegram API 사용하기

- test.py 파일을 생성한다.

```python
token = '비밀'
url = f'https://api.telegram.org/bot{token}/' # 텔레그렘 API 사용가이드에서 확인 할 수 있음
print(url)
```

- 위에 결과를 실행하면 터미널창에 특정  url이 생성된 것을 확인 할 수 있다.

- 생성된 url 뒤에 '/getUpdates' 를 추가로 입력하고 웹으로 접속해 보자.

  ('https://api.telegram.org/bot{token값}/getUpdates')

- Json 자료형에서 'user_id' 라는 속성을 확인할 수 있다. 대부분의 API에서 파라미터 값으로 요구하기 때문에 'user_id' 의 value 값을 변수로 저장하자.

```python
token = '비밀'
url = f'https://api.telegram.org/bot{token}/' # 텔레그렘 API 사용가이드에서 확인 할 수 있음
user_id = '비밀'
print(url)
```

- token 과 user_id 가 외부로 노출될 경우 내가 생성한 챗봇이 다른 개발자에 의해 강제 될 수 있으므로 숨겨야할 필요가 있다.
  - 변수를 숨기기 위한 방법(decouple 라이브러리)
    1. 터미널 창에 'pip install decouple' 을 입력해 다운받는다.
    2. 'test.py' 파일과 같은 위치에 '.env' 파일을 생성한다.(파일명은 미리 정해져 있으므로 반드시 지켜야 한다.)
    3. 



### 네이버 API 사용하기



python anywhere