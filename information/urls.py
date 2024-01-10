from .views import InformationViewSet, PaisesViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r"information", InformationViewSet)
router.register(r"paises", PaisesViewSet)

urlpatterns = [
    path("", include(router.urls))
]
