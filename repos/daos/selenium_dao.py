from abc import ABC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDAO(ABC):

    def __init__(self, driver, wait, actions):
        self.driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = wait
        self.actions: ActionChains = actions