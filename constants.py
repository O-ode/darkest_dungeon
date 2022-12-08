import inspect
import re
import sys
from enum import Enum, IntFlag, auto
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, sort_dicts=False)
stats = ["MAX HP", "DODGE", "PROT", "SPD", "ACC MOD", "CRIT", "DMG"]
resolve_levels = [1, 2, 3, 4, 5]

colored_dots_regex = re.compile(r'(Yellow|Red) dot\.png', re.I)
damage_regex = re.compile(r'([+\-]?\d+)%?', re.I)
flags_for_effect_regex = re.compile(r'(Other\s+Heroes:)', re.I)
range_regex = re.compile(r'(\d+)-(\d+)', re.I)
range_values_regex = re.compile(r'(Melee|Ranged)', re.I)
skill_attributes_regex = re.compile(r'(Range|Rank|Target|Damage|Accuracy|Crit\s+mod|Effect|Self|Heal)', re.I)
skip_regex = re.compile(r'(Expand|Further\s*levels)', re.I)
resolve_level_attributes_regex = re.compile(r"(max_hp|dodge|prot|spd|acc_mod|crit|dmg)", re.I)
other_attrs_regex = re.compile(r"(movement|crit_buff_bonus|religious|provisions)", re.I)
resistances_regex = re.compile(r"(bleed|blight|disease|debuff|death_blow|trap|stun|move)")

classes = [value for name, value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]


class Position(IntFlag):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()


class RangeEnum(Enum):
    MELEE: re.Pattern = re.compile(r"Melee", re.I)
    RANGED: re.Pattern = re.compile(r"Ranged", re.I)

    @classmethod
    def from_string(cls, s: str):
        values = {item.value for item in Range}
        return s in values


class Effects(Enum):
    BLEED: re.Pattern = re.compile(r"bleed.*\d+", re.I)
    BLIGHT: re.Pattern = re.compile(r"Blight.*\d+", re.I)
    DMG_VS_MARKED: re.Pattern = re.compile(r"\+\d+%.*DMG.*vs.*Marked", re.I)
    FORWARD: re.Pattern = re.compile(r"Forward.*\d+", re.I)
    KNOCKBACK: re.Pattern = re.compile(r"Knockback.*\d+", re.I)
    STUN: re.Pattern = re.compile(r"stun.*\d+", re.I)


def pretty(obj):
    return pp.pformat(obj)
