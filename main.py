# Вложенные списки

# a = [1, 38.6, True, False, "sfs", (1, 2)] a - array
N = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matrix = [[1] * N for _ in range(N)] # _ - переменная кот не используется нигде
print(matrix)
# обход 2-мерного списка (матрицы)
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col])
# print(matrix)

