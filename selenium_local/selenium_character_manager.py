import logging
import re
import traceback

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from constants import pretty, skill_attributes_regex, skip_regex, resolve_level_attributes_regex
from model.hero_model import HeroModel
from model.kwargs import skill_kwargs
from model.skill_model import SkillModel
from selenium_local.value_retrieving_functions import str_from_inner_text

logger = logging.getLogger()


class SeleniumCharacterManager:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.characters: [HeroModel] = []

    def get_characters(self):
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

        for s_name in section_names:
            section = self.driver.find_element(By.CSS_SELECTOR, s_name)
            for el in section.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]'):
                name = re.search(r"[a-zA-Z\s-]*$", el.get_attribute("innerText")).group().lstrip()
                self.characters.append(HeroModel(name))

        self.characters = [c for c in self.characters[::-1]]
        logger.info(f'Character list:\n{pretty([_character.name for _character in self.characters])}')
        yield from self.characters

    def get_skills_of_character(self):
        logger.info(f'Getting skills')
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f'//span[text()="Combat Skills" or text()="Combat Abilities"]')))

        table_selector = f'table.wikitable.tablebg[style*="text-align:center"]'
        elements = self.driver.find_elements(By.CSS_SELECTOR, table_selector)
        assert elements is not None and len(elements) > 0
        for table in elements:
            try:
                skill_name = table.find_element(
                    By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > th').get_attribute('innerText')

                if skip_regex.search(skill_name):
                    continue
                logger.info(f'skill_name: {skill_name}')
                kwargs = {"skill_name": skill_name}
            except:
                try:
                    if not self.driver.find_element(By.XPATH, f'//span[text()="Shieldbreaker"]'):
                        logger.error(traceback.format_exc())
                except:
                    logger.error(traceback.format_exc())
                    with open(r'lolmao.png', 'wb') as file:
                        file.write(table.screenshot_as_png)
                continue

            try:
                info_row = table.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(3)")
            except Exception as _:
                logger.error(traceback.format_exc())
                continue

            try:
                titles_row = table.find_element(By.CSS_SELECTOR, 'tbody > tr[class="accent1tablecell"]')
            except Exception as _:
                logger.error(traceback.format_exc())
                continue

            for i, col in enumerate(titles_row.find_elements(By.CSS_SELECTOR, 'td')[1:], start=1):
                skill_attribute_name = str_from_inner_text(col)
                logger.info(skill_attribute_name)
                skill_attribute_name = skill_attributes_regex.search(skill_attribute_name).group()
                skill_attribute_name, value_obtaining_function, value_modifying_function = \
                    skill_kwargs[skill_attribute_name]

                value = info_row.find_element(By.CSS_SELECTOR, f'td:nth-child({i})')
                value = value_obtaining_function(value)
                value = value_modifying_function(value)

                kwargs[skill_attribute_name] = value

            logger.info(f'kwargs:\n{pretty(kwargs)}')
            skill = SkillModel(**kwargs)
            logger.info(f'New skill: {skill}')
            yield skill

    # def _get_character_values_from_character_table(self):
    #     logger.info(f'Getting all character stats and other values')
    # 
    #     table = self.wait.until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))
    # 
    #     kwargs_list = [{}, {}]
    #     for i, row in enumerate(table.find_elements(By.CSS_SELECTOR, f'tr'), start=1):
    #         if 5 <= i <= 11:
    #             lvl_attribute, values = _get_resolve_lvl_attribute(row)
    #             kwargs_list[0][lvl_attribute] = values
    #         elif 13 <= i <= 16:
    #             for r_name, r_value in _get_resistance_values(row):
    #                 kwargs_list[1][r_name] = r_value
    #         else:
    #             _get_other_info_of_character(row)
    #             continue
    # 
    #     logger.info(f'Raw values kwargs:\n{pretty(kwargs_list)}')
    #     for i in range(5):
    #         new_kwargs = {attribute_name: values[i] for attribute_name, values in kwargs_list[0].items()}
    #         new_model = CharacterStatModel(**new_kwargs)
    #         logger.info(new_model)
    #         yield new_model
    # 
    #     yield ResistanceStatModel(**kwargs_list[1])

    def _get_resolve_level_attribute_name(self, row: WebElement):
        lvl_attribute_name = row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)').get_attribute("innerText")
        lvl_attribute_name = unicodedata.normalize('NFKD', lvl_attribute_name)
        lvl_attribute_name = resolve_level_attributes_regex.search(lvl_attribute_name).group()
        lvl_attribute_name = re.sub(r'\s+', '_', lvl_attribute_name).lower()
        return lvl_attribute_name

    def _hero_level_raw_values_from_inner_text(self, row: WebElement) -> list[str]:
        return [unicodedata.normalize('NFKD', cell.get_attribute("innerText"))
                for cell in row.find_elements(By.CSS_SELECTOR, f'td')[1:]]

    def _get_hero_resolve_level_raw_attributes(self, character_table: WebElement) -> dict:
        raw_attributes = {}
        for row in character_table.find_elements(By.CSS_SELECTOR, f'tr')[4:11]:
            attribute_name = self._get_resolve_level_attribute_name(row)
            # attribute_class_tuple = self.str_self_dict[attribute_name]
            values = self._hero_level_raw_values_from_inner_text(row)
            raw_attributes[attribute_name] = values
        return raw_attributes

    def _transform_raw_resolve_level_attributes(self, raw_attrs: dict):
        transformed_attrs = {i: {} for i in range(1, 6)}
        for attribute_name, values in raw_attrs.items():
            for i, value in enumerate(values, start=1):
                transformed_attrs[i].update({attribute_name: value})
        return transformed_attrs

    # def fetch_hero_resolve_level_raw_details(self):
    #     for character in self.characters:
    #         parsed = re.sub(r' ', '_', character.name)
    #         url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
    #         self.driver.get(url)
    #
    #         character_table = self.wait.until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))
    #         hero_level_attributes: dict = self._get_transformed_resolve_level_attributes(character_table)
    #         yield hero_level_attributes
    #
    #         # character.add_skills([s for s in self.get_skills_of_character()])
    #         # for i, values in enumerate(self._get_character_values_from_character_table()):
    #         #     if i < 5:
    #         #         character.add_stats(values)
    #         #     elif i == 5:
    #         #         character.add_resistances(values)
    #         #     # elif
    #         #     # .add_other_info([o for o in self.get_other_info_of_character()])
    #     # return self.characters
