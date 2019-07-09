#### 2019년 7월 9일

# StartCamp _ 쳇봇 Quest_Day2



####  Program Download
- [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)  -> path 추가 박스 체크 후 설치
- git bash -> 설치 중간에 'Use Git and optional Unix tools from the Command Prompt (리눅스 베이스 명령어)' 체크 / 터미널
- vscode -> path 추가에 있는 모든 박스 체크 후 설치





### Git Bash 사용방법

> CLI(Command Line Interface) 를 조작하기 위한 터미널 환경을 제공하는 프로그램 중 하나

##### 명령어 종류

	-  ls => list 의 약자 / 현재 디렉토리의 목록을 확인할 때 사용하는 명령어 / -a 옵션을 사용해 숨김파일을 확인 할 수 있음
	-  cd => change directory 의 약자 / 마우스로 폴더를 더블 클릭해 디렉토리를 이동하는 것과 같은 명령을 수행
	-  mkdir => make directory 의 약자 / 새폴더를 생성
	-  touch => 파일을 만드는 명령어
	-  echo => 문자열을 출력해주는 명령어
	-  mv => move 의 약자 / 'mv (띄어쓰기) 옮길파일명 (띄어쓰기) 디렉토리명' 형식으로 작성 / 파일명을 바꿀때도 사용
	-  rm => remove 의 약자 / 파일을 이나 폴더( - r)를 지울 때 사용하는 명령어
	-  exit -> 터미널 종료 명령어





### VS Code 를 사용해 컴퓨터 조작하기

- 사용환경 설정 : [shift + ctrl + p] 를 눌러 'Terminal: Select Default Shell' 설치 / 그외 팝업으로 추천해주는 것 들 설치

#### 브라우저 조작(Crawling)

##### webbrowser

- browser.py 새파일 생성

```python
import webbrowser

webbrowser.open("https://www.naver.com") # 괄호 안의 주소로 오픈해줌
```

- [ctrl + `] 로 터미널 창을 오픈해 : python browser.py 를 실행시켜 결과를 확인

##### requests

- kosip.py 새파일 생성
- 터미널 창에서  'pip install requests' 를 입력해 설치

```python
import requests

res = requests.get("https://finance.naver.com/sise/")
print(res.text)
```

- 터미널 창에서 실행해 결과를 확인

##### BeautifulSoup

- python 이 알아먹기 쉽게 변환시켜주는 함수

- 터미널 창에 'pip install bs4' 를 입력해 설치

```python
import requests
from bs4 import BeautifulSoup
# 사람이 보기에는 똑같지만 python 입장에서 사용하기 쉽게 변경시켜줌

response = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(response, 'html.parser')

kospi = soup.select_one('#KOSPI_now') # select_one -> 은 하나의 값만 가져옴
#kospi = soup.select('#KOSPI_now') # select -> list타입으로 모든 값을 다 가져옴
print(kospi.text)
```

#### Computer  조작
##### Faker

> 랜덤한 정보를 얻기 위해 사용하는 외장함수

- 터미널에 'pip install faker' 입력해 다운로드

```python
  from faker import Faker
  import os
  
  f = Faker('ko_KR') #한글로 사용하기 위해 'ko_KR' 옵션 주기
  for i in range(100):
      filename = f"{i}_{f.name()}.txt"
      cmd = f"touch {filename}"
      os.system(cmd)
```

##### os

> Operating System(운영체제) 의 약자로 컴퓨터를 조작하기 위한 외장함수

```python
import os
# os.chdir => 디렉토리 변경
# os.listdir => 디렉토리 내 파일 확인
# os.rename => 파일 이름 변경
# str.replace("str1", "str2") => 파일 이름 변경(str1 을 str2로 변경함, 일부분만 변경가능)

os.chdir(r'C:\Users\student\startcamp\students')
# 주소 앞에 'r' 은 'raw'의 약자로 \ 를 특정 기능이 아닌 디렉토리를 구분하는
# 그대로 사용하기 위해 써준다.
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG_" + filename)
```



### Git -> (분산) 버전 관리 시스템

> 버전 관리와 협업을 위해 사용 

#### Github

> Git을 이용해 만들어진 소스코드 클라우드



##### Github 처음 시작하기

  (0. Github 사이트 가입은 알아서...)

1. 'https://gitignore.io/' 에 접속해 사용하고 있는 운영체제, 개발환경, 프로그래밍 언어를 입력하고 '생성' 버튼을 클릭

2. 생성된 문장을 복사하고 Github 에 올릴 파일이 있는 디렉토리에 'gitignore' 라는 파일을 만들고 복사한 내용을 붙여 넣는다.(gitignore 파일은 확장자 없음)

   (---여기까지 필요한 파일만 서버에 올리기 위한 작업---)

3. Git Bash(터미널 환경) 에 접속해 Github 에 올릴 파일이 있는 디렉토리에 접속한다.


```
# cd 이동할 디렉토리 주소

student@DESKTOP MINGW64 ~
$ cd startcamp

student@DESKTOP MINGW64 ~/startcamp
$
```
4. 'git init' 이라는 명령어를 입력해 master 디렉토리로 지정해준다.

```
student@DESKTOP MINGW64 ~/startcamp
$ git init

student@DESKTOP MINGW64 ~/startcamp (master)
$ 
```

5. 'git add' 명령어로 동기화 시킬 파일 선택

```
# . => 디렉토리 내 모든 파일 선택
# 또는 파일 이름을 작성해준다(ex)temp.txt)

student@DESKTOP MINGW64 ~/startcamp (master)
$ git add .
```

6. 'git commit' 명령어를 이용해 올릴 파일 확정

```
# -m => message 약자 / ""를 이용해 내용을 편하게 작성하기 위해 사용 / message는 commit 씨 반드시 필요하다.

student@DESKTOP MINGW64 ~/startcamp (master)
$ git commit -m "first commit"
```

7. email, name 등록하기

```
# 처음 하는 과정 이라면 6번의 과정에서 Enter 입력시 오류 나는게 정상
# 아래의 과정을 완료 한 후 6번의 명령을 다시 실행하면 Github 로그인 팝업이 뜬다.
# 같은 컴퓨터에서는 최초 한 번만 로그인 하면 된다.

student@DESKTOP MINGW64 ~/startcamp (master)
$ git config --global user.email "메일주소"
$ git config --global user.name "이름"
```

8. Github 에서 New repository 를 생성하고 서버 주소를 등록

```
student@DESKTOP MINGW64 ~/startcamp (master)
$ git remote add origin Git주소

# Tip 입력할 명령어는 repository 생성 시 보여지는 코드 중 가장 긴 라인과 같음!!
```

9. 'git push' 명령어를 이용 클라우드와 연동시킨다.

```
student@DESKTOP MINGW64 ~/startcamp (master)
$ git push origin master
```



##### Github 파일 올리기

- 처음 올리기 과정에서 5, 6, 8, 9  번의 과정을 순서대로 진행

  (repository  는 디렉토리 하나당 하나씩 생성해 관리하는게 좋다.)



##### Github 에서  Computer 로 파일 받기

- 아무것도 없는 상황에서 최초로 컴퓨터에 파일을 내려 받을 때

```
# 가장 먼저 컴퓨터 내 파일을 저장할 디렉토리로 이동하고
# clone 명령을 이용해 내려받을 수 있다.

student@DESKTOP MINGW64 ~/Desktop
$ git clone Git저장소주소
```

- 협업하는 상황에서 서버에 업데이트 된 내용을 컴퓨터에 최신화 적용시킬 때

```
# 최신화 시킬 디렉토리로 이동(master) 되어 있어야 함

student@DESKTOP MINGW64 ~/Desktop/end-to-end
$ git full origin master
```

