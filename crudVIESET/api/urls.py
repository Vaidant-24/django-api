from django.urls import path,include
from api import views


urlpatterns = [
    path('studentapi/', views.student_api),
    path('studentapi/<int:id>', views.student_api)
]
