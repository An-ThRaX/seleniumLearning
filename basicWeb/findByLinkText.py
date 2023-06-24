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

        elementByLinkText = driver.find_element(By.LINK_TEXT, "HOME")
        if elementByLinkText is not None:
            print("Element found -> By Link Text")

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if elementByPartialLinkText is not None:
            print("Element found -> By Partial Link Text")


run_tests = FindByXPathCSS()
run_tests.test()