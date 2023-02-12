#!/usr/bin/python3
def new_in_list(my_list, idx, element):

   """Description
   Write a function that replaces an element in a list at a specific
   position without modifying the original list (like in C).

    Parameters:
    		my_list: the list of element
		idx: the position of the element
		element: the item in the list
	Return
	a modified list
   """
   new_list = my_list[:]
   element = new_list[idx]

   if (my_list[idx] - 1) > my_list[idx] < 0:
   	return my_list
   return my_list
