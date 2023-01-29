from base_classes.character_attributes import IncompatiblePartyMember, QuirkModifier, DeathReaction, HPReaction, \
    OverstressedModifier, ActivityModifier
from base_classes.skill_attributes import Effect
from factories.hero_factory import HeroFactory


class FlagellantFactory(HeroFactory):

    @classmethod
    def prepare_incompatible_party_member(cls, value_id: str, hero_tag: str):
        return IncompatiblePartyMember(value_id, hero_tag)

    @classmethod
    def prepare_quirk_modifier(cls, incompatible_class_ids: list[str]):
        return QuirkModifier(incompatible_class_ids)

    @classmethod
    def prepare_death_reaction(cls, target_allies: bool, target_enemies: bool, effects: list[Effect]):
        return DeathReaction(target_allies, target_enemies, effects)

    @classmethod
    def prepare_hp_reaction(cls, hp_ratio: float, is_under: bool, effects: list[Effect]):
        return HPReaction(hp_ratio, is_under, effects)

    @classmethod
    def prepare_overstressed_modifier(cls, override_trait_type_ids: str, override_trait_type_chances: float):
        return OverstressedModifier(override_trait_type_ids, override_trait_type_chances)

    @classmethod
    def prepare_activity_modifier(cls, override_valid_activity_ids: list[str], override_stress_removal_amount_low: int,
                                  override_stress_removal_amount_high: int):
        return ActivityModifier(override_valid_activity_ids, override_stress_removal_amount_low,
                                override_stress_removal_amount_high)
