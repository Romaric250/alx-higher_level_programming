#!/usr/bin/python3
"""check if object is an instance of a class that
inherited from
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
