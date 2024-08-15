import os

from selenium import webdriver
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        # что с путем делать?
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)
    print(driver.get_log('browser'))
    yield driver
    driver.quit()
