
from django.urls import include, path

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auto_park', include('apps.auto_parks.urls')),
]
