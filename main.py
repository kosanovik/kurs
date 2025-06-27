# Cтроки (immutable, iterable) является не изменяемыми
from ctypes.wintypes import PWORD

# abc = "абвгдеёжзийклмнопрстуфхцшщъыьэюя"

# print(dir(abc))

phrase = "Язык Python"

print(phrase.lower()) # все маленькие
print(phrase.upper()) # все большие
print(phrase.capitalize()) # толькая первая буква заглавная
print(phrase.title()) # все слова с заглавной

print("Ура! " * 3) # повторение строки

print("Телевизор". count("е")) # количество вхождений подстроки
print("Python".index("h")) # индекс символа

# Каждая буква повторяется столько раз, какой ее номер в строке (считаем с 1)

word = "статор"
res = ""

for i in range(len(word)):
    print(word[i] * (i + 1), end="")


