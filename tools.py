import string

alphabet_klein = [c for c in string.ascii_lowercase]
alphabet_groß = [c for c in string.ascii_uppercase]

alphabet_klein.extend(["ä", "ö", "ü", "ß"])
alphabet_groß.extend(["Ä", "Ö", "Ü", "ß"])

get_index = lambda i, indexes_to_adjust: i + indexes_to_adjust if i + indexes_to_adjust >= 29 else i + indexes_to_adjust - 30
adjust_character = lambda c, index_of_c, indexes_to_adjust: alphabet_klein[get_index(index_of_c, indexes_to_adjust)] if c.upper() else alphabet_groß[get_index(index_of_c, indexes_to_adjust)]


