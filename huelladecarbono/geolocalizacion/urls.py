from django.urls import path
from .views import  CalculateDistanceView



geolocalizacion_pattern  =([
    path('', CalculateDistanceView.as_view(), name='calculate_view'),
], 'geolocalizacion')