def fold_matrix(list_first, list_second):
    matrix = []
    for line_first, line_second in zip(list_first, list_second):
        line_new = [a + b for a, b in zip(line_first, line_second) ]
        matrix.append(line_new)
    return matrix

def matrix_multiplication(matrix_s, matrix_n):
    multiplicated_matrix = [ [0 for _ in range(len(matrix_s))] for _ in range(len(matrix_s)) ]
    for s in range(len(matrix_s)):
        for n in range(len(matrix_n)):
            for i in range(len(multiplicated_matrix)):
                multiplicated_matrix[s][n] += matrix_s[s][i] * matrix_n[i][n]
    return multiplicated_matrix
def raise_degree_of_matrix(matrix, degree):
    raised_matrix = matrix
    for _ in range(degree - 1):
        raised_matrix = matrix_multiplication(raised_matrix, matrix)
    return raised_matrix

def convert_to_reachability_matrix(adjacency_matrix):
    list_of_matrix = []
    decard_matrix = adjacency_matrix
    for i in range(2, len(adjacency_matrix)):
        decard_matrix = fold_matrix(decard_matrix, raise_degree_of_matrix(adjacency_matrix, i))

    for i in range(len(decard_matrix)):
        for j in range(len(decard_matrix)):
            if decard_matrix[i][j] > 0:
                decard_matrix[i][j] = 1
    return decard_matrix

if __name__ == '__main__':
    adjacency_matrix = [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    matrix = convert_to_reachability_matrix(adjacency_matrix)
    for row in matrix:
        print(row)
