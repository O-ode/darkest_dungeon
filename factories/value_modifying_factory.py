import multiprocessing as mp
import re

from base_classes.int_over_rounds import IntOverRounds
from base_classes.skill_attributes import Effect
from constants import percentage_regex, range_regex, SkillTypeEnum, PositionFlag, SkillBooleans

logger = mp.get_logger()


class ValueModifyingFactory:

    @classmethod
    def do_nothing(cls, obj):
        return obj

    @classmethod
    def text_to_effect_per_line(cls, s: str):
        return [Effect(line) for line in s.split('\n') if line != ""]

    @classmethod
    def text_to_float_div_100(cls, s: str):
        try:
            num = percentage_regex.search(s).group(1)
        except AttributeError:
            return 0
        return float(num) / 100

    @classmethod
    def text_to_int_range(cls, s: str):
        split = re.split(r'[\- ]', s)
        lower = ValueModifyingFactory.text_to_int(split[0])
        upper = ValueModifyingFactory.text_to_int(split[1])
        return lower, upper

    @classmethod
    def text_to_int(cls, s: str):
        return int(s)

    @classmethod
    def text_to_one_int_from_regex(cls, s: str):
        return int(re.search(r'\d+', s).group())

    @classmethod
    def text_to_lines(cls, s: str):
        return s.split('\n')

    @classmethod
    def text_to_int_or_int_tuple(cls, s: str):
        match = range_regex.search(s)
        if match:
            lower, higher = match.group(1), match.group(2)
            return lower, higher
        else:
            return cls.text_to_int(s)

    @classmethod
    def merge_skill_booleans(cls, is_crit_valid=True, is_continue_turn=False, generation_guaranteed=False,
                             ignore_guard=False, ignore_stealth=False, ignore_protection=False,
                             refresh_after_each_wave=False, is_stall_invalidating=True) -> SkillBooleans:
        mapping = {
            'is_continue_turn': SkillBooleans.CONTINUE_TURN,
            'is_crit_valid': SkillBooleans.CRIT_VALID,
            'generation_guaranteed': SkillBooleans.GENERATION_GUARANTEED,
            'ignore_guard': SkillBooleans.IGNORE_GUARD,
            'ignore_stealth': SkillBooleans.IGNORE_STEALTH,
            'ignore_protection': SkillBooleans.IGNORE_PROTECTION,
            'refresh_after_each_wave': SkillBooleans.REFRESH_AFTER_EACH_WAVE,
            'is_stall_invalidating': SkillBooleans.STALL_INVALIDATING
        }

        flag = 0
        if is_crit_valid:
            flag |= mapping['is_crit_valid']
            logger.debug(flag)
        if is_continue_turn:
            flag |= mapping['is_continue_turn']
            logger.debug(flag)
        if generation_guaranteed:
            flag |= mapping['generation_guaranteed']
            logger.debug(flag)
        if ignore_guard:
            flag |= mapping['ignore_guard']
            logger.debug(flag)
        if ignore_stealth:
            flag |= mapping['ignore_stealth']
            logger.debug(flag)
        if ignore_protection:
            flag |= mapping['ignore_protection']
            logger.debug(flag)
        if refresh_after_each_wave:
            flag |= mapping['refresh_after_each_wave']
            logger.debug(flag)
        if is_stall_invalidating:
            flag |= mapping['is_stall_invalidating']
            logger.debug(flag)

        return SkillBooleans(flag)

    @classmethod
    def str_to_skill_type(cls, s: str) -> SkillTypeEnum:
        for item in list(SkillTypeEnum):
            if re.search(item.value, s, re.I):
                return item

    @classmethod
    def str_to_position_flag(cls, values: str) -> PositionFlag:
        # do not delete
        mapping = {'S': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '@': 5,
                   '~': 6,
                   '?': 7}
        flag = PositionFlag(0)
        if len(values) == 0:
            values = 'S'
        logger.info(f'HERE: {repr(values)}')
        for letter in values:
            position_index = mapping[letter]
            flag |= PositionFlag(2 ** position_index)
        logger.info(f'HERE: {flag}')
        return flag

    @classmethod
    def text_to_int_over_rounds(cls, value: str) -> IntOverRounds:
        match = re.match(r'(\d+) pts/rd for (\d+) rds', value)
        return IntOverRounds(match.group(1), match.group(2))

    @classmethod
    def text_to_hp_modification_value(cls, value: str) -> float or IntOverRounds or int:
        if '%' in value:
            return cls.text_to_float_div_100(value)
        if '-' in value:
            return cls.text_to_int_range(value)
        elif 'rds' in value:
            return cls.text_to_int_over_rounds(value)
        else:
            return cls.text_to_int(value)

    @classmethod
    def text_to_effect_list(cls, value: str):
        effect_line_list = []
        for v in re.split(r'\n', value):
            p = v.replace('\n', '')
            if p != '':
                effect_line_list.append(Effect(p))
        return effect_line_list
