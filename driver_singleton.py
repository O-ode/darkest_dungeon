import logging
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger()
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('log-level=3')
service = Service(
    ChromeDriverManager(path=fr"{Path.home()}\.virtualenvs\darkest_dungeon-IEFPBDCG\src").install()
)


class DriverSingleton:
    __driver: webdriver.Chrome = webdriver.Chrome(service=service, options=options)
    __wait: WebDriverWait = WebDriverWait(__driver, 10)
    __actions: ActionChains = ActionChains(__driver)

    @classmethod
    def close(cls, wait=False):
        try:
            if wait:
                sleep(30)
        except KeyboardInterrupt as _:
            pass
        cls.__driver.close()

    @classmethod
    def get_driver(cls):
        return cls.__driver

    @classmethod
    def get_actions(cls):
        return cls.__actions

    @classmethod
    def get_wait(cls):
        return cls.__wait
