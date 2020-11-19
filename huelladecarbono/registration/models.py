from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

#para que se borre lo que habia antes
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True, height_field=None, width_field=None, max_length=None)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True, max_length=200)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    #para que se ejecute solo una vez al crear perfil
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user=instance)
        #crea usuario y perfil enlazado