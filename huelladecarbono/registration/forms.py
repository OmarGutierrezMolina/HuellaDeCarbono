from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from geolocalizacion.models import Address
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(help_text="Requerido, 254 caracteres como máximo y debe ser válido", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    #Para validar mail unico
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe en la base de datos")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['avatar','bio','link']
        exclude = ['address',]
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3','placeholder':'Enlace'})
        }

class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ['location','destination','conveyance','footprint']
        widgets = {
            'location' : forms.TextInput(attrs={'class':'form-control mt-3','placeholder':'Origen'}),
            'destination': forms.Select(attrs={'class':'form-control mt-3','placeholder':'Destino'}),
            
            'conveyance': forms.Select(attrs={'class':'form-control mt-3','placeholder':'Medio de transporte'}),
        }



class EmailForm(forms.ModelForm):
    email = forms.EmailField(help_text="Requerido, 254 caracteres como máximo y debe ser válido", required=True)
    class Meta:
        model = User
        fields = ['email']

    #Para validar mail unico
    def clean_email(self):
        email=self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya existe en la base de datos")
        return email
