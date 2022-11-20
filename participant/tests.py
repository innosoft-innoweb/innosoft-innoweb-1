import unittest
from django.test import TestCase
from participant.models import Participant

class ParticipantTestCase(TestCase):
    def setUp(self):
        Participant.objects.create(username = "Amekit", first_name = "Tomas", last_name = "Camero", email = "tcamerob@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
        
    def test_participant_create(self):
        participant = Participant.objects.get(username = "Amekit")
        self.assertIsNotNone(participant)
        self.assertEqual(participant.username,"Amekit")
        self.assertEqual(participant.first_name,"Tomas")
        self.assertEqual(participant.last_name,"Camero")
        self.assertEqual(participant.email,"tcamerob@gmail.com")
        self.assertEqual(participant.photo,"https://cdn-icons-png.flaticon.com/512/149/149071.png")
        
    def test_participant_delete(self):
        participant = Participant.objects.get(username="Amekit")
        participant.delete()
        self.assertEqual(0,len(Participant.objects.all()))
    
    def test_participant_update(self):
        participant = Participant.objects.get(username="Amekit")
        participant.username="Prueba"
        participant.first_name="Prueba"
        participant.last_name="Prueba"
        participant.email="Prueba@gmail.com"
        participant.photo="https://www.google.es"
        participant.save()
        participant_nuevo = Participant.objects.get(username="Prueba")
        self.assertIsNotNone(participant_nuevo)
        self.assertEqual(participant_nuevo.username,"Prueba")
        self.assertEqual(participant_nuevo.first_name,"Prueba")
        self.assertEqual(participant_nuevo.last_name,"Prueba")
        self.assertEqual(participant_nuevo.email,"Prueba@gmail.com")
        self.assertEqual(participant_nuevo.photo,"https://www.google.es")
        
    @unittest.expectedFailure   
    def test_participant_create_username_negative(self):
        Participant.objects.create(username = "Amekit",first_name = "Tomas", last_name = "Camero", email = "tcamerob@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
        
   
        
        
 

    
