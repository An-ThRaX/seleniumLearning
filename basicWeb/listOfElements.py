# example on how to find elements by LINK_TEXT and PARTIAL_LINK_TEXT - not recommended

from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():
    def test(self):
        base_url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)
        # find all the elements, by ClassName
        element_list_by_class_name = driver.find_elements(By.CLASS_NAME, 'inputs')

        if element_list_by_class_name is not None:
            print("By Class Name, the size of the list is: " + str(len(element_list_by_class_name)))

        # find all the elements, by TagName
        element_list_by_tag_name = driver.find_elements(By.TAG_NAME, 'td')

        if element_list_by_tag_name is not None:
            print("By Tag Name, the size of the list is: " + str(len(element_list_by_tag_name)))


run_tests = ListOfElements()
run_tests.test()
