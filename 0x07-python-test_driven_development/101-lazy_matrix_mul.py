#!/usr/bin/python3

"""This mod contains a function that multiplies two matrices lazilly hmm"""

import numpy as num


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices it did.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (num.matmul(m_a, m_b))
