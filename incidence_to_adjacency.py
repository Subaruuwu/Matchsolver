def incidence_to_adjacency(incidence_matrix):
    if all(incidence_matrix[i][j] >= 0 for i in range(len(incidence_matrix)) for j in range(len(incidence_matrix[0]))):
        flag = 1 #Неориентированная матрица
    else:
        flag = 2 #Ориентированная матрица

    adjacency_matrix = [[0] * len(incidence_matrix) for _ in range(len(incidence_matrix))]

    for j in range(len(incidence_matrix[0])):
        end = []
        begin = []
        for i in range(len(incidence_matrix)):
            if incidence_matrix[i][j] != 0:
                if incidence_matrix[i][j] == 2:
                    adjacency_matrix[i][i] += 1
                elif incidence_matrix[i][j] == 1:
                    begin.append(i)
                elif incidence_matrix[i][j] == -1:
                    end.append(i)
        if len(begin) == 2:
            adjacency_matrix[begin[0]][begin[1]] = 1
            adjacency_matrix[begin[1]][begin[0]] = 1
        elif len(begin) == 0:
            pass
        elif len(begin)*len(end):
            try:
                adjacency_matrix[begin[0]][end[0]] = 1
            except Exception as e:
                print(begin, end, e)

    return adjacency_matrix


if __name__ == '__main__':
    incidence_matrix = [
        [2, 2, 2, 2, 1, 1, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 1, 1, 0, -1],
        [0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 1],
    ]

    adjacency_matrix = incidence_to_adjacency(incidence_matrix)
    for row in adjacency_matrix:
        print(row)