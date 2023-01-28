from enum import IntFlag, auto

from base_classes.basic_attribute import BasicAttribute


class Size(BasicAttribute):
    pass


class MonsterBrain(BasicAttribute):
    pass


class DeathClass(BasicAttribute):
    pass


class Loot(BasicAttribute):
    pass


class Initiative(BasicAttribute):
    pass


# noinspection PyArgumentList
class BattleModifier(IntFlag):
    ACCELERATE_STALL_PENALTY = auto()
    DISABLE_STALL_PENALTY = auto()
    CAN_SURPRISE = auto()
    CAN_BE_SURPRISED = auto()
    ALWAYS_SURPRISE = auto()
    ALWAYS_BE_SURPRISED = auto()


"accelerate_stall_penalty"
"disable_stall_penalty"
"can_surprise"
"can_be_surprised"
"always_surprise"
"always_be_surprised"
