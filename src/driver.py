from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


class Driver:
    def __init__(self, headless):
        self.headless = headless
        self.options = Options()
        self.options.headless = self.headless
        self.options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=self.options)
        self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

