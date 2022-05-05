from django.urls import path,include
from .views import OrderViewSet,DeliveryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders',OrderViewSet,basename="order")
router.register(r'deliveries',DeliveryViewSet,basename="delivery")


urlpatterns = [
    path('',include(router.urls)),
]