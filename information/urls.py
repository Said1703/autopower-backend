from .views import InformationViewSet, PaisesViewSet, AutosViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r"information", InformationViewSet)
router.register(r"paises", PaisesViewSet)
router.register(r"autos", AutosViewSet)

urlpatterns = [
    path("", include(router.urls))
]
