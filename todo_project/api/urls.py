from rest_framework import routers
from django.urls import path, include
from .views import TaskViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
     path('', views.home, name='home'),    # 👈 homepage
    path('api/', include(router.urls)),  # 👈 API endpoints
]
