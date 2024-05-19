from django.contrib import admin
from django.urls import path,include
from API import views
from API.views import CompanyViewSet,EmployeeViewSet,StudentViewSet,SchoolViewSet
from rest_framework import routers

router  = routers.DefaultRouter()
router.register(r'company',CompanyViewSet)
router.register(r'employee',EmployeeViewSet)
router.register(r'student',StudentViewSet)
router.register(r'school',SchoolViewSet)


urlpatterns = [
    path('home/',views.home,name='home'),
    path('',include(router.urls)),
]
