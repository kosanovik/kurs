# Вложенные списки
N = 3
matrix = [[i + j for j in range(N)]for i in range(1, 10, 3)]
print(matrix)


# matrix = []
# table = []
#
# start = 1
# N = 4
#
# for i in range(N):
#     for j in range(start, start + N):
#         table.append(j)
#     matrix.append(table)
#     table = []
#     start += N
#
# print(matrix)

