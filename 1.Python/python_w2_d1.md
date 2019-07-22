#### 2019년 7월 22일

# Python



---

- Octotree 설치(chrome 확장 프로그램)
- 문제풀이
  - 04homework
  - 04workshop
  - problem04
  - project01
  - 하노이탑

---



### 1. 리스트 내포(List Comprehension)

> list를 만들 수 있는 간단한 방법

- comprehension 안에 for문을 사용해 보자.

  ```python
  # 사용예시
  # 1~10 까지의 숫자로 만든 세제곱 담긴 리스트 생성
  
  numbers = range(1, 11)
  # 일반적인 방법
  cubic_list = []
  for number in numbers:
      cubic_list.append(number ** 3)
  print(cubic_list)
  
  # Comprehension 사용
  cubic_list = [number ** 3 for number in numbers]
  print(cubic_list)
  ```

- comprehension 안에 반복문과 조건문을 여러번 사용 할 수도  있다.

  ```python
  # 사용예시1
  # 1~10까지의 숫자중 짝수만 담긴 리스트 생성
  numbers = range(1, 11)
  
  # 일반적인 방법
  even_list = []
  for number in numbers:
      if not (number % 2) :
          even_list.append(number)
  print(even_list)
      
  # Comprehension 사용
  even_list = [number for number in numbers if not (number % 2)]
  print(even_list)
  
  
  
  # 사용예시2
  # 피타고라스 정리
  # (x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아라.
  
  # 일반적인 방법
  pita = []
  for x in range(1, 50):
      for y in range(x, 50):
          for z in range(y, 50):
              if x**2 + y**2 == z**2:
                  pita.append((x, y, z))
  print(pita)
  
  # comprehension 사용
  pita = [(x, y, z) for x in range(1, 50)
                     for y in range(x, 50)
                     for z in range(y, 50)
                     if x**2 + y**2 == z**2]
  print(pita)
  ```

- list 타입 외에, set, dictionary, tuple 자료형에도 comprehension을 사용할 수 있음





### 2. 딕셔너리 메소드(Dictionary Method) 활용

- __.pop(key[, default])__

  - key가 딕셔너리에 있으면 제거하고 그 값을 반환

  - key 값이 없을 경우 에러를 일으키거나 defalut 값을 지정해줘 특정 값을 반환 할 수 도 있다.

    ```python
    # .pop() 사용예시
    my_dict = {'apple': '사과', 'banana': '바나나'}
    
    print(my_dict.pop('apple')) # '사과'
    print(my_dict.pop('melon')) # 결과값으로 에러 발생
    print(my_dict.pop('melon', 'Not exist')) # 'Not exist' 반환
    ```


- .update()

  - 값을 제공하는 key, value 로 덮어씀

    ```python
    # .update() 사용예시
    my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
    my_dict.update(apple = '사과아') # my_dict['apple'] = '사과아' 와 같다.
    print(my_dict) # 'apple': '사과아', 'banana': '바나나', 'melon': '멜론'}
    ```

- __.get(key[, default])__

  - key 를 통해 value를 가져온다.

  - __key 값이 없으면 None을 반환하며, 특정한 값을 반환하도록 지정할 수 있다.(오류 발생 X)__
  
    ```python
    # .get() 사용예시
    my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
    
    print(my_dict.get('apple')) # '사과'
    print(my_dict.get('pineapple')) # None
    print(my_dict.get('pineapple', 'Not exist')) # 'Not exist'
    ```



### 3. 세트 메소드(Set Method) 활용

- __.add(element)__

  - element를 세트에 추가

    ```python
    # .add() 사용예시
    fruits = {"사과", "바나나", "수박"}
    fruits.add('포도')
    fruits.add('포도') # set 타입은 중복이 안되기 때문에 결과값은 변하지 않는다.
    print(fruits) # {'포도', '바나나', '수박', '사과'}
    ```

- .update(iterable)

  - 여러가지 값을 추가

    ```python
    # .update() 사용예시
    fruits = {"사과", "바나나", "수박"}
    fruits.update({'망고', '딸기', '딸기'})
    print(fruits)
    ```

- .remove(element)

  - element 를 삭제하고, __없는 값을 삭제할려는 경우 KeyError 발생__

    ```python
    # .remove() 사용예시
    fruits = {"사과", "바나나", "수박"}
    fruits.remove('수박')
    print(fruits) # {'바나나', '사과'}
    fruits.remove('메론')
    print(fruits) # KeyError 발생
    ```

- .discard(element)

  - element를 삭제하고, 없어도 에러가 발생하지 않는다.

    ```python
    # .discard() 사용예시
    fruits = {"사과", "바나나", "수박"}
    fruits.discard('메론')
    print(fruits) # {'사과', '수박', '바나나'}
    ```

- __.pop()__

  - __임의의 원소를 제거해 반환__

    ```python
    # .pop() 사용예시
    a = {"사과", "바나나", "수박", "아보카도"}
    print(a.pop()) # 아보카도
    print(a) # {'바나나', '수박', '사과'}
    ```





### 4. 모듈(Module)

> 파이썬  정의와 문장을 담고 있는 파일 / 모듈은 확장자 .py 를 붙인다

- 피보나치 수열을 __'fibo.py'__모듈로 만들어 추가하기

  - fibo.py 파일을 생성하기(__메인파일__과 __같은 위치__에 생성해줘야 한다.)

    ```python
    # fibo.py 파일
    
    # 재귀함수를 사용해 n 번째 피보나치 수열의 값을 반환하는 함수
    def fib(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
    # 반복문을 사용해 n 번째 피보나치 수열의 값을 반환하는 함수
    def fib_loop(n):
        result = [1, 1,]
        for i in range(1, n):
            fib_sum = result[-1] + result[-2]
            result.append(fib_sum)
        return result[-1]
    ```
    
  - 메인 파일 안에서 fibo.py 파일 불러오기
  
    ```python
    # 메인파일
    import fibo
    
    print(dir(fibo)) # 아래와 같이 출력되며 만들어 놓은 fibo, fibo_loop 함수가 있음을 확인
    # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib_loop']
    
    print(fibo.fib(5)) # 8
    print(fibo.fib_loop(6)) # 13
    
    # 변수에 할당해서 사용 가능하다.
    my_fib = fibo.fib
    print(my_fib(10)) # 89
    ```
  
    

### 5. 패키지(Package)

> 비슷한 특징을 가진 모듈을 모아 놓은 것

- 패키지로 취급하게 만들기 위해서는 `__init__.py` 파일이 필요(내용은 없음)

- 아래와 같은 파일 구조를 가짐

  ```
  # 패키지 구조 예시
  myPackage/ -┬---__init__.py => 패키지 디렉터리 임을 구분하기 위한 파일
  		    │
  		    ├---math/-┬-__init__.py
  		    │		  └-formula.py	=> 모듈파일
              │
  		    └---web/-┬-__init__.py
  		    		 └-url.py => 모듈파일
  ```

- 패키지 사용예시

  - 메인파일과 같은 위치에 `myPackage` 폴더 생성

  - `myPackage` 폴더 안에 `__init__.py` 파일과 `math`, `web` 폴더 생성

  - `math` 폴더 안에 `__init__.py`, `formula.py` 파일 생성

  - `web` 폴더 안에 `__init.py__`, `url.py` 파일 생성

    ```python
    #  formula.py 파일 안에 간단하게 테스트할 함수와 변수 선언
    
    pi  = 3.141592
    
    def my_max(a, b):
        if a > b:
            print(f'{a}가 {b}보다 큽니다.')
        else:
            print(f'{b}가 {a}보다 큽니다.')
    ```

    ```python
    # url.py 파일 안에 테스트할 함수 선언
    
    def my_url(itemPerPage=10, **kwargs):
        if itemPerPage not in range(1,11):
            return "1~10사이의 숫자를 입력하세요"
        if 'key' not in kwargs or 'targetDt' not in kwargs:
            return '필수값 누락'
            
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
        base_url += f'itemPerPage={itemPerPage}&'
    
        for key, value in kwargs.items():
            base_url += f'{key}={value}&'
            
        return base_url
    ```

  - 메인파일에서 패키지 불러오기

    ```python
    import myPackage # 패키지 전체를 불러옴
    from myPackage import web # web 모듈을 불러옴
    from myPackage.math.formula import * # formula 모듈에서 모든 변수와 함수를 불러옴
    from myPackage.web.url import my_url as api_url # as를 사용해 별칭으로 가져오기
    
    print(pi) # 3.141592
    my_max(2, 3) # 3가 2보다 큽니다.
    api_url() # '필수값 누락'
    ```





### 6. 에러와 예외(Errors and Exceptions)

1. __에러(Errors)__

   - 문법 에러 (Syntax Error)

     > 가장 흔한 에러로 파일 이름과 줄, ^ 을 통해 문제 발생 위치를 표시해줌

     ```python
     # if
     if True:
         print('True')
     else	# SyntaxError: invalid syntax
         print('False')
         
     # EOL
     print('hi) # SyntaxError: EOL while scanning string literal
           
     # EOF
     print('hi' # SyntaxError: unexpected EOF while parsing
     ```

2.  __예외 (Exceptions)__

   - 예외 종류
     - ZeroDivisionError
     - NameError
     - TypeError
     - ValueError
     - IndexError
     - KeyError
     - ModuleNotFoundError
     - ImportError
     - KeyboardInterrupt

3. __예외 처리__

   - try - except 구문을 이용해 예외 처리를 할 수 있다.

     ```
     # try-except 사용방법
     try:
     	codeblock1 # 실행하고자 하는 코드
     except 예외:
     	codeblock2 # 실행하고 싶은 코드에서 에러가 발생했을 경우 처리
     ```

     ```python
     # 사용예시
     try:
         number = input('숫자를 입력하세요: ')
         print(int(number))
     except (ValueError):
         print('숫자 모르나??')
     ```

   - 복수의 예외처리

     ```
     try:
         codeblock1
     except (예외1, 예외2):
         codeblock2
         
     또는
     
     try:
         codeblock1
     except 예외1:
         codeblock2
     escept 예외2:
     	codeblock3
     ```

     ```python
     # 복수의 예외처리 사용예시
     try:
         num = input('100을 나눌 값을 입력하세요: ')
         print(100 / int(num))
     except (ValueError, ZeroDivisionError):
         print('하... 초등학교 안나왔나 보네...')
     
     # 각각 다른 오류를 출력
     try:
         num = input('100을 나눌 값을 입력하세요: ')
         print(100 / int(num))
     except ValueError:
         print('숫자가 뭔지 모르나?')
     except ZeroDivisionError:
         print('0 으로 어떻게 나누지...')
     except Exception: # 가장 상위 개념의 예외 처리 이므로 Exception 으로 첫 예외를 처리할 경우 아래의 예외들은 처리 되지 않는다. 따라서 가장 밑에서 처리해주는게 바람직하다.
         print('모든 예외 처리를 할 수 있지!!')
     ```

   - else 와 __finally__

     - else: 에러가 나지 않았을 경우에만 실행

     - finally: 에러 발생 유무와 상관없이 무조건 실행

       ```python
       # else를 사용예시
       try:
           numbers = [1, 2, 3]
           number = numbers[200]
       except IndexError:
           print('Error!!')
       else:
           print(number**3)
       
       # finally 사용예시
       try:
           fruits = {'apple', 'banana', 'mango', 'peach'}
           fruits['pineapple']
       except KeyError as err:
           print(f'{err}, 오류 발생')
       finally:
           print('finally는 오류 발생과 상관없이 무조건 실행되지')
       ```

   - raise : 강제로 예외를 발생시킴