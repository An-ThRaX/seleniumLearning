from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import chrome_driver_home, chrome_driver_work
import time
class ElementState():
    def isEnabled(self):
        base_url = 'https://www.google.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        e1 = driver.find_element(By.ID, 'APjFqb')
        e1_state = e1.is_enabled()  # True or False
        print("E1 is enabled? " + str(e1_state))

        # google asks to accept cookies, this will close the window
        close_cookies = driver.find_element(By.XPATH, '//button[@id="W0wltc"]/div')
        close_cookies.click()

        e1.send_keys('sad')
        time.sleep(10)


e = ElementState()
e.isEnabled()

