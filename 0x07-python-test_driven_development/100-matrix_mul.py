#!/usr/bin/python3

"""
module to multiply two matrices
"""
class check_matrix:

    def __init__(self, mat, mat_name):
        self.__mat_name = mat_name
        self.__mat = mat
    
    def check_is_list(self):
        message = self.__mat_name + ' must be a list'
        if type(self.__mat) is not list:
            raise TypeError(message)

    def check_is_list_of_lists(self):
        message = self.__mat_name + ' must be a list of lists'
        for i in self.__mat:
            if type(i) is not list:
                raise TypeError(message)

    def check_is_empty(self):
        message = self.__mat_name + " can't be empty"
        if len(self.__mat) == 0:
            raise ValueError(message)
        for i in self.__mat:
            if len(i) == 0:
                raise ValueError(message)

    def check_elements(self):
        message = self.__mat_name + " should contain only integers or floats"
        for i in  self.__mat:
            for j in i:
                if type(j) not in [int, float]:
                    raise TypeError(message)
    def check_is_rectangle(self):
        message = "each row of " + self.__mat_name + " must be of the same size"
        a = len(self.__mat[0])
        for i in self.__mat:
            if len(i) != a:
                raise TypeError(message)

def matrix_mul(m_a, m_b):

    #checks for matrix a
    a = check_matrix(m_a, 'm_a')
    b = check_matrix(m_b, 'm_b')

    a.check_is_list()
    b.check_is_list()

    a.check_is_list_of_lists()
    b.check_is_list_of_lists()
    
    a.check_is_empty()
    b.check_is_empty()

    a.check_elements()
    b.check_elements()

    a.check_is_rectangle()
    b.check_is_rectangle()

    check_can_mul(m_a, m_b)

    ans = []
    ans_row = []
    ans_elem = 0
    i = 0
    j = 0
    
    while i < len(m_a):
        while j < len(m_a[i]):
            ans_elem = mul_row_column(get_row(m_a, i), get_column(m_b, j))
            ans_row.append(ans_elem)
            j += 1
        ans.append(ans_row)
        ans_row = []
        j = 0
        i += 1

    return ans

def get_row(mat, row):
    return mat[row]

def get_column(mat, column):
    l = len(mat)
    c = []
    i = 0
    while i < l:
        c.append(mat[i][column])
        i += 1
    return c
def mul_row_column(row, column):
    i = 0
    value = 0
    while i < len(row):
        value += row[i] * column[i]
        i += 1
    return value

def check_can_mul(m_a, m_b):
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
