from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    """Form definition for Address."""

    class Meta:
        """Meta definition for Addressform."""

        model = Address
        fields = ('destination',)
