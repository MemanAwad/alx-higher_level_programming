#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        a = len(matrix[i])
        for j in range(a):
            if j != a - 1:
                endd = ' '
            else:
                endd = ''
            print("{:d}" .format(matrix[i][j]), end=endd)
        print("")
