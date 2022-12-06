from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from event.models import Event
from score.models import Score
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class HomeViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']

    @classmethod
    def setUpClass(cls):
        super(HomeViewTest, cls).setUpClass()
        options = webdriver.ChromeOptions()
        options.headless = True
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(HomeViewTest, cls).tearDownClass()

    def test_title(self):
        self.browser.get(self.live_server_url)
        assert "Innoweb - Inicio" == self.browser.title

    def test_podium(self):
        self.browser.get(self.live_server_url)

        podium_items = self.browser.find_elements(By.CSS_SELECTOR, '.podium-item')
        # get winners from db
        [first, second, third] = self.get_global_winners()
        winners = [second, first, third]

        # check if there are only 3 winners
        assert len(podium_items) == 3

        positions = ['2', '1', '3']
        for podium_item, winner, position in zip(podium_items, winners, positions):

            # check if position is correct
            podium_position = podium_item.find_element(By.CSS_SELECTOR, '.podium-position')
            assert podium_position.text == position

            # check if winner is correct
            podium_winner = podium_item.find_element(By.CSS_SELECTOR, '.podium-winner')
            assert podium_winner.text == winner.username

            # check if winners link redirects to profile
            podium_link = podium_item.find_element(By.CSS_SELECTOR, 'a')
            assert podium_link.get_attribute('href') == self.live_server_url + '/participante/' + str(winner.id)

            # check if winners img is correct
            podium_link = podium_item.find_element(By.CSS_SELECTOR, 'img')
            assert podium_link.get_attribute('src') == winner.photo

    def test_events(self):
        self.browser.get(self.live_server_url)

        event_cards = self.browser.find_elements(By.CSS_SELECTOR, 'a.event-card')
        open_events = Event.objects.filter(status="Abierto")

        # check open events number
        assert len(event_cards) == open_events.count()

        # check if the events are the correct ones from db
        for event_card, open_event in zip(event_cards, open_events.all()):

            # check if card title is correct
            card_title = event_card.find_element(By.CSS_SELECTOR, '.title-event')
            assert card_title.text == open_event.name

            # check if card link redirects to event
            assert event_card.get_attribute('href') == self.live_server_url + '/evento/' + str(open_event.id)

            # check if card img is correct
            card_img = event_card.find_element(By.CSS_SELECTOR, '.event-image')
            assert card_img.get_attribute('src') == open_event.photo

    @classmethod
    def get_global_winners(cls):
        scores = Score.objects.order_by('-value')

        first = None
        second = None
        third = None

        if len(scores) > 0:
            scores_dict = {}
            for score in scores:
                if score.participant in scores_dict:
                    scores_dict[score.participant] += score.value
                else:
                    scores_dict[score.participant] = score.value

            participants = sorted(scores_dict, key=scores_dict.get, reverse=True)

            if len(participants) >= 3:
                third = participants[2]
                third.username = third.get_username()

            if len(participants) >= 2:
                second = participants[1]
                second.username = second.get_username()

            if len(participants) >= 1:
                first = participants[0]
                first.username = first.get_username()

        winners = [first, second, third]
        return winners

class LoginViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']

    @classmethod
    def setUpClass(cls):
        super(LoginViewTest, cls).setUpClass()
        options = webdriver.ChromeOptions()
        options.headless = True
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(LoginViewTest, cls).tearDownClass()
    
    def test_login_success(self):
        
        username = "tomcambor"
        password = "Estaesmicontraseña"
        PORT = self.live_server_url.split(":")[2]
        self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:" + PORT + "/login")
     
      
        self.browser.find_element("name", "username").send_keys(username)
        
        self.browser.find_element("name","password").send_keys(password)
        
        self.browser.find_element("name", "submit").click()
        
        assert self.browser.find_element(By.CLASS_NAME,"podium").is_enabled() == True
       
        
    def test_login_username_fail(self):
        username = "incorrectusername"
        password = "Estaesmicontraseña"
        PORT = self.live_server_url.split(":")[2]
        self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:" + PORT + "/login")
     
      
        self.browser.find_element("name", "username").send_keys(username)
        
        self.browser.find_element("name","password").send_keys(password)
        
        self.browser.find_element("name", "submit").click()
        
        assert len(self.browser.find_elements("id","error-form")) == 1
        
    def test_login_password_fail(self):
        username = "tomcambor"
        password = "incorrectpassword"
        PORT = self.live_server_url.split(":")[2]
        self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:" + PORT + "/login")
     
      
        self.browser.find_element("name", "username").send_keys(username)
        
        self.browser.find_element("name","password").send_keys(password)
        
        self.browser.find_element("name", "submit").click()
        
        assert len(self.browser.find_elements("id","error-form")) == 1
        
    
class EventViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']

    @classmethod
    def setUpClass(cls):
        super(EventViewTest, cls).setUpClass()
        options = webdriver.ChromeOptions()
        options.headless = True
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(EventViewTest, cls).tearDownClass()
    
    def test_register_event(self):
        username = "tomcambor"
        password = "Estaesmicontraseña"
        PORT = self.live_server_url.split(":")[2]
        self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:" + PORT + "/login")

        self.browser.find_element("name", "username").send_keys(username)
        
        self.browser.find_element("name","password").send_keys(password)
        
        self.browser.find_element("name", "submit").click()
        
        self.browser.get(self.live_server_url)
        event_cards = self.browser.find_elements(By.CSS_SELECTOR, 'a.event-card')
        first_event_ulr = event_cards[0].get_attribute('href')
        self.browser.get(first_event_ulr)
        register_button = self.browser.find_element(By.CSS_SELECTOR, 'a.sign-up')
        register_button.click()
        assert self.browser.find_element(By.CLASS_NAME,"alert-success").is_enabled() == True
    
    def test_register_event_already_registered(self):
        username = "tomcambor"
        password = "Estaesmicontraseña"
        PORT = self.live_server_url.split(":")[2]
        self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:" + PORT + "/login")
      
        self.browser.find_element("name", "username").send_keys(username)
        
        self.browser.find_element("name","password").send_keys(password)
        
        self.browser.find_element("name", "submit").click()
        
        self.browser.get(self.live_server_url)
        event_cards = self.browser.find_elements(By.CSS_SELECTOR, 'a.event-card')
        first_event_ulr = event_cards[0].get_attribute('href')
        self.browser.get(first_event_ulr)
        register_button = self.browser.find_element(By.CSS_SELECTOR, 'a.sign-up')
        register_button.click()
        self.browser.get(first_event_ulr)
        register_button = self.browser.find_element(By.CSS_SELECTOR, 'a.sign-up')
        register_button.click()
        assert self.browser.find_element(By.CLASS_NAME,"alert-warning").is_enabled() == True


    def test_register_event_without_login(self):
        self.browser.get(self.live_server_url)
        event_cards = self.browser.find_elements(By.CSS_SELECTOR, 'a.event-card')
        first_event_ulr = event_cards[0].get_attribute('href')
        self.browser.get(first_event_ulr)
        register_button = self.browser.find_element(By.CSS_SELECTOR, 'a.sign-up')
        register_button.click()
        assert self.browser.find_element(By.CLASS_NAME,"alert-danger").is_enabled() == True

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
    
    def test_next_events_are_shown(self):
        username = "tomcambor"
        password = "Estaesmicontraseña"
        PORT = self.live_server_url.split(":")[2]
        self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:" + PORT + "/login")

        self.browser.find_element("name", "username").send_keys(username)
        
        self.browser.find_element("name","password").send_keys(password)
        
        self.browser.find_element("name", "submit").click()
        
        self.browser.get(self.live_server_url)
        event_cards = self.browser.find_elements(By.CSS_SELECTOR, 'a.event-card')
        first_event_ulr = event_cards[0].get_attribute('href')
        self.browser.get(first_event_ulr)
        register_button = self.browser.find_element(By.CSS_SELECTOR, 'a.sign-up')
        register_button.click()
        profile_url = self.browser.find_element(By.CSS_SELECTOR, 'a.navbar-link-primary').get_attribute('href')
        self.browser.get(profile_url)
        assert self.browser.find_element(By.CSS_SELECTOR, 'td.event-name').is_enabled() == True   

    
