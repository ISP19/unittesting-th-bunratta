ERROR_MESSAGES = {
    "invalid_type": "Invalid Type"
}


class InvalidTypeException(Exception):
    def __init__(self):
        super().__init__(ERROR_MESSAGES["invalid_type"])


def unique(lst):
    """Return a list containing only the first occurence of each distint
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
    freq_list = {}
    for item in lst:
        if item not in freq_list:
            freq_list.update({item: 1})
        else:
            freq_list[item] += 1
    return list(freq_list.keys())


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
