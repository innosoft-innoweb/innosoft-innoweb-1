from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100, help_text="Nombre del evento")
    description = models.TextField()
    date = models.DateTimeField()
    place = models.CharField(max_length=100, help_text="Lugar del evento")
    photo = models.URLField(max_length=10000, help_text="Url de la imagen del evento")
    status = models.CharField(choices=[('Abierto','Abierto'),('En proceso','En proceso'), ('Finalizado', 'Finalizado')], default='Abierto', max_length=100)
    

    def __str__(self):
        return self.name