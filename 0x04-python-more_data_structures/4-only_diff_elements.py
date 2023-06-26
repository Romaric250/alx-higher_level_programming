#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set_1 = set_1 - set_2
    unique_set_2 = set_2 - set_1
    return unique_set_1.union(unique_set_2)
