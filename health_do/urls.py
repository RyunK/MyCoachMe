from django.urls import path

from . import views

#나중에는 ''부분에 'health_do/'가 놓여지게 될 것으로 예상
urlpatterns = [
    path('<int:video_id>/<str:user_id>', views.health_do, name='health_do'),
    path('<int:video_id>/<str:user_id>/loading', views.loading, name='loading'),
    path('<int:video_id>/<str:user_id>/makingreport', views.makeReport, name='makeReport'),
    # path('health_report/',views.health_report,name='health_report'),
    # path('upload/', views.upload_video, name='upload_video'),
]