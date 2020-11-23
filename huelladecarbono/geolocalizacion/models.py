from django.db import models

# Create your models here.

class Address(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
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
