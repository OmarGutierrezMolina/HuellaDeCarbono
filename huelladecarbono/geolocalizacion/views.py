from django.shortcuts import render, get_object_or_404
from .models import Address
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from .forms import AddressForm
from django.urls import reverse_lazy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium

# Create your views here.
""" INTENTAR ELIMINAR ESTO
"""

class CalculateDistanceView(FormView):
    
    template_name = "geolocalizacion/main.html"
    form_class = AddressForm
    success_url = reverse_lazy('geolocalizacion:calculate_view')
    
    __mapa = folium.Map(width=800, height=500, location=(-33.43,-70.65))
    __destination = None
    __origin = None
    __distance = None
    __ip = None

    def form_valid(self, form):
        instance = form.save(commit=False)
        geolocator = Nominatim(user_agent="geolocalizacion")

        #IP FIJA DE PRUEBA
        ip = '190.215.153.175'
        CalculateDistanceView.__ip = get_ip_address(self.request)
        print("La dirección IP es:", CalculateDistanceView.__ip)
        country, city, l_lat, l_lon = get_geo(ip)

        ###TRANSFORMA LA CIUDAD EN ALGO MAS PEQUEÑO Y PIOLA
        location = geolocator.geocode(city)
        CalculateDistanceView.__origin = city['city']
        ### PUNTO DE ORIGEN, COORDENADAS
        pointA = (l_lat,l_lon)
        

        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        CalculateDistanceView.__destination = destination
        d_lat = destination.latitude
        d_lon = destination.longitude
        ###PUNTO DESTINO, COORDENADAS
        pointB=(d_lat,d_lon)

        ### DISTANCIA
        distance = round(geodesic(pointA,pointB).km,2)
        CalculateDistanceView.__distance = distance

        ### GENERACIÓN DE MAPA
        CalculateDistanceView.__mapa = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat,l_lon,d_lat,d_lon), zoom_start=get_zoom(distance))

        #MARCADOR PARA EL ORIGEN
        folium.Marker([l_lat,l_lon], tooltip="Click para ver más", popup=city['city'], icon=folium.Icon(color='purple')).add_to(CalculateDistanceView.__mapa)

        #MARCADOR PARA EL DESTINO
        folium.Marker([d_lat,d_lon], tooltip="Click para ver más", popup=destination, icon=folium.Icon(color='blue', icon='cloud')).add_to(CalculateDistanceView.__mapa)

        ### DIBUJAR LINEA ENTRE PUNTOS

        line = folium.PolyLine(locations=[pointA,pointB], weight=2, color='blue')

        CalculateDistanceView.__mapa.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Address, id=1)
        map=CalculateDistanceView.__mapa
        map= map._repr_html_()
        destination = CalculateDistanceView.__destination
        origin = CalculateDistanceView.__origin
        distance = CalculateDistanceView.__distance

        ### AGREGAR VARIABLES AL CONTEXTO
        context["map"] = map
        context["destination"] = destination
        context["origin"] = origin
        context["distance"] = distance
        return context
    
    