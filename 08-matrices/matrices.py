
# representation of a vector.
# a vector is represented as a list of scalars
 

# representation of a matrix.
# a matrix is represented as a list of lists of scalars. (list of rows; each inner list is a row)
# all the rows must have the same size
# MODIFYING MATRICES IS FORBIDDEN
# (other option: sharing of rows is forbidden)

def constant_vector(s, n):
    # input: value of s; dimension of the vector (n)
    return [s] * n

def constant_matrix(s, m, n):
    # make a matrix whose all elements will be the scalar s.
    # input: value of s; number of rows (m) ; number of columns (n)
    return [[s] * n] * m

def identity_matrix(n):
   #input: number of dimensions (equal number of rows and columns)
   result = []
   for i in range(n):
       row = [0] * n
       row[i] = 1
       result.append(row)
   return result

def scalar_multiplication(k, A):
    # input: k : scalar; A : matrix
    # output: new matrix
    result = []
    for i in range(len(A)):
        row = A[i]
        new_row = []
        for j in range(len(row)):
           new_row.append(k*A[i][j])
        result.append(new_row)
    return result
    # for row in A:
    #     for i in range(len(row)):

def matrix_addition(A, B):
    # input: A, B : matrices of same dimension
    assert len(A)==len(B), "Input matrices dimensions don't match"
    result = []
    for i in range(len(A)):
        assert len(A[i])==len(B[i]), "Input matrices dimensions don't match"
        new_row = []
        for j in range(len(A[i])):
            new_row.append(A[i][j] + B[i][j])
        result.append(new_row)
    return result

def print_matrix(A):
    for row in A:
        print(row)

#     # output: the matrix (as a list of lists)
# 「
# |
# |
# |
# print(constant_vector(3.45, 4))
# print_matrix(constant_matrix(1.5, 4, 3))
# i5 = identity_matrix(5)
i5 = constant_matrix(1.23,5,5)
print_matrix(i5)
print_matrix(scalar_multiplication(2,i5))
m1 = [[1,2],[3,4]]
m2 = [[2,3,4],[5,6,5]]
print_matrix(matrix_addition(m1,m2))

