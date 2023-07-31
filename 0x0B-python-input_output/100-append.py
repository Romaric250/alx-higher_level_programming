#!/usr/bin/python3
"""This mode defines a texfilet  insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line g a given string in a file
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
