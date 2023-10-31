#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be list of lists contain integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a list of lists with integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
divisor = 2
result = matrix_divided(matrix, divisor)
print(result)
