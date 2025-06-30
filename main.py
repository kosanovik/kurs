# Cтроки (immutable, iterable) является не изменяемыми
from ctypes.wintypes import PWORD

from pyexpat.errors import messages

# s = "" - строка не изменяемый объект
# s = set()
# res = s.add()
# s = set("") - итерированный объект преобразует в множество (изменяемый объект)

# Создаем алфавит
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphabet_u += alphabet.upper()


# Получаем входные данные
message = input("Введите строку: ").strip().lower() # обрубаем пробелы
key = int(input("Введите ключ: "))

# Инициализируем пустую строку для результата
encrypted = ("")

# Перебираем каждый символ
for letter in message:
    # Проверяем, является ли символ буквой из алфавита
    if letter in alphabet.index(letter)
    #
    # Вычисляем новую позицию с учетом сдвига
    new_key = (t + key) % len(alphabet)
    # Добавляем зашифрованный символ
    encrypted += alphabet[new_key]
else:
    # Если символ не буква, оставляем его без изменений
    encrypted += letter

# Для расшифровки достаточно изменит форму вычисления позиции:
# new_key = (t - key) % len(alhabet)

print("Зашифрованное сообщение: ",encrypted)