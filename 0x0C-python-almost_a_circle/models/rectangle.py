#!/usr/bin/python3
""" inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangular shape.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the top-left corner of the rectangle
        y (int): Y-coordinate of the top-left corner of the rectangle.
        id (int or None): Unique identifier of the rectangle.

    Methods:
        __init__: Initializes a new Rectangle object.
        width (property): gets the width attribute of the object
        width (width.setter): sets the new width attribute of the object
        height (property): gets the height attribute of the object
        height (height.setter): sets the new height attribute of the object

    Examples:
        Creating a Rectangle width specified width, height, and coordinates:
        >>> rectangle = Rectangle(width=10, height=20, x=5, y=5, id=1)
        Accessing the height of the rectangle:
        >>> rectangle.height
        20
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization a Rectangle object.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the top-left corner (default=0).
            y (int, optional): Y-coordinate of the top-left corner (default=0).
            id (int or None, optional): Unique identifier (default is None)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        get the width of an attribute of the object

        This property getter is used to retrieve the currect
        width attribute of the object.
        The width determines the horizintal size or extent of the object

        Returns: private width attribute int or float
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the object

        This setter method is used to update the width attribute of the object.
        The width determines the horizontal size or extent of the object

        Args:
            value (int or float): The new width to be set for the object
        Returns:
            None: This method does not return any value.

        Raises:
            TypeError: If the provided value is not numeric type (int or float),
                        a TypeError is raised.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
        get the height of an attribute of the object

        This property getter is used to retrieve the current
        height attribute of the object.
        The height determines the vertical size or extent of the object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the object

        This setter method is used to update the height attribute of the object.
        The height determines the vertical size or extent of the object

        Args:
            value (int or float): The new height to be set for the object
        Returns:
            None: This method does not return any value.

        Raises:
            TypeError: If the provided value is not numeric type (int or float),
                        a TypeError is raised.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """
        get the x of an attribute of the object

        This property getter is used to retrieve the currect
        x attribute of the object.
        The x determines the vertical size or extent of the object
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x of the object

        This setter method is used to update the x attribute of the object.
        The x determines the vertical size or extent of the object

        Args:
            value (int or float): The new x to be set for the object
        Returns:
            None: This method does not return any value.

        Raises:
            TypeError: If the provided value is not numeric type (int or float),
                        a TypeError is raised.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """
        get the y of an attribute of the object

        This property getter is used to retrieve the current
        y attribute of the object.
        The y determines the vertical size or extent of the object
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y of the object

        This setter method is used to update the y attribute of the object.
        The y determines the vertical size or extent of the object

        Args:
            value (int or float): The new y to be set for the object
        Returns:
            None: This method does not return any value.

        Raises:
            TypeError: If the provided value is not numeric type (int or float),
                        a TypeError is raised.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """
        Returns: Area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Return the dictionary representation of a Rectangle.
            Returns:
                dict: Dictionary with keys 'id', 'width', 'height', 'x', 'y'.
        """
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def to_dictionary(self):
        """
            Return the dictionary representation of a Rectangle.

            Returns:
                dict: Dictionary with keys 'id', 'width', 'height', 'x', 'y'.
        """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    def __str__(self):
        """overriding the magic string function (__str__(self))"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Args:
            *args: Arguments in the order id, width, height, x, y
        Returns:
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))
