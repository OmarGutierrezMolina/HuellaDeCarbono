from django.shortcuts import render, get_object_or_404
from .models import Address
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from .forms import AddressForm
from django.urls import reverse_lazy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo


# Create your views here.
""" INTENTAR ELIMINAR ESTO
"""
def calculate_distance_view(request):
    obj = get_object_or_404(Address, id=1)
    context={
        'distance':obj,
    }
    return render(request, 'geolocalizacion/main.html', context)

class CalculateDistanceView(FormView):
    template_name = "geolocalizacion/main.html"
    form_class = AddressForm
    success_url = reverse_lazy('geolocalizacion:calculate_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Address, id=1)
        context["distance"] = obj
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        geolocator = Nominatim(user_agent="geolocalizacion")

        #IP FIJA DE PRUEBA
        ip = '190.215.153.175'
        country, city, l_lat, l_lon = get_geo(ip)

        ###TRANSFORMA LA CIUDAD EN ALGO MAS PEQUEÑO Y PIOLA
        location = geolocator.geocode(city)

        ### PUNTO DE ORIGEN, COORDENADAS
        pointA = (l_lat,l_lon)

        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        d_lat = destination.latitude
        d_lon = destination.longitude

        ###PUNTO DESTINO, COORDENADAS
        pointB=(d_lat,d_lon)
        distance = round(geodesic(pointA,pointB).km,2)

        instance.location = location
        instance.distance = distance
        instance.save()
        return super().form_valid(form)
    
    