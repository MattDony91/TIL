#### 2019년 8월 7일

# Web - Framework

---

#### Django 관리자 사용하기

- 터미널 환경에서 아래와 같은 명령어를 입력해 아이디를 생성

  - `$ python manage.py createsuperuser`

- `app 폴더` 안의 `admin.py` 파일에서 아래와 같이 등록해준다.

  ```python
  from django.contrib import admin
  from .models import Todo # 등록하기 위해 import 시킨다.
  
  admin.site.register(Todo) # 등록
  ```

- `localhost:8000/admin` 주소를 입력해 생성한 아이디와 비밀번호로 접속하고 데이터를 확인

---

