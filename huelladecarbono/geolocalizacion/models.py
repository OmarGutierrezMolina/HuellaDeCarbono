from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from registration.models import Profile

# Create your models here.

class Destination(models.Model):
    """Model definition for Destination."""

    # TODO: Define fields here
    name = models.CharField(null=True, max_length=100)
    addr = models.CharField(null=True,max_length=100)
    

    class Meta:
        """Meta definition for Destination."""

        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        """Unicode representation of Destination."""
        return f"{self.name}"

class Conveyance(models.Model):
    """Model definition for Conveyance."""

    # TODO: Define fields here
    name = models.CharField(null=True, max_length=50)
    footprint = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    class Meta:
        """Meta definition for Conveyance."""

        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'

    def __str__(self):
        """Unicode representation of Conveyance."""
        return f"{self.name}"


class Region(models.Model):
    """Model definition for Region."""

    # TODO: Define fields here
    region = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=3)
    capital = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Region."""

        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'

    def __str__(self):
        """Unicode representation of Region."""
        return f"{self.abreviatura} {self.region}"



class Provincia(models.Model):
    """Model definition for Provincia."""

    # TODO: Define fields here
    provincia = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Provincia."""

        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        """Unicode representation of Provincia."""
        return self.provincia


class Comuna(models.Model):
    """Model definition for Comuna."""

    # TODO: Define fields here
    comuna = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comuna."""

        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'

    def __str__(self):
        """Unicode representation of Comuna."""
        return self.comuna

class Address(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here


    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    location = models.CharField( max_length=200, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    destination = models.ForeignKey(Destination, null=True, on_delete=models.CASCADE)
    distance = models.DecimalField( max_digits=10, null=True, decimal_places=2)
    footprint = models.DecimalField( max_digits=10, null=True, decimal_places=2)
    conveyance = models.ForeignKey(Conveyance, verbose_name="Medio de transporte", null=True, on_delete=models.CASCADE)
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"Distancia de {self.location} a {self.destination} es de {self.distance} km, huella de {self.footprint}"

@receiver(post_save, sender=Profile)
def ensure_address_exists(sender, instance, **kwargs):
    #para que se ejecute solo una vez al crear perfil
    if kwargs.get('created',False):
        Address.objects.get_or_create(profile=instance)
