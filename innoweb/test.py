
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from participant.models import Participant
from event.models import Event
# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class RegisterViewTest(StaticLiveServerTestCase):
    fixtures = ['fixtures/initial.json']
    driver = webdriver.Chrome("chromedriver")
    driver.get('http://localhost:8000/registro')
    username = driver.find_element('id','id_username')
    firstname = driver.find_element('id','id_first_name')
    lastname = driver.find_element('id','id_last_name')
    email = driver.find_element('id','id_email')
    password1 = driver.find_element('id','id_password1')
    password2 = driver.find_element('id','id_password2')
    photo = driver.find_element('id','id_photo')
    submit = driver.find_element('id','id_submit_button')

    def test_register_user(self):

        self.username.send_keys("usernameTest")
        self.firstname.send_keys("firstnameTest")
        self.lastname.send_keys("Lastname Test")
        self.email.send_keys("emailtest@gmail.com")
        self.password1.send_keys("estaEsMiPassword17")
        self.password2.send_keys("estaEsMiPassword17")
        self.photo.send_keys("http://cdn.onlinewebfonts.com/svg/img_569204.png")

        self.submit.send_keys(Keys.RETURN)
        #chek if participant has been created 
        WebDriverWait(driver=self.driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        self.driver.close()
        #self.assertTrue(Participant.objects.filter(username="usernameTest").exists())
        print(Participant.objects.all())
        print(Event.objects.all())

        # participantRegister = Participant.objects.get(username="usernameTest")
        # #check if participantRegister exists
        # if participantRegister.first_name == "firstnameTest":
        #     participantRegister.delete()

    




