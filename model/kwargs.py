from selenium_local.text_modifying_functions import text_to_float_div_100, text_to_int, dont_modify, \
    text_to_effect_per_line, text_to_effects_dict
from selenium_local.value_retrieving_functions import character_level_values_from_innerText, value_from_innerText, \
    value_from_dots

character_level_kwargs = {
    "max_hp": (character_level_values_from_innerText, text_to_int),
    "dodge": (character_level_values_from_innerText, text_to_float_div_100),
    "prot": (character_level_values_from_innerText, text_to_float_div_100),
    "spd": (character_level_values_from_innerText, text_to_int),
    "acc_mod": (character_level_values_from_innerText, text_to_int),
    "crit": (character_level_values_from_innerText, text_to_float_div_100),
    "dmg": (character_level_values_from_innerText, dont_modify)
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
    "Range": ("on_range", value_from_innerText, dont_modify),
    "Rank": ("rank", value_from_dots, dont_modify),
    "Target": ("target", value_from_dots, dont_modify),
    "Damage": ("dmg_mod", value_from_innerText, text_to_float_div_100),
    "Accuracy": ("acc", value_from_innerText, text_to_int),
    "Crit mod": ("crit_mod", value_from_innerText, text_to_float_div_100),
    "Effect": ("effects", value_from_innerText, text_to_effects_dict),
    "Self": ("on_self", value_from_innerText, text_to_effect_per_line),
    "Heal": ("heal", value_from_innerText, dont_modify)
}
