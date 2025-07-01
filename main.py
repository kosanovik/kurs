# Словари
# Частотный анализ

res = {}

text = "Министерство: труда и социальной защиты, разработало проект календаря праздничных и выходных дней на 2026-й год. "

commas = (",", "-", ".", "!", ":")
for x in commas:
    text = text.replace(x, "")

lst = text.strip().lower().split()
print(lst)

for item in lst:
    if item in res.keys():
        res[item] += 1
    else:
        res[item] = 1

print("Частотный анализ слов текста")
for k, v in  res.items():
    print(f"\t{k}: {v}")


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
    (55.75, 37.5): "Москва"
}

print(d[(55.75, 37.5)])

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
if "стул" in d.values():
    print("Да есть")

print("доступ к несуществующему ключу без исключений")
pear = d.get("pear", "Груши нет") # мягкое обращение по ключу
print("Где груша: ", pear)

# перебор по умолчанию
for key in d:
    print(key, "->", d[key])

# перебор пар "ключ-значение"
for k, v in d.items():
    print(k, "->", v)

print(d.keys()) # список ключей (list)
print(list(d.keys())) # - список
print(d.values()) # список значений
print(d.items()) # список пар (ключ-значения)

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

