import datetime
import unittest
from django.test import TestCase

from .models import Event
# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="EventName", description="EventDescription is this", date=datetime.datetime.now(), place="Etsii", photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Abierto")
        Event.objects.create(name="EventUpdate", description="EventUpdateDescription is this", date=datetime.datetime.now(), place="UpdateEtsii2", photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Abierto")
    

    def test_event_create(self):
        event = Event.objects.get(name="EventName")
        self.assertEqual(event.description, "EventDescription is this")
        self.assertEqual(event.place, "Etsii")
        self.assertEqual(event.photo, "https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000")
        self.assertEqual(event.status, "Abierto")
    
    def test_event_delete(self):
        event = Event.objects.get(name="EventName")
        event.delete()
        self.assertEqual(Event.objects.count(), 1)
    
    def test_event_update(self):
        event = Event.objects.get(name="EventName")
        event.name = "NewEventName"
        event.description = "NewDescription"
        event.place = "NewPlace"
        event.photo = "https://cdn.portalfruticola.com/2020/01/8dc0c7b7-maquinaria-campo-adobestock_188819540.jpeg"
        event.status = "En proceso"
        event.save()
        event_nuevo = Event.objects.get(name="NewEventName")
        self.assertIsNotNone(event_nuevo)
        self.assertEqual(event_nuevo.name, "NewEventName")
        self.assertEqual(event_nuevo.description, "NewDescription")
        self.assertEqual(event_nuevo.place, "NewPlace")
        self.assertEqual(event_nuevo.photo, "https://cdn.portalfruticola.com/2020/01/8dc0c7b7-maquinaria-campo-adobestock_188819540.jpeg")
        self.assertEqual(event_nuevo.status, "En proceso")
    
    #Create tests

    def test_event_create_photo_incorrect(self):
        with self.assertRaises(Exception):        
            event = Event(name="EventName", description="EventDescription is this", date=datetime.datetime.now(), place="Etsii", photo="Han Solo", status="Abierto")
            event.save()

    def test_event_create_status_incorrect(self):
        with self.assertRaises(Exception): 
            event = Event(name="EventName", description="EventDescription is this", date=datetime.datetime.now(), place="Etsii", photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Han Solo")
            event.save()
    
    def test_event_create_name_blank(self):
        with self.assertRaises(Exception): 
            event = Event(description="EventDescription is this", date=datetime.datetime.now(), place="Etsii", photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Abierto")
            event.save()
    
    def test_event_create_description_blank(self):
        with self.assertRaises(Exception): 
            event = Event(name="EventName", date=datetime.datetime.now(), place="Etsii", photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Abierto")
            event.save()

    def test_event_create_date_blank(self):
        with self.assertRaises(Exception): 
            event = Event(name="EventName", description="EventDescription is this", place="Etsii", photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Abierto")
            event.save()

    def test_event_create_place_blank(self):
        with self.assertRaises(Exception): 
            event = Event(name="EventName", description="EventDescription is this", date=datetime.datetime.now(), photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000", status="Abierto")
            event.save()

    # #Update tests
    def test_event_update_photo_incorrect(self):
        with self.assertRaises(Exception):        
            event = Event.objects.get(name="EventUpdate")
            event.photo = "Han Solo"
            event.save()
    
    def test_event_update_status_incorrect(self):
        with self.assertRaises(Exception): 
            event = Event.objects.get(name="EventUpdate")
            event.status = "Han Solo"
            event.save()
    
    def test_event_update_name_blank(self):
        with self.assertRaises(Exception): 
            event = Event.objects.get(name="EventUpdate")
            event.name = ""
            event.save()
    
    def test_event_update_description_blank(self):
        with self.assertRaises(Exception): 
            event = Event.objects.get(name="EventUpdate")
            event.description = ""
            event.save()
    
    def test_event_update_date_blank(self):
        with self.assertRaises(Exception): 
            event = Event.objects.get(name="EventUpdate")
            event.date = ""
            event.save()
    
    def test_event_update_place_blank(self):
        with self.assertRaises(Exception): 
            event = Event.objects.get(name="EventUpdate")
            event.place = ""
            event.save()
    
    