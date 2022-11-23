from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from event.models import Event

class HomeViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']
    
    @classmethod
    def setUpClass(cls):
        super(HomeViewTest, cls).setUpClass()
        # cls.selenium = WebDriver()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(HomeViewTest, cls).tearDownClass()
    
    def test_title(self):
        self.browser.get(self.live_server_url)

        print(self.live_server_url)
        print(self.browser.title)
        assert "Innoweb - Inicio" == self.browser.title

    def test_podium(self):
        self.browser.get(self.live_server_url)

        podium_items = self.browser.find_elements(By.CSS_SELECTOR, '.podium-item')
        # TODO: get winners from db
        winners = ['Jesús Luque', 'Ester García', 'Juan Salas']
        
        # check if there are only 3 winners
        assert len(podium_items) == 3
        
        positions = ['2', '1', '3']
        for podium_item, winner, position in zip(podium_items, winners, positions):
            
            # check if position is correct
            podium_position = podium_item.find_element(By.CSS_SELECTOR, '.podium-position')
            assert podium_position.text == position
            
            # check if winner is correct
            podium_winner = podium_item.find_element(By.CSS_SELECTOR, '.podium-winner')
            assert podium_winner.text == winner
        
            # TODO: check if winners link redirects to profile
            # podium_link = podium_item.find_element(By.CSS_SELECTOR, 'a')
            # assert podium_link.get_attribute('href') == self.live_server_url + '/#'
        
            # TODO: check if winners img is correct
            # podium_link = podium_item.find_element(By.CSS_SELECTOR, 'a')
            # assert podium_link.get_attribute('href') == self.live_server_url + '/#'
    
    def test_events(self):
        self.browser.get(self.live_server_url)

        event_cards = self.browser.find_elements(By.CSS_SELECTOR, 'a.event-card')
        open_events = Event.objects.filter(status="Abierto")
        
        # check open events number
        # assert len(event_cards) == open_events.count()
        
        # check if the events are the correct ones from db
        for event_card, open_event in zip(event_cards, open_events.all()):
            print(event_card.text)
            
            # TODO: check if card title is correct
            # card_title = event_card.find_element(By.CSS_SELECTOR, '.title-event')
            # assert card_title.text == open_event.name
            
            # TODO: check if card link redirects to event
            # assert event_card.get_attribute('href') == self.live_server_url + '/#'
            
            # TODO: check if card img is correct
            # card_img = event_card.find_element(By.CSS_SELECTOR, '.image-card')
            # assert card_img.get_attribute('href') == open_event.photo

