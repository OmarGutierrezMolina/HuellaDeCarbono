from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Address(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField( max_length=200)
    destination = models.CharField( max_length=200)
    distance = models.DecimalField( max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return f"Distancia de {self.location} a {self.destination} es de {self.distance} km"
"""
@receiver(post_save, sender=User)
def ensure_address_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Address.object.get_or_create(user=instance)
        print("Se crea una dirección por cada usuario")

"""