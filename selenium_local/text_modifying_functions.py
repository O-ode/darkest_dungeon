from constants import damage_regex, range_regex, flags_for_effect_regex
from model.effect_model import EffectModel


def do_nothing(obj):
    return obj


def text_to_effect_per_line(s: str):
    return [EffectModel(line) for line in s.split('\n') if line != ""]


def text_to_effects_dict(text: str):
    results = {}
    current_key = "Default"
    split_by_flag = flags_for_effect_regex.split(text)
    for i, s in enumerate(split_by_flag):
        if i % 2 == 0:
            results[current_key] = [EffectModel(st.rstrip()) for st in s.split('\n') if st != '']
        else:
            current_key = s
    return results


def text_to_float_div_100(s: str):
    try:
        num = damage_regex.search(s).group(1)
    except AttributeError:
        return 0
    return float(num) / 100


def text_to_int(s: str):
    return int(s)


def text_to_lines(s: str):
    return s.split('\n')


def text_to_range_or_int(s: str):
    match = range_regex.search(s)
    if match:
        lower, higher = match.group(1), match.group(2)
        return lower, higher
    else:
        return text_to_int(s)
