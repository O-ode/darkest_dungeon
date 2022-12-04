import inspect
import re
import sys
from enum import Enum
from pprint import pformat

stats = ["MAX HP", "DODGE", "PROT", "SPD", "ACC MOD", "CRIT", "DMG"]
resolve_levels = [1, 2, 3, 4, 5]

colored_dots_regex = re.compile(r'(Yellow|Red) dot\.png', re.I)
damage_regex = re.compile(r'([+\-]?\d+)%?', re.I)
flags_for_effect_regex = re.compile(r'(Other\s+Heroes:)', re.I)
range_regex = re.compile(r'(\d+)-(\d+)', re.I)
range_values_regex = re.compile(r'(Melee|Ranged)', re.I)
skill_attributes_regex = re.compile(r'(Range|Rank|Target|Damage|Accuracy|Crit\s+mod|Effect|Self|Heal)', re.I)
skip_regex = re.compile(r'(Expand|Further\s*levels)', re.I)
resolve_level_attributes_regex = re.compile(r"(MAX\s*HP|DODGE|PROT|SPD|ACC\s*MOD|CRIT|DMG)", re.I)

classes = [value for name, value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]


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


def pretty(obj):
    return pformat(obj, indent=4)
