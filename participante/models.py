from django.db import models

# Create your models here.
class Participante(models.Model):
    nombre = models.CharField(max_length=50, help_text="Introducce tu nombre")
    apellidos = models.CharField(max_length=50, help_text="Introduce tus apellidos")
    correo = models.EmailField(max_length=50, help_text="Introduce tu correo")
    foto = models.URLField(max_length=200, help_text="Introduce la url de tu foto")
    
    #Metadata
    class Meta:
        ordering = ['nombre']
    
    #Métodos
    def get_name(self):
        return self.nombre

    def get_surname(self):
        return self.apellidos

    def get_email(self):
        return self.correo
    
    