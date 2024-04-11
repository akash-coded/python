from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer


@api_view(["GET", "POST"])
def country(request):

    if request.method == "GET":  # user requesting data
        snippets = Country.objects.all()
        serializer = CountrySerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":  # user posting data
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
