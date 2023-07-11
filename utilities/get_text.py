from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit

class GetText:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url_letskodeit)

        # gets the text of a specific element
        open_tab_elem = driver.find_element(By.ID, 'opentab')
        element_text = open_tab_elem.text
        print("Text on element is: " + element_text)


ff = GetText()
ff.test()