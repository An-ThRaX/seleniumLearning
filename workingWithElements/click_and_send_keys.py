from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from basicWeb import url_letskodeit, chrome_driver_home, chrome_driver_work


class ClickAndSendKeys():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)  # selenium will wait for 10 seconds before it searches again for the elements -
        # it applies for all the below cases

        # capture the login field in a variable and apply actions on it
        login_link = driver.find_element(By.XPATH, '//div[@id="navbar-inverse-collapse"]//a[@href="/login"]')
        login_link.click()

        # capture the email field in a variable and apply actions on it
        email_field = driver.find_element(By.ID, 'email')
        email_field.send_keys('test')

        # capture the password field in a variable and apply actions on it
        password_field = driver.find_element(By.ID, 'login-password')
        password_field.send_keys('test')

        time.sleep(3)
        email_field.clear()

        time.sleep(3)
        email_field.send_keys('test')


ff = ClickAndSendKeys()
ff.test()
