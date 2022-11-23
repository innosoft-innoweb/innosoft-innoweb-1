import unittest
from django.test import TestCase
from participant.models import Participant

class ParticipantTestCase(TestCase):
    def setUp(self):
        Participant.objects.create(username = "Amekit", first_name = "Tomas", last_name = "Camero", email = "tcamerob@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
        Participant.objects.create(username = "UserUpdate", first_name = "UserUpdate", last_name = "UserUpdate", email ="UserUpdate@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
        
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
        self.assertEqual(1,Participant.objects.count())
    
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
        
    #Create Tests
        
    def test_participant_create_email_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "User3", first_name = "Tomas", last_name = "Camero", email = "tcamerob@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
          
    def test_participant_create_username_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "Amekit",first_name = "User2", last_name = "User2", email = "User2@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
    
    def test_participant_create_photo_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "User4", first_name = "User4", last_name = "User4", email = "User4@gmail.com", photo = "urlincorrect")
            
    def test_participant_create_email_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "User5", first_name = "User5", last_name = "User5", email = "User5gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
            
    def test_participant_create_username_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(first_name = "User6", last_name = "User6", email = "User6gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
            
    def test_participant_create_first_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "User7", last_name = "User7", email = "User7gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
            
    def test_participant_create_sur_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "User8", first_name="User8", last_name = "User8", email = "User8gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png") 
    
    def test_participant_create_email_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "User9", first_name="User9", last_name = "User9", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png") 
    
    def test_participant_create_photo_blank(self):
        with self.assertRaises(Exception):
             Participant.objects.create(username = "User10", first_name="User10", last_name = "User10", email = "User10@gmail.com") 

    #Update Tests
    
    def test_participant_update_email_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.update(username = "UserUpdate", first_name = "UserUpdate", last_name = "UserUpdate", email ="tcamerob@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
        
    def test_participant_update_username_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.update(username = "Amekit", first_name = "UserUpdate", last_name = "UserUpdate", email ="UserUpdate@gmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
    
    def test_participant_update_photo_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.update(username = "UserUpdate", first_name = "UserUpdate", last_name = "UserUpdate", email ="UserUpdate@gmail.com", photo = "noturl")
            
    def test_participant_update_email_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.update(username = "UserUpdate", first_name = "UserUpdate", last_name = "UserUpdate", email ="UserUpdate", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
        
    def test_participant_update_username_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(first_name = "UserUpdate", last_name = "UserUpdate", email = "UserUpdategmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
            
    def test_participant_update_first_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "UserUpdate", last_name = "UserUpdate", email = "UserUpdategmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png")
            
    def test_participant_update_sur_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "UserUpdate", first_name="UserUpdate", last_name = "UserUpdate", email = "UserUpdategmail.com", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png") 
    
    def test_participant_update_email_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(username = "UserUpdate", first_name="UserUpdate", last_name = "UserUpdate", photo = "https://cdn-icons-png.flaticon.com/512/149/149071.png") 
    
    def test_participant_update_photo_blank(self):
        with self.assertRaises(Exception):
             Participant.objects.create(username = "UserUpdate", first_name="UserUpdate", last_name = "UserUpdate", email = "User10@gmail.com") 

    
