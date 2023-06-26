#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return ', '.join([f"{k}: {v}" for k, v in a_dictionary.items()])
