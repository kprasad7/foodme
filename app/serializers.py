# quicky_api/serializers.py
from rest_framework import serializers
from .models import Restaurant, MenuItem, RestaurantLocation


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_name', 'logo', 'on_near', 'zip_code', 'menu_items']

class RestaurantSerializernew(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_name',  'zip_code']


     

class RestaurantLocationSerializer(serializers.ModelSerializer):
    #restaurant = RestaurantSerializer()

    class Meta:
        model = RestaurantLocation
        fields = '__all__'        



class CustomRestaurantLocationSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializernew()

    class Meta:
        model = RestaurantLocation
        fields = '__all__'        

    

