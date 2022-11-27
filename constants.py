import inspect
import logging
import re
import sys
import traceback
from enum import Enum

import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from model.effect_model import EffectModel

damage_regex = re.compile(r'([+\-]?\d+)%?', re.I)
range_regex = re.compile(r'(\d+)-(\d+)', re.I)
colored_dots_regex = re.compile(r'(Yellow|Red) dot\.png', re.I)
stats = ["MAX HP", "DODGE", "PROT", "SPD", "ACC MOD", "CRIT", "DMG"]
resolve_levels = [1, 2, 3, 4, 5]
classes = [value for name, value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
skill_attributes_regex = re.compile(r'(Range|Rank|Target|Damage|Accuracy|Crit\s+mod|Effect|Self|Heal)', re.I)
range_values_regex = re.compile(r'(Melee|Ranged)', re.I)

logger = logging.getLogger()


class Range(Enum):
    MELEE: re.Pattern = re.compile(r"Melee", re.I)
    RANGED: re.Pattern = re.compile(r"Ranged", re.I)


class Effects(Enum):
    BLEED: re.Pattern = re.compile(r"bleed.*\d+", re.I)
    BLIGHT: re.Pattern = re.compile(r"Blight.*\d+", re.I)
    DMG_VS_MARKED: re.Pattern = re.compile(r"\+\d+%.*DMG.*vs.*Marked", re.I)
    FORWARD: re.Pattern = re.compile(r"Forward.*\d+", re.I)
    KNOCKBACK: re.Pattern = re.compile(r"Knockback.*\d+", re.I)
    STUN: re.Pattern = re.compile(r"stun.*\d+", re.I)


def dont_modify(obj):
    return obj


def text_to_float_div_100(s: str):
    try:
        num = damage_regex.search(s).group(1)
    except AttributeError:
        return 0
    return float(num) / 100


def text_to_int(s: str):
    return int(s)


def text_to_lines(s: str):
    return s.split('\n')


def effects_from_lines(s: str):
    return [EffectModel(line) for line in s.split('\n') if line != ""]


def text_to_range_or_int(s: str):
    match = range_regex.search(s)
    if match:
        lower, higher = match.group(1), match.group(2)
        return lower, higher
    else:
        return text_to_int(s)


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
            logger.debug(temp)
            temp = unicodedata.normalize('NFKD', temp)
            logger.debug(temp)
            if colored_dots_regex.search(temp) is not None:
                yield j
            else:
                continue

    return list(gen_from_dots())


def value_from_innerText(value: WebElement):
    return unicodedata.normalize('NFKD', value.get_attribute('innerText'))


def character_level_values_from_innerText(row: WebElement):
    return [cell.get_attribute("innerText") for cell in
            row.find_elements(By.CSS_SELECTOR, f'td')[1:]]


character_level_kwargs = {
    "max_hp": (character_level_values_from_innerText, text_to_int),
    "dodge": (character_level_values_from_innerText, text_to_float_div_100),
    "prot": (character_level_values_from_innerText, text_to_float_div_100),
    "spd": (character_level_values_from_innerText, text_to_int),
    "acc_mod": (character_level_values_from_innerText, text_to_int),
    "crit": (character_level_values_from_innerText, text_to_float_div_100),
    "dmg": (character_level_values_from_innerText, dont_modify)
}

skill_kwargs = {
    "Range": ("on_range", value_from_innerText, dont_modify),
    "Rank": ("rank", value_from_dots, dont_modify),
    "Target": ("target", value_from_dots, dont_modify),
    "Damage": ("dmg_mod", value_from_innerText, text_to_float_div_100),
    "Accuracy": ("acc", value_from_innerText, text_to_int),
    "Crit mod": ("crit_mod", value_from_innerText, text_to_float_div_100),
    "Effect": ("effects", value_from_innerText, effects_from_lines),
    "Self": ("on_self", value_from_innerText, effects_from_lines),
    "Heal": ("heal", value_from_innerText, dont_modify)
}
