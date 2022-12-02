import logging
import re
import traceback

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from constants import colored_dots_regex

logger = logging.getLogger()


def value_from_dots(value: WebElement):
    try:
        r_value = value_from_innerText(value)
        if r_value != '':
            logger.info(f'Returning text instead of dots: {r_value}')
            return r_value
    except:
        logger.error(traceback.print_exc())

    def gen_from_dots():
        # table.wikitable: nth - child(15) > tbody:nth - child(1) > tr: nth - child(3) > td:nth - child(
        #     2) > div: nth - child(1) > img:nth - child(3)
        for j, dot in enumerate(value.find_elements(By.CSS_SELECTOR, f'div img'), start=1):
            temp = dot.get_attribute('alt')
            temp = unicodedata.normalize('NFKD', temp)
            if colored_dots_regex.search(temp) is not None:
                yield j
            else:
                continue

    return list(gen_from_dots())


def find_element_and_get_str_from_innerText(root_element: WebElement, css_selector: str, r_string: str):
    s = root_element.find_element(By.CSS_SELECTOR, css_selector).get_attribute("innerText")
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r'\s+', '_', s).lower()
    s = re.search(r_string, s, re.I).group()
    return s



def value_from_innerText(element: WebElement):
    return unicodedata.normalize('NFKD', element.get_attribute('innerText'))


def character_level_values_from_innerText(row: WebElement):
    return [cell.get_attribute("innerText") for cell in
            row.find_elements(By.CSS_SELECTOR, f'td')[1:]]
