#!/usr/bin/python3
class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """initialize the square function"""
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)
    @size.setter
    def size(self, value):
        """initialize the square function"""
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value
    def area(self):
        """area of square"""
        area = self.__size * self.__size
        return area