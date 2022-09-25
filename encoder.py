import string
from typing import List

from tools import get_index, adjust_character

def caesar_encode(
    indexes_to_adjust: int,
    string_to_encode: str,
    characters_to_ignore: List[str] = [
        "ö",
        "Ö",
        "ü",
        "Ü"
    ]
):
    for character_to_remove in [
        ".", ",", ":", ";", "-", "_"
    ]:
        string_to_encode = string_to_encode.replace(character_to_remove, "")
    
    return_str = ""
    for character in string_to_encode:
        if character == " ":
            return_str += " "
            continue

        if character in characters_to_ignore:
            return_str += character
            continue

        try:
            is_upper = character.isupper()
            index_of = string.ascii_uppercase.index(character) if is_upper else string.ascii_lowercase.index(character)
        
        except:
            print("failed on character " + character + ".")
            return False, return_str

        return_str += adjust_character(character, index_of, indexes_to_adjust)

    return True, return_str