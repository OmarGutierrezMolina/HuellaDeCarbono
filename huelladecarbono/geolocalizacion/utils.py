from django.contrib.gis.geoip2 import GeoIP2

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