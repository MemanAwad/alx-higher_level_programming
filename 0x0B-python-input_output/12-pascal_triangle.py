#!/usr/bin/python3
""" pascal triangle module"""


def pascal_triangle(n):
    """pascal triangle"""

    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        pas = pascal[-1]
        tmp = [1]
        for i in range(len(pas) - 1):
            tmp.append(pas[i] + pas[i + 1])
        tmp.append(1)
        pascal.append(tmp)

    return pascal
