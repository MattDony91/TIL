#### 2019년 7월 10일

# StartCamp_W2_D3



### 파일조작하기

> (쓰고 : 'w', '읽고' : 'r', 추가하고 : 'a')

- open() 내장함수를 이용해 조작

- 다 사용한 후에는 반드시  close()를 써줘야 한다.

  (with open 사용시 close()를 작성하지 않아도 자동으로 닫아 줌)

  

- open() 사용시

```python
# open() 내장함수에 생성할 파일 이름을 정하고, 'w' 옵션을 준다
# 파일 조작이 끝난 후에는 close()를 이용해 닫아준다.
# 파일을 조작할 내용은 open() 과 close() 사이에 작성해 준다.

f = open('student.txt', 'w')
f.write('안녕하세요')
f.close()
```

- with open() 사용시

```python
# 위의 open() 예시와 같은 동작을 수행함
# (괄호) 안에는 open()함수와 같이 작성
# 'as f'는 open()의 예시에서 'f = open' 과 같은 기능으로 끝에 콜론(:)을 써준다.
# 파일을 조작할 내용은 들여쓰기를 통해 구분

with open('student.txt', 'w') as f:
    f.write('안녕하세요')
```

- 응용하기

  >  크롤링을 이용해 데이터를 가져와 csv 파일로 저장해보자

```python
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

tr = soup.select('tbody > tr')
with open('naver_exchange.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for r in tr:
        tit = r.select_one('.tit').text.strip()
        sale = r.select_one('.sale').text.strip()
        row = [tit, sale]
        csv_writer.writerow(row)
```





### HTML & CSS

> HTML (HyperText Markup Language) :  기본 구조를 잡아줌
>
> CSS (Cascade Style Sheet) : 디자인 적인 요소를 가미
>
> (JavaScript : 동적인 페이지로 만들 수 있게 해줌)



- HTML 사용하기

```html
<!DOCTYPE html>
<head>
	<!-- 제목, 메타데이터, 링크 등등 을 작성 -->    
</head>
<body>
	<!-- <태그이름 속성명1="속성값1" 속성명2="속성값2">내용</태그이름> -->    
</body>
```

- CSS 사용하기

```css
/*
적용할 태그, 아이디, 이름 등 {
	속성을 정의	
}
*/

/* 사용예시 */
h1 {
    background-color: orangered;
    color: skyblue;
    margin: 0%
}

#id {
    /*id 속성을 선택할때는 '#'을 붙인다.*/
}

.black {
    /*class 속성을 선택할때는 '.'을 붙인다.*/
}

/*여러개의 CSS가 중복되어 영향을 미치는 경우 우선순위가 존재*/
/* 'id -> class -> 태그'순으로 적용됨(자세한 내용은 본과정에서)*/
```





### Github 에 hosting 하기

- Repository name 에 '(Owner)닉네임.github.io' 형식을 맞춰서 작성하면 ID당 하나의 주소를 호스트 할 수 있다