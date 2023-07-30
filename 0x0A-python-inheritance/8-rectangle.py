#!/usr/bin/python3
"""Inheri from baseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
