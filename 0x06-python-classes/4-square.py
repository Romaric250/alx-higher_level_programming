#!/usr/bin/python3
"""mdoule defines a  square """


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """instantiate the class
        Args:
            size: the size of the square 
        Raises:
            TypeError: called when size is not int
            ValueError: caled if size is < 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """recover size of sqaure"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Cal the area of square
        Returns: size**2
        """

        return (self.__size ** 2)
