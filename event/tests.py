import datetime
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from event.models import Event
from score.models import Score

# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            name="EventName",
            description="EventDescription is this",
            date=datetime.datetime.now(),
            place="Etsii",
            photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
            status="Abierto",
        )
        Event.objects.create(
            name="EventUpdate",
            description="EventUpdateDescription is this",
            date=datetime.datetime.now(),
            place="UpdateEtsii2",
            photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
            status="Abierto",
        )

    def test_event_create(self):
        event = Event.objects.get(name="EventName")
        self.assertEqual(event.description, "EventDescription is this")
        self.assertEqual(event.place, "Etsii")
        self.assertEqual(
            event.photo,
            "https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
        )
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
        self.assertEqual(
            event_nuevo.photo,
            "https://cdn.portalfruticola.com/2020/01/8dc0c7b7-maquinaria-campo-adobestock_188819540.jpeg",
        )
        self.assertEqual(event_nuevo.status, "En proceso")

    # Create tests

    def test_event_create_photo_incorrect(self):
        with self.assertRaises(Exception):
            event = Event(
                name="EventName",
                description="EventDescription is this",
                date=datetime.datetime.now(),
                place="Etsii",
                photo="Han Solo",
                status="Abierto",
            )
            event.save()

    def test_event_create_status_incorrect(self):
        with self.assertRaises(Exception):
            event = Event(
                name="EventName",
                description="EventDescription is this",
                date=datetime.datetime.now(),
                place="Etsii",
                photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                status="Han Solo",
            )
            event.save()

    def test_event_create_name_blank(self):
        with self.assertRaises(Exception):
            event = Event(
                description="EventDescription is this",
                date=datetime.datetime.now(),
                place="Etsii",
                photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                status="Abierto",
            )
            event.save()

    def test_event_create_description_blank(self):
        with self.assertRaises(Exception):
            event = Event(
                name="EventName",
                date=datetime.datetime.now(),
                place="Etsii",
                photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                status="Abierto",
            )
            event.save()

    def test_event_create_date_blank(self):
        with self.assertRaises(Exception):
            event = Event(
                name="EventName",
                description="EventDescription is this",
                place="Etsii",
                photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                status="Abierto",
            )
            event.save()

    def test_event_create_place_blank(self):
        with self.assertRaises(Exception):
            event = Event(
                name="EventName",
                description="EventDescription is this",
                date=datetime.datetime.now(),
                photo="https://img.freepik.com/foto-gratis/campo-cesped-nubes_1112-621.jpg?w=2000",
                status="Abierto",
            )
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


class EventDetailViewTest(StaticLiveServerTestCase):
    fixtures = ["fixtures/initial.json"]

    @classmethod
    def setUpClass(cls):
        super(EventDetailViewTest, cls).setUpClass()
        options = webdriver.ChromeOptions()
        options.headless = True
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(EventDetailViewTest, cls).tearDownClass()

    def test_title(self):
        events = Event.objects.all()

        titles = ["Innoweb - " + event.name for event in events]

        for i in range(len(titles)):
            self.browser.get(self.live_server_url + "/evento/" + str(events[i].id))

            assert self.browser.title == titles[i]

    def test_event_detail(self):
        events = Event.objects.all()
        for event in events:
            self.browser.get(self.live_server_url + "/evento/" + str(event.id))
            # find element by class name
            name = self.browser.find_element(By.CLASS_NAME, "title-event")
            image = self.browser.find_element(By.CLASS_NAME, "event-image")
            description = self.browser.find_element(By.CLASS_NAME, "event-description")

            self.assertEqual(name.text, event.name)
            self.assertEqual(image.get_attribute("src"), event.photo)
            self.assertIn(event.description, description.text)
            self.assertIn(event.place, description.text)
            self.assertIn(event.date.strftime("%d/%m/%Y a las %H:%M"), description.text)

            status = self.browser.find_element(By.ID, "status")
            self.assertEqual(status.text, event.status)

    def test_count_participants_in_event(self):
        events = Event.objects.all()
        for event in events:
            scores = Score.objects.filter(event=event).order_by("-value")
            self.browser.get(self.live_server_url + "/evento/" + str(event.id))
            rows = self.browser.find_elements(By.XPATH, "//table/tbody/tr")
            self.assertEqual(len(rows), len(scores))

    def test_participants_in_event(self):

        events = Event.objects.all()
        for event in events:
            scores = Score.objects.filter(event=event).order_by("-value")
            self.browser.get(self.live_server_url + "/evento/" + str(event.id))
            rows = self.browser.find_elements(By.XPATH, "//table/tbody/tr")
            for i in range(len(rows) - 1):
                TABLE_ROW = "//table/tbody/tr[" + str(i + 1) + "]"
                position = self.browser.find_element(By.XPATH, TABLE_ROW + "/td[1]")
                name = self.browser.find_element(By.XPATH, TABLE_ROW + "/td[2]")

                surnames = self.browser.find_element(By.XPATH, TABLE_ROW + "/td[3]")
                score = self.browser.find_element(By.XPATH, TABLE_ROW + "/td[4]")

                self.assertEqual(position.text, str(i + 1))
                self.assertEqual(name.text, scores[i].participant.first_name)
                self.assertEqual(surnames.text, scores[i].participant.last_name)
                self.assertEqual(score.text, str(scores[i].value))

    def test_participants_in_podium(self):
        events = Event.objects.all()
        for event in events:
            scores = Score.objects.filter(event=event).order_by("-value")
            self.browser.get(self.live_server_url + "/evento/" + str(event.id))
            if len(scores) > 0:
                for i in range(3):
                    username = (
                        self.browser.find_elements(By.CLASS_NAME, "podium-item")[i]
                        .find_element(By.CLASS_NAME, "podium-winner-wrapper")
                        .find_element(By.CLASS_NAME, "podium-winner")
                        .text
                    )
                    photo = (
                        self.browser.find_elements(By.CLASS_NAME, "podium-item")[i]
                        .find_element(By.CLASS_NAME, "podium-winner-wrapper")
                        .find_element(By.CLASS_NAME, "podium-photo")
                        .get_attribute("src")
                    )
                    position = (
                        self.browser.find_elements(By.CLASS_NAME, "podium-item")[i]
                        .find_element(By.CLASS_NAME, "podium-position")
                        .text
                    )

                    self.assertEqual(
                        username, scores[int(position) - 1].participant.get_username()
                    )
                    self.assertEqual(photo, scores[int(position) - 1].participant.photo)
