import itertools
import logging
import re
import traceback
from typing import Any, Generator

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from constants import pretty, skip_regex
from driver_singleton import DriverSingleton
from factories.web_element_value_factory import WebElementValueFactory
from model.hero_model import HeroModel
from model.skill.kwargs import skill_kwargs

logger = logging.getLogger()


class HeroDAO:
    @classmethod
    def get_level_attributes(cls, hero: HeroModel) -> Generator[dict[str, str], Any, None]:
        raw_attributes = \
            [[WebElementValueFactory.str_underscored_lower_from_inner_text(element) for element in elements_row]
             for elements_row in HeroSeleniumDAO.get_level_attributes_elements(hero)]

        raw_attributes = {row[0]: row[1:] for row in raw_attributes}
        for i in range(5):
            level_attrs = {name: values[i] for name, values in raw_attributes.items()}
            logger.info(pretty(level_attrs))
            yield level_attrs

    @classmethod
    def get_resistances(cls, hero) -> Generator[dict[str, str], Any, None]:
        for name_element, value_element in HeroSeleniumDAO.get_resistances(hero):
            resistance_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
            resistance_value = WebElementValueFactory.str_text_from_inner_text(value_element)
            yield {'name': resistance_name, 'value': resistance_value}

    @classmethod
    def get_other_info(cls, hero) -> Generator[dict[str, str], Any, None]:
        for name_element, value_element in HeroSeleniumDAO.get_other_info(hero):
            other_attribute_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
            other_attribute_value = WebElementValueFactory.str_text_from_inner_text(value_element)
            yield {'name': other_attribute_name, 'value': other_attribute_value}

    @classmethod
    def get_skills(cls, hero) -> Generator[dict[str, str], Any, None]:

        for i, skill_table_attrs in enumerate(HeroSeleniumDAO.get_skills(hero)):
            logger.info(f'skill_table_attrs: {pretty(skill_table_attrs)}')
            factory_values = {}
            # factory_values["skill_name"] = \
            #     WebElementValueFactory.str_underscored_lower_from_inner_text(skill_table_attrs["skill_name"])
            # logger.info(f'factory_values: {factory_values}')

            skill_name = WebElementValueFactory.str_underscored_lower_from_inner_text(skill_table_attrs["skill_name"])
            factory_values['skill_name'] = skill_name

            if 'limit' in skill_table_attrs.keys():
                limit = WebElementValueFactory.str_text_from_inner_text(skill_table_attrs["limit"])
            else:
                limit = None
            factory_values['limit'] = limit

            skill_attribute_names = \
                [WebElementValueFactory.str_underscored_lower_from_inner_text(e)
                 for e in skill_table_attrs['title_elements']]

            temp_values = {zipped[0]: [v for v in zipped[1:] if v is not None]
                           for zipped in itertools.zip_longest(
                    *[skill_attribute_names, *skill_table_attrs['value_elements']]
                )}

            for attr_name, attr_values in temp_values.items():
                if 'effect' == attr_name:
                    _, value_factory_method = skill_kwargs[attr_name]
                    on_target_on_other_heroes = {'on_target': [], 'on_other_heroes': []}
                    for value in attr_values:
                        res = value_factory_method(value)
                        on_target_on_other_heroes['on_target'].append(res['on_target'])
                        on_target_on_other_heroes['on_other_heroes'].append(res['on_other_heroes'])
                    factory_values.update(on_target_on_other_heroes)
                else:
                    skill_attr_name, value_factory_method = skill_kwargs[attr_name]
                    transformed_values = [value_factory_method(value) for value in attr_values]

                    factory_values[skill_attr_name] = transformed_values[0] \
                        if len(transformed_values) == 1 \
                           and attr_name not in ['damage', 'accuracy', 'crit_mod', 'effect', 'self', 'heal'] \
                        else transformed_values

            # factory_values['leveled_attributes'] = []
            # # logger.info(f'factory_values: {pretty(factory_values)}')
            # for attribute_value_row in skill_table_attrs['value_elements']:
            #     level_attributes = {}
            #
            #     for tup in zip(skill_attribute_names, attribute_value_row):
            #         skill_attr_name = tup[0]
            #         attribute_value_element = tup[1]
            #
            #         if 'effect' == skill_attr_name:
            #             _, value_factory_method = skill_kwargs[skill_attr_name]
            #             logger.info(f'tup: {pretty(tup)}')
            #             level_attributes.update(value_factory_method(attribute_value_element))
            #         else:
            #             skill_attr_name, value_factory_method = skill_kwargs[skill_attr_name]
            #             skill_attr_value = value_factory_method(attribute_value_element)
            #             if 'rank' == skill_attr_name:
            #                 skill_attr_value = [v for v in skill_attr_value[::-1]]
            #             level_attributes[skill_attr_name] = skill_attr_value
            #
            #     factory_values['leveled_attributes'].append(level_attributes)
            # first_row = factory_values['leveled_attributes'][0]
            # factory_values['target'] = first_row.pop('target')
            # factory_values['rank'] = first_row.pop('rank')
            # if 'range' in first_row.keys():
            #     factory_values['range'] = first_row.pop('range')

            logger.info(f'factory_values: {pretty(factory_values)}')
            yield factory_values

            # for name_element, attr_element in iter(skill_table_attrs):
            #     logger.info(f'name_element: {name_element}')
            #     skill_attr_name = WebElementValueFactory.str_underscored_lower_from_inner_text(name_element)
            #     logger.info(f'skill_attr_name: {skill_attr_name}')
            #
            #     if 'effect' == skill_attr_name:
            #         _, value_factory_method = skill_kwargs[skill_attr_name]
            #         factory_values.update(value_factory_method(attr_element))
            #     else:
            #         skill_attr_name, value_factory_method = skill_kwargs[skill_attr_name]
            #         skill_attr_value = value_factory_method(attr_element)
            #         if 'rank' == skill_attr_name:
            #             skill_attr_value = [v for v in skill_attr_value[::-1]]
            #         factory_values[skill_attr_name] = skill_attr_value
            #
            # if 'limit' not in factory_values.keys():
            #     factory_values['limit'] = None


class HeroSeleniumDAO:

    @classmethod
    def get_level_attributes_elements(cls, hero: HeroModel) -> list[list[WebElement]]:
        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'

        if DriverSingleton.get_driver().current_url != url:
            DriverSingleton.get_driver().get(url)

        character_table = DriverSingleton.get_wait().until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)'))
        )

        for row in iter(character_table.find_elements(By.CSS_SELECTOR, f'tr')[3:11]):
            yield row.find_elements(By.CSS_SELECTOR, f'td')

    @classmethod
    def get_other_info(cls, hero):
        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'

        if DriverSingleton.get_driver().current_url != url:
            DriverSingleton.get_driver().get(url)

        character_table = DriverSingleton.get_wait().until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)'))
        )

        for row in character_table.find_elements(By.CSS_SELECTOR, f'tr')[-4:]:
            other_attribute_name, other_attribute_value = tuple(row.find_elements(By.CSS_SELECTOR, f'td'))
            yield other_attribute_name, other_attribute_value

    @classmethod
    def get_resistances(cls, hero):
        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'

        if DriverSingleton.get_driver().current_url != url:
            DriverSingleton.get_driver().get(url)

        character_table = DriverSingleton.get_wait().until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.charactertable > tbody:nth-child(1)'))
        )

        for row in character_table.find_elements(By.CSS_SELECTOR, f'tr')[12:16]:
            elements = row.find_elements(By.CSS_SELECTOR, f'td')
            elements = [(elements[0], elements[1]), (elements[2], elements[3])]
            for name_element, value_element in elements:
                yield name_element, value_element

    @classmethod
    def get_skills(cls, hero):
        parsed = re.sub(r' ', '_', hero.name)
        url = f'https://darkestdungeon.fandom.com/wiki/{parsed}'

        if DriverSingleton.get_driver().current_url != url:
            DriverSingleton.get_driver().get(url)

        _ = DriverSingleton.get_wait().until(
            EC.presence_of_element_located((By.XPATH, f'//span[text()="Combat Skills" or text()="Combat Abilities"]'))
        )

        table_selector = f'table.wikitable.tablebg[style*="text-align:center"]'
        tables = DriverSingleton.get_driver().find_elements(By.CSS_SELECTOR, table_selector)
        assert tables is not None and len(tables) > 0

        for table in tables:
            table_attrs = {}
            try:
                skill_name_element = table.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > th')
                skill_name = skill_name_element.get_attribute('innerText')

                if skip_regex.search(skill_name):
                    logger.warning(f'not recognized: {skill_name}')
                    continue
                logger.info(f'skill_name: {skill_name}')
                table_attrs['skill_name'] = skill_name_element

                # skill_attributes_elements = [skill_name_element]

            except:
                try:
                    if not DriverSingleton.get_driver().find_element(By.XPATH, f'//span[text()="Shieldbreaker"]'):
                        logger.error(traceback.format_exc())
                except:
                    logger.error(traceback.format_exc())
                    with open(r'lolmao.png', 'wb') as file:
                        file.write(table.screenshot_as_png)
                continue

            titles_row = table.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(2)')
            title_elements = titles_row.find_elements(By.CSS_SELECTOR, 'td')[:0:-1]
            [logger.debug(WebElementValueFactory.str_underscored_lower_from_inner_text(e)) for e in title_elements]
            table_attrs['title_elements'] = title_elements

            values_row = table.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child(3)")
            value_elements = values_row.find_elements(By.CSS_SELECTOR, 'td')[::-1]
            table_attrs['value_elements'] = [value_elements]

            # if table.find_element(By.XPATH, f'//span[text()="Limit"]'):
            #     limit_name_element = table.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(5) > td:nth-child(1)')
            #     limit_value_element = table.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(5) > td:nth-child(2)')
            #     skill_attributes_elements.append(tuple([limit_name_element, limit_value_element]))

            # skill_attributes_elements.extend(((tup[0], tup[1]) for tup in zip(title_elements, value_elements)))
            logger.info(f'table_attrs: {pretty(table_attrs)}')

            table.find_element(By.CSS_SELECTOR, f'table.mw-collapsed:nth-child(1)') \
                .find_element(By.XPATH, f'//*[text()="Expand"]') \
                .click()

            inner_table = table.find_element(
                By.CSS_SELECTOR,
                f'tbody:nth-child(1) > tr:nth-child(4) > th:nth-child(1) > table:nth-child(1) > tbody:nth-child(1)'
            )

            [table_attrs['value_elements'].append(row.find_elements(By.CSS_SELECTOR, f'td')[:0:-1])
             for row in inner_table.find_elements(By.CSS_SELECTOR, f'tr')[1:5]]

            try:
                limit_value_element = table.find_element(
                    By.CSS_SELECTOR,
                    f'tbody:nth-child(1) > tr:nth-child(5) > td.infoboxlabel.infoboxcellaccent + td'
                )
                table_attrs['limit'] = limit_value_element
            except:
                logger.warning(f'Couldn\'t find limit for skill')
                pass

            # skill_attributes_elements.clear()
            # temp_value_elements = row.find_elements(By.CSS_SELECTOR, f'td')[1:]
            # skill_attributes_elements.extend(
            #     ((tup[0], tup[1]) for tup in zip(title_elements, temp_value_elements))
            # )
            # yield skill_attributes_elements
            # table_attrs['value_elements'].append(row.find_elements(By.CSS_SELECTOR, f'td')[1:])
            yield table_attrs
