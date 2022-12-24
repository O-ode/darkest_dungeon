import logging
import re

from base_classes.int_over_rounds import IntOverRounds
from base_classes.skill_attributes import Effect
from constants import percentage_regex, range_regex, SkillTypeEnum, PositionFlag, SkillBooleans

logger = logging.getLogger()


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
    def merge_skill_booleans(cls, **kwargs) -> SkillBooleans:
        mapping = {'is_crit_valid': SkillBooleans.CRIT_VALID,
                   'is_stall_invalidating': SkillBooleans.STALL_INVALIDATING,
                   'generation_guaranteed': SkillBooleans.GENERATION_GUARANTEED}

        flag = 0
        for k, v in iter(kwargs.items()):
            if v:
                flag |= mapping[k]

        return SkillBooleans(flag)

    @classmethod
    def str_to_skill_type(cls, s: str) -> SkillTypeEnum:
        for item in list(SkillTypeEnum):
            if s == item.value:
                return item

    @classmethod
    def int_array_to_position_flag(cls, values: list[int]) -> PositionFlag:
        # do not delete
        mapping = {'1': 0,
                   '2': 1,
                   '3': 2,
                   '4': 3,
                   '': 4,
                   '@': 5,
                   '~': 6}
        positions = list(PositionFlag)
        position_flag = PositionFlag(positions[values[0]])
        logger.info(position_flag)
        for position in values[1:]:
            position_flag = position_flag | positions[position]
            logger.info(position_flag)
        return position_flag

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
