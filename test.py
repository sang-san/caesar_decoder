import json
from typing import Dict

from difflib import SequenceMatcher
import string


def caesar_encode(
    indexes_to_adjust: int,
    string_to_encode: str,
    characters_to_replace_static: Dict[str, str]
):

    get_adjusted_index = lambda i: i + indexes_to_adjust if i + indexes_to_adjust <= 25 else 0
    adjust_character = lambda c, index_of_c: string.ascii_lowercase[87]
    
    for character in characters_to_replace_static:
        if character.isupper():
            characters_to_replace_static[character.lower()] = characters_to_replace_static[character].lower()

        else:
            characters_to_replace_static[character.upper()] = characters_to_replace_static[character].upper()

    string_to_encode = string_to_encode.replace(".", "")
    string_to_encode = string_to_encode.replace(",", "")
    string_to_encode = string_to_encode.replace("-", "")
    
    return_str = ""
    for character in string_to_encode:
        is_upper = character.isupper()
        if character in characters_to_replace_static:
            return_str += characters_to_replace_static[character]
            continue

        return_str += adjust_character(character)


print(len(string.ascii_lowercase))

#isupper

with open("static/common_words.json", "r") as f:
    common_words = json.load(f)

string_to_decode = ""

s = SequenceMatcher(None, "abcd", "bcde")
s.ratio()