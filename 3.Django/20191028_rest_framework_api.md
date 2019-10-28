#### 2019년 10월 28일

# Django

### 1. rest_framework 의 serializer 를 이용해 json 타입으로 변환하기

> django 에서 DB 에 접근해 값을 얻어 올때 query_set 타입을 반환해주며 이는 django 에서만 사용할 수 있는 타입이므로 일반적으로 사용할 수 없다.
>
> 이런 문제점을 해결하기 위해 일반적으로 많이 사용되는 json(JavaScript Object Notation) 타입으로 변환 데이터를 리턴해주기 위해 serializer 를 사용한다.



공식문서: __` https://www.django-rest-framework.org/ `__

터미널창에서 다운받기: __`pip install djangorestframework`__





DB에 입력되어 있는 데이터를 json 형식의 파일로 저장하는 명령어(.json 파일 생성)

python manage.py dumpdata --indent 2 musics > my_dumpdata.json





.json 파일을 DB에 입력하는 명령어

python manage.py loaddata musics/my_dumpdata.json



settings.py 의 INSTALLED_APP 에 추가해준다.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]
```





__`serializers.py`__ 파일을 생성하고 아래와 같은 코드를 작성(파일이름은 달라도 되자만 이렇게 쓰자...)

```python
from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)
```





__`views.py`__ 에서 아래와 같이 코드를 작성

```python
from django.shortcuts import render
from .models import Music
from rest_framework.decorators import api_view
from .serializers import MusicSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all() # jquery 타입으로 반환 -> django 에서만 사용되는 타입
    serializer = MusicSerializer(musics, many=True) # jquery -> json 타입으로 전환
    return Response(serializer.data)
```





응답 데이터를 쉽게 확인하는 Tip

구글에서 __`postman chrome extension`__ 검색해 확장프로그램에 추가하면 쉽게 데이터 타입을 확인 할 수 있다.





### 2. drf-yasg - Yet another Swagger generator

> url 을 보기 좋게 꾸며주는 library

공식문서를 통해 사용방법을 확인 할 수 있다. __`https://github.com/axnsan12/drf-yasg `__

터미널창에서 다운받기: __`pip install -U drf-yasg`__



settings.py 의 INSTALLED_APP 에 추가해준다.

```python
INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
]
```



project 폴더 안의 __`urls.py`__ 에 아래와 같은 코드를 추가

```python
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
    #   description="Test description",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('musics.urls')),
    path('redocs/', schema_view.with_ui('redoc')),
    path('swagger/', schema_view.with_ui('swagger')),
]
```

