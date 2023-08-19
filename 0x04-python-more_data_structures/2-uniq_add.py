#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Add all unique integer in the list

    Parameters
    my_list:

    Return:
        List of element
    """

    result = 0
    for x in set(my_list):
        result += x

    return (result)
