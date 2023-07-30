#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """method not implemented yet oops"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
