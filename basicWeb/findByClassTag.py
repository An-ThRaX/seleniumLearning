# example on how to find elements by CLASS_NAME and TAG_NAME - not recommended

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from basicWeb import chrome_driver_home, chrome_driver_work
from selenium.webdriver.common.by import By


class FindByXPathCSS():
    def test(self):
        base_url = "https://www.letskodeit.com/practice"
        # chrome_service = Service(executable_path=chrome_driver_home)
        # driver = webdriver.Chrome(service=chrome_service)

        driver = webdriver.Chrome()  # This line is equal with the two above
        driver.get(base_url)
        driver.implicitly_wait(10)

        element_by_class = driver.find_element(By.CLASS_NAME, "inputs")
        if element_by_class is not None:
            print("Element found -> By Class Name")
            element_by_class.send_keys("Testing")

        element_by_tag_name = driver.find_element(By.TAG_NAME, "a")
        if element_by_tag_name is not None:
            print("Element found -> By Tag Name: " + element_by_tag_name.text)

        time.sleep(5)




run_tests = FindByXPathCSS()
run_tests.test()
