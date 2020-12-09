from django.contrib import admin
from .models import Address, Destination, Conveyance
# Register your models here.

admin.site.register(Address)

admin.site.register(Destination)

admin.site.register(Conveyance)