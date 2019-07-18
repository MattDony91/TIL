#### 2019년 7월 17일

# Python 함수

### 1. 매개변수

- 기본값(Default Argument Values)
  - 함수가 호출될 때, 인자를 정하지 않아도 기본값(Default)을 설정 할 수 있다.

  - 기본값이 정해져 있더라도 함수호출시 다른 값을 대입하면 기본값은 무시 된다.

  - __기본값을 갖는 매개변수는 항상 맨 뒤에 선언 되어야 한다.__
  
    ```python
    """
    아래와 같이 작성하면 오류
    def greeting(name='익명', age):
        print(f'{name}님은 {age}살 입니다.')
    greeting(20)
    """
    
    # 올바르게 작성한 경우
    def greeting(age, name='익명'):
        print(f'{name}님은 {age}살 입니다.')
  greeting(20)
    ```
  



- 키워드 인자(Keyword Arguments)

  - 함수 호출시 매개변수의 이름을 선택해 값을 넣어 주면, 매개변수의 순서와 상관 없이 사용 가능 하다.

    ```python
    # 키워드 인자 예시
    def greeting(age, name='john'):
        print(f'{name}은 {age}살입니다.')
    greeting(20, 'dony')
    greeting(name = 'dony', age = 20)
    ```

    

- 가변 인자 리스트

  - 받아올 매개변수의 개수를 알수 없을때 사용한다.(대표적인 예: 내장함수 print() )

  - __tuple 형태로 처리__가 되며, *로 표현된다.

    ```python
    # 가변 인자 리스트 예시
    def my_max(*args):
        max_num = args[0]
        for arg in args:
            if arg > max_num:
                max_num = arg
        print(max_num)
    my_max(-1, -2, -3, -4)
    ```



- 정의되지 않은 인자를 처리

  - __dict 형태로 처리__가 되며, **로 표현된다.

    ```python
    # **로 인자를 입력받아 Dictionary를 생성해 보자.
    def fake_dict(**kwargs):
        result = {}
        for key, val in kwargs.items():
            result[key] = val
        return result
    print(fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
    
    # dict 처리가 되기 때문에 바로 return 해줘도 위와 같은 결과를 얻을 수 있다.
    def my_fake_dict(**kwargs):
        return kwargs
    print(my_fake_dict(한국어='안녕', 영어='hi', 독일어='Gu\ten Tag'))
    ```

  - **dict를 통해 함수에 인자를 넘길 수 있다.

    ```python
    # user 검증(유사 회원가입)을 작성예시
    def user(username, password, password_con):
        if password == password_con:
            print(f'{username}님 가입되었습니다.')
        else:
            print('비밀번호가 일치하지 않습니다.')
    
    my_account = {
        'username': '홍길동',
        'password': '1q2w3e4r',
        'password_con': '1q2w3e4r'
    }
    
    user('dony', 123, 123) # 매개변수를 하나씩 대입하기
    user(**my_account) # Dictionary 형태로 매개변수를 대입하기
    ```





### 2. 이름공간 및 스코프(Scope)

- 변수는 각자의 이름공간에 존재하며 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나간다.(=>LEGB)

  - Local scope: 정의된 함수
  - Enclosed scope: 상위 함수
  - Global scope: 함수 밖의 변수 혹은 import된 모듈
  - Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성

- 이름공간은 각자의 수명주기가 있다.

  - built-in scope : 파이썬이 실행된 이후부터 끝까지
  - Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지
  - Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할때 까지

  ```python
  # 전역변수를 바꾸기 위한 시도(안바뀜)
  global_num = 3
  def localscope2():
      global_num = 5
      print(f'global_num이 {global_num}으로 바꼈습니다.')
  localscope2()
  print(global_num) # 출력결과 global_num 은 3이 그대로이다.
  
  # global 키워드를 위한 g_num 변경
  g_num = 3
  def g_func():
      global g_num #global 을 사용해 전역변수 g_num을 불러옴
      g_num = 5
      print(f'g_num이 {g_num}으로 바꼈습니다.')
  g_func()
  print(g_num) # 출력결과 g_num 이 바뀐걸 확인할 수 있다.
  ```