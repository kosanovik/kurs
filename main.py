# Спичочные выражения (list comprehension)
# Зансти в список каждое третье слово из предложения
text = "Списочные выражения применяются для эффективности кода"

res = [a for a in text.split() if (text.index(a) + 1) % 3 == 0] # не корректно
print(res)
res = [a for a in text.split()[2::3]] # операции со списком
print(res)
res = set(a for a in text.split()[2::3])
print(res)