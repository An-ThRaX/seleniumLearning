from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit


# create a class which can find elements by specific identifies
class HandyWrappers:
    def __init__(self, driver):  # deliver the driver to the method, so it will use it
        self.driver = driver

    def get_by_type(self, locator_type):  # define the fct, which take one parameter: locator_type (id, xpath, so on)
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID  # borrow the By method from selenium
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        else:
            print('Locator type  ' + locator_type + ' not correct/supported!')
        return False

    def get_element(self, locator, locator_type='id'):  # locator = the name which we search by
        element = None
        try:
            locator_type = locator_type.lower()  # save the loc type argument in a var
            by_type = self.get_by_type(locator_type)  # detect the type of "locator_type" and save it in a var
            element = self.driver.find_element(by_type, locator)  # use the .find_element method from selenium
            #  to find the element via the arguments and save in a var
            print("Element found!")
        except:
            print("Element not found!")
        return element

    def is_element_preset(self, locator, by_type):  # define a method to check if an element is available or not
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("Element found!")
                return True
            else:
                print("Element not found!")
                return False
        except:
            print("Element not found!")
            return False

    def is_element_present_check(self, locator, by_type):
        try:
            elements_list = self.driver.find_elements(by_type, locator)  # .find_elements returns a list
            if len(elements_list) > 0:
                print("Element found!")
                return True
            else:
                print("Element not found!")
                return False
        except:
            print("Element not found!")
            return False
