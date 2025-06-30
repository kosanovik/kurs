# Списки (list)
# Создание аббревиатур

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

N = 5

lst = [] # пустой список

while (word := input("Введите слово: ").strip()) != "":
    lst.append(word[0].upper())

print("Получилась аббревиатура", end=": ")
print(*lst, sep="") # *lst[:10] - первые 10



