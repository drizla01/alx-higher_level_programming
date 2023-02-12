#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

   """Description
   Write a function that replaces an element of a list at a
   specific position (like in C).
      ---------
      Parameter:
      		my_list:
			the list of element
		idx:
			the position of element
		element:
			the items in list
	Return:
		the list after an element has been replace
   """
   my_list[idx] = element
   if (my_list[idx] - 1)  > my_list[idx] < 0:
      	return my_list
   else:
   	return my_list
