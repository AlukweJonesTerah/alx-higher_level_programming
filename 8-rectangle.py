#!/usr/bin/python3
"""This class defines a rectangle class"""


class Rectangle:
    """This rep a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Init new object of rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rec"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rec"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns: perimeter of the rectangle object
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns: # rep the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        else:
            shape = (str(self.print_symbol) * self.__width + '\n') * self.__height
            return ''.join(shape)

    def __repr__(self):
        """
        Returns: str rep of the rectangle
        """
        return f'Rectangle({str(self.__width)}, {str(self.__height)})'

    def __del__(self):
        """
        print bye message when rec is deleted based on instance occured
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that return bigger or equal recs"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
