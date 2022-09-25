import string



get_index = lambda i, indexes_to_adjust: i + indexes_to_adjust if i + indexes_to_adjust >= 25 else i + indexes_to_adjust - 26 
adjust_character = lambda c, index_of_c, indexes_to_adjust: string.ascii_lowercase[get_index(index_of_c)] if c.upper() else string.ascii_uppercase[get_index(index_of_c)]