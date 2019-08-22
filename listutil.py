ERROR_MESSAGES = {
    "invalid_type": "Invalid Type"
}


class InvalidTypeException(Exception):
    def __init__(self):
        super().__init__(ERROR_MESSAGES["invalid_type"])


def unique(lst):
    """Returns a list containing only the first occurrence of each distinct
       element in list.  That is, all duplicates are omitted.

    Arguments:
        lst: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list
        (error)

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []

    """
    if type(lst) is not list:
        raise InvalidTypeException()
    freq_list = []
    for item in lst:
        if item not in freq_list:
            freq_list.append(item)
    return list(freq_list)


if __name__ == "__main__":
    """Run the doctests in all methods."""
    # from random import randint
    # print([randint(0, 22) for i in range(10000)])
    import doctest
    doctest.testmod(verbose=True)
