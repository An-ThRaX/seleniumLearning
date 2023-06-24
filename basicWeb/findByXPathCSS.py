from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from basicWeb import chrome_driver_home, chrome_driver_work
from selenium.webdriver.common.by import By


class FindByXPathCSS():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        # chrome_service = Service(executable_path=chrome_driver_home)
        # driver = webdriver.Chrome(service=chrome_service)

        driver = webdriver.Chrome()  # This line is equal with the two above
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByXPath = driver.find_element(By.XPATH, "//input[@name='show-hide']")
        if elementByXPath is not None:
            print("Element found -> By XPath")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSS is not None:
            print("Element found -> By CSS")


run_tests = FindByXPathCSS()
run_tests.test()