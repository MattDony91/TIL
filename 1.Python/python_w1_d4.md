#### 2019년 7월 18일

# Python 

### 1. 재귀함수(Recursive Function)

> 함수 내부에서 자기 자신을 호출 하는 함수

- 함수 내에서 자기 자신을 호출시 함수는 종료되지 않은 상태에서 계속해서 새로운 함수가 선언된다.

- 함수가 호출될 때마다 메모리에 쌓여 프로그램 실행속도가 느려진다.

  (python 에서는 1000번이 넘어가면 종료 시킴)

- 재귀함수를 작성시에는 반드시 base case(반복되지 않고 최종적으로 도달하는 곳)가 존재해야 한다.

- 재귀함수의 장단점

  - __장점__: 재귀 함수는 문제의 범위를 점점 줄여나가며 문제를 풀며, 코드가 직관적이고 이해하기 쉽다.
  - __단점__: 코드를 작성하기 어렵다. 자기 자신을 다시 호출 할때 함수를 종료시키지 않고 또 함수를 호출 하므로 메모리 공간에 쌓여 프로그램 실행 속도가 느려진다.

  ```python
  # 팩토리얼 만들기
  
  # 1.반복문 사용
  def fact(n):
      result = 1
      while n > 1:
          result *= n
          n-= 1
      return result
  print(fact(5))
  
  # 2.재귀함수 사용
  def factorial(n):
      if n <= 1:
          return n
      else:
          return factorial(n-1) * n
  print(factorial(5))
  ```





### 2. 문자열 메소드(String Method)

> 원본의 data는 건드리지 않고 메소드를 적용한 결과 값을 반환한다.

 - __.capitalize()__: 앞글자를 대문자로 변환 후 반환

 - __.title()__: 어퍼스트로피(')나 공백 이후를 대문자로 변환 후 반환

 - __.upper()__: 모두 대문자로 만들어 변환 후 반환

 - __.lower()__: 모두 소문자로 만들어 변환 후 반환

 - __.swapcase()__: 대 <-> 소문자로 변환 후 반환

 - __.join(iterable)__: iterable을 값들 사이마다 문자열을 합쳐서 반환

 - __.replace(old, new[, count])__ 바꿀 대상 글자를 새로운 글자로 바꿔서 반환(count를 지정해 해당 갯수만큼 시행가능)

 - __.strip([chars])__: 특정문자를 제거(lstrip 으로 왼쪽을 제거한거 rstrip 으로 오른쪽을 제거 할 수 있음)

 - __.find(x)__: x의 위치를 반환(x가 여럿일 경우 첫 번째 위치를 반환), __값이 없을 경우 -1을 반환__

 - __.index(x)__: x의 위치를 반환(x가 여럿일 경우 첫 번째 위치를 반환), __값이 없을 경우 오류__

 - __.split()__: 문자열을 특정한 단위로 나누어 리스트로 반환

   ```python
   # 사용예시
   a = "hI! Everyone, I'm kim"
   
   print(f'capitalize() 결과: {a.capitalize()}') # .capitalize()
   print(f'title() 결과: {a.title()}') # .title()
   print(f'upper() 결과: {a.upper()}') # .upper()
   print(f'lower() 결과: {a.lower()}') # .lower()
   print(f'swapcase() 결과: {a.swapcase()}') # .swapcase()
   
   print('-'.join(['010', '1111', '2222'])) # .join()
   
   word = 'wow!'
   print(word.replace('o', 'a')) # .replace()
   print(word2.replace('o', 'a', 3)) # .replace()
   
   word = '             hello          '
   print(word.rstrip() + '!') # .rstrip()
   print(word.lstrip() + '!') # .lstrip()
   print(word.strip() + '!') # .strip()
   
   word2 = 'hello!!!!!!!!!!!!!!'
   print(word2.strip('!')) # .strip()
   
   b = 'banana'
   print('apple'.find('a')) # .find()
   print('apple'.find('z')) # .find()
   print('apple'.index('a')) # .index()
   print('apple'.index('z')) # .index()
   
   fruits = 'apple banana mango'
   print(fruits.split()) # .split()
   ```

 - 그 외 다양한 확인 메소드: 참/거짓 변환

   ```python
   .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()
   
   #dir('string') -> 으로 확인할 수 있다.
   ```

   

### 3. 리스트 메소드(List Method)

> 원본 data를 직접 조작한다.

- __append(x)__: 값을 추가

- __extend(iterable)__: iterable 값을 추가 할 수 있음

- __insert(idx, x)__: 정해진 위치 index에 x값을 추가

- __remove(x)__: 첫 번째 x값을 찾아 삭제

- __pop(idx)__: 해당 index에 있는 값을 삭제하며 idx번째에서 삭제된 값을 반환

- __index(x)__: x 값을 찾아 해당 index 값을 반환(없는 값을 찾을시 에러)

- __count(x)__: 원하는 값(x)의 개수를 확인

- __sort()__: 리스트 안의 값들을 정렬(오름차순이 기본이며, 'reverse = True' 옵션을 통해 내림차순으로 정렬가능)

- __reverse()__: 리스트 안의 값의 위치를 반대로 위치시킴(반대로 뒤집음 / 정렬아님!!)

- __clear()__: 리스트 안의 모든 항목을 삭제

- __리스트 복사__ (= mutable 자료형의 복사)

  > immutable 자료형은 `a = b` 와 같이 간단하게 복사 할 수 있지만, mutable 자료형은 변수에 값이 아닌 값의 주소를 담고 있기 때문에 위 와 같이 작성한다면 같은 주소를 참조하여 제대로된 복사가 이뤄지지 않는다.

	  ```python
# 복사가 이뤄지지 않는 예시
  original_list = [1, 2, 3]
copy_list = original_list
  copy_list[0] = 123
print(original_list) # [123, 2, 3]
  print(copy_list) # [123, 2, 3]
  
  # copy_list의 값만 변경하고 싶었지만 original_list 값도 변경 된 것을 확인할 수 있다.
    ```

  - __얕은 복사(Shallow copy)__: mutable 을 쉽게 복사 할 수 있지만 일부의 경우에 한정해서 사용할 수 있다.

    ```python
    # 얕은 복사 예시
    a = [1, 2, 3]
    b = a[:] # 얕은 복사 방법1
    c = list(a) # 얕은 복사 방법2
    b[0] = 123
    c[0] = 321
    print(a) # [1, 2, 3]
    print(b) # [123, 2, 3]
    print(c) # [321, 2, 3]
    ```
  
  - __깊은 복사(Deep copy)__: mutabel 안에 mutable 자료가 들어있는 경우 얕은 복사로는 해결되지 않는다.
  
    ```python
    # 얕은 복사로 해결할 수 없는 예시
    a1 = [1, 2, [9, 10]]
    sc = list(a1)
    sc[0] = 111
    sc[2][0] = 9999
    print(a1) # [1, 2, [9999, 10]]
    print(sc) # [111, 2, [9999, 10]]
    # mutable 안의 mutable 자료형은 완전한 복사가 이뤄지지 않았음을 알 수 있다.
    
    # 깊은 복사 예시(copy 모듈 사용)
    import copy
    a2 = [1, 2, [9, 10]]
    dc = copy.deepcopy(a2)
    dc[0] = 111
    dc[2][0] = 9999
    print(a2) # [1, 2, [9, 10]]
    print(dc) # [111, 2, [9999, 10]]
    ```