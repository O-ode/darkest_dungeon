import itertools
import logging
import re
import traceback

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from constants import colored_dots_regex, flags_for_effect_regex

logger = logging.getLogger()


class WebElementValueFactory:

    @classmethod
    def value_from_dots(cls, value: WebElement):
        try:
            r_value = cls.str_text_from_inner_text(value)
            if re.search(r'self', r_value, re.I):
                return [0]
            elif r_value != '':
                logger.error(f'Returning text instead of dots: {r_value}')
                return r_value
        except:
            logger.error(traceback.print_exc())

        positions = []
        for j, dot in enumerate(value.find_elements(By.CSS_SELECTOR, f'div img')):
            temp = dot.get_attribute('alt')
            temp = unicodedata.normalize('NFKD', temp)
            if colored_dots_regex.search(temp) is not None:
                positions.append(j)
            else:
                continue
        assert len(positions) > 0
        return positions

    @classmethod
    def subdivide_hero_effects_from_inner_text(cls, element: WebElement):
        effects_str = cls.str_text_from_inner_text(element)
        return itertools.zip_longest(
            ['on_target', 'on_other_heroes'], flags_for_effect_regex.split(effects_str), fillvalue=''
        )

    @classmethod
    def str_text_from_inner_text(cls, element: WebElement):
        return unicodedata.normalize('NFKD', element.get_attribute('innerText')).lstrip().rstrip()

    @classmethod
    def str_underscored_lower_from_inner_text(cls, element: WebElement):
        return re.sub(r"\s+", "_",
                      unicodedata.normalize('NFKD', element.get_attribute('innerText')).lstrip().rstrip().lower()
                      )

    @classmethod
    def str_matched_underscored_lower_from_inner_text(cls, element: WebElement, r: re.Pattern):
        s = re.sub(r"\s+", "_",
                   unicodedata.normalize('NFKD', element.get_attribute('innerText')).lstrip().rstrip().lower()
                   )
        try:
            return r.search(s).group()
        except:
            logger.error(f'Did\'nt find regex {repr(r)} in str {s}')
            raise
