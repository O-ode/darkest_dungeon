import logging
import re
import traceback

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from constants import colored_dots_regex, PositionFlag

logger = logging.getLogger()


def value_from_dots(value: WebElement) -> PositionFlag or str:
    try:
        r_value = str_from_inner_text(value)
        if r_value != '':
            logger.info(f'Returning text instead of dots: {r_value}')
            return r_value
    except:
        logger.error(traceback.print_exc())

    def gen_from_dots():
        # table.wikitable: nth - child(15) > tbody:nth - child(1) > tr: nth - child(3) > td:nth - child(
        #     2) > div: nth - child(1) > img:nth - child(3)
        for j, dot in enumerate(value.find_elements(By.CSS_SELECTOR, f'div img')):
            temp = dot.get_attribute('alt')
            temp = unicodedata.normalize('NFKD', temp)
            if colored_dots_regex.search(temp) is not None:
                yield j
            else:
                continue

    gen = gen_from_dots()
    positions = list(PositionFlag)
    position_flag = PositionFlag(positions[next(gen)])
    for position in gen:
        position_flag = position_flag | positions[position]

    return position_flag


def str_from_inner_text(element: WebElement):
    return unicodedata.normalize('NFKD', element.get_attribute('innerText'))


def str_underscored_lower_from_inner_text(element: WebElement):
    return re.sub(r"\s+", "_",
                  unicodedata.normalize('NFKD', element.get_attribute('innerText')).lower().lstrip().rstrip()
                  )


def str_matched_underscored_lower_from_inner_text(element: WebElement, r: re.Pattern):
    s = re.sub(r"\s+", "_",
               unicodedata.normalize('NFKD', element.get_attribute('innerText')).lower().lstrip().rstrip()
               )
    try:
        return r.search(s).group()
    except:
        logger.error(f'Did\'nt find regex {repr(r)} in str {s}')
        raise
