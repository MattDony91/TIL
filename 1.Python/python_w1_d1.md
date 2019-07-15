#### 2019년 7월 15일

# Pyton 기초문법

---

#### 사전준비(jupyter notebook 설치)

> 노트형식으로 한줄씩 실행할 수 있는 python  개발 도구

- 터미널 환경에 'pip install jupyter' 입력해 설치하기
- 'jupyter notebook' 명령어를 입력해 실행

---



### 1. 식별자

> 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름

- 첫 글자에 숫자가 올 수 없음

- 식별자는 알파벳(대, 소문자 구분), _, 숫자로 구성(한글도 지원하지만 사용하지 않는게 바람직 하다)

- 미리 정의된 예약어는 사용할 수 없다. (예약어는 아래 주소 참조)

  ([https://docs.python.org/ko/3.7/reference/lexical_analysis.html?ighlight=%EC%98%88%EC%95%BD%EC%96%B4](https://docs.python.org/ko/3.7/reference/lexical_analysis.html?highlight=예약어))

- jupyter notebook 에서 예약어 확인하는 방법

  ```python
  import keyword
  print(keywrod.kwlist)
  ```





### 2. 여러가지 기본문법

- 코딩선언

  > 기본 utf-8로 설정 되어 있기 때문에 안해줘도 크게 상관 없음

  ```python
  # -*- coding: <encoding-name-> -*-
  ```

- __주석(Comment)__

  - 보틍은 '#' 으로 표시 (사용예시: `# 여기는 주석`)
  - 여러줄의 주석을 작성할 때는 """ 으로 표시

  ```python
  """
  여러줄의
  주석을
  작성할 수 있습니다.
  """
  
  def mysum(a, b):
      """
      a, b 두 개의 인자가 필요하며 a + b 값을 반환합니다.
      
      함수안에서 사용할 경우 함수를 설명하는 메뉴얼로 사용되며
      __doc__ 를 작성해 메뉴얼만 불러 올 수 있습니다.
      """
      return a + b
  
  mysuml.__doc__
  ```






### 3. 변수(Variable) 및 자료형(Type)

- __변수(Variable)__

  > __재사용__을 목적으로 특정한 값을 사용하기 편한 이름으로 지정(할당) 하는 것

  - 변수는 = 을 통해 할당 (예시: `a = 1`)
  - 변수의 자료형을 확인하기 위해서는 type() 활용 (예시: `a.type()`)
  - id()를 활용해 메모리 주소를 확인 할 수 있음 (예시: `a.id()`)

  

- __자료형(Type)__

  - __수치형(Numbers)__

    - __정수(int ; integer)__

      - 모든 정수는 int로 표현됨(3.x 버전에서는 long 타입 사라짐)

      - arbitrary-precision arithmetic 을 이용해 부족한 바이트 만큼 동적으로 할당

      - 여러 진수 표현방법

        ```python
        binary_number = 0b10 # 2진수 표현법 (결과값: 2)
        octal_number = 0o10 # 8진수 표현법 (결과값: 8)
        decimal_number = 10 # 10진수 표현법 (결과값: 10)
        hex_number = 0x10 # 16진수 표현법 (결과값: 16)
        ```

    - __부동소수점(float)__

      >실수를 컴퓨터가 표현하는 과정에서 요류가 발생할 수 있으므로 주의

      ```python
      pi = 3.14
      print(type(pi)) # float
      ```

      - __복소수(complex)__
    
        > 허수부를 j로 표현
    
        ```python
        a = 3 - 4j
        print(type(a)) # complex
        ```
  
  
  
  - __Bool 형__
  
    - True, False로 이뤄져있음
  
    - 비교/논리 연산을 수행
  
    ```python
    # True를 반환하는 경우
    print(bool(1))
    print(bool([1, 2, 3]))
    print(bool('True'))
    
    # False를 반환하는 경우
    print(bool(0))
    print(bool([]))
    print(bool(''))
    ```
  
  
  
  - __None__
  
    > 다른 언어에서는 NULL 로 표현하며 값이 없음을 표현하기 위해 존재
  
    ```python
    a = None
    print(type(a)) # NoneType
    ```
  
  
  
  - __문자형(String)__
  
    - Single quotes(')나 Double quotes(") 를 활용해 표현 가능
    - 문자열을 묶을 때 동일한 부호를 활용해야 함
  
    ```python
    name = 'honggil Dong'
    print(type(name)) # <class 'str'>
    ```
  
    - 여러줄에 걸쳐있는 문장은 """안에 내용을 기입해 작성"""
  
    ```python
    # 문장에 개행이 적용된 그대로 출력
    print("""
    Hello
    python
    world
    """)
    ```
  
  - __이스케이프 문자열__
  
    > 특수문자나 특정 기능을 수행하기 위해 '\\' 활용해 구분하는 것
  
    - '\n' => 줄바꿈
  
    - '\t' => 탭
  
    - '\r' => 캐리지리턴(커서를 맨 앞으로 보냄)
  
      ```python
      print('1234567\r***') # ***4567
      ```
  
    - '\0' => 널(NULL)
  
    - '\\\\' => \\표시
  
    - '\\' => Single quotes
  
    - '\\' => Double quotes
  
  - __문자열 보간(String interpolation)__
  
    - % - formattion
  
    ```python
    name = 'gildong'
    print('반갑습니다. %s'  % name)
    ```
  
    - str.format()
  
      > 참조: https://pyformat.info/
  
    ```python
    name = 'gildong'
    print('{} 반갑습니다.'.format(name))
    ```
  
    - f-string (파이썬 3.6버전 이후에 지원)
  
    ```python
    name = 'gildong'
    print(f'반갑습니다. {name}')
    ```





### 4. 연산자

- __산술 연산자__

  - 기본적인 사칙연산(+, -, *, /) 가능
  - 특수한 연산(//: 몫 구하기, %: 나머지 구하기, **: 거듭제곱) 도 있음

  ```python
  print(2**5) # 32
  print(5 // 2) # 2
  print(5 % 2) # 1
  ```

  

- __비교 연산자__

  - 수학에서 배운 연산자와 동일하게 값을 비교
  
    - a > b : 초과
    - a < b : 미만
    - a >= b : 이상
    - a <= b : 이하
    - a == b : 같다
    - a != b : 같지 않다

  

- __논리 연산자__
  - __and__ => 두 조건 모두 True 일때만 True
  - __or__ =>  두 조건 중 하나만 True 이면 True
  - __not__ => True->False, False->True

  ```python
  # and 연산 결과
  print(True and True) # True
  print(True and False) # False
  print(False and False) # False
  
  # or 연산 결과
  print(True or True) # True
  print(True or False) # True
  print(False or False) # False
  
  # not 연산 결과
  print(not True) # False
  print(not False) # True
  ```

  - 단축평가 and 와 or
    - 단축평가 and: a가 거짓이면  a를 리턴, 참이면 b를 리턴
    - 단축평가 or: a가 참이면  a를 리턴, 거짓이면 b를 리턴

    ```python
    # 단축평가(short-circuit evaluation) and
    print(0 and 5) # 0 (a가 거짓이므로 a를 리턴)
    print(3 and 5) # 5 (a가 참이므로 b를 리턴)
    
    # 단축평가(short-circuit evaluation) or
    print(0 or 5) # 5 (a가 거짓이므로 b를 리턴)
    print(3 or 5) # 3 (a가 참이므로 a를 리턴)
    ```

    

- __복합 연산자__
  - 연산과 대입이 함께 이뤄지는 연산자
  - 반복문을 통해 개수를 카운트 할때 가장 많이 활용됨
  - (a += b) 형태로 사용하며 (a = a + b) 와 완전히 같은 의미이다.



- __기타 연산자__
  - in => 연산자를 통해 속해있는지 여부를 확인
  - is => 연산자를 통해 동일한  object 인지 확인
  - Indexing/Slicing => [] 통한 값 접근 및 [:] 을 통한 슬라이싱



- __연산자 우선순위__
  - ()
  - 슬라이싱
  - 인덱싱
  - 제곱연산자 (**)
  - 단항연산자 (+, -)
  - 산술연산자 (*, /, %)
  - 산술연산자(+, -)
  - 비교연산자, in, is
  - not
  - and
  - or






### 5.  형변환

- 기초 형변환(= 암시적 형변환)

  > 사용자가 의도하지 않아도 자동으로 형변환 하는 경우

  - 아래의 상황에서만 가능
    - bool
    - Numbers(int, float, complex)

- __명시적 형변환__

  > 명시적으로 형 변환을 입력해주서야 하는 경우

  - 자료형 타입으로 변환할 데이터를 감싸 형변환 시킴

  - string -> integer : 형식에 맞는 숫자만 가능
  - integer -> string : 모두 가능

  ```python
  a = '10'
  print(type(int(a))) # int
  ```






### 6. 시퀀스 자료형 과 Set, Dictionary  자료형

- __시퀀스(sequence) 자료형__
  
  > 순서로 나열된 형식(정렬되었다는 뜻은 아님!!)
  
- 인덱스를 통해 접근 가능하며 슬라이싱 또한 가능
  - 시퀀스 자료형들
    - __list__ => [] 안에 작성, 요소 변경 가능
    - __tuple__ => () 안에 작성, 요소 변경 불가능(immutable)
    - __range__
    - __string__
    - binary



- __Set, Dictionary__

  > 순서가 없는 데이터 모음 / 둘 다 {중괄호} 안에 입력함

  - set => 수학에서와 동일하게 차집합, 합집합, 교집합 등을 사용할 수 있음
    - 차집합(difference, -)
    - 합집합(union, |)
    - 교집합(intersection, &)
  - __dictionary__ => key, value 쌍으로 이루어져 있다.
    - dict.keys() => key 값만 불러옴
    - dict.values() =>  value 값만 불러옴
    - dict.items() => key 와 value 쌍을 불러옴