from django.contrib.gis.geoip2 import GeoIP2
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from decimal import Decimal

#HELPER FUNCTIONS

def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon

def get_center_coordinates(latA, lonA, latB=None, lonB=None):
    cord = (latA,lonA)
    if latB:
        cord=[(latA+latB)/2,(lonA+lonB)/2]
    return cord

def get_zoom(distance):
    if distance >=100:
        return 9
    elif distance > 30 and distance < 100:
        return 10
    elif distance < 30 and distance > 10 :
        return 11
    else:
        return 12

def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTPS_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_geolocate(location):
    geolocator = Nominatim(user_agent="geolocalizacion")
    location_ = geolocator.geocode(location)
    l_lat = location_.latitude
    l_lon = location_.longitude
    l_point = (l_lat,l_lon)
    return location_, l_lat, l_lon, l_point

def get_distance(origin, destination):
    origin_ , o_lat, o_lon, o_point = get_geolocate(origin)
    destination_, d_lat, d_lon, d_point = get_geolocate(destination)
    distance = round(geodesic(o_point,d_point).km,2)
    return distance

def get_footprint(distance, footprint):
    footprint_ = Decimal(distance)*footprint
    return footprint_
    """
    if footprint == "Bicicleta":
        footprint_=distance*1.0
        print("La huella de carbono en bicicleta: ", footprint_)
        return footprint_
    elif footprint == "Transporte público":
        footprint_=distance*2.0
        print("La huella de carbono en Transporte público: ", footprint_)
        return footprint_
    elif footprint == "Vehículo privado":
        footprint_=distance*3.0
        print("La huella de carbono en Vehículo privado: ", footprint_)
        return footprint_
    """