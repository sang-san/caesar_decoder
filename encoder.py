# -*- coding: utf-8 -*-
from tools import get_index, adjust_character, alphabet_gross, alphabet_klein, characters_to_ignore

def caesar_encode(
    indexes_to_adjust: int,
    string_to_encode: str,
):
    return_str = ""

    for character in string_to_encode:
        if character == " ":
            return_str += " "
            continue


        if character in characters_to_ignore:
            return_str += character
            continue
        
        else:
            
            if not character in alphabet_gross and not character in alphabet_klein:
                continue

        try:
            is_upper = character.isupper()
            index_of = alphabet_gross.index(character) if is_upper else alphabet_klein.index(character)
        
        except:
            print("failed on character " + character + ".")
            return False, return_str

        return_str += adjust_character(character, index_of, indexes_to_adjust)

    return True, return_str