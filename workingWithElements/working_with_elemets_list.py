from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
import time


class WorkingWithElementsList:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url_letskodeit)
        driver.implicitly_wait(3)

        # create a list with all the radio buttons which fills the conditions
        radio_btn_list = driver.find_elements(
            By.XPATH, '//input[contains(@type, "radio") and contains(@name, "cars")]')
        size = len(radio_btn_list)
        print("Size of the list = " + str(size))

        # iterate through the list and click on each element if it's not selected
        for radio_button in radio_btn_list:
            is_selected = radio_button.is_selected()

            if not is_selected:
                radio_button.click()
            time.sleep(1)


run_test = WorkingWithElementsList()
run_test.test()
