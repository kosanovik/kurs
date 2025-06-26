# Подбор по росту
# 150 < height < 180
# вводим до момента когда будет введен -1
# число кандидатов, число прошедших по критерию, минимальное и максимальное значение по критерию
from functools import total_ordering

total = 0
total_success = 0
total_unsuccess = 0
min_val = float("inf")
max_val = float("-inf")

while (num := int(input("Введите рост: "))) != -1:
    if 150 <= num <= 180:
        total_success += 1
        if min_val > num:
            min_val = num
        if num > max_val:
            max_val = num
    total += 1

print(f"Число кандидатов: {total}")
print(f"Число прошедших отбор: {total_success}")
print(f"Число минимального роста: {min_val}")
print(f"Число максимального роста: {max_val}")