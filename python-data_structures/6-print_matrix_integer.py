#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        spc = ""
        for element in row:
            print("{:s}{:d}".format(spc, element), end="")
            spc = " "
        print()
