import logging

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from model.kwargs import resistance_model_kwargs
from selenium_local.value_retrieving_functions import find_element_and_get_str_from_innerText, value_from_innerText

logger = logging.getLogger()


def _get_resistance_values(row):
    logger.info(f'Getting resistance values')
    elements = row.find_elements(By.CSS_SELECTOR, f'td')
    elements = [(elements[0], elements[1]), (elements[2], elements[3])]
    for name_element, value_element in elements:
        resistance_name = find_element_and_get_str_from_innerText(name_element, f'a:nth-child(2)',
                                                                  r"(stun|blight|disease|death_blow|move|bleed|debuff|trap)")
        logger.info(resistance_name)

        resistance_value = value_from_innerText(value_element)
        logger.info(resistance_name)

        value_modifying_function = resistance_model_kwargs[resistance_name]
        resistance_value = value_modifying_function(resistance_value)

        yield resistance_name, resistance_value


# def _get_resolve_lvl_attribute(row: WebElement):
#     logger.info(f'Getting resolve level values')
#     lvl_attribute_name = unicodedata.normalize('NFKD',
#                                           row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)')
#                                           .get_attribute("innerText"))
#     lvl_attribute_name = re.search(r"(MAX\s*HP|DODGE|PROT|SPD|ACC\s*MOD|CRIT|DMG)", lvl_attribute_name, re.I).group()
#     lvl_attribute_name = re.sub(r'\s+', '_', lvl_attribute_name).lower()
#     values_obtaining_function, value_modifying_function = \
#         character_level_kwargs[lvl_attribute_name]
#
#     values = values_obtaining_function(row)
#     values = [value_modifying_function(value) for value in values]
#     return lvl_attribute_name, values


def _get_other_info_of_character(row: WebElement):
    logger.info(f'Getting other info')
    lvl_attribute = unicodedata.normalize('NFKD',
                                          row.find_element(By.CSS_SELECTOR, f'td:nth-child(1)')
                                          .get_attribute("innerText"))

    pass
