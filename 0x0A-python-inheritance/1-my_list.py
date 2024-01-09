#!urs/bin/python3
""" inherits from the list class"""


class MyList(list):
    """class that inherits from list obj"""

    def print_sorted(self):
        """
        Returns:prints a sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
