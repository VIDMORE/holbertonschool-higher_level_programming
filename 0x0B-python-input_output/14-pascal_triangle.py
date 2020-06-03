#!/usr/bin/python3
"""This module defines the functions for the pascal triangle"""

def pascal_triangle(n):
    """
    Gets each row and appends to the triangle

    Args:
        n times

    Returns:
        triangle
    """

    triangle = []
    for i in range(n):
        triangle.append(rows(i))
    return triangle


def rows(n):
    """
    Gets each row

    Args:
        n times

    Returns:
        row to append
    """

    litt = []
    if n == 0:
        return [1]
    else:
        row = rows(n-1)
        litt.append(1)
        litt += [row[i] + row[i+1] for i in range(n-1)]
        litt.append(1)

        return litt
