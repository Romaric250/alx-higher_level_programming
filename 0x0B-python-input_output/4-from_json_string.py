#!/usr/bin/python3
"""This defines a JSON-to-object func"""


import json


def from_json_string(my_str):
    """Returns the Python object repre of a JSON string"""
    return json.loads(my_str)
