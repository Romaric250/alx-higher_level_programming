#!/usr/bin/python3
"""Check if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    class, otherwise false
    """
    return (type(obj) == a_class)
