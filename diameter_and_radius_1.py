def calculate_diameter_and_radius(adjacency_matrix):
    n = len(adjacency_matrix)

    # Инициализируем матрицу расстояний
    distance_matrix = [[float('inf')] * n for _ in range(n)]

    # Заполняем матрицу расстояний на основе матрицы смежности
    for i in range(n):
        for j in range(n):
            if i == j:
                distance_matrix[i][j] = 0
            elif adjacency_matrix[i][j] == 1:
                distance_matrix[i][j] = 1

    # Алгоритм Флойда-Уоршелла для нахождения кратчайших расстояний между всеми парами вершин
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    print('\n'.join(str(s) for s in distance_matrix))

    # Находим диаметр и радиус графа
    diameter = max(max(line) for line in distance_matrix)
    radius = min(max(line) for line in distance_matrix)

    return diameter, radius

if __name__ == '__main__':
    # Пример матрицы смежности
    adjacency_matrix = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    diameter, radius = calculate_diameter_and_radius(adjacency_matrix)

    #print(f"Диаметр графа: {diameter}")
    #print(f"Радиус графа: {radius}")
