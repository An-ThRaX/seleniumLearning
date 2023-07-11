from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HiddenElements():
    def test_lets_kode_it(self):
        base_url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # find the state of the text box
        text_box_element = driver.find_element(By.ID, "displayed-text")
        text_box_state = text_box_element.is_displayed() # True if visible, False if hidden
        # exception if not present in the DOM
        print("Text is visible? " + str(text_box_state))
        time.sleep(2)

        # click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()

        # find the state of the text box
        text_box_state = text_box_element.is_displayed()
        print("Text is visible? " + str(text_box_state))
        time.sleep(2)

        # click the Show button
        driver.find_element(By.ID, "show-textbox").click()

        # find the state of the text box
        text_box_state = text_box_element.is_displayed()
        print("Text is visible? " + str(text_box_state))
        time.sleep(2)



    # a BS of website, good for nothing - loads different pages
    def test_expedia(self):
        base_url = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        click_flights = driver.find_element(By.XPATH, '//*[@class="uitk-tabs-container"]//span[contains(text(),"Flights")]')
        click_flights.click()
        time.sleep(2)

        click_1_traveler = driver.find_element(By.XPATH, '//*[@data-testid="travelers-field"]')
        click_1_traveler.click()
        time.sleep(2)

        select_child = driver.find_element(By.XPATH, "//*[@aria-label='Increase children']")
        select_child.click()
        time.sleep(2)

        drop_down_element = driver.find_element(By.ID, "child-age-input-0-0")
        print("Element visible? " + str(drop_down_element.is_displayed()))


ff = HiddenElements()
for i in range(5):
    ff.test_expedia()

