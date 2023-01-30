from base_classes.stats_attributes import HP, Spd, Dodge
from composites.stats_composite import StatsBaseComposite
from base_classes.weapon_attributes import Dmg, Crit
from factories.hero_armor_factory import HeroArmorFactory
from factories.hero_weapon_factory import HeroWeaponFactory
from model.armor_model import Armor
from model.weapon_model import Weapon


class HeroStatsComposite(StatsBaseComposite):

    def __init__(self):
        self._armor: Armor = Armor(HeroArmorFactory)
        self._weapon: Weapon = Weapon(HeroWeaponFactory)

    def set_armor_name(self, value: str):
        self._armor.set_name(value)
        return self

    def set_weapon_name(self, value: str):
        self._weapon.set_name(value)
        return self

    def set_hp(self, value: str):
        self._armor.set_hp(value)
        return self

    def set_spd(self, value: str):
        self._weapon.set_spd(value)
        return self

    def set_prot(self, value: str):
        pass

    def set_dodge(self, value: str):
        self._armor.set_dodge(value)
        return self

    def set_dmg(self, value: list[str]):
        self._weapon.set_dmg(value)
        return self

    def set_crit(self, value: str):
        self._weapon.set_crit(value)
        return self

    def get_dmg(self) -> Dmg:
        return self._weapon.get_dmg()

    def get_crit(self) -> Crit:
        return self._weapon.get_crit()

    def get_hp(self) -> HP:
        return self._armor.get_hp()

    def get_spd(self) -> Spd:
        return self._weapon.get_spd()

    def get_prot(self) -> None:
        return None

    def get_dodge(self) -> Dodge:
        return self._armor.get_dodge()

    def get_armor(self) -> Armor:
        return self._armor

    def get_weapon(self) -> Weapon:
        return self._weapon
