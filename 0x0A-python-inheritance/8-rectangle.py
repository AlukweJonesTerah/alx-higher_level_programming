#!/usr/bin/pythpn3
class BaseGeometry:
    """
    geometry class
    """

    def area(self):
        """
        Returns: raise exception error of area not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates value
        Args:
            name: str
            value: int
        Returns: raise typeerror and value errors
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
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
