from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import Profile
from geolocalizacion.models import Address, Comuna, Provincia, Region
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm, AddressForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from decimal import Decimal
from django.http import JsonResponse

#IMPORTACIONES PARA GRÁFICAR MAPA

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geolocalizacion.utils import get_geo, get_center_coordinates, get_zoom, get_ip_address, get_geolocate, get_distance, get_footprint
import folium
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
        #print("EL USUARIO ES", self.request.user.profile.address)
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        #print("BLABLABLA: ", user)
        #new_address = Address.objects.create(location='NO REGISTRADA', destination='NO REGISTRADA', distance=0)
        #new_address.save()
        #print("DIRECCIÓN CREADA")
        #profile= Profile.objects.get_or_create(address=new_address)
        
        
        return profile
    """
    def form_valid(self, form):
        instance = form.save(commit=False)
        print("La distancia es: ", self.request.user.profile.address.distance)
        print("La huella es: ", self.request.user.profile.address.footprint)
        print("La huella del medio es: ", self.request.user.profile.address.conveyance.footprint)
        print("La fakin multiplicación da: ", Decimal(self.request.user.profile.address.distance)*self.request.user.profile.address.conveyance.footprint)
        instance.footprint = Decimal(self.request.user.profile.address.distance)*self.request.user.profile.address.conveyance.footprint
        print("El resultado asignado será: ", instance.footprint)
        instance.save()
        return super().form_valid(form)
        """
    

"""   
    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=self.request.user)

        args = {
            'profile':profile
        }
        return render(request, self.template_name, args)
"""
    



    
@method_decorator(login_required, name='dispatch')
class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('map_view')
    template_name = "registration/profile_update_address_form.html"
    def form_valid(self, form):
        instance = form.save(commit=False)
        location = f"{self.request.user.profile.address.calle} {self.request.user.profile.address.altura} {self.request.user.profile.address.comuna.comuna} {self.request.user.profile.address.region.region}"
        
        #CALCULAR LA DISTANCIA
        origin, o_lat, o_lon, o_point = get_geolocate(location)
        destination, d_lat, d_lon, d_point = get_geolocate(self.request.user.profile.address.destination.addr)
        distance = round(geodesic(o_point,d_point).km,2)


        #distance = get_distance(location, form.cleaned_data.get('destination')) NO SE PQ NO FUNCIONA AL LLAMAR LA FUNCION
        instance.distance = distance
        print("La distancia es de: ", distance)
        #print("La huella es: ", instance.footprint)
        #instance.footprint = get_footprint(distance, self.request.user.profile.address.conveyance.footprint)
        instance.save()
        return super().form_valid(form)


    """
    def get_object(self, queryset=None):
        
        
        return address
    
    def get_form(self, form_class=None):
        form = super(AddressUpdateView, self).get_form()
        form.fields['location'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección de origen'})
        form.fields['destination'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección de destino'})
        form.fields['distance'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Distancia recorrida'})
    """


@method_decorator(login_required, name='dispatch')
class MapView(TemplateView):
    template_name = "registration/profile_map.html"
    success_url = reverse_lazy('profile')
    """
    __mapa = folium.Map(width=800, height=500, location=(-33.43,-70.65))
    __origin = None
    __destination = None
    __distance = None
    
    def get(self, request, *args, **kwargs):
        print("La dirección es:", self.request.user.profile.address.location)
        print("El destino es:", self.request.user.profile.address.destination.addr)
        print("La huella es:", self.request.user.profile.address.conveyance.footprint)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    """
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mapa = folium.Map(width=800, height=500, location=(-33.43,-70.65))
        #MAPEO DE LAS VARIABLES
        geolocator = Nominatim(user_agent="registration")
        origin_ = f"{self.request.user.profile.address.calle} {self.request.user.profile.address.altura} {self.request.user.profile.address.comuna.comuna} {self.request.user.profile.address.region.region}"
        destination_ = self.request.user.profile.address.destination.addr
        #destination = geolocator.geocode(destination_)
        #GEOLOCALIZACIÓN DE ORIGEN
        origin, o_lat, o_lon, o_point = get_geolocate(origin_)
        destination, d_lat, d_lon, d_point = get_geolocate(destination_)
        distance = round(geodesic(o_point,d_point).km,2)
        

        #GENERACIÓN DE MAPA
        mapa = folium.Map(width=800, height=500, location=get_center_coordinates(o_lat,o_lon,d_lat,d_lon), zoom_start=get_zoom(distance))

        #MARCADOR PARA EL ORIGEN
        folium.Marker([o_lat,o_lon], tooltip="Click para ver más", popup=origin, icon=folium.Icon(color='purple')).add_to(mapa)

        #MARCADOR PARA EL DESTINO
        folium.Marker([d_lat,d_lon], tooltip="Click para ver más", popup=destination, icon=folium.Icon(color='blue', icon='cloud')).add_to(mapa)
        line = folium.PolyLine(locations=[o_point,d_point], weight=2, color='blue')
        mapa.add_child(line)
        """
        print("este es el origen: ", origin)
        print("este es el latitud: ", o_lat)
        print("este es la longitud: ", o_lon)
        print("este es el punto: ", o_point)
        
        origin = geolocator.geocode(origin_)
        o_lat = origin.latitude
        o_lon = origin.longitude
        o_point = (o_lat,o_lon)
        
        #GEOLOCALIZACOÓN DE DESTINO
        destination = geolocator.geocode(destination_)
        d_lat = destination.latitude
        d_lon = destination.longitude
        d_point = (d_lat,d_lon)
        #CALCULAR DISTANCIA
        distance = round(geodesic(o_point,d_point).km,2)

        
        #GENERACIÓN DE MAPA
        CalculateDistanceView.__mapa = folium.Map(width=800, height=500, location=get_center_coordinates(o_lat,o_lon,d_lat,d_lon), zoom_start=get_zoom(distance))

        #MARCADOR PARA EL ORIGEN
        folium.Marker([o_lat,o_lon], tooltip="Click para ver más", popup=origin, icon=folium.Icon(color='purple')).add_to(mapa)

        #MARCADOR PARA EL DESTINO
        folium.Marker([d_lat,d_lon], tooltip="Click para ver más", popup=destination, icon=folium.Icon(color='blue', icon='cloud')).add_to(mapa)
        line = folium.PolyLine(locations=[o_point,d_point], weight=2, color='blue')
        """
        mapa = mapa._repr_html_()
        
        
        context["map"] = mapa
        return context
    


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


def load_provincia(request):
    region_id = request.GET.get('region_id')
    provincias = Provincia.objects.filter(region_id=region_id).order_by('provincia')
    return render(request, 'registration/provincia_dropdown_list_options.html', {'provincias':provincias})

def load_comuna(request):
    provincia_id = request.GET.get('provincia_id')
    comunas = Comuna.objects.filter(provincia_id=provincia_id).order_by('comuna')
    return render(request, 'registration/comuna_dropdown_list_options.html', {'comunas':comunas})
    

