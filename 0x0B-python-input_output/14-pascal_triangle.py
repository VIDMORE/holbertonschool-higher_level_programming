#!/usr/bin/python3


def pascal_triangle(n):

    counter = 1
    triangle = [[1]]
    row = []
    for i in range(1, n):
        row = [1]
        for i in range(i - 1):
            row.append(i + counter)
        counter += 1
        row.append(1)
        triangle.append(row)
    return triangle
