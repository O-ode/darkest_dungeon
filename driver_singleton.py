from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class DriverSingleton:
    __driver: webdriver.Chrome
    __wait: WebDriverWait
    __actions: ActionChains

    @classmethod
    def init(cls):
        if cls.__driver is None:
            cls.__driver, cls.__wait, cls.__actions = cls.setup_driver()
        return cls

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver, cls.__wait, cls.__actions = cls.setup_driver()
        return cls.__driver

    @classmethod
    def get_actions(cls):
        if cls.__driver is None:
            cls.__driver, cls.__wait, cls.__actions = cls.setup_driver()
        return cls.__actions

    @classmethod
    def get_wait(cls):
        if cls.__driver is None:
            cls.__driver, cls.__wait, cls.__actions = cls.setup_driver()
        return cls.__wait

    @classmethod
    def setup_driver(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('log-level=3')
        service = Service(
            ChromeDriverManager(path=fr"{Path.home()}\.virtualenvs\darkest_dungeon-k9hrbMGS\src").install())
        _driver = webdriver.Chrome(service=service, options=options)

        _wait = WebDriverWait(_driver, 10)
        _actions = ActionChains(_driver)
        return _driver, _wait, _actions