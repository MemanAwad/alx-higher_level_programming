#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        a = len(i)
        k = 0
        for j in i:
            k += 1
            if a > k:
                print("{:d} " .format(j), end=" ")
            else:
                print("{:d}" .format(j), end="")
        print()
