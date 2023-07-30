#!/usr/bin/python3
"""check if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    """
    return (isinstance(obj, a_class))
