def flip_case(phrase, character):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    out = ""
    for char in phrase:
        if char.lower() == character.lower():
            char = char.swapcase()
        out += char

    return out
