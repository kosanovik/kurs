# Списки (list)
# Создание аббревиатур

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

N = 5

lst = [] # пустой список

for i in range(N):
    print(f"Кладём книгу {i + 1} в стопку.")
    lst.append(i+1)

print("---")

while lst:
    item = lst.pop()
    print(f"<Берём книгу {item} из стопки.")



