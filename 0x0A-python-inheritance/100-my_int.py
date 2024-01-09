#!/usr/bin/python3
""" class to inherit form int obj"""


class MyInt(int):
    """
    a class to change '==' and '!='
    """

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)
