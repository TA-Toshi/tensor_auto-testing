import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseLocators:
    sbis_contacts = (
        By.CSS_SELECTOR, "li[class = 'sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm']")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def to_contacts(self):
        time.sleep(2)
        return self.find_element(BaseLocators.sbis_contacts).click()

    @staticmethod
    def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return float(s)

    @staticmethod
    def done_download():
        path = os.getcwd()
        for each in os.listdir(path):
            if each.endswith('.exe'):
                return True
        return False
