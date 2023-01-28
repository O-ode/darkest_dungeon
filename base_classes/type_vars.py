from typing import TypeVar

from base_classes.enemy_stats_composite import EnemyStatsComposite
from base_classes.hero_stats_composite import HeroStatsComposite
from base_classes.resistances import Stun, Move, Blight, Bleed, Disease, Debuff, DeathBlow, Trap
from model.skill.enemy_skills.enemy_skill import EnemySkill
from model.skill.hero_combat_skills.hero_heal_combat_skill import HeroHealCombatSkill
from model.skill.hero_combat_skills.hero_offensive_combat_skill import HeroOffensiveCombatSkill

ResistanceType = TypeVar("ResistanceType", Stun, Move, Blight, Bleed, Disease, Debuff, DeathBlow, Trap)
StatsType = TypeVar("StatsType", HeroStatsComposite, EnemyStatsComposite)
CombatSkillType = TypeVar("CombatSkillType", HeroOffensiveCombatSkill, HeroHealCombatSkill, EnemySkill)
