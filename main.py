# Cтроки (immutable, iterable) является не изменяемыми
# Начало и окончание строки
# startswith и endswith

s = "Cмотреть"

if s.lower().startswith("смо"):
    print("Да")

if s.endswith("еть"):
    print("Да")