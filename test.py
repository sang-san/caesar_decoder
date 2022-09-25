import json
from typing import List

from difflib import SequenceMatcher
import string

from encoder import caesar_encode
from decoder import caesar_decode

success, res = caesar_encode(
    5,
    "Hallo Bin der Jochen"
)
#print(res)

caesar_decode("Mama")
#isupper

with open("static/common_words.json", "r") as f:
    common_words = json.load(f)

string_to_decode = ""

s = SequenceMatcher(None, "abcd", "bcde")
s.ratio()