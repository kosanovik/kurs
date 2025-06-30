# Cтроки (immutable, iterable) является не изменяемыми
# Начало и окончание строки
# 1. find ("подстрока")
# 2. find ("подстрока, start") - с какого
# 3. find ("подстрока, start, end") - с какого
import numbers
from itertools import count

import start

s = "Cмотреть, вертеть, видеть"

index = s.find("еть") # ищем с начала строки s
print(index)

index = s.find("еть", 10) # ищем с позиции start
print(index)

index = s.find("еть", 10, 15) # ищем с start по end
print(index)


s = "синхрофазотрон" # ищем "о": сколько их и где находятся
ch = "о"

if ch in s:
    count = s.count(ch)
    print(f" {ch} встречается в слове {s} {count} раз.")
    print("Её позиция/позиции:", end="")
    for i in range(count):
        pos = s.find(ch, start)
        numbers.add(pos)
        start += pos + 1
        print(pos, end="")
else:
    print(f"Буквы {ch} нет в слове {s}.")

index = s.find("о")
print(index)
