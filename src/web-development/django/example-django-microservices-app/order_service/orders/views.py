import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.conf import settings


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data["user_id"]
        product_id = serializer.validated_data["product_id"]

        # Check if user exists
        user_url = f"{settings.USER_SERVICE_URL}/users/{user_id}/"
        user_response = requests.get(user_url)
        if user_response.status_code != 200:
            return Response(
                {"error": "Invalid user"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if product exists and is available
        product_url = f"{settings.PRODUCT_SERVICE_URL}/products/{product_id}/"
        product_response = requests.get(product_url)
        if product_response.status_code != 200:
            return Response(
                {"error": "Invalid product"}, status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
