import datetime
from django.test import TestCase
from event.models import Event
from participant.models import Participant
from score.models import Score

class ScoreTestCase(TestCase):

    def setUp(self):
        self.e1 = Event.objects.create(
                            name="Evento 1",
                            description="Esta es la descripción del evento",
                            date=datetime.datetime.now(),
                            place="Etsii",
                            photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                            status="Abierto"
                            )
        self.p1 = Participant.objects.create(username = "juanperez", first_name="Juan", last_name="Perez", email="juanperez@gmail.com")
        self.score = Score.objects.create(participant=self.p1, event=self.e1, value=100)

        self.e2 = Event.objects.create(
                            name="Evento 2",
                            description="Esta es la descripción del evento",
                            date=datetime.datetime.now(),
                            place="Etsii",
                            photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                            status="Abierto"
                            )
        self.p2 = Participant.objects.create(username = "juanperez2", first_name="Juan2", last_name="Perez2", email="juanperez2@gmail.com")

    def tearDown(self):
        super().tearDown()
        self.e1 = None
        self.p1 = None
        self.score = None
        self.e2 = None
        self.p2 = None

    def test_score_create(self):
        self.score = Score.objects.create(participant=self.p2, event=self.e2, value=100)

        self.assertEqual(self.score.value, 100)
        self.assertEqual(self.score.participant, self.p2)
        self.assertEqual(self.score.event, self.e2)

    def test_score_delete(self):
        self.score.delete()

        self.assertEqual(Score.objects.count(), 0)

    def test_score_update(self):
        new_e = Event.objects.get(name="Evento 2")
        new_p = Participant.objects.get(username="juanperez2")
        new_value = 500

        self.score.participant = new_p
        self.score.event = new_e
        self.score.value = new_value
        self.score.save()
        updated_score = Score.objects.get(participant=new_p, event=new_e)

        self.assertIsNotNone(updated_score)
        self.assertEqual(updated_score.participant, new_p)
        self.assertEqual(updated_score.event, new_e)
        self.assertEqual(updated_score.value, new_value)

    def test_score_create_value_zero(self):
        self.score = Score.objects.create(participant=self.p2, event=self.e2, value=0)
        self.score.save()

    def test_score_create_event_blank(self):
        with self.assertRaises(Exception):
            score2 = Score.objects.create(participant=self.p2, value=100)
            score2.save()

    def test_score_create_participant_blank(self):
        with self.assertRaises(Exception):
            score2 = Score.objects.create(event=self.e2, value=100)
            score2.save()

    def test_score_create_value_blank(self):
        with self.assertRaises(Exception):
            score2 = Score.create(event=self.e2, participant=self.p2)
            score2.save()

    def test_score_create_value_negative(self):
        with self.assertRaises(Exception):
            score2 = Score.objects.create(participant=self.p2, event=self.e2, value=-100)
            score2.save()

    def test_score_create_unique_event_participant(self):
        with self.assertRaises(Exception):
            score2 = Score.objects.create(participant=self.p1, event=self.e1, value=100)
            score2.save()

    def test_score_participant_on_delete(self):
        with self.assertRaises(Exception):
            self.p1.delete()
            self.score = Score.objects.get(participant=self.p1, event=self.e1)

    def test_score_event_on_delete(self):
        with self.assertRaises(Exception):
            self.e1.delete()
            self.score = Score.objects.get(participant=self.p1, event=self.e1)
