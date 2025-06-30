# Списки (list)



# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

lst = [] # пустой список
while (item := input("Ингредиенты: ")) != "":
    lst.append(item)

# исключаем повторы
temp = set(lst)
lst = list(temp)

# набираем ингредиенты, сортируем
print(f"У нас есть {len(lst)} ингредиентов: ")
lst.sort()

# выводим список
for i in range(len(lst)):
    print(f"\t{i + 1}. {lst[i]}")


