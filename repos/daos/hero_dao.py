import logging
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from constants import resolve_level_attributes_regex, other_attrs_regex, resistances_regex
from model.hero_model import HeroModel
from repos.daos.selenium_dao import SeleniumDAO
from selenium_local.value_retrieving_functions import str_from_inner_text, \
    str_matched_underscored_lower_from_inner_text

logger = logging.getLogger()


class HeroDAO(SeleniumDAO):

    @classmethod
    def get_transformed_resolve_level_attributes(cls, hero: HeroModel):

        def _get_resolve_level_attribute_name(row: WebElement):
            lvl_attribute_name = str_matched_underscored_lower_from_inner_text(
                row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)'),
                resolve_level_attributes_regex
            )
            return lvl_attribute_name

        def _hero_level_raw_values_from_inner_text(row: WebElement) -> list[str]:
            return [str_from_inner_text(cell) for cell in row.find_elements(By.CSS_SELECTOR, f'td')[1:]]

        def _get_hero_resolve_level_raw_attributes() -> dict:
            _raw_attributes = {}
            for row in character_table.find_elements(By.CSS_SELECTOR, f'tr')[4:11]:
                attribute_name = _get_resolve_level_attribute_name(row)
                # attribute_class_tuple = .str__dict[attribute_name]
                values = _hero_level_raw_values_from_inner_text(row)
                _raw_attributes[attribute_name] = values
            return _raw_attributes

        def _transform_raw_resolve_level_attributes(raw_attrs: dict):
            transformed_attrs = {i: {} for i in range(1, 6)}
            for attribute_name, values in raw_attrs.items():
                for i, value in enumerate(values, start=1):
                    transformed_attrs[i].update({attribute_name: value})
            return transformed_attrs.items()

        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
        cls.pre_load(url)
        character_table = cls.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))

        raw_attributes = _get_hero_resolve_level_raw_attributes()
        yield from _transform_raw_resolve_level_attributes(raw_attributes)

    @classmethod
    def get_other_info(cls, hero):
        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
        cls.pre_load(url)

        character_table = cls.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))

        for row in character_table.find_elements(By.CSS_SELECTOR, f'tr')[-4:]:
            other_attribute_name, other_attribute_value = tuple([e for e in row.find_elements(By.CSS_SELECTOR, f'td')])
            other_attribute_name = str_matched_underscored_lower_from_inner_text(
                other_attribute_name,
                other_attrs_regex
            )
            other_attribute_value = str_from_inner_text(other_attribute_value)
            yield other_attribute_name, other_attribute_value

    @classmethod
    def get_resistances(cls, hero):
        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
        cls.pre_load(url)

        character_table = cls.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)')))

        for row in character_table.find_elements(By.CSS_SELECTOR, f'tr')[12:16]:
            elements = row.find_elements(By.CSS_SELECTOR, f'td')
            elements = [(elements[0], elements[1]), (elements[2], elements[3])]
            for name_element, value_element in elements:
                resistance_name = str_matched_underscored_lower_from_inner_text(name_element, resistances_regex)
                resistance_value = str_from_inner_text(value_element)
                yield resistance_name, resistance_value

    # @classmethod
    # def get_skills(cls, hero):
    #     parsed = re.sub(r' ', '_', hero.name)
    #     url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'
    #     cls.pre_load(url)
    #
    #     cls.wait.until(EC.presence_of_element_located(
    #         (By.XPATH, f'//span[text()="Combat Skills" or text()="Combat Abilities"]')))
    #
    #     table_selector = f'table.wikitable.tablebg[style*="text-align:center"]'
    #     elements = cls.driver.find_elements(By.CSS_SELECTOR, table_selector)
    #     assert elements is not None and len(elements) > 0
    #
    #     for table in elements:
    #         try:
    #             skill_name = table.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > th') \
    #                 .get_attribute('innerText')
    #
    #             if skip_regex.search(skill_name):
    #                 continue
    #             logger.info(f'skill_name: {skill_name}')
    #             kwargs = {"skill_name": skill_name}
    #         except:
    #             try:
    #                 if not cls.driver.find_element(By.XPATH, f'//span[text()="Shieldbreaker"]'):
    #                     logger.error(traceback.format_exc())
    #             except:
    #                 logger.error(traceback.format_exc())
    #                 with open(r'lolmao.png', 'wb') as file:
    #                     file.write(table.screenshot_as_png)
    #             continue
    #
    #         try:
    #             info_row = table.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(3)")
    #         except Exception as _:
    #             logger.error(traceback.format_exc())
    #             continue
    #
    #         try:
    #             titles_row = table.find_element(By.CSS_SELECTOR, 'tbody > tr[class="accent1tablecell"]')
    #         except Exception as _:
    #             logger.error(traceback.format_exc())
    #             continue
    #
    #         for i, col in enumerate(titles_row.find_elements(By.CSS_SELECTOR, 'td')[1:], start=1):
    #             skill_attribute_name = str_from_inner_text(col)
    #             logger.info(skill_attribute_name)
    #             skill_attribute_name = skill_attributes_regex.search(skill_attribute_name).group()
    #
    #
    #
    #             skill_attribute_name, value_obtaining_function, value_modifying_function = \
    #                 skill_kwargs[skill_attribute_name]
    #
    #             value = info_row.find_element(By.CSS_SELECTOR, f'td:nth-child({i})')
    #             value = value_obtaining_function(value)
    #             value = value_modifying_function(value)
    #
    #             kwargs[skill_attribute_name] = value
    #
    #         logger.info(f'kwargs:\n{pretty(kwargs)}')
    #         skill = SkillModel(**kwargs)
    #         logger.info(f'New skill: {skill}')
    #         yield skill
