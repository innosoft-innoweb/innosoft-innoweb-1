
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from participant.models import Participant
from event.models import Event
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class RegisterViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']
    username = "usernameTest"
    firstname = "firstnameTest"
    lastname = "Lastname Test"
    email = "emailtest@gmail.com"
    password = "estaEsMiPassword17"
    password2 = "estaEsMiPassword17"
    photo = "http://cdn.onlinewebfonts.com/svg/img_569204.png"

    @classmethod
    def setUpClass(cls):
        super(RegisterViewTest, cls).setUpClass()
        options = webdriver.ChromeOptions()
        options.headless= True
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(RegisterViewTest, cls).tearDownClass()

    def send_keys(self, username, firstname, lastname, email, password, password2, photo):
        if username is not None:
            self.browser.find_element('id','id_username').send_keys(username)
        if firstname is not None:
            self.browser.find_element('id','id_first_name').send_keys(firstname)
        if lastname is not None:
            self.browser.find_element('id','id_last_name').send_keys(lastname)
        if email is not None:
            self.browser.find_element('id','id_email').send_keys(email)
        if password is not None:
            self.browser.find_element('id','id_password1').send_keys(password)
        if password2 is not None:
            self.browser.find_element('id','id_password2').send_keys(password2)
        if photo is not None:
            self.browser.find_element('id','id_photo').send_keys(photo)
        self.browser.find_element('id','id_submit_button').send_keys(Keys.RETURN)
    
    def test_register_success(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, self.email, self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"podium").is_enabled() == True

    def test_register_username_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(None, self.firstname, self.lastname, self.email, self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_firstname_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, None, self.lastname, self.email, self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_lastname_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, None, self.email, self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_email_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, None, self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True

    def test_register_password_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, self.email, None, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_password2_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, self.email, self.password, None, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_username_exist_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys("juasaljur", self.firstname, self.lastname, self.email, self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_email_exist_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, "juasaljur@alum.us.es", self.password, self.password2, self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_password_different_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, self.email, self.password, "estaEsMiPassword18", self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True
    
    def test_register_password_weak_fail(self):
        self.browser.get(self.live_server_url + '/registro/')
        self.send_keys(self.username, self.firstname, self.lastname, self.email, "hola", "hola", self.photo)
        assert self.browser.find_element(By.CLASS_NAME,"errorlist").is_enabled() == True

