from .views import BuyerViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'buyer', BuyerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
