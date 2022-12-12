import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from driver_singleton import DriverSingleton
from factories.web_element_value_factory import WebElementValueFactory

HEROES_LIST_URL = r"https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)"


class HeroesDAO:
    @classmethod
    def get_heroes_names(cls):
        for name_element in HeroesSeleniumDAO.get_heroes_names():
            name = WebElementValueFactory.str_text_from_inner_text(name_element)
            yield re.search(r'\d+ ([a-zA-Z- ]+)', name).group(1)


class HeroesSeleniumDAO:

    @classmethod
    def get_heroes_names(cls):
        if DriverSingleton.get_driver().current_url != HEROES_LIST_URL:
            DriverSingleton.get_driver().get(HEROES_LIST_URL)
        try:
            DriverSingleton.get_wait().until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
        except:
            pass

        DriverSingleton.get_wait().until(EC.presence_of_element_located((By.XPATH, f'//*[text()="Classes"]')))

        section_names = [f'li[class="toclevel-1 tocsection-17"]',
                         f'li[class="toclevel-1 tocsection-34"]']

        elements = []
        for s_name in iter(section_names):
            section = DriverSingleton.get_driver().find_element(By.CSS_SELECTOR, s_name)
            elements += section.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]')
        yield from elements
