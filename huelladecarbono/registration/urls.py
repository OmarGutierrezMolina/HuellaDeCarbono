from django.urls import path
from .views import SignUpCreateView, ProfileUpdateView, EmailUpdateView, AddressUpdateView, MapView, load_comuna, load_provincia, check_address_exist

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email/', EmailUpdateView.as_view(), name='profile_email'),
    path('profile/address/<int:pk>/', AddressUpdateView.as_view(), name='profile_address'),
    path('profile/map/', MapView.as_view(), name='map_view'),
    path('ajax/load-comunas/', load_comuna, name='ajax_load_comunas'),
    path('ajax/load-provincias/', load_provincia, name='ajax_load_provincias'),
    path('address_exost/', check_address_exist, name='check_address_exist'),
]