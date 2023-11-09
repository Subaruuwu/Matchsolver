def adjacency_to_incidence(adj_matrix):
    num_vertices = len(adj_matrix)
    num_edges = 0

    #Проверка на ориентированность
    if all(adj_matrix[i][j] == adj_matrix[j][i] for i in range(num_vertices) for j in range(num_vertices)):
        flag = 1 #Неориентированный граф
        print("Неориентированный граф")
    else:
        flag = 2 #Ориентированный граф
        print("Ориентированный граф")

    for i in range(num_vertices):
        begin = i if flag == 1 else 0
        for j in range(begin, num_vertices):
            if adj_matrix[i][j] > 0:
                num_edges += adj_matrix[i][j]
    print(num_edges)

    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    edge_count = 0

    for i in range(num_vertices):
        begin = i if flag == 1 else 0
        for j in range(begin, num_vertices):
            if adj_matrix[i][j] > 0:
                if i == j:
                    # Учтем петли
                    for k in range(adj_matrix[i][j]):
                        incidence_matrix[i][edge_count] = 2
                        edge_count += 1
                else:
                    incidence_matrix[i][edge_count] = 1
                    incidence_matrix[j][edge_count] = -1 if flag == 2 else 1
                    edge_count += 1

    return incidence_matrix

if __name__ == '__main__':
    # Пример матрицы смежности для графа (ориентированный и неориентированный)
    adjacency_matrix = [
        [4, 1, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    incidence_matrix = adjacency_to_incidence(adjacency_matrix)

    for row in incidence_matrix:
        print(row)
