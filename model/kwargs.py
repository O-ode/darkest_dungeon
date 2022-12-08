from selenium_local.text_modifying_functions import text_to_float_div_100, text_to_int, do_nothing, \
    text_to_effect_per_line, text_to_effects_dict
from selenium_local.value_retrieving_functions import character_level_values_from_inner_text, str_from_inner_text, \
    value_from_dots

character_level_kwargs = {
    "max_hp": (character_level_values_from_inner_text, text_to_int),
    "dodge": (character_level_values_from_inner_text, text_to_float_div_100),
    "prot": (character_level_values_from_inner_text, text_to_float_div_100),
    "spd": (character_level_values_from_inner_text, text_to_int),
    "acc_mod": (character_level_values_from_inner_text, text_to_int),
    "crit": (character_level_values_from_inner_text, text_to_float_div_100),
    "dmg": (character_level_values_from_inner_text, do_nothing)
}

resistance_model_kwargs = {
    "bleed": text_to_float_div_100,
    "blight": text_to_float_div_100,
    "debuff": text_to_float_div_100,
    "death_blow": text_to_float_div_100,
    "disease": text_to_float_div_100,
    "move": text_to_float_div_100,
    "stun": text_to_float_div_100,
    "trap": text_to_float_div_100
}

skill_kwargs = {
    "Range": ("on_range", str_from_inner_text, do_nothing),
    "Rank": ("rank", value_from_dots, do_nothing),
    "Target": ("target", value_from_dots, do_nothing),
    "Damage": ("dmg_mod", str_from_inner_text, text_to_float_div_100),
    "Accuracy": ("acc", str_from_inner_text, text_to_int),
    "Crit mod": ("crit_mod", str_from_inner_text, text_to_float_div_100),
    "Effect": ("effects", str_from_inner_text, text_to_effects_dict),
    "Self": ("on_self", str_from_inner_text, text_to_effect_per_line),
    "Heal": ("heal", str_from_inner_text, do_nothing)
}
