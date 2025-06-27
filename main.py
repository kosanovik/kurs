# Cтроки (immutable, iterable) является не изменяемыми
# Таблица символов

s = "\xB0"
u = "\u2603"

# две удобные функции
# ord(симмвол) - возвращает код символа в unicode
# ord(код) - возвращает символа по unicode-коду

print(u)
print("25" + s + "C")
print(f"Код снеговика в Unicode: {ord("☃")}")
print(chr(9731))
print(chr(10000))
print(chr(176)) # ASCII и Unicode

