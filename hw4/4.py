def flatten_2d_matrix(matrix):
    return [item for row in matrix for item in row]

print(flatten_2d_matrix([[1,3,4],[2,5,6]]))