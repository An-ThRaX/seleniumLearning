from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from basicWeb import url_letskodeit


class RadioAndCheckBoxButtons:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url_letskodeit)
        driver.implicitly_wait(3)

        # click on the bmw radio button
        bmw_radio_btn = driver.find_element(By.ID, 'bmwradio')
        bmw_radio_btn.click()

        time.sleep(2)

        # click on the benz radio button
        benz_radio_btn = driver.find_element(By.ID, 'benzradio')
        benz_radio_btn.click()

        time.sleep(2)

        # click on the bmw check button
        bmw_check_btn = driver.find_element(By.ID, 'bmwcheck')
        bmw_check_btn.click()

        time.sleep(2)

        # click on the benz check button
        benz_check_btn = driver.find_element(By.ID, 'benzcheck')
        benz_check_btn.click()

        time.sleep(2)

        # return true or false, depending on the buttons state
        print("BMW radio button is selected? " + str(bmw_radio_btn.is_selected()))
        print("Benz radio button is selected? " + str(benz_radio_btn.is_selected()))
        print("BMW check button is selected? " + str(bmw_check_btn.is_selected()))
        print("Benz check button is selected? " + str(benz_check_btn.is_selected()))


run_test = RadioAndCheckBoxButtons()
run_test.test()
