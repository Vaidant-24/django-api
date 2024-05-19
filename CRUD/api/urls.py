from django.urls import path,include
from api import views


urlpatterns = [
    path('stucreate/', views.student_create,name='stucreate'),
    path('studetail/', views.student_detail,name='studetail'),
    path('stuupdate/', views.student_update,name='stuupdate'),
    path('studelete/', views.student_delete,name='studelete'),
]
