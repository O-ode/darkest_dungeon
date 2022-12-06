import logging
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from constants import pretty
from model.character_model import CharacterModel
from repos.daos.selenium_dao import SeleniumDAO

logger = logging.getLogger()


class HeroDAO(SeleniumDAO):

    def get_heroes_names(self):
        self.driver.get("https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
        except:
            pass

        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[text()="Classes"]')))

        # TODO: UNCOMMENT TWO FOLLOWING LINES
        # section_names = [f'li[class="toclevel-1 tocsection-17"]',
        #                  f'li[class="toclevel-1 tocsection-34"]']

        section_names = [f'li[class="toclevel-1 tocsection-34"]']

        characters = []
        for s_name in section_names:
            section = self.driver.find_element(By.CSS_SELECTOR, s_name)
            for el in section.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]'):
                name = re.search(r"[a-zA-Z\s-]*$", el.get_attribute("innerText")).group().lstrip()
                characters.append(CharacterModel(name)) # TODO: YIELD STRINGS ONE BY ONE AND STORE INFO IN REPO

        characters = [c for c in characters[::-1]]
        logger.info(f'Character list:\n{pretty([character.name for character in characters])}')
        yield from characters
