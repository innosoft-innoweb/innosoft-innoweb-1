from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class ProfileViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']

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
        titles = ["Innoweb - ezegonmac", "Innoweb - tomcambor","Innoweb - juasaljur","Innoweb - ismperort","Innoweb - migromarj"]

        self.browser.get(self.live_server_url)

        for i in range(2,7):
            self.browser.get("http://localhost:" + PORT + "/participante/"+str(i))
            assert titles[i-2] == self.browser.title

    def test_participant_name(self):

        PORT = self.live_server_url.split(":")[2]
        names = ["Ezequiel González", "Tomás Camero","Juan Salado","Ismael Pérez","Miguel Romero"]

        self.browser.get(self.live_server_url)

        for i in range(2,7):
            
            self.browser.get("http://localhost:" + PORT + "/participante/"+str(i))
            participant_name = self.browser.find_element(By.CSS_SELECTOR, 'h3.user-name').text

            assert names[i-2] == participant_name

    def test_participant_total_points(self):

        PORT = self.live_server_url.split(":")[2]
        total_points = ["356", "352", "265", "376", "181"]

        self.browser.get(self.live_server_url)

        for i in range(2,7):
            
            self.browser.get("http://localhost:" + PORT + "/participante/"+str(i))
            participant_total_points = self.browser.find_element(By.CSS_SELECTOR, 'h1.user-points-number').text
          
            assert total_points[i-2] == participant_total_points

    def test_participant_total_events(self):

        PORT = self.live_server_url.split(":")[2]
        total_events = ["5", "4", "3", "5", "4"]

        self.browser.get(self.live_server_url)

        for i in range(2,7):
            
            self.browser.get("http://localhost:" + PORT + "/participante/"+str(i))
            participant_total_events = self.browser.find_element(By.CSS_SELECTOR, 'h2.user-events-number').text

            assert total_events[i-2] == participant_total_events

    def test_participant_events(self):

        PORT = self.live_server_url.split(":")[2]

        events_ezegonmac = [{"name": "Torneo Futbolín 2022","position": "#1","points": "96"},
                            {"name": "Torneo Ajedrez 2022","position": "#1","points": "90"},
                            {"name": "Torneo Brawhalla 2022","position": "#2","points": "70"},
                            {"name": "Torneo de Cartas 2022","position": "#2","points": "68"},
                            {"name": "Escape Room 2022","position": "#3","points": "32"}]

        events_tomcambor = [{"name": "Torneo Brawhalla 2022","position": "#1","points": "100"},
                            {"name": "Torneo Futbolín 2022","position": "#2","points": "94"},
                            {"name": "Torneo de Bolos 2022","position": "#1","points": "93"},
                            {"name": "Torneo Ajedrez 2022","position": "#3","points": "65"}]

        events_juasaljur = [{"name": "Gymkhana Innosoft 2022","position": "#1","points": "97"},
                            {"name": "Escape Room 2022","position": "#1","points": "95"},
                            {"name": "Torneo Futbolín 2022","position": "#3","points": "73"}]

        events_ismperort = [{"name": "Torneo de Cartas 2022","position": "#1","points": "97"},
                            {"name": "Gymkhana Innosoft 2022","position": "#2","points": "88"},
                            {"name": "Torneo de Bolos 2022","position": "#2","points": "78"},
                            {"name": "Torneo Ajedrez 2022","position": "#2","points": "67"},
                            {"name": "Escape Room 2022","position": "#2","points": "46"},]

        events_migromarj = [{"name": "Torneo Brawhalla 2022","position": "#3","points": "64"},
                            {"name": "Gymkhana Innosoft 2022","position": "#3","points": "50"},
                            {"name": "Torneo de Cartas 2022","position": "#3","points": "47"},
                            {"name": "Torneo de Bolos 2022","position": "#3","points": "20"}] 

        all_participants_events = [events_ezegonmac, events_tomcambor, events_juasaljur, events_ismperort, events_migromarj]

        self.browser.get(self.live_server_url)

        for i in range(2,7):
            
            participant_events = all_participants_events[i-2]

            self.browser.get("http://localhost:" + PORT + "/participante/"+str(i))
            participant_events_table = self.browser.find_elements(By.CSS_SELECTOR, 'tr')

            for event in range(1, len(participant_events_table)):
                event_info = participant_events_table[event].find_elements(By.CSS_SELECTOR, 'td')
                assert participant_events[event-1]["name"] == event_info[0].text
                assert participant_events[event-1]["position"] == event_info[1].text
                assert participant_events[event-1]["points"] == event_info[2].text