#!/usr/bin/python3
"""inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
        Args:
            obj (any): object to check.
            a_class (type): class to match the type of obj to.
        Returns:True. Otherwise - False.
        """
    return isinstance(obj, a_class)
