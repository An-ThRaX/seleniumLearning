# example on how to find elements by XPATH and CSS - highly recommended


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

        element_by_x_path = driver.find_element(By.XPATH, "//input[@name='show-hide']")
        if element_by_x_path is not None:
            print("Element found -> By XPath")

        element_by_css = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if element_by_css is not None:
            print("Element found -> By CSS")


run_tests = FindByXPathCSS()
run_tests.test()
