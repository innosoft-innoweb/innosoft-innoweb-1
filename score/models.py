from django.db import models
import importlib

p = importlib.import_module("participant.models")
e = importlib.import_module("event.models")

# Create your models here.
class Score(models.Model):
    participant = models.ForeignKey(p.Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(e.Event, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(default=0, null=False, blank=False)

    #unique constraint for participant and event
    class Meta:
        unique_together = (('participant', 'event'),)  

    def __str__(self):
        return str(self.participant) + " - " + str(self.event) + " - " + str(self.value)
