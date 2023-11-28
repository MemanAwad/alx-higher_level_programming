#!/usr/bin/python3

""" funddtion to divide the elements of the matrix
Args:
    matrix_divided(function): the function
    matrix(list): the matrix
    div(int) the divide number"""

def matrix_divided(matrix, div):
    """ function that divide the elments of the matrix by
    the given number"""

    new = []
    new_m = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new.append(round((matrix[i][j] / div), 2))
        new_m.append(new)
        new = []
    return new_m

