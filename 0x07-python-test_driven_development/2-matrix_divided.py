#!/usr/bin/python3
"""
module with a function to divide the elements of a matrix
"""

def matrix_divided(matrix, div):
    """matrix_divided 

    description:
        function to divide all the elements of a matrix by div
    args:
        matrix - the matrix to be divided
        div - the divisor
    return: 
        matrix containing divided elements
    """
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
    """check_matrix
    function to raise exception if matrix is not a list of lists or\
            elements of the matrix are not integers or floats
    args:
        matrix- matrix to be divided
    """

    #check if matrix is not of class int
    if type(matrix) is not list:
        raise_matrix_error()

    #exception if matrix is empty
    if len(matrix) == 0:
        raise_matrix_error()

    #exception if matrix row are not list or are empty
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
    """
    check if element is of type int or float

    args:
        elements in the matrix
    """

    if type(element) not in [float, int]:
        raise_matrix_error()


def check_div(div):
    """
    raise exception if div is not of required format

    args:
        div - the divisor
    """
    if type(div) not in [float, int]:
        raise TypeError('div must be a number')
    if div != div:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

def raise_matrix_error():
    """
    raise exception if matrix error is found

    args:
        none
    """

    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
