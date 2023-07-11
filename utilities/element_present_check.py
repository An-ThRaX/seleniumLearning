import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
from utilities.handy_wrappers import HandyWrappers
class UsingWrappers:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        hw = HandyWrappers(driver)  # create an instance of the HandyWrappers class with the driver as argument (row 8)
        driver.get(url_letskodeit)

        element_result1 = hw.is_element_preset('name', 'id')
        print(str(element_result1))

        element_result2 = hw.is_element_present_check('//*[@id="name1"]', 'xpath')
        print(str(element_result2))


ff = UsingWrappers()
ff.test()
