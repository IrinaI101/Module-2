def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        inner_list = []
        matrix.append(inner_list)
        for j in range(m):
            inner_list.append(value)
    return matrix
result1 = get_matrix(2, 4, 8)
result2 = get_matrix(4, 3, 7)
result3 = get_matrix(5, 6, 9)
print(result1)
print(result2)
print(result3)
