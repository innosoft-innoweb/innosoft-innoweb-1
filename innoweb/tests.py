from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class TestsLogin():
    
    def test_login_success(self):
        #credentials
        username = "tomcambor"
        password = "Estaesmicontraseña"

        # initialize the Chrome driver
        driver = webdriver.Chrome("chromedriver")

        # head to github login page
        driver.get("http://localhost:8000/login")
        # find username/email field and send the username itself to the input field
        driver.find_element("name", "username").send_keys(username)
        # find password input field and insert password as well
        driver.find_element("name","password").send_keys(password)
        # click login button
        driver.find_element("name", "submit").click()

        # wait the ready state to be complete
        WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )

        
        assert driver.find_element(By.CLASS_NAME,"podium").is_enabled() == True
        # close the driver
        driver.close()
        
    def test_login_username_fail(self):
        #credentials
        username = "notusernamelogin"
        password = "Estaesmicontraseña"

        # initialize the Chrome driver
        driver = webdriver.Chrome("chromedriver")

        # head to github login page
        driver.get("http://localhost:8000/login")
        # find username/email field and send the username itself to the input field
        driver.find_element("name", "username").send_keys(username)
        # find password input field and insert password as well
        driver.find_element("name","password").send_keys(password)
        # click login button
        driver.find_element("name", "submit").click()

        # wait the ready state to be complete
        WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        
        # get the errors (if there are)
        errors = driver.find_elements("id","error-form")
        # print the errors optionally
        # for e in errors:
        #     print(e.text)
        # if we find that error message within errors, then login is failed
        if (len(errors)):
            print("Login failed")
        
        assert driver.find_element("name", "username").is_enabled() == True
        # close the driver
        driver.close()
        
    def test_login_password_fail(self):
        #credentials
        username = "tomcambor"
        password = "passwordincorrect"

        # initialize the Chrome driver
        driver = webdriver.Chrome("chromedriver")

        # head to github login page
        driver.get("http://localhost:8000/login")
        # find username/email field and send the username itself to the input field
        driver.find_element("name", "username").send_keys(username)
        # find password input field and insert password as well
        driver.find_element("name","password").send_keys(password)
        # click login button
        driver.find_element("name", "submit").click()

        # wait the ready state to be complete
        WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        
        # get the errors (if there are)
        errors = driver.find_elements("id","error-form")
        # print the errors optionally
        # for e in errors:
        #     print(e.text)
        # if we find that error message within errors, then login is failed
        if (len(errors)):
            print("Login failed")

        assert driver.find_element("name", "password").is_enabled() == True
        # close the driver
        driver.close()