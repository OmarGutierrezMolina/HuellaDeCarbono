from django.urls import path
from .views import SignUpCreateView, ProfileUpdateView, EmailUpdateView, AddressUpdateView

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/email/', EmailUpdateView.as_view(), name='profile_email'),
    path('profile/address/', AddressUpdateView.as_view(), name='profile_address'),
]