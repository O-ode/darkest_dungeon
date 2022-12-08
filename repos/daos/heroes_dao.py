import re

from selenium.webdriver.common.by import By

from repos.daos.selenium_dao import SeleniumDAO
from selenium.webdriver.support import expected_conditions as EC

HEROES_LIST_URL = "https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)"


class HeroesDAO(SeleniumDAO):

    @classmethod
    def get_heroes_names(cls):
        cls.pre_load(HEROES_LIST_URL)
        try:
            cls.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
        except:
            pass

        cls.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[text()="Classes"]')))

        section_names = [f'li[class="toclevel-1 tocsection-17"]',
                         f'li[class="toclevel-1 tocsection-34"]']

        names = []
        for s_name in iter(section_names):
            section = cls.driver.find_element(By.CSS_SELECTOR, s_name)
            for el in iter(section.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]')):
                name = re.search(r"[a-zA-Z\s-]*$", el.get_attribute("innerText")).group().lstrip()
                names.append(name)
        yield from names
