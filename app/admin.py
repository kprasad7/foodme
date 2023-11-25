# quicky_api/admin.py
from django.contrib import admin
from .models import Restaurant, MenuItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant_name', 'logo', 'on_near', 'zip_code')
    search_fields = ('restaurant_name', 'zip_code')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'thumbnail', 'type', 'restaurant')
    search_fields = ('name', 'restaurant__restaurant_name')  # Use double underscores to search related fields
    list_filter = ('type', 'restaurant__on_near')  # Filter by type and on_near
