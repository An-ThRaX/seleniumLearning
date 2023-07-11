from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit

class GetText:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url_letskodeit)

        # gets the value of a specific attribute
        elem = driver.find_element(By.ID, 'name')
        result = elem.get_attribute("type")

        print("Value of attribute is: " + result)


ff = GetText()
ff.test()