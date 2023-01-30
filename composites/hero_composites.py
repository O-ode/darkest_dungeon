from typing import Type, Any

from base_classes.character_attributes import OverstressedModifier, HPReaction, DeathReaction, \
    QuirkModifier, IncompatiblePartyMember, ActivityModifier
from builders.flagellant_builder import FlagellantBuilder
from builders.hero_builder import HeroBuilder
from composites.hero_composite import HeroComposite
from factories.hero_factories.flagellant_factory import FlagellantFactory


class Abomination(HeroComposite):
    pass


class Antiquarian(HeroComposite):
    pass


class Arbalest(HeroComposite):
    pass


class BountyHunter(HeroComposite):
    pass


class Crusader(HeroComposite):
    pass


class GraveRobber(HeroComposite):
    pass


class Hellion(HeroComposite):
    pass


class Highwayman(HeroComposite):
    pass


class Houndmaster(HeroComposite):
    pass


class Jester(HeroComposite):
    pass


class Leper(HeroComposite):
    pass


class ManAtArms(HeroComposite):
    pass


class Occultist(HeroComposite):
    pass


class PlagueDoctor(HeroComposite):
    pass


class Vestal(HeroComposite):
    pass


class Flagellant(HeroComposite):
    def __init__(self, factory: Type[FlagellantFactory]):
        super(Flagellant, self).__init__(factory)
        self._activity_modifier: ActivityModifier or None = None
        self._overstressed_modifier: OverstressedModifier or None = None
        self._hp_reaction: HPReaction or None = None
        self._death_reaction: list[DeathReaction] = []
        self._quirk_modifier: QuirkModifier or None = None
        self._incompatible_party_member: IncompatiblePartyMember or None = None

    def set_activity_modifier(self, value: Any):
        self._activity_modifier = self._factory.prepare_activity_modifier(*value)
        return self

    def get_activity_modifier(self):
        return self._activity_modifier

    def set_overstressed_modifier(self, value: Any):
        self._overstressed_modifier = self._factory.prepare_overstressed_modifier(*value)
        return self

    def get_overstressed_modifier(self):
        return self._overstressed_modifier

    def set_hp_reaction(self, value: Any):
        self._hp_reaction = self._factory.prepare_hp_reaction(*value)
        return self

    def get_hp_reaction(self):
        return self._hp_reaction

    def set_death_reaction(self, value: Any):
        self._death_reaction = self._factory.prepare_death_reaction(*value)
        return self

    def get_death_reaction(self):
        return self._death_reaction

    def set_quirk_modifier(self, value: Any):
        self._quirk_modifier = self._factory.prepare_quirk_modifier(*value)
        return self

    def get_quirk_modifier(self):
        return self._quirk_modifier

    def set_incompatible_party_member(self, value: Any):
        self._incompatible_party_member = self._factory.prepare_incompatible_party_member(*value)
        return self

    def get_incompatible_party_member(self):
        return self._incompatible_party_member

hero_builder_map = {'Abomination': HeroBuilder, 'Antiquarian': HeroBuilder, 'Arbalest': HeroBuilder,
                    'BountyHunter': HeroBuilder, 'Crusader': HeroBuilder, 'GraveRobber': HeroBuilder,
                    'Hellion': HeroBuilder, 'Highwayman': HeroBuilder, 'Houndmaster': HeroBuilder,
                    'Jester': HeroBuilder, 'Leper': HeroBuilder, 'ManAtArms': HeroBuilder, 'Occultist': HeroBuilder,
                    'PlagueDoctor': HeroBuilder, 'Vestal': HeroBuilder, 'Flagellant': FlagellantBuilder}
