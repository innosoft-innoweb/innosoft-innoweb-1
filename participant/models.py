from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Participant(AbstractUser):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(("first name"), max_length=150)
    last_name = models.CharField(("last name"), max_length=150)
    email = models.EmailField(unique=True)
    photo = models.URLField(max_length=200, help_text="Introduce la url de tu foto", blank=True)
    