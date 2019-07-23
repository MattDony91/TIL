#### 2019년 7월 23일

# Python



### 1. map(), zip(), filter()

- __map(function, iterable)__

  - Iterable의 모든 원소에  function을 적용한 후 그 결과를 돌려준다.

  - return은 map_object 형태로 반환 된다.

    ```python
    # numbers 를 문자열 '123'으로 만들어 보자
    numbers = [1, 2, 3]
    
    # map() 사용
    print(''.join(list(map(str, numbers))))
    # compreshension 사용
    print(''.join([str(num) for num in numbers]))
    ```



- zip(*iterables)

  - 복수의 iterables 한 것들을 모아 주는 함수

  - 결과는 튜플의 모음으로 zip object를 반환

  - iterables 의 길이가 다른 경우 기본적으로 짧은 길이에 맞춰서 반환

    (긴 것을 맞춰서 반환 할 수도 있지만, 사용하는 일이 거의 없다.)

    ```python
    # .zip() 사용예시
    a = '123'
    b = '567'
    
    for digit_a, digit_b in zip(a, b):
        print(digit_a, digit_b)
    ```

    

- __filter(function, iterable)__

  - iterable에서 function의 반환된 결과 중 참인 것들로만 구성해 반환

    ```python
    # .filter() 사용예시
    def even(n):
        return not n%2
    
    numbers = [1, 2, 3, 4, 5]
    print(list(filter(even, numbers)))
    ```





### 2. 객체 지향 프로그래밍  - OOP (Object Oriented Programming)

> 컴퓨터 프로그래밍의 패러다임의 하나로서 프로그램을 하나가 아닌 여러 개의 독린된 단위로 생각하는 것.

- __OOP 의 기본 구성요소__

  - __클래스 (Class)__
    - 속성과 행위를 정의한 것으로 데이터형이라고 할 수 있다.
    - `class ClassName:`의 형식으로 선언한다.
  - __인스턴스 (Instance)__
    - 클래스에서 정의한 것을 실제로 메모리상에 할당된 것
  - __속성 (Attribute)__
    - 클래스 / 인스턴스 가 가지고 있는 속성
  - __메서드 (Method)__
    - 클래스 / 인스턴스가 할 수 있는 행위

  ```python
  class MyList: # 클래스 선언
      data = []	# attribute
      
      def append(self, num): # 메서드
          self.data += [num]
          
      def pop(self):
          element =  self.data[-1]
          self.data = self.data[:-1]
          return element
          
      def reverse(self):
          self.data = self.data[::-1]
                  
      def count(self, num):
          cnt = 0
          for i in self.data:
              if i == num:
                  cnt += 1
          return cnt
      
      def clear(self):
          self.data = []
          
      def __repr__(self):
          print(f'내 리스트에는 {data} 이 담겨있다.')
  ```

  ```python
  test_list = MyList() # 클래스를 인스턴스화
  
  test_list.append(1)
  test_list.append(2)
  test_list.append(3)
  test_list.append(2)
  print(test_list.data)
  print('append test 완료')
  print('=' * 20)
  print(test_list.count(2))
  print('count test 완료')
  print('=' * 20)
  test_list.reverse()
  print(test_list.data)
  print('reverse test 완료')
  print('=' * 20)
  print(test_list.pop())
  print(test_list.pop())
  print(test_list.data)
  print('pop test 완료')
  print('=' * 20)
  test_list.clear()
  print(test_list.data)
  print('clear test 완료')
  ```

  - __생성자__ / 소멸자

    - 생성자는 객체가 생성되는 과정에서 호출되는 함수

    - 소멸자는 객체가 소멸되는 과정에서 호출되는 함수

      ```python
      # __함수__ => 형태의 메서드를 '스페셜 메서드' 또는 '매직 메서드'라고 한다.
      def __init__(self): # 생성자
          print('생성될 때 자동으로 호출되는 메서드입니다.')
          
      def __del__(self): # 소멸자
          print('소멸될 때 자동으로 호출되는 메서드입니다.')
      ```

      ```python
      # 사용예시
      class Person:
          def __init__(self):
              print('생성')
          def __del__(self):
              print('소멸')
      ```
      
      ```python
      # 인스턴스 생성
      p1 = Person('humanoid') # '생성' 출력됨
      ```
      
      ```python
      # 인스턴스 삭제
      del p1 # '소멸' 출력됨
      ```
      
      