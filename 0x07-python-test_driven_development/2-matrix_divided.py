#!/usr/bin/python3
"""
module with a function to divide the elements of a matrix
"""

def matrix_divided(matrix, div):
    check_matrix(matrix) #check whether if parameter is a matrix
    check_div(div) #check whether divider is of right type
    dividedMatrix = []
    new_list = []
    for i in matrix:
        for j in i:
            check_element(j) #check that element in matrix are integers of floats
            new_list.append(float(round(j/div, 2)))
        dividedMatrix.append(new_list)
        new_list = []
    return dividedMatrix

def check_matrix(matrix):
    if type(matrix) is not list:
        raise_matrix_error()
    if len(matrix) == 0:
        raise_matrix_error()
    for i in matrix:
        if type(i) is not list:
            raise_matrix_error()
        if len(i) == 0:
            raise_matrix_error()

    #check that each row is of the same length
    a = len(matrix[0])
    for row in matrix:
        if len(row) != a:
            raise TypeError('Each row of the matrix must have the same size')

def check_element(element):
    if type(element) not in [float, int]:
        raise_matrix_error()


def check_div(div):
    if type(div) not in [float, int]:
        raise TypeError('div must be a number')
    if div != div:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

def raise_matrix_error():
    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
