import unittest
from django.test import TestCase
from participant.models import Participant
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver


class ParticipantTestCase(TestCase):
    def setUp(self):
        Participant.objects.create(
            username="Amekit",
            first_name="Tomas",
            last_name="Camero",
            email="tcamerob@gmail.com",
            photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
        )
        Participant.objects.create(
            username="UserUpdate",
            first_name="UserUpdate",
            last_name="UserUpdate",
            email="UserUpdate@gmail.com",
            photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
        )

    def test_participant_create(self):
        participant = Participant.objects.get(username="Amekit")
        self.assertIsNotNone(participant)
        self.assertEqual(participant.username, "Amekit")
        self.assertEqual(participant.first_name, "Tomas")
        self.assertEqual(participant.last_name, "Camero")
        self.assertEqual(participant.email, "tcamerob@gmail.com")
        self.assertEqual(
            participant.photo, "https://cdn-icons-png.flaticon.com/512/149/149071.png"
        )

    def test_participant_delete(self):
        participant = Participant.objects.get(username="Amekit")
        participant.delete()
        self.assertEqual(1, Participant.objects.count())

    def test_participant_update(self):
        participant = Participant.objects.get(username="Amekit")
        participant.username = "Prueba"
        participant.first_name = "Prueba"
        participant.last_name = "Prueba"
        participant.email = "Prueba@gmail.com"
        participant.photo = "https://www.google.es"
        participant.save()
        participant_nuevo = Participant.objects.get(username="Prueba")
        self.assertIsNotNone(participant_nuevo)
        self.assertEqual(participant_nuevo.username, "Prueba")
        self.assertEqual(participant_nuevo.first_name, "Prueba")
        self.assertEqual(participant_nuevo.last_name, "Prueba")
        self.assertEqual(participant_nuevo.email, "Prueba@gmail.com")
        self.assertEqual(participant_nuevo.photo, "https://www.google.es")

    # Create Tests

    def test_participant_create_email_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User3",
                first_name="Tomas",
                last_name="Camero",
                email="tcamerob@gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_username_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="Amekit",
                first_name="User2",
                last_name="User2",
                email="User2@gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_photo_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User4",
                first_name="User4",
                last_name="User4",
                email="User4@gmail.com",
                photo="urlincorrect",
            )

    def test_participant_create_email_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User5",
                first_name="User5",
                last_name="User5",
                email="User5gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_username_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                first_name="User6",
                last_name="User6",
                email="User6gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_first_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User7",
                last_name="User7",
                email="User7gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_sur_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User8",
                first_name="User8",
                last_name="User8",
                email="User8gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_email_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User9",
                first_name="User9",
                last_name="User9",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_first_name_incorrect_lenght(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User10",
                first_name="UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
                last_name="User10",
                email="User10gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_last_name_incorrect_lenght(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User11",
                first_name="User11",
                last_name="UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
                email="User11gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_create_photo_incorrect_lenght(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="User12",
                first_name="User12",
                last_name="User12",
                email="User12gmail.com",
                photo="https://UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUcdn-icons-png.flaticon.com/512/149/149071.png",
            )

    # Update Tests

    def test_participant_update_email_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.update(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="tcamerob@gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_username_duplicated(self):
        with self.assertRaises(Exception):
            Participant.objects.update(
                username="Amekit",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdate@gmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_photo_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.update(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdate@gmail.com",
                photo="noturl",
            )

    def test_participant_update_email_incorrect(self):
        with self.assertRaises(Exception):
            Participant.objects.update(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdate",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_username_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdategmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_first_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdategmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_sur_name_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdategmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_email_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_photo_blank(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="User10@gmail.com",
            )

    def test_participant_update_first_name_incorrect_lenght(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                first_name="UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
                last_name="UserUpdate",
                email="UserUpdategmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_last_name_incorrect_lenght(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
                email="UserUpdategmail.com",
                photo="https://cdn-icons-png.flaticon.com/512/149/149071.png",
            )

    def test_participant_update_photo_incorrect_lenght(self):
        with self.assertRaises(Exception):
            Participant.objects.create(
                username="UserUpdate",
                first_name="UserUpdate",
                last_name="UserUpdate",
                email="UserUpdategmail.com",
                photo="https://UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUcdn-icons-png.flaticon.com/512/149/149071.png",
            )


class ProfileViewTest(StaticLiveServerTestCase):
    fixtures = ["fixtures/initial.json"]

    @classmethod
    def setUpClass(cls):
        super(ProfileViewTest, cls).setUpClass()
        options = webdriver.ChromeOptions()
        options.headless = True
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(ProfileViewTest, cls).tearDownClass()

    def test_title(self):

        PORT = self.live_server_url.split(":")[2]
        titles = [
            "Innoweb - ezegonmac",
            "Innoweb - tomcambor",
            "Innoweb - juasaljur",
            "Innoweb - ismperort",
            "Innoweb - migromarj",
        ]

        self.browser.get(self.live_server_url)

        for i in range(2, 7):
            self.browser.get("http://localhost:" + PORT + "/participante/" + str(i))
            assert titles[i - 2] == self.browser.title

    def test_participant_name(self):

        PORT = self.live_server_url.split(":")[2]
        names = [
            "Ezequiel González",
            "Tomás Camero",
            "Juan Salado",
            "Ismael Pérez",
            "Miguel Romero",
        ]

        self.browser.get(self.live_server_url)

        for i in range(2, 7):

            self.browser.get("http://localhost:" + PORT + "/participante/" + str(i))
            participant_name = self.browser.find_element(
                By.CSS_SELECTOR, "h3.user-name"
            ).text

            assert names[i - 2] == participant_name

    def test_participant_total_points(self):

        PORT = self.live_server_url.split(":")[2]
        total_points = ["356", "352", "265", "376", "181"]

        self.browser.get(self.live_server_url)

        for i in range(2, 7):

            self.browser.get("http://localhost:" + PORT + "/participante/" + str(i))
            participant_total_points = self.browser.find_element(
                By.CSS_SELECTOR, "h1.user-points-number"
            ).text

            assert total_points[i - 2] == participant_total_points

    def test_participant_total_events(self):

        PORT = self.live_server_url.split(":")[2]
        total_events = ["5", "4", "3", "5", "4"]

        self.browser.get(self.live_server_url)

        for i in range(2, 7):

            self.browser.get("http://localhost:" + PORT + "/participante/" + str(i))
            participant_total_events = self.browser.find_element(
                By.CSS_SELECTOR, "h2.user-events-number"
            ).text

            assert total_events[i - 2] == participant_total_events

    def test_participant_events(self):

        PORT = self.live_server_url.split(":")[2]

        events_ezegonmac = [
            {"name": "Torneo Futbolín 2022", "position": "#1", "points": "96"},
            {"name": "Torneo Ajedrez 2022", "position": "#1", "points": "90"},
            {"name": "Torneo Brawhalla 2022", "position": "#2", "points": "70"},
            {"name": "Torneo de Cartas 2022", "position": "#2", "points": "68"},
            {"name": "Escape Room 2022", "position": "#3", "points": "32"},
        ]

        events_tomcambor = [
            {"name": "Torneo Brawhalla 2022", "position": "#1", "points": "100"},
            {"name": "Torneo Futbolín 2022", "position": "#2", "points": "94"},
            {"name": "Torneo de Bolos 2022", "position": "#1", "points": "93"},
            {"name": "Torneo Ajedrez 2022", "position": "#3", "points": "65"},
        ]

        events_juasaljur = [
            {"name": "Gymkhana Innosoft 2022", "position": "#1", "points": "97"},
            {"name": "Escape Room 2022", "position": "#1", "points": "95"},
            {"name": "Torneo Futbolín 2022", "position": "#3", "points": "73"},
        ]

        events_ismperort = [
            {"name": "Torneo de Cartas 2022", "position": "#1", "points": "97"},
            {"name": "Gymkhana Innosoft 2022", "position": "#2", "points": "88"},
            {"name": "Torneo de Bolos 2022", "position": "#2", "points": "78"},
            {"name": "Torneo Ajedrez 2022", "position": "#2", "points": "67"},
            {"name": "Escape Room 2022", "position": "#2", "points": "46"},
        ]

        events_migromarj = [
            {"name": "Torneo Brawhalla 2022", "position": "#3", "points": "64"},
            {"name": "Gymkhana Innosoft 2022", "position": "#3", "points": "50"},
            {"name": "Torneo de Cartas 2022", "position": "#3", "points": "47"},
            {"name": "Torneo de Bolos 2022", "position": "#3", "points": "20"},
        ]

        all_participants_events = [
            events_ezegonmac,
            events_tomcambor,
            events_juasaljur,
            events_ismperort,
            events_migromarj,
        ]

        self.browser.get(self.live_server_url)

        for i in range(2, 7):

            participant_events = all_participants_events[i - 2]

            self.browser.get("http://localhost:" + PORT + "/participante/" + str(i))
            participant_events_table = self.browser.find_elements(By.CSS_SELECTOR, "tr")

            for event in range(1, len(participant_events_table)):
                event_info = participant_events_table[event].find_elements(
                    By.CSS_SELECTOR, "td"
                )
                assert participant_events[event - 1]["name"] == event_info[0].text
                assert participant_events[event - 1]["position"] == event_info[1].text
                assert participant_events[event - 1]["points"] == event_info[2].text
