# api/models.py
from django.db import models

class Restaurant(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='restaurant_logos/')  # Adjust the upload_to path as needed
    on_near = models.IntegerField(choices=[(1, 'On-Campus'), (2, 'Near-Campus')])
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return self.restaurant_name
    
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='menuitem_thumbnails/')  # Adjust the upload_to path as needed
    type = models.CharField(max_length=10, choices=[('veg', 'Vegetarian'), ('non-veg', 'Non-Vegetarian'), ('vegan', 'Vegan')])
    
    def __str__(self):
        return self.name
    
class RestaurantLocation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    website = models.URLField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    state_name = models.CharField(max_length=2)
    city_name = models.CharField(max_length=100)
    hours_interval = models.TextField()
    cuisine_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.restaurant.restaurant_name} - {self.address}, {self.city_name}, {self.state_name} {self.zip_code}"    