from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service

class runChromeTests():

    def demo_test(self):
        chrome_service = Service(executable_path="C:\\Users\\cipri\\PycharmProjects\\seleniumLearning\\drivers\\chromedriver.exe")
        # Instantiate browser
        driver = webdriver.Chrome(service=chrome_service)
        # Open the provided URL
        driver.get("https://www.letskodeit.com/practice")


runtests = runChromeTests()
runtests.demo_test()
