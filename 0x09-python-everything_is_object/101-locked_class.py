#!/usr/bin/python3
"""This method defines a locked class"""


class LockedClass:
    """
    Only allows instatiation of an attribute called first_name oops    """

    __slots__ = ["first_name"]