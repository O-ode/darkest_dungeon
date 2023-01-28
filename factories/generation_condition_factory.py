import re


class GenerationConditionFactory:

    @classmethod
    def prepare_bool_value(cls, value: str) -> bool:
        if re.search(r'true', value, re.I):
            b = True
        else:
            b = False
        return b

    @classmethod
    def prepare_str_value(cls, value: str) -> str:
        return value

    @classmethod
    def prepare_int_value(cls, value: str) -> int:
        return int(value)

    @classmethod
    def prepare_float_value(cls, value: str) -> float:
        return float(value)
