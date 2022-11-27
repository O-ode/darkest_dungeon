from pprint import pformat


class CharacterLevelModel:

    def __init__(self, max_hp, dodge, prot, spd, acc_mod, crit, dmg):
        self.max_hp: int = max_hp
        self.dodge: float = dodge
        self.prot: int = prot
        self.spd: int = spd
        self.acc_mod: int = acc_mod
        self.crit: int = crit
        self.dmg: str = dmg

    def __str__(self):
        return pformat(self.__dict__)

    def __repr__(self):
        return pformat(self.__dict__)
