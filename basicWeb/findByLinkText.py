# example on how to find elements by LINK_TEXT and PARTIAL_LINK_TEXT - not recommended


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

        element_by_link_text = driver.find_element(By.LINK_TEXT, "HOME")
        if element_by_link_text is not None:
            print("Element found -> By Link Text")

        element_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if element_by_partial_link_text is not None:
            print("Element found -> By Partial Link Text")


run_tests = FindByXPathCSS()
run_tests.test()
