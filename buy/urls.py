from django.urls import path, include
from .views import BuyViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'buy', BuyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
