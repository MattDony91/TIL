#### 2019년 7월 8일

# StartCamp _ 쳇봇 Quest_Day1

### 컴퓨터의 주요 기능

- 계산
- 저장



### 프로그래밍이란?

- 컴퓨터에게 일을 지시하기 위한 ==___명령어 집합___==




### 프로그래밍의 3형식

- 변수(기억)
- 조건문 (if 문)
- 반복문 (while 문/ for 문)



### 변수를 담기 위한 여러가지 형태의 BOX(집합 자료형)

- List :  대괄호를 사용해 값들을 묶어 주며 순서를 이용해 원하는 데이터에 접근 가능
   ```python
  # List 예시
  myList = [1, 2, 3, 4, 5]
  
  print(myList[1]) # 2 (list의 첫번째 원소는 0 번 부터 시작)
  ```

- Dictionary : 중괄호를 사용해 값들을 묶어 주며 key 와 value  한 쌍으로 구성됨, 순서가 없음

  ```python
  # Dictionary 예시
  myDictionary = {
      "key1" : "value1",
  	"key2" : "value2",
  	"key3" : "value3"
  }
  
  print(myDictionary["key1"]) # value1
  ```




### 내장함수
 - 기본적으로 많이 사용하는 기능을 바로 사용할 수 있게 해놓은 것
 - ex) `print()`



### 외장함수
- 특정한 기능이 필요할 때  import 키워드를 사용하여 불러와 사용하는 함수
 ```python
# 사용방법 예제
import random
ranNum = random.choice(range(10)) # 0 ~ 9 사이의 숫자 중 랜덤하게 한 숫자를 선택
ranNums = random.sample(range(1, 46), 6) # 1 ~ 45 사이의 숫자 중 랜덤하게 6개의 숫자 선택
 ```