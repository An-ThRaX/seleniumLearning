from selenium import webdriver
from basicWeb import chrome_driver_home, chrome_driver_work

class BrowserInteractions():

    def test(self):
        base_url = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()

        # windows max
        driver.maximize_window()

        # open the url
        driver.get(base_url)

        # get title of page
        title = driver.title
        print("The pages title is" + title)

        # get current url
        current_url = driver.current_url
        print("The current url is" + current_url)

        # browser refresh
        driver.refresh()
        print('First refresh.')
        driver.get(current_url)
        print('Second refresh.')

        # open another url
        driver.get('https://www.letskodeit.com/support')

        # browser back
        driver.back()
        print("Go one step back in browser history.")

        # browser forward
        driver.forward()
        print("One step forward in browser history.")

        # get page source
        page_source = driver.page_source
        # print(page_source)

        # browser close and quit

        #driver.close()
        driver.quit()


ff = BrowserInteractions()
ff.test()