from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30, null=True, blank=True)
    localidad = models.CharField(max_length=30, null=True, blank=True)
    provincia = models.CharField(max_length=30, null=True, blank=True)
    pais = models.CharField(max_length=30)
    institucion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)

