from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Participant(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(("first name"), max_length=150)
    last_name = models.CharField(("last name"), max_length=150)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    photo = models.URLField(max_length=200, help_text="Introduce la url de tu foto", blank=True, default="http://cdn.onlinewebfonts.com/svg/img_569204.png")

    
    def __str__(self):
        return self.username

    def get_name(self):
        return self.first_name 

    def get_last_name(self):
        return self.last_name

    def get_short(self):
        return self.first_name + " " + self.last_name[0] + "."

    def get_username(self):
        return self.username

    