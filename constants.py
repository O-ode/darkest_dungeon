import re
from enum import Enum, IntFlag, StrEnum, auto
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, compact=False, sort_dicts=False)
stats = ["MAX HP", "DODGE", "PROT", "SPD", "ACC MOD", "CRIT", "DMG"]
level_levels = [1, 2, 3, 4, 5]

colored_dots_regex = re.compile(r'(Yellow|Red)\sdot.+png', re.I)
percentage_regex = re.compile(r'([+\-]?\s*\d+)%?', re.I)
flags_for_effect_regex = re.compile(r'Other\s+Heroes:', re.I)
range_regex = re.compile(r'(\d+)\s*-\s*(\d+)', re.I)
range_values_regex = re.compile(r'(Melee|Ranged)', re.I)
skill_attributes_regex = re.compile(r'(Range|Rank|Target|Damage|Accuracy|Crit\s+mod|Effect|Self|Heal)', re.I)
skip_regex = re.compile(r'(Expand|Further\s*levels)', re.I)
level_level_attributes_regex = re.compile(r"(max_hp|dodge|prot|spd|acc_mod|crit|dmg)", re.I)
resistances_regex = re.compile(r"(bleed|blight|disease|debuff|death_blow|trap|stun|move)")


class Effects(Enum):
    BLEED: re.Pattern = re.compile(r"bleed.*\d+", re.I)
    BLIGHT: re.Pattern = re.compile(r"Blight.*\d+", re.I)
    DMG_VS_MARKED: re.Pattern = re.compile(r"\+\d+%.*DMG.*vs.*Marked", re.I)
    FORWARD: re.Pattern = re.compile(r"Forward.*\d+", re.I)
    KNOCKBACK: re.Pattern = re.compile(r"Knockback.*\d+", re.I)
    STUN: re.Pattern = re.compile(r"stun.*\d+", re.I)


# noinspection PyArgumentList
class PositionFlag(IntFlag):
    SELF = 0
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()

    def __repr__(self):
        return f'PositionFlag.{self.name}: {self.value}'


class ResistancesEnum(StrEnum):
    STUN = r'stun'
    MOVE = r'move'
    BLIGHT = r'blight'
    BLEED = r'bleed'
    DISEASE = r'disease'
    DEBUFF = r'debuff'
    DEATH_BLOW = r'death_blow'
    TRAP = r'trap'


class RangeEnum(StrEnum):
    MELEE = "Melee"
    RANGED = "Ranged"
    SUPPORT = "Support"


def pretty(obj):
    return pp.pformat(obj)
