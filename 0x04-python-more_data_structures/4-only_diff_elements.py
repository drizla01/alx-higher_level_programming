#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
  3     """
  4     Return the set of common element present in only one set
  5 
  6     Parameter:
  7         set_1 : first set of element
  8         set_2 : second set of element
  9 
 10     Return:
 11         the result of the element present in only one sets
 12     """
 13 
 14     return (set_1 ^ set_2)

