from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Participant(AbstractUser):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    photo = models.URLField(max_length=200, help_text="Introduce la url de tu foto", blank=True, default="http://cdn.onlinewebfonts.com/svg/img_569204.png)

    