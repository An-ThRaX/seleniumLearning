from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from basicWeb import chrome_driver_home, chrome_driver_work # variables with chrome driver path

class runChromeTests():

    def demo_test(self):
        # Create a service variable in which we store the path of the driver's locationfgyfff
        chrome_service = Service(executable_path=chrome_driver_work)
        # Instantiate browser
        driver = webdriver.Chrome(service=chrome_service)
        # Open the provided URL
        driver.get("https://www.letskodeit.com/practice")


runtests = runChromeTests()
runtests.demo_test()
