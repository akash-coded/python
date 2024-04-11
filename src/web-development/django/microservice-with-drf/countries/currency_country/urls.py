from django.urls import path
from .views import country

urlpatterns = [path("country/", country, name="countries")]
