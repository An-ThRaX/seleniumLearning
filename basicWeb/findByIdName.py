# example on how to find elements by ID and NAME - highly recommended


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from basicWeb import chrome_driver_home, chrome_driver_work
from selenium.webdriver.common.by import By


class FindByIdName():
    def test(self):
        base_url = "https://www.letskodeit.com/practice"
        chrome_service = Service(executable_path=chrome_driver_home)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(base_url)
        driver.implicitly_wait(10)

        element_by_id = driver.find_element(By.ID, "displayed-text")
        if element_by_id is not None:
            print("Element found -> By Id")

        element_by_name = driver.find_element(By.NAME, "show-hide")
        if element_by_name is not None:
            print("Element found -> By Name")


run_tests = FindByIdName()
run_tests.test()
