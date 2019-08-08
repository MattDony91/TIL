#### 2019년 8월 8일

# Web - Framework

---

#### Django - models.py

- Relational DB 에서 __관계 설정__하기

  - model 들 간의 관계를 설정하기 위해 __ForeignKey(외래키)__ 를 사용한다.

  - __1 : N 의 관계__를 설정하는 방법

    - 1의 primarykey 를 N의 foreignkey로 설정해주며 django에서는 아래와 같이 작성한다.

      ```python
      from django.db import models
      
      class Question(models.Model):
          title = models.CharField(max_length=50)
          content = models.CharField(max_length=100)
          user = models.CharField(max_length=20)
          created_at = models.DateTimeField(auto_now_add=True)
      
      class Answer(models.Model):
          content = models.CharField(max_length=100)
          question = models.ForeignKey(Question, on_delete=models.CASCADE)
          # ForeignKey 는 클래스 전체를 받아와야 한다.
          # on_delete=models.CASCADE 속성은 참조하고 있는 primarykey 가 삭제될 경우 참조하고 있는 모든 foreignkey 를 같이 삭제시킨다.
      ```
    
    - 같은 primarykey 를 참조하고 있는 값들을 한 번에 불러오기 위한 방법
      - __html: `[pimarykey인스턴스].[foreignkey class명]_set.all`__
      - __py: `[pimarykey인스턴스].[foreignkey class명]_set.all()`__

