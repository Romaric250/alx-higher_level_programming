#!/usr/bin/python3
# 0-square.py by Ehoneah Obed
""" module defines a square """


class Square:
    """ represents a square"""

    def __init__(self, size=0):
        """the square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: called if size is not int
            ValueError: called if size is <0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        this func cal the area fo square
        Returns: square
        """

        return (self.__size ** 2)
