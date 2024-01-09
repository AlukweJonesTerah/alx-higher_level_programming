#!/usr/bin/pythpn3
"""Rectangle child to BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inherits BaseGeometry."""
    def __init__(self, width, height):
        """
        initializes Rectangle class
        Args:
            width: int value
            height: int value
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
        self.area()

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'[{str(self.__class__.__name__)}] {str(self.__width)}/{str(self.__height)}'
