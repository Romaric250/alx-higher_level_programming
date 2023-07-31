#!/usr/bin/python3
"""This defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file in JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
