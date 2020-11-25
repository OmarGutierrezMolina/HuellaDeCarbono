from django.db import models

# Create your models here.


class Place(models.Model):
    """Model definition for Place."""

    # TODO: Define fields here
    name = models.CharField( max_length=30)
    address = models.CharField( max_length=50)
    class Meta:
        """Meta definition for Place."""

        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        """Unicode representation of Place."""
        return self.name

class Restaurant(models.Model):
    """Model definition for Restaurant."""

    # TODO: Define fields here
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField(default = False)
    serves_pizza = models.BooleanField(default = False)
    serves_completitos = models.BooleanField(default =False)

    class Meta:
        """Meta definition for Restaurant."""

        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        """Unicode representation of Restaurant."""
        return self.place.name

