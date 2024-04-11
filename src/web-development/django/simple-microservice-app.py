# Create a Django project
django-admin startproject countries

# Create an app
python manage.py startapp currency_country

# Add the app to the INSTALLED_APPS setting in the project's settings.py file
INSTALLED_APPS = [
    ...
    'currency_country',
]

# Create a model for the countries
class Country(models.Model):
    name = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)

# Create a serializer for the Country model
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'currency')

# Create a viewset for the Country model
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# Register the viewset with the router
router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)

# Wire up the API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Run the development server
python manage.py runserver