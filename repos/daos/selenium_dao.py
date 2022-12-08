from abc import ABC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from driver_singleton import DriverSingleton


class SeleniumDAOFactory(ABC):

    @classmethod
    def get_driver(cls):
        return DriverSingleton.get_driver()

    @classmethod
    def get_wait(cls):
        return DriverSingleton.get_wait()

    @classmethod
    def get_actions(cls):
        return DriverSingleton.get_actions()


class SeleniumDAO:
    driver: webdriver.Chrome
    wait: WebDriverWait
    actions: ActionChains

    @classmethod
    def init(cls):
        DriverSingleton.init()
        cls.driver = DriverSingleton.get_driver()
        cls.wait = DriverSingleton.get_wait()
        cls.actions = DriverSingleton.get_actions()

    @classmethod
    def pre_load(cls, url: str):
        if cls.driver.current_url != url:
            cls.driver.get(url)
        return cls
