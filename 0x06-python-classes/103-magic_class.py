#!/usr/bin/python3
import math
class MagicClass:
    """Magic initializtion"""
    def __init__(self, radius=0):
        self._magicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._magicClass__radius = radius
    def area(self):
        return self._magicClass__radius ** 2 * math.pi
    def circumference(self):
        return 2 * math.pi * self._magicClass__radius