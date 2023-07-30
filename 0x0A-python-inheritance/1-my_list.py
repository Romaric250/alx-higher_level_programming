#!/usr/bin/python3
"""This modul inherits from the list class"""


class MyList(list):
    """A class that inherits from a list"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
