from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=50, help_text="Introducce tu nombre")
    surname = models.CharField(max_length=50, help_text="Introduce tus apellidos")
    email = models.EmailField(max_length=50, help_text="Introduce tu correo")
    photo = models.URLField(max_length=200, help_text="Introduce la url de tu foto", blank=True)
    
    #Metadata
    class Meta:
        ordering = ['name']
    
    #Métodos
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email
    
    