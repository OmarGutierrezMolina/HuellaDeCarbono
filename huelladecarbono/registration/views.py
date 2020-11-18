from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import Profile
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
    

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_form.html"

    #para recuperar el objeto que se editara
    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdateView(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_email_form.html"

    #para recuperar la instancia del usuario a editar
    def get_object(self, queryset=None):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdateView, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        return form