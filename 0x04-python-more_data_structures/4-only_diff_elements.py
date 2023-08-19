#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Return the set of common element present in only one set

    Parameter:
          set_1 : first set of element
          set_2 : second set of element

    Return:
         the result of the element present in only one sets
    """

    return (set_1 ^ set_2)
