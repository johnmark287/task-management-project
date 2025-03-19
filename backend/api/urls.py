from django.urls import path, include
from  . import views
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'tasks', views.TaskViewSet, basename="tasks")

urlpatterns = [
  path("", views.index, name="index"),
  path("v1/", include(router.urls)),
]
