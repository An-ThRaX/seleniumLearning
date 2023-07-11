import time

from selenium import webdriver
from basicWeb import url_letskodeit
from utilities.handy_wrappers import HandyWrappers
class UsingWrappers:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        hw = HandyWrappers(driver)  # create an instance of the HandyWrappers class with the driver as argument (row 8)
        driver.get(url_letskodeit)

        text_field = hw.get_element('name')  # get the element with "name" as locator - default is 'ID'
        text_field.send_keys("Test")  # use the .send_keys method from selenium to write in the field
        time.sleep(2)
        text_field_2 = hw.get_element('//*[@id="name"]', locator_type="xpath")  # get the element with given xpath
        text_field_2.clear()  # use the .clear() method from selenium to clear the field
        time.sleep(10)


ff = UsingWrappers()
ff.test()
