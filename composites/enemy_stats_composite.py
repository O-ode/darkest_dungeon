from typing import Any

from base_classes.stats_attributes import Dodge, Prot, Spd, HP
from composites.stats_composite import StatsBaseComposite
from factories.enemy_factory import EnemyFactory


class EnemyStatsComposite(StatsBaseComposite):

    def __init__(self, factory):
        self._factory: EnemyFactory = factory  # Need to write EnemyFactoryType
        self._hp: HP or None = None  # level
        self._spd: Spd or None = None  # level
        self._prot: Prot or None = None  # level
        self._dodge: Dodge or None = None  # level

    def set_hp(self, value: Any):
        self._hp.append(self._factory.prepare_hp(value))
        return self

    def set_spd(self, value: Any):
        self._spd.append(self._factory.prepare_spd(value))
        return self

    def set_prot(self, value: Any):
        self._prot.append(self._factory.prepare_prot(value))
        return self

    def set_dodge(self, value: Any):
        self._dodge.append(self._factory.prepare_dodge(value))
        return self

    def get_hp(self) -> HP:
        return self._hp

    def get_spd(self) -> Spd:
        return self._spd

    def get_prot(self) -> Prot:
        return self._prot

    def get_dodge(self) -> Dodge:
        return self._dodge
