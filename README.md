# MyCoachMe
## DB 추가하는 법
1. 각 앱의 models.py 내용 복사 및 붙여넣기
2. 터미널, 프로젝트 경로에서 다음 명령어 사용

```
py manage.py makemigration main
py manage.py makemigration health_do
```

그 후 다음 명령어 사용
```
py manage.py migrate
```
참고 : DB 구조 시트
https://docs.google.com/spreadsheets/d/1bEPFfrn552N6-JXK5pWC_CzyTg8nL3VsW77ZMLw0NTI/edit?usp=sharing

## admin 페이지에서 DB 보는 법

1. main/admin.py에 다음 내용 추가
```python
from .models import User_data
from .models import Models

admin.site.register(User_data)
admin.site.register(Models)
```

2. health_do/admin.py 페이지에 다음 내용 추가

```python
from .models import Train_video
from .models import Training_data

admin.site.register(Train_video)
admin.site.register(Training_data)
```

User_data, Models >> main/models.py 에서 정의

Training_data, Train_video >> health_do/models.py 에서 정의
