from django.urls import path
from .views import calculate_distance_view, CalculateDistanceView



geolocalizacion_pattern  =([
    path('', CalculateDistanceView.as_view(), name='calculate_view'),
], 'geolocalizacion')