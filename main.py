# Cтроки (immutable, iterable) является не изменяемыми
s = ""
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


