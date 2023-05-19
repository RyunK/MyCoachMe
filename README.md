# MyCoachMe
##DB 추가하는 법
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

User_data, Models >> main/models.py 에서 정의

Training_data, Train_video >> health_do/models.py 에서 정의
