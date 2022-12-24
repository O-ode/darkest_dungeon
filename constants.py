import re
from enum import Enum, IntFlag, StrEnum, auto
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, sort_dicts=False)
stats = ["MAX HP", "DODGE", "PROT", "SPD", "ACC MOD", "CRIT", "DMG"]
level_levels = [1, 2, 3, 4, 5]

percentage_regex = re.compile(r'([+\-]?\s*\d+)(\.\d+)?%?', re.I)
range_regex = re.compile(r'(\d+)\s*-\s*(\d+)', re.I)


class Effects(Enum):
    BLEED: re.Pattern = re.compile(r"bleed.*\d+", re.I)
    BLIGHT: re.Pattern = re.compile(r"Blight.*\d+", re.I)
    DMG_VS_MARKED: re.Pattern = re.compile(r"\+\d+%.*DMG.*vs.*Marked", re.I)
    FORWARD: re.Pattern = re.compile(r"Forward.*\d+", re.I)
    KNOCKBACK: re.Pattern = re.compile(r"Knockback.*\d+", re.I)
    STUN: re.Pattern = re.compile(r"stun.*\d+", re.I)


# noinspection PyArgumentList
class PositionFlag(IntFlag):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()
    SELF = auto()
    ALSO_SELF = auto()
    SIMULTANEOUS = auto()

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


# noinspection PyArgumentList
class SkillBooleans(IntFlag):
    CRIT_VALID = auto()
    STALL_INVALIDATING = auto()
    GENERATION_GUARANTEED = auto()


class SkillTypeEnum(StrEnum):
    MELEE = "melee"
    RANGED = "ranged"
    MOVE = "move"


def pretty(obj):
    return pp.pformat(obj)
