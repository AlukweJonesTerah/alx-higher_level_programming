#!/usr/bin/python3
""" module defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Args:
            attrs: attribute
        Returns: json

        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json_data):
        """
        Args:
            json_data: data
        Returns: set attributes
        """
        for key, value in json_data.item():
            setattr(self, key, value)
