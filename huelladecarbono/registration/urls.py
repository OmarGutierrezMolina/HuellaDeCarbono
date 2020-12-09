from django.urls import path
from .views import SignUpCreateView, ProfileUpdateView, EmailUpdateView, AddressUpdateView, MapView

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email/', EmailUpdateView.as_view(), name='profile_email'),
    path('profile/address/<int:pk>', AddressUpdateView.as_view(), name='profile_address'),
    path('profile/map/', MapView.as_view(), name='map_view')
]