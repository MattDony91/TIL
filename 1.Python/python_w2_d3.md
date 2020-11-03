#### 2019년 7월 24일

# Python OOP



### 1. 클래스 변수 / 인스턴스 변수

- 클래스 변수
  - 클래스의 속성
  - 클래스 선언 블록 최상단에 위치
  - Class.class_variable 로 접근 / 할당
- 인스턴스 변수
  - 인스턴스의 속성
  - self.instance_variable 로 접근 / 할당



### 2. 인스턴스 메서드 / 클래스 메서드 / 스태틱(정적) 메서드

- 인스턴스 메서드

  - 정의 위에 아무런 데코레이터도 없으며, 자동으로 인스턴스 메서드가 된다.
  - __첫 번째 인자로 `self`를 받도록 정의__
  - 인스턴스는 3가지 메서드 모두 접근할 수 있지만, 클래스와 스태틱 메서드는 호출하지 않아야 한다.

- 클래스 메서드

  - 클래스가 사용할 매서드
  - 정의 위에 `@classmethod` 데코레이터를 사용
  - __첫 번째 인자로 `cls`를 받도록 정의__
  - 클래스는 3가지 메서드 모두 접근할 수 있지만, 인스턴스 메서드는 호출하지 않아야 한다.

- 스태틱(정적) 메서드

  - 정의 위에 `@staticmethod` 데코레이터를 사용

  - 인자 정의는 자유롭게 하며, 어떠한 인자도 자동으로 넘아가지 않는다.

    ```python
    # 메서드 종류 3가지 사용예시
    class Doggy:
        num_of_dogs = 0
        birth_of_dogs = 0
        def __init__(self, name, age):
            self.name = name
            self.age = age
            Doggy.num_of_dogs += 1
            Doggy.birth_of_dogs += 1
        def __del__(self):
            Doggy.num_of_dogs -= 1
        def bark(self):
            print(f'{self.name} 짖는다: 멍멍멍')
        @classmethod
        def status(cls):
            print(f'태어난 강아지: {cls.birth_of_dogs}마리\n현재 강아지: {cls.num_of_dogs}마리')
        @staticmethod
        def info():
            return '이것은 강아지입니다.'
    ```

    ```python
    # 인스턴스를 만들고 함수를 실행해보자.
    d1 = Doggy('핫도그', 3)
    d2 = Doggy('콜도그', 2)
    d3 = Doggy('도그', 4)
    
    d1.bark()
    Doggy.status()
    Doggy.info()
    ```

    

### 3. 오버라이딩(중복정의)

> 파이썬에 기본적으로 정의된 연산자를 직접적으로 정의하여 활용할 수 있다.

    ```python
    +  __add__
    -  __sub__
    *  __mul__
    <  __lt__
    <= __le__
    == __eq__
    != __ne__
    >= __ge__
    >  __gt__
    ```

```python
# 사용예시
# 사람과 사람을 같은지 비교하면, 이는 나이가 같은지 비교한 결과를 반환하도록 만들어봅시다.
class Person:
    population = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
```

```python
p1 = Person('노인', 100)
p2 = Person('아기', 5)
p1 < p2
```



### 4. 상속

- 한 클래스에 정의된 모든 속성을 다른 클래스에서 재사용 할 수 있게 하는 것

- 상속하는 클래스를 부모 클래스, 상속 받는 클래스를 자식 클래스라고 한다.

- 자식 클래스는 상속 받은 메서드 이외에 다양한 메서드를 추가해 다양한 형태로 사용 할 수 있다.

- __super()__를 이용해 부모클래스의 내용을 사용 할수도 있다.

  ```python
  # 상속 예시
  # Person 클래스 생성
  class Person:
      def __init__(self, name, age, number, email):
          self.name = name
          self.age = age
          self.number = number
          self.email = email 
          
      def greeting(self):
          print(f'안녕, {self.name}')
          
  # Person을 상속받는 Student 클래스 생성        
  class Student(Person):
      def __init__(self, name, age, number, email, student_id):
          # 부모 클래스인 Person 에 있는 생성자를 가져와 사용
          super().__init__(name, age, number, email)
          self.student_id = student_id
          
  
  class Soldier(Person):
      def __init__(self, name, age, number, email, army_id):
          super().__init__(name, age, number, email)
          self.army_id = army_id
       
      # 부모 클래스인 Person 에 있는 greeting 메서드를 오버라이딩(재정의)해 사용
      def greeting(self):
          print(f'충성! 이병 {self.name}')
          
          
  
  ```

  ```python
  p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
  s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
  a1 = Soldier('굳건이', 20, '999888777', 'army@email.com', 22113354)
  
  p1.greeting()
  s1.greeting() # Student 클래스 에 없지만 부모인 Person에 정의 되어 있으므로 사용 할 수 있다.
  a1.greeting() # Soldier 클래스에 재정의(오버라이딩) 된 함수가 사용되는 것을 볼 수 있다.
  ```

  
