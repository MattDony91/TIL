#### 2019년 8월 6일

# Web - Framework



### 1. Django

- __데이터 전달__

  > 데이터를 전달하는 방식에는 크게 get 방식과 post 방식이 있으며 get은 DB에 있는 값을 그냥 요청할때(변경사항이 없을 때) 사용되며 post방식은 DB에 저장된 값에 변화를 줄 수 있거나 보안을 위한 목적으로 사용된다.

  - __form 태그__

    - __get 방식__

      - form 태그의 action 속성에 데이터를 넘겨줄 경로를 작성해 준다.

        ```django
        <!--{# 중괄호 안은 DTL(Django Templat Language) #}-->
        {% extends 'base.html' %}
        {% block body %}
          <h3>여기는 ping</h3>
          <form action="/pong/">
            <input type="text" name="name" placeholder="이름">
            <input type="number" name="age" placeholder="나이">
            <input type="submit">
          </form>
        {% endblock %}
        ```

      - 넘겨받은 데이터를 views 파일에서 가져오기

        ```python
        # 앱폴더 안의 views.py 파일
        def pong(request):
            name = request.GET.get('name') # 넘겨받은 데이터는 request 안에 들어있으며
            age = request.GET.get('age') # GET 이라는 키워드를 사용해 가져온다.
            context = {
                'user_name': name,
                'user_age': age,
            }
            return render(request, 'pong.html', context)
        ```

    - __post 방식__

      - form 태그의 action 속성에 데이터를 넘겨주며 method 속성에서 post 방식으로 지정해준다.

        ```django
        {% extends 'base.html' %}
        {% block body %}
          <h1>post-ping</h1>
          <!--{# method 는 default 가 get 방식이다. #}-->
          <form action="/post-pong/" method="POST">
            {% csrf_token %}
            <!--{# post 방식의 접근으로부터 서버를 보호하기 위해 csrf_token을 이용해 올바른 접근인지 판단하다.(데이터를 넘겨주며 확인도장을 찍어주는 개념) #}-->
            <input type="text" name="username" placeholder="ID 입력">
            <input type="text" name="password" placeholder="PW 입력">
            <input type="submit" value="LOGIN">
          </form>
        {% endblock %}
        ```

      - 넘겨받은 데이터를 views 파일에서 가져오기

        ```python
        def post_pong(request):
            username = request.POST.get('username') # post 방식은 POST 키워드로
            password = request.POST.get('password') # 데이터를 가져온다.
            context = {
                'username': username,
                'password': password,
            }
            return render(request, 'post_pong.html', context)
        ```

  - __Static data__

    - 정적인 데이터란 사용자의 컴퓨터에 저장된 그 데이터 자체를 한번 불러와 변하지 않고 그대로 사용하는 것이다.(컴퓨터에 저장된 사진, 정의된 css 파일 등)

    - static data 사용하기

      - `app 이름의 폴더` 안에 `static` 이라는 폴더를 생성하고 그 안에 image 파일이나 css 파일등을 위치한다.

      - html 파일에서 사용하는 방법은 아래의 코드를 참고하자

        ```django
        {% extends 'base.html' %}
        {% load static %}
        <!--{# static data를 사용하기 위해선 extends 바로 밑에서 load 해줘야 함 #}-->
        
        {% block head %}
          <link rel="stylesheet" href="{% static 'css/style.css' %}">
        {% endblock %}
        
        {% block body %}
          <h1>Larva</h1>
          <img src="{% static 'image/larva.jpg' %}" alt="">
          <!--{# static 이라는 명령어 다음 가져올 이미지의 주소를 ''안에 작성 #}-->
        {% endblock %}
        ```



- __하나의 project에서 여러개의 app 을 관리하기__

  - project명 폴더 안의 urls.py(master urls)을 통해 경로를 설정하고 관리할때 app을 여러개 생성한다면 경로가 어떤 app에서 사용되는 것인지 구별할 수가 없다.

  - 따라서 project명 폴더 안의 urls.py(master urls)에서는 app을 구분하여 주고 상세한 경로는 app 폴더 안에 urls.py 파일을 생성해 관리하는 것이 바람직하다.

  - master urls 파일 수정하기

    ```python
    # pjoect 명 폴더 안의 urls.py 파일
    
    from django.contrib import admin
    from django.urls import path, include # include 를 이용해 app을 구분하여 준다.
    # from pages from views # views 관련한 내용은 pages폴더 안의 urls.py 에서 처리 하므로 import 할 필요가 없다.
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('pages/', include('pages.urls')),
        # include() 안에 앱이름.urls 로 처리하여 준다.
        path('utilities/', include('utilities.urls')),
    ]
    ```

  - app 이름의 폴더 안에 urls.py 파일 생성하기

    ```python
    from django.urls import path # path를 사용하기 위한 import
    from . import views
    # from pages import views 와 같은 의미인데 views와 urls의 위치가 같으므로 . 으로 표시할 수 있다.
    
    urlpatterns = [
        path('ping/', views.ping),
        path('pong/', views.pong),
        path('post-ping/', views.post_ping),
        path('post-pong/', views.post_pong),
        path('static-example/', views.static_example),
    ]
    ```

  - html 파일 중 form 태그의 action 속성을 이용해 정해주던 경로가 변경 되었으므로 수정해 준다.

    ```django
    <!--{# ping.html 의 form 태그 action 을 아래와 같이 변경 #}-->
    <form action="/pages/pong/">
    
    <!--{# post_ping.html 의 form 태그 action 을 아래와 같이 변경 #}-->
    <form action="/pages/post-pong/" method="POST">
    ```





### 2. DataBase(DB)

- __ORM(Object-Relational Mapping)__

  >  python 코드를 DB에서 사용할수 있도록(sql로) 번역해줌

  - __데이터 조작 (CRUD)__ 
    - 데이터를 가지고 할 수 있는 작업으로는 CRUD 가 있다.
    - C (Create) : DB에 새로운 데이터를 생성한다.
    - R (Read) : DB에 저장된 데이터를 읽는다.
    - U (Update) : DB에 저장된 기존의 데이터를 수정한다.
    - D (Delete)  : DB에 저장된 데이터를 삭제한다.



- Django 에서 지원하는 DB 생성하기

  - DB를 생성할 app 폴더의 models.py파일에 ORM 을 사용하기 위한 class 생성

    ```python
    from django.db import models
    
    class Post(models.Model):
        title = models.CharField(max_lenth=100)
        content = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        # auto_now_add=True <= 데이터 베이스에 생성된 날짜를 자동으로 추가해주는 속성
        
        # 프린트의 기본값을 title로 함
        # django 관리자페이지에서 데이터를 확인할때 한눈에 알아볼 수 있다.
        def __str__(self):
            return self.title
    ```

- 터미널 창에서 아래와 같은 명령어를 실행해 준다.

  - python 문법을 sql 로 번역하는데 있어서 한번에 갈수 없고 중간 번역작업이 필요하고 그 중간 번역본을 생성하는 명령어
  - `$ python manage.py makemigrations` : 중간번역본을 생성
  - `$ python manage.py migrate` : 번역 실행(DB 생성)

- shell 모드로 접근해 DB를 조작해 보자.

  - `$ python manage.py shell` : 터미널 환경에서 쉘 모드를 실행(아래와 같이 시작점이 바뀌는것을 볼 수 있다.)
  - `>>> from posts.models import Post` : posts 앱의 models 파일에 접근해 Post 클래스를 불러온다.
  - `>>> p = Post()` : Post 클래스의 인스턴스를 하나 생성하고
  - `>>> p.title = "제목이지요"` : attribute를 초기화한다.
  - `>>> p.content = "내용입니다"`
  - `>>> p.save()` : 정의한 내용을 저장한다.
  - `>>> Post.objects.all() ` : 저장한 내용을 전부 다 불러오는 명령어
  - `>>> exit()` shell 모드 종료

- shell  모드를 시작하고 닫을 때마다 import 환경이나 선언한 변수가 다 초기화 되는 것을 방지하기 위해 새로운 모듈을 하나 설치해보자.

  - `$ pip install django_extensions` : 터미널창에 입력해 설치한다.
  - `$ python manage.py shell_plus` : 쉘 모드를 실행하는데 있어서 _plus  명령어가 추가 된 것을 확인 할 수 있다.
  - `>>> Post.objects.get(id=1)` : 하나만 접근 가능 중복되는 데이터가 있을시 오류
  - `>>> Post.objects.filter(title="안녕하세요")` : 중복 되는 데이터 모두를 가져옴
  - `>>> p.title = "hello"` : DB에 저장된 데이터를 변경
  - `>>> p.delete()` : 데이터 삭제