def frequency(list, search_term):
    """Return frequency of term in list.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """

    count = list.count(search_term)
    return count
