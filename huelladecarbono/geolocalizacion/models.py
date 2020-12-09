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


class Address(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here


    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    location = models.CharField( max_length=200, null=True)
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
