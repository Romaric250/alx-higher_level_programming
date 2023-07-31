#!/usr/bin/python3
"""This defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle 
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
