from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
import time

class DynamicXpathFormat:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url_letskodeit)

        # Login on the website
        driver.find_element(By.LINK_TEXT, "SIGN IN").click()
        email = driver.find_element(By.ID, 'email')
        email.send_keys('test@email.com')
        password = driver.find_element(By.ID, "login-password")
        password.send_keys('abcabc')
        driver.find_element(By.ID, 'login').click()

        # search for courses
        all_courses = driver.find_element(By.XPATH, '//li[@data-id="41189"]/a[@href="/courses"]')
        all_courses.click()
        search_courses = driver.find_element(By.XPATH, '//input[@id="search"]')
        search_courses.send_keys('JavaScript for beginners')

        # select a course
        _course = '//div[contains(@id="course-list") and contains (text(), "{0}")]'
        _course_locator = _course.format('JavaScript for beginners')
        time.sleep(3)

        course_element = driver.find_element(By.XPATH, _course)
        course_element.click()
        time.sleep(10)


ff = DynamicXpathFormat()
ff.test()