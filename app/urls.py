from django.urls import path
from .views import RestaurantListView, RestaurantLocationById,RestaurantLocationListView,RestaurantDetailView, RestaurantByZipcodeView, logo_image, MenuItemCreateView,MenuItemsByRestaurantView, RestaurantLocationListCreateView
from django.conf import settings
from django.conf.urls.static import static
from .views import  logo_image

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<str:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/zipcode/<str:zip_code>/', RestaurantByZipcodeView.as_view(), name='restaurant-by-zipcode'),
    path('logo/<str:logo>/', logo_image, name='logo_image'),  # New URL pattern for logo images
    path('menuitems/', MenuItemCreateView.as_view(), name='menuitem-create'),
    path('menuitems/restaurant/<restaurant_id>/', MenuItemsByRestaurantView.as_view(), name='menuitems-by-restaurant'),
    path('restaurant-locations/', RestaurantLocationListCreateView.as_view(), name='restaurant-location-list-create'),
    path('restaurant-list/', RestaurantLocationListView.as_view(), name='restaurant-location-list-create'),
    path('restaurant-list/<str:pk>/', RestaurantLocationById.as_view(), name='book-detail'),

    
]




# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

