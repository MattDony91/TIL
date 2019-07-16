#### 2019년 7월 16일

# Python 제어문 (Control of Flow)

> python 에선 __들여쓰기__로 영역을 구분하며 4 Space( = 1 Tab) 을 기본으로 한다.



### 1. 조건문 (if 문)

- 참 / 거짓을 판단 할 수 이쓴 조건식과 함께 사용

- 콜론(:) if문 끝을 닫아준다.

- 참인 경우 __if__ 이후의 문장을 수행

- 거짓인 경우 __else__ 이후의 문장을 수행

- __if__는 조건은 무조건 쓰여야 하며 __else__는 상황에 따라 사용하지 않아도 된다

- 분기점이 셋 이상인 경우 __if__-__elif__-__else__ 를 사용해 분기할 수 있으며 __elif__는 여러번 작성할 수 있다. (복수 조건문)

  ```python
  # 실습!
  score = 96
  if score >= 90:
      print('A')
      if score >= 95:
          print('참잘했어요')
  elif score >= 80:
      print('B')
  elif score >= 70:
      print('C')
  elif socre >= 60:
      print('D')
  else:
      print('F')
  ```

- 조건 표현식(Conditional Expression)

  > true_value if <Condition> else false_value

  - 다른 언어의 삼항연산자와 같은 기능

    ```python
    # 사용예시
    a = int(input("숫자를 입력하세요 : "))
    print('0보다 큼') if a > 0 else print('0보다 크지 않음')
    ```





### 2. 반복문 (while 문 / for 문)

> while 이나 for 안에 조건식을 넣어 조건이 참인 동안 반복해서 실행하며 끝에 콜론(:)을 붙여준다.

 - __while 문__

   - 조건식이 참(True)인 경우 반복적으로 코드를 실행

   - __종료조건을 반드시 설정해주어야 한다.__

     ```python
     # 사용예시
     a = 0
     while a < 5:
         print(a)
         a += 1
     print('끝')
     ```

   

 - __for 문__
   - 시퀀스에서 순차적으로 코드를 실행

     ```python
     # 사용예시
     for i in range(5): # for 문에서 선언된 변수 i 는 for문이 끝난 후에 바깥에서도 사용이 가능
         print(i)
     print(i)
     print('끝')
     ```

   - index 와 함께 사용하기 => 내장함수 __enumerate()__ 를 활용

     - enumerate() 는 이터레이터 객체(= 시퀀스형) 에 대해 값과 메서드 카운트 값을 반환해주는 함수

       ```python
       # 사용예시
       names = ['kim', 'oh', 'park', 'jung']
       print(list(enumerate(names)))
       # [(0, 'kim'), (1, 'oh'), (2, 'park'), (3, 'jung')]
       ```

   - dictionary 와 for문 함께 사용하기

     ```python
     # 여기에 코드를 작성하세요.
     blood_type = {"A": 4, "B": 2, "AB": 3, "O":1}
     
     # 0. dictionary (key 반복)
     keys1 = ''
     for key in blood_type:
         keys1 += key + ' '
     print(f'혈액형의 종류는 다음과 같습니다 => {keys1}')
     
     # 1. key 반복
     keys2 = ''
     for key in blood_type.keys():
         keys2 += key + ' '
     print(f'혈액형의 종류는 다음과 같습니다 => {keys2}')
     
     # 2. value 반복
     total = 0
     for val in blood_type.values():
         total += val
     print(f'총인원은 {total}명입니다.')
     
     # 3. key와 value 반복
     for key, val in blood_type.items():
         print(f'{key}형은 {val}명입니다.', end = ' ')
     ```



- __break, continue, else__

  - __break__

    > 특정 조건에서 반복문을 끝내는 명령어

    ```python
    # 사용예시
    for i in range(10):
        if i > 1:
            print('0과 1 만 필요함')
            break
        print(i)
    ```

  - __continue__

    > 특정 조건에서 반복문안의 실행문장을 건너뛰고 다음 반복을 실행하는 명령어

    ```python
    # 사용예시
    for i in range(10):
        if i % 2: # 홀수 일때 참이므로 홀수는 출력하지 않고 다음 반복으로 넘어간다.
            continue
        print(i)
    ```

  - __else__

    > 반복문 안에서 else 는 break를 만나지 않았을때(반복문이 정상적으로 종료 되었을 때) 실행된다.

    ```python
    # 사용예시
    numbers = [1, 5, 10]
    for number in numbers:
        if number == 3:
            print('True')
            break
    else:
        print('False')
    ```





---



# 함수(fucntion)

> 효율적인 Coding 을 위해 사용

- 함수 선언은 def 로 시작하여 콜론(:) 으로 끝나고, 다음은 4 Space 들여쓰기로 코드 블록을 만든다.

- 함수는 매개변수(parameter) 를 넘겨즐 수도 있다.

- 함수는 return 값을 전달해줄 수도 있다.

  ```python
  # 함수 사용예시
  # 함수로 정의 해놓으면 코드블록 안에 내용을 중복해서 여러번 작성하지 않아도
  # 함수의 호출만으로 반복해서 사용할 수 있다.
  
  def rectangle_spec(height, width):
      r = 2 * (height + width)
      a = height * width
      print(f'직사각형 둘레: {r}, 면적: {a}입니다.')
      
  rectangle_spec(30, 20)
  rectangle_spec(20, 40)
  ```

- 내장함수 => 자주 사용하는 기능은 python 에서 내장함수로 기본적으로 제공함

  ```python
  dir(__builtins__) # 입력해 내장함수들을 확인 할 수 있다.
  ```

  