#!/usr/bin/pythpn3
"""Square child to Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        initializes Square class
        Args:
            size: int value
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
