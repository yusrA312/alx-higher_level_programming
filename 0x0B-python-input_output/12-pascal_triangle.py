#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tg = [[1]]
    while len(tg) != n:
        tri = tg[-1]
        tmpe = [1]
        for i in range(len(tri) - 1):
            tmpe.append(tri[i] + tri[i + 1])
        tmpe.append(1)
        tg.append(tmpe)
    return tg
