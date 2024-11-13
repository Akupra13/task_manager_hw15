from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet
#  для ViewSet
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)
#  для категорий и задач
urlpatterns = [
    path('', include(router.urls)),
]
