#!/usr/bin/python3
"""module deifines a square"""


class Square:
    """class represents a square"""

    def __init__(self, size=0):
        """initialise the square class
        Args:
            size: the size of the square
        Raises:
        TypeError: called when size is not an int
        ValueError: called if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
