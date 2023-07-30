#!/usr/bin/python3

"""This mod contains a function that multiplies two matrices lazilly hmm"""

import numpy as np


def lazy_matrix_mul(ma, mb):
    """Return the multiplication of two matrices it did.
    Args:
        ma (list of lists of ints/floats): The first matrix.
        mb (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(ma, mb))
