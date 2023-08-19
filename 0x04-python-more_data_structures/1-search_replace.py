def search_replace(my_list, search, replace):
    """
    Replace all occurence of an elements by another

    Parameters
    my_list : list
    search : integers of the list
    replace new integer to be replace

    Return:
        a new list with the replace element

    """

    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
