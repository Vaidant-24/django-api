from django.urls import path,include
from api import views
from rest_framework import routers
from api.views import StudentModelViewSet

router = routers.DefaultRouter()
router.register('studentapi', StudentModelViewSet,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('login/', include('rest_framework.urls' , namespace= 'rest_framework'))
]
