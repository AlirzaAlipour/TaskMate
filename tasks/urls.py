from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .import views



router = DefaultRouter()
router.register("tasks", views.TaskViewset,basename='tasks')


urlpatterns = [
    path(r'', include(router.urls)),

]