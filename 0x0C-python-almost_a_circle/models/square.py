#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the top-left corner (default is 0).
            y (int, optional): Y-coordinate of the top-left corner (default is 0).
            id (int or None, optional): Unique identifier (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square.

        Returns:
            dict: Dictionary with keys 'id', 'size', 'x', 'y'.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Override the __str__ method."""
        # return f"[Square] ({self.id}) <{self.x}>/<{self.y}> - <{self.width}>"
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """
        Update the Square attributes using both no-keyword and key-worded arguments.

        Args:
            *args (int or None): No-keyword arguments in the order id, size, x, y.
            **kwargs (dict): Key-worded arguments representing attribute-value pairs.
        """
        if len(args):
            for a, arg in enumerate(args):
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
