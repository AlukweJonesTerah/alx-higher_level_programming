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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
