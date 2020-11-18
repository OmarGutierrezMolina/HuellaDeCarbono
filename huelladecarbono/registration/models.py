from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True, height_field=None, width_field=None, max_length=None)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True, max_length=200)