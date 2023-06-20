from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from basicWeb import chrome_driver_home, chrome_driver_work


class runChromeTests():

    def demo_test(self):
        chrome_service = Service(executable_path=chrome_driver_home)
        # Instantiate browser
        driver = webdriver.Chrome(service=chrome_service)
        # Open the provided URL
        driver.get("https://www.letskodeit.com/practice")


runtests = runChromeTests()
runtests.demo_test()
