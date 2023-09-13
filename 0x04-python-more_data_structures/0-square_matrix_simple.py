#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newa = []
    for ele in matrix:
        newe = []
        for n in range(0, len(ele)):
            newe.append(ele[n] ** 2)
        newa.append(newe)
    return newa
