import json

from difflib import SequenceMatcher
from tools import alphabet_groß, alphabet_klein

from tools import get_index, adjust_character

with open("static/common_words.json", "r") as f:
    common_words = json.load(f)

def get_percentage_matches(
    word: str,
    case_stuff: bool = True
):
    return_lst = []
    for common_word in common_words:
        
        s = SequenceMatcher(None, word, common_word)
        sR = s.ratio()
        if case_stuff:
            b = SequenceMatcher(None, word.upper(), common_word) if word.islower() else SequenceMatcher(None, word.lower(), common_word)
            bR = b.ratio()
        
        chosen_ratio = (
            sR if sR >= bR else bR
        ) if case_stuff else sR

        return_lst.append([
            common_word,
            chosen_ratio
        ])
        
        if chosen_ratio == 1.0:
            break

    return_lst.sort(key=lambda l: l[1], reverse=True)
    return return_lst

def caesar_decode(
    string_to_decode: str
):
    adjustment_index_res_lists = []

    for adjustment_index in range(len(alphabet_klein)):
        total_match = 0.0
        individual_match_lists = []

        for word in string_to_decode.split(" "):#
            best_match = get_percentage_matches(word)[0]
            
            total_match += best_match[1]
            individual_match_lists.append(best_match)

        

# [[adjustment_index, total_match, [["Hallo", 1.0], ["Simon", 0.5]]]]