# -*- coding: utf-8 -*-
from cgitb import text
import json
from typing import List

from difflib import SequenceMatcher
import string

from encoder import caesar_encode
from decoder import caesar_decode

text_to_encode = "Ü Ich bin der Simon und wir machen ein Treffen Samstag Abend."
success, res = caesar_encode(
    10,
    text_to_encode
)
print("Text To Encode: ")
print(text_to_encode)
print("Encoded: "+ res)

caesar_decode("AIVHIR")
#isupper

