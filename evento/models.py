from django.db import models

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del evento")
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100, help_text="Lugar del evento")
    imagen = models.URLField(max_length=10000, help_text="Url de la imagen del evento")
    estado = models.CharField(choices=[('Abierto','Abierto'),('En proceso','En proceso'), ('Finalizado', 'Finalizado')], default='Abierto', max_length=100)
    

    def __str__(self):
        return self.nombre