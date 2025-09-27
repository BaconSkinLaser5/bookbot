def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_char_dict_list(chars):
    char_dict_list = []
    for char in chars:
        if char.isalpha() == True:
            char_dict_list.append({'char': char, 'num': chars[char]})
    return char_dict_list
