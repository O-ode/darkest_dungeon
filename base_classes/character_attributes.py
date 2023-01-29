from base_classes.basic_attribute import BasicAttribute
from base_classes.skill_attributes import Effect


class Tag(BasicAttribute):
    pass


class ActivityModifier:
    def __init__(self, override_valid_activity_ids: list[str], override_stress_removal_amount_low: int,
                 override_stress_removal_amount_high: int):
        self.override_valid_activity_ids = override_valid_activity_ids
        self.override_stress_removal_amount_low = override_stress_removal_amount_low
        self.override_stress_removal_amount_high = override_stress_removal_amount_high


class OverstressedModifier:
    def __init__(self, override_trait_type_ids: list[str], override_trait_type_chances: list[float]):
        self.override_trait_type_ids = override_trait_type_ids
        self.override_trait_type_chances = override_trait_type_chances


class HPReaction:
    def __init__(self, hp_ratio: float, is_under: bool, effects: list[Effect]):
        self.hp_ratio = hp_ratio
        self.is_under: bool = is_under
        self.effects = effects


class DeathReaction:
    def __init__(self, target_allies: bool, target_enemies: bool, effects: list[Effect]):
        self.target_allies = target_allies
        self.target_enemies = target_enemies
        self.effects = effects


class QuirkModifier:
    def __init__(self, incompatible_class_ids: list[str]):
        self.incompatible_class_ids = incompatible_class_ids


class IncompatiblePartyMember:
    def __init__(self, value_id: str, hero_tag: str):
        self.value_id = value_id
        self.hero_tag = hero_tag
