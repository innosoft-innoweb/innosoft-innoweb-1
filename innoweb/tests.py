from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager



        
class LoginViewTest(StaticLiveServerTestCase):
    
    fixtures = ['fixtures/initial.json']

    @classmethod
    def setUpClass(cls):
        super(LoginViewTest, cls).setUpClass()
        cls.browser = webdriver.Chrome(ChromeDriverManager().install())


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
        
    
        
    