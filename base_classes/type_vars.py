from typing import TypeVar

from base_classes.resistances import Stun, Move, Blight, Bleed, Disease, Debuff, DeathBlow, Trap

ResistanceType = TypeVar("ResistanceType", Stun, Move, Blight, Bleed, Disease, Debuff, DeathBlow, Trap)
