#!/usr/bin/pythpn3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    geometry class
    """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate a parameter as an integer.
        Args:
            name: name of the parameter
            value: parameter to validate
        Returns: TypeError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
