#!/usr/bin/python3
""" define the function trilange """


def pascal_triangle(n):
    """ function to define the value n """

    if n <= 0:
        return []

    tri = [[1]]

    while len(tri) != n:
        t = tri[-1]
        p = [1]

        for x in range(len(t) - 1):
            p.append(t[x] + t[x + 1])

        p.append(1)
        tri.append(p)
    return tri
