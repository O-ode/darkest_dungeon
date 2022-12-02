import logging
import re
import traceback
from time import sleep

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from constants import pretty, skill_attributes_regex, skip_regex
from model.character_model import CharacterModel
from model.character_stat_model import CharacterStatModel
from model.kwargs import skill_kwargs, character_level_kwargs, resistance_model_kwargs
from model.resistance_stat_model import ResistanceStatModel
from model.skill_model import SkillModel
from selenium_local.value_retrieving_functions import find_element_and_get_str_from_innerText, value_from_innerText

logger = logging.getLogger()


def get_characters_with_effects(_characters: [CharacterModel], patterns: [re.Pattern]):
    for pattern in patterns:
        yield get_characters_with_effect(_characters, pattern)


def get_characters_with_effect(_characters: [CharacterModel], pattern: re.Pattern):
    def _get_skills_with_effect(_skills: [SkillModel], _pattern: re.Pattern):
        for skill in iter(_skills):
            for effect in iter(skill.effects):
                if _pattern.search(effect.description):
                    yield skill

    for character in iter(_characters):
        skills = [skill for skill in _get_skills_with_effect(character.skills, pattern)]
        if len(skills) > 0:
            yield CharacterModel(character.class_name, skills)


def _get_resistance_values(row):
    logger.info(f'Getting resistance values')
    elements = row.find_elements(By.CSS_SELECTOR, f'td')
    elements = [(elements[0], elements[1]), (elements[2], elements[3])]
    for name_element, value_element in elements:
        resistance_name = find_element_and_get_str_from_innerText(name_element, f'a:nth-child(2)', r"(stun|blight|disease|death_blow|move|bleed|debuff|trap)")
        logger.info(resistance_name)

        resistance_value = value_from_innerText(value_element)
        logger.info(resistance_name)

        value_modifying_function = resistance_model_kwargs[resistance_name]
        resistance_value = value_modifying_function(resistance_value)

        yield resistance_name, resistance_value


class SeleniumCharacterManager:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_characters(self):
        self.driver.get("https://darkestdungeon.fandom.com/wiki/Heroes_(Darkest_Dungeon)")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="ACCEPT"]'))).click()
        except:
            pass

        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[text()="Classes"]')))

        # section_names = [f'li[class="toclevel-1 tocsection-17"]',
        #                  f'li[class="toclevel-1 tocsection-34"]']
        section_names = [f'li[class="toclevel-1 tocsection-34"]']
        _characters: [CharacterModel] = []
        for s_name in section_names:
            section = self.driver.find_element(By.CSS_SELECTOR, s_name)
            for el in section.find_elements(By.CSS_SELECTOR, 'li[class*="toclevel-2"]'):
                name = re.search(r"[a-zA-Z\s-]*$", el.get_attribute("innerText")).group().lstrip()
                _characters.append(CharacterModel(name))

        _characters = [c for c in _characters[::-1]]
        logger.info(f'Character list:\n{pretty([_character.name for _character in _characters])}')
        yield from _characters

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
                skill_attribute_name = value_from_innerText(col)
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

    # def get_stats_of_character(self):
    #     logger.info(f'Getting stats')
    #
    #     table = self.wait.until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))
    #     kwargs = {}
    #     for i, row in enumerate(table.find_elements(By.CSS_SELECTOR, f'tr'), start=1):
    #         if 5 <= i <= 11:
    #             row_name = unicodedata.normalize('NFKD',
    #                                              row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)')
    #                                              .get_attribute("innerText"))
    #             row_name = re.search(r"(MAX\s*HP|DODGE|PROT|SPD|ACC\s*MOD|CRIT|DMG)", row_name, re.I).group()
    #             row_name = re.sub(r'\s+', '_', row_name).lower()
    #             values_obtaining_function, value_modifying_function = \
    #                 character_level_kwargs[row_name]
    #
    #             values = values_obtaining_function(row)
    #             values = [value_modifying_function(value) for value in values]
    #             kwargs[row_name] = values
    #
    #     logger.info(f'kwargs:\n{pretty(kwargs)}')
    #
    #     for i in range(5):
    #         new_kwargs = {attribute_name: values[i] for attribute_name, values in kwargs.items()}
    #         new_model = CharacterStatModel(**new_kwargs)
    #         logger.info(new_model)
    #         yield new_model

    def _get_resolve_lvl_attribute(self, row: WebElement):
        logger.info(f'Getting resolve level values')
        lvl_attribute = unicodedata.normalize('NFKD',
                                              row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)')
                                              .get_attribute("innerText"))
        lvl_attribute = re.search(r"(MAX\s*HP|DODGE|PROT|SPD|ACC\s*MOD|CRIT|DMG)", lvl_attribute, re.I).group()
        lvl_attribute = re.sub(r'\s+', '_', lvl_attribute).lower()
        values_obtaining_function, value_modifying_function = \
            character_level_kwargs[lvl_attribute]

        values = values_obtaining_function(row)
        values = [value_modifying_function(value) for value in values]
        return lvl_attribute, values

    def _get_other_info_of_character(self, row: WebElement):
        logger.info(f'Getting other info')
        lvl_attribute = unicodedata.normalize('NFKD',
                                              row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)')
                                              .get_attribute("innerText"))

        
        pass

    def _get_character_values_from_character_table(self):
        logger.info(f'Getting all character stats and other values')

        table = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))

        kwargs_list = [{}, {}]
        for i, row in enumerate(table.find_elements(By.CSS_SELECTOR, f'tr'), start=1):
            if 5 <= i <= 11:
                lvl_attribute, values = self._get_resolve_lvl_attribute(row)
                kwargs_list[0][lvl_attribute] = values
            elif 13 <= i <= 16:
                for r_name, r_value in _get_resistance_values(row):
                    kwargs_list[1][r_name] = r_value
            else:
                self._get_other_info_of_character(row)
                continue

        logger.info(f'Raw values kwargs:\n{pretty(kwargs_list)}')
        for i in range(5):
            new_kwargs = {attribute_name: values[i] for attribute_name, values in kwargs_list[0].items()}
            new_model = CharacterStatModel(**new_kwargs)
            logger.info(new_model)
            yield new_model

        yield ResistanceStatModel(**kwargs_list[1])

    def fetch_characters_details(self, characters: [CharacterModel]):
        for character in characters:
            parsed = re.sub(r' ', '_', character.name)
            url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
            self.driver.get(url)

            character.add_skills([s for s in self.get_skills_of_character()])
            for i, values in enumerate(self._get_character_values_from_character_table()):
                if i < 5:
                    character.add_stats(values)
                elif i == 5:
                    character.add_resistances(values)
                # elif
                # .add_other_info([o for o in self.get_other_info_of_character()])
        return characters
