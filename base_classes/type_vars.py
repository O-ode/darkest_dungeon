from typing import TypeVar
from base_classes.other_hero_attributes import *
from base_classes.resistances import *

from model.character_attributes.base_attributes import BaseLevelAttributesModel
from model.character_attributes.hero_attributes import HeroLevelAttributesModel

DerivedFromBasicAttributes = TypeVar("DerivedFromBasicAttributes", BaseLevelAttributesModel,
                                     HeroLevelAttributesModel)

DerivedFromResistanceBase = TypeVar("DerivedFromResistanceBase", ResistanceBase, Stun, Move, Blight, Bleed, Disease,
                                    Debuff, DeathBlow, Trap)

DerivedFromOtherAttributeBase = TypeVar("DerivedFromOtherAttributeBase", OtherAttributeBase, Movement, CritBuffBonus,
                                        Religious)