#!/usr/bin/python3
"""python OOP: inheritance
"""

class MyList(list):

    """Class that inherits the attributes references of class list

    args:
        list: list

    """

    def print_sorted(self):
        """ Method that prints the sorted list
        """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
