# Кортеж (tuple, immutable) не изменямый список
# Функция sorted() - возвращает сортированный список

s = {'петров', 'сидоров', 'иванов'}
r = False # True

# lst = list(s)
# lst.sort()

lst = sorted(s, reverse=r)

print(*lst, sep=", ")