from django.urls import include, path
from rest_framework import routers
from products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
