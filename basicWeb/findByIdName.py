from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from basicWeb import chrome_driver_home, chrome_driver_work
from selenium.webdriver.common.by import By


class FindByIdName():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        chrome_service = Service(executable_path=chrome_driver_home)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementById = driver.find_element(By.ID, "displayed-text")
        if elementById is not None:
            print("Element found -> By Id")

        elementByName = driver.find_element(By.NAME, "show-hide")
        if elementByName is not None:
            print("Element found -> By Name")


run_tests = FindByIdName()
run_tests.test()