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
print(res)

caesar_decode(res)
#isupper

