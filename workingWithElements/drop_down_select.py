from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



class DropDownSelect1:
    def test(self):
        base_url = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element(By.ID, 'carselect')
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")
        time.sleep(2)


class DropDownSelect2:
    def test(self):
        base_url = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # provide the element "carselect" to the Select class and store in "select"
        select = Select(driver.find_element(By.ID, 'carselect'))
        # this will take each option and
        for option in select.options:
            # print(option.text)
            # from the "select" variable, based on its text, click on each option
            select.select_by_visible_text(option.text)
            time.sleep(1)


ff = DropDownSelect2()
ff.test()
