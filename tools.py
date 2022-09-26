# -*- coding: utf-8 -*-
from operator import index
import string

alphabet_klein = [c for c in string.ascii_lowercase]
alphabet_gross = [c for c in string.ascii_uppercase]

alphabet_klein.extend(["ä", "ö", "ü"])
alphabet_gross.extend(["Ä", "Ö", "Ü"])
characters_to_ignore = ["ß"]

get_index = lambda i, indexes_to_adjust: i + indexes_to_adjust if i + indexes_to_adjust <= 28 else i + indexes_to_adjust - 29
adjust_character = lambda c, index_of_c, indexes_to_adjust: alphabet_klein[get_index(index_of_c, indexes_to_adjust)] if c.islower() else alphabet_gross[get_index(index_of_c, indexes_to_adjust)]

def adjust_word(
    word: str,
    indexes_to_adjust: int
):
    new_word = ""
    for character in word:
        if character in characters_to_ignore:
            new_word += character
            continue

        try:
            is_upper = character.isupper()
            index_of = alphabet_gross.index(character) if is_upper else alphabet_klein.index(character)
        
        except:
            print("failed on character " + character + ".")
            return False, new_word, "failed on character " + character + "."
            
            
        new_word += adjust_character(character, index_of, indexes_to_adjust)
        
    return True, new_word, ""