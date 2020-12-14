from django.contrib import admin
from .models import Address, Destination, Conveyance, Region, Provincia, Comuna
# Register your models here.

admin.site.register(Address)

admin.site.register(Destination)

admin.site.register(Conveyance)

admin.site.register(Region)

admin.site.register(Provincia)

admin.site.register(Comuna)