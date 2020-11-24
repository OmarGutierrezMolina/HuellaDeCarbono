from django.urls import path
from .views import  CalculateDistanceView, HuellaCarbono



geolocalizacion_pattern  =([
    path('', CalculateDistanceView.as_view(), name='calculate_view'),
    path('huellaCarbono/', HuellaCarbono.as_view(), name='huellacarbono')
], 'geolocalizacion')