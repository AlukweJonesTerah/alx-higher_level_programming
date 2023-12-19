#!/usr/bin/python3
class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the square function"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @property
    def position(self):
        """Get/set the current size of the square."""
        return (self.__position)
    @size.setter
    def size(self, value):
        """initialize the square function"""
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of square"""
        area = self.__size * self.__size
        return area


    def my_print(self):
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print("", end="") for l in range(0, self.__position[0])]
                [print("#", end="") for j in range(0, self.__size)]
                print("#")
        else:
            print("")