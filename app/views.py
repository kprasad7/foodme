from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, MenuItem, RestaurantLocation
from .serializers import RestaurantSerializer, MenuItemSerializer, RestaurantLocationSerializer, CustomRestaurantLocationSerializer

from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.shortcuts import get_object_or_404
import os
from rest_framework.views import APIView


class RestaurantListView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantByZipcodeView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        zip_code = self.kwargs['zip_code']
        restaurants = Restaurant.objects.filter(zip_code=zip_code)
        return restaurants

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"restaurants": serializer.data})

def logo_image(request, logo):
    logo_path = os.path.join(settings.MEDIA_ROOT, 'restaurant_logos', logo)
    try:
        with open(logo_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')  # Assuming logos are in PNG format
    except FileNotFoundError:
        return HttpResponseNotFound("Logo not found")
    


class MenuItemCreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    

class MenuItemsByRestaurantView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return MenuItem.objects.filter(restaurant__id=restaurant_id)    
    

class RestaurantLocationListCreateView(generics.ListCreateAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = RestaurantLocationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

class RestaurantLocationListView(generics.ListAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = CustomRestaurantLocationSerializer


class RestaurantLocationById(generics.RetrieveAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = CustomRestaurantLocationSerializer








