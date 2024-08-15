from base import BasePage
from selenium.webdriver.common.by import By
import os


class SbisLocators:
    tensor_logo = (
        By.CSS_SELECTOR, "a[href = 'https://tensor.ru/']")
    people_power = (
        By.XPATH, "//div[@class = 'tensor_ru-Index__block4-content tensor_ru-Index__card']/p[1]")
    about = (
        By.XPATH, "//div[@class = 'tensor_ru-Index__block4-content tensor_ru-Index__card']/p[4]/a[1]")
    work_block = (
        By.XPATH, "//div[@class = 'tensor_ru-container tensor_ru-section tensor_ru-About__block3']/div[2]/div")


class SbisLocatorsSecond:
    region = (
        By.XPATH, "//span[@class = 'sbis_ru-Region-Chooser__text sbis_ru-link']")
    partner_list = (
        By.XPATH, "//div[@data-qa='items-container']/div[@data-qa='item']")
    dialog = (By.XPATH,
              "//div[@name = 'dialog']/div[@class = 'sbis_ru-Region-Panel__container']/ul[1]/li/span[@title = 'Камчатский край']")


class SbisLocatorsThree:
    download = (
        By.XPATH, "//a[@href = '/download']")
    file_download = (
        By.XPATH, "//a[@href = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
    plugin = (
        By.XPATH, "//div[@data-id = 'plugin']")
    win_os = (
        By.XPATH, "//div[@data-id = 'default']")


class SbisHelperFirst(BasePage):

    def to_tensor(self):
        self.find_element(SbisLocators.tensor_logo).click()
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def check_people_power(self):
        return self.find_element(SbisLocators.people_power)

    def to_about(self):
        element = self.find_element(SbisLocators.people_power)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self.find_element(SbisLocators.about).click()

    def check_size(self):
        wb = self.find_elements(SbisLocators.work_block)
        sizes = []
        for i in wb:
            pic = i.find_element(By.TAG_NAME, "img")
            sizes.append((pic.get_attribute("width"), pic.get_attribute("height")))
        return sizes


class SbisHelperSecond(BasePage):
    def check_region(self):
        return self.find_element(SbisLocatorsSecond.region).text

    def check_partner_list(self):
        partners = []
        for i in self.find_elements(SbisLocatorsSecond.partner_list):
            partner = i.text.split('\n')[0]
            if partner:
                partners.append(partner)
        return partners

    def regions(self):
        return self.find_element(SbisLocatorsSecond.region).click()

    def dialog(self):
        return self.find_element(SbisLocatorsSecond.dialog).click()


class SbisHelperThree(BasePage):

    def to_download(self):
        return self.find_element(SbisLocatorsThree.download).click()

    def file_download(self):
        self.find_element(SbisLocatorsThree.plugin).click()
        self.find_element(SbisLocatorsThree.win_os).click()
        return self.find_element(SbisLocatorsThree.file_download).click()

    def size_on_site(self):
        size = self.find_element(SbisLocatorsThree.file_download).text
        size = size.split(" ")
        size = size[2]
        return float(size)

    def local_size(self):
        path = os.getcwd()
        files = os.listdir(path)
        files = [os.path.join(path, file) for file in files]
        files = [file for file in files if os.path.isfile(file)]
        name = max(files, key=os.path.getctime)
        return self.convert_size(os.path.getsize(name))
