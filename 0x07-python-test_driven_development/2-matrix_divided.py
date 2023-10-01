#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    lent = len(matrix[0])
    for ele in matrix:
        if lent != len(ele):
            raise TypeError("Each row of the matrix must have the same size")
    for ele in matrix:
        for inner in ele:
            if not isinstance(inner, int) and not isinstance(inner, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    res = []
    for i in matrix:
        new = []
        for j in i:
            new.append(round((j / div), 2))
        res.append(new)
    return res
