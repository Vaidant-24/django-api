from django.urls import path,include
from api import views
from rest_framework import routers
from api.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'studentapi', StudentViewSet,basename='student')

urlpatterns = [
    path('',include(router.urls)),
]
