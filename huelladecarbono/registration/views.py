from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail

# Create your views here.

class SignUpCreateView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    def get_success_url(self):
        return reverse_lazy('login') +'?register'

    ###para dar estilo al formulario en ejecucion, la gracia es no pisar la logica de validación propia de django
    def get_form(self, form_class=None):
        form = super(SignUpCreateView, self).get_form()
        #Modificar el formulario
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repetir Contraseña'})
        return form
    
   