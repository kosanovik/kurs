# ДЗ: Функция (которая выводит число чловами): выводить число словами 56 -> триста пятьдесят шесть
def num_to_word(num):
    if str(num) > 3:
        return
    e = num % 10
    list = ["один", "два"]

# Функции (Do not Repeat Yourself)
# Return Value

def square(num):
    return num ** 2

def even_odd(num):
    if num % 2 == 0:
        return "Четное"
    return "Нечетное"

def print_string(s=None):
    if s is None:
        return
    print(s)

t = square(5)
print(even_odd(5))
print(t)
