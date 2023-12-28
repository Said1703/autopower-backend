from .views import InformationViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r"information", InformationViewSet)

urlpatterns = [
    path("", include(router.urls))
]
