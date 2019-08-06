#### 2019년 8월 5일

# Web - Back end Framwork

---

#### <사전준비> 

-  __가상환경 설정__

1. 터미널 환경에서 설정하기

   - 가상환경 생성

     `$ python -m venv venv`  venv라는 명령어를 사용해 venv라는 이름의 가상환경을 설정한다.

   - 가상환경 설정

     `$ source venv/Scripts/activate`

   - 가상환경 해제

     `$ deactivate`

2. vs code 안에서 가상환경 설정하기
   - 단축키 `shift + ctrl + p` 또는  `F1` 을 누르고
   - `Python: Select Interpreter` 



- __django 설치__
  - `$ pip install django`

---



### 1. Django

- __MTV design pattern (MVC 와 같은 의미)__

  - M (Model) - 데이터를 관리(데이터 베이스)
  - T (Template) - 사용자가 보는 화면
  - V (View) - 중간 관리자(M-T 사이에 데이터를 주고 받음)

  

- __기본 명령어__

  - __django project 생성__
    
- `$ django-admin startproject 프로젝트이름 프로젝트생성위치`
    
  - __django 서버 실행__
  
  - `$ python manage.py runserver`
  
  - __app 생성__
  
    - `$ django-admin startapp 앱이름` 또는 `$ python manage.py startapp 앱이름`
    - __앱은 생성 후 반드시 프로젝트에 등록해야 한다.__
      - settings.py (기본으로 생성되는 파일 중 하나) 파일 안에
    - INSTALLED_APPS 라는 리스트 변수 안에 '앱이름' 을 추가 한다.
      - 직접 만든 앱이 리스트 인덱스의 우선순위에 있는 것을 권장한다.

  - __MTV 패턴으로 page를 추가하는 방법__

    - `project이름의 폴더` 안에 `urls.py 파일`을 열어 다음과 같이 작성한다.
  
      ```python
      from django.contrib import admin
      from django.urls import path
      from pages import views # 새로 만든 앱안에 자동으로 만들어주는 views 를 import 한다.
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('greeting/<str:name>/', views.greeting), # 사용자에게 요청받을 경로와 요청을 처리할 경로를 작성해준다.
    ]
      ```

    - `app이름의 폴더` 안에 `views.py 파일`을 열어 다음과 같이 작성한다.
  
      ```python
      from django.shortcuts import render
      
      # Create your views here.
      def greeting(request, name): # 요청을 처리할 메서드를 작성
          context = {
              'name': name,
          }
        return render(request, 'greeting.html', context) # html 파일에 data를 넘겨주기 위해선 반드시 dictionary 형태의 한 덩어리로 묶어서 보내줘야 한다.
      ```

    - `app이름의 폴더` 안에 `templates 폴더`를 생성하고 그 안에 `greeting.html` 파일을 생성한다.
  
      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
      </head>
      <body>
        <!--{# dtl(django template language) 중괄호 두개 안에 context에 기술한 key 값을 써주면 value 값을 가져 올 수 있다. #}-->
        <h1>{{name}}님 안녕하세요.</h1>
      </body>
      </html>
      ```
    



- __DTL(Django Template Language)__
  - 반복문
    - {% for 요소 in 데이터 %}
    - {% endfor %}
  - 조건문
    - {% if 조건문 %}
    - {% empty %} : else와 같은 뜻
    - {% endif %}