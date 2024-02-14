from django.urls import path, include
from api.views import TaskViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]