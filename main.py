# Словари
# Пустой словарь
# 1. d = {}
# 2. d = dict()
# Предзаполненый словарь

d = {
    "table": ["таблица", "стол"],
    "well": ["хорошо", "колодец"],
    "chair": "стул",
    "apple": "яблоко",
    1: "один",
}

print(d["table"])
print(d["well"][0])

if type(d["well"]) == list:
    d["well"].append("скважина")

print(d[1])

d["plum"] = "слива"
d["well"].append("скважина")
print(d["plum"])
del d["well"]

# print(d) # - словарь целиком как есть

deleted_item = d.pop("apple")
print("Удалился элемент:", deleted_item)

print("Если стул в словаре")
if "chair" in d:
    print("Да есть")

for key in d:
    print(key, "->", d[key])

# методы словаря
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


# N = 3
# matrix = [[i + j for j in range(N)]for i in range(1, 10, 3)]
# print(matrix)


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

