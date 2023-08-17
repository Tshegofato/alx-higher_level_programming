#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            squared_value = element ** 2
            new_row.append(squared_value)
        result_matrix.append(new_row)
    return result_matrix
