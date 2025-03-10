from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
    path('set_client/', views.set_client, name='set_client'),
]
