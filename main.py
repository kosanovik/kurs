# Вложенные списки

matrix = []
table = []

start = 1
N = 4

for i in range(N):
    for j in range(start, start + N):
        table.append(j)
    matrix.append(table)
    table = []
    start += N

print(matrix)

