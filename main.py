# Cтроки (immutable, iterable) является не изменяемыми
# Задача: посчитать количество гласных в слове


s = "язык python"

v = 0 # Число гласных

for ch in s:
    # if ch in {"а", "е", "и", "о", "у", "ы", "э", "ю", "я"}:
    #   v += 1
    if ch in "аеёиоуыэюяyo":
        v += 1

print(f"Число гласных в слове {s} = {v}")

# Перебор строки по числовому индексу
for index in range(len(s)):
    print(s[index])


print(id(s)) # адрес
s += "Привет"
print(id(s))
print(s)
print(id(s))
s += ", Дмитрий!"
print(s)
print(id(s))

#    012345
s = "Python"
# s[3] = "y" - "y" error
# Индекс может быть отрицательным (с конца)
print(f"Длина слова: {len(s)}")
print(s[-5])


