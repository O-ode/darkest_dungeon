from typing import Type, Any

from base_classes.enemy_attributes import Size, Loot, DeathClass, BattleModifier, MonsterBrain, Initiative
from base_classes.stats_attributes import Spd
from base_classes.type_vars import CombatSkillType, StatsType
from factories.enemy_factory import EnemyFactory
from model.character_model import CharacterComposite


class EnemyComposite(CharacterComposite):

    def get_stats(self) -> list[StatsType]:
        pass

    def get_combat_skills(self) -> list[CombatSkillType]:
        pass

    def __init__(self, factory: Type[EnemyFactory]):
        super(EnemyComposite, self).__init__(factory)
        self._size: Size | None = None
        self._initiative: Initiative | None = None
        self._monster_brain: MonsterBrain | None = None
        self._battle_modifier: BattleModifier | None = None

        self._loot: list[Loot] = []
        self._death_class: list[DeathClass] = []

    def add_loot(self, loot: Loot):
        self._loot.append(loot)
        return self

    def add_death_class(self, death_class: DeathClass):
        self._death_class.append(death_class)
        return self

    def set_prot(self, value: Any):
        self._prot = self._factory.prepare_prot(value)
        return self

    def get_prot(self):
        return self._prot

    def set_size(self, value: Any):
        self._size = self._factory.prepare_size(value)
        return self

    def get_size(self):
        return self._size

    def set_initiative(self, value: Any):
        self._initiative = self._factory.prepare_initiative(value)
        return self

    def get_initiative(self):
        return self._initiative

    def set_monster_brain(self, value: Any):
        self._monster_brain = self._factory.prepare_monster_brain(value)
        return self

    def get_monster_brain(self):
        return self._monster_brain

    def set_battle_modifier(self, value: Any):
        self._battle_modifier = self._factory.prepare_battle_modifier(value)
        return self

    def get_battle_modifier(self):
        return self._battle_modifier

    def set_dodge(self, value: Any):
        self._dodge = self._factory.prepare_dodge(value)
        return self

    def set_hp(self, value: Any):
        self._hp = self._factory.prepare_hp(value)
        return self

    def set_spd(self, value: Any):
        self._spd = self._factory.prepare_spd(value)
        return self

    def get_dodge(self):
        return self._dodge

    def get_hp(self):
        return self._hp

    def get_spd(self) -> Spd:
        return self._spd

    def get_loot(self) -> list[Loot]:
        return self._loot

    def get_death_class(self) -> list[DeathClass]:
        return self._death_class
