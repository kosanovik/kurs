# Cтроки (immutable, iterable) является не изменяемыми
# Таблица символов
from importlib.metadata import pass_none

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

s = set()
word = input("Введите фразу для зашифровки: ")
# Зашифровываем
for ch in word:
    s.add(ord(ch))

print(s)

# Расшифровываем

res = ""
for i in s:
    res += chr(i)
print(res)