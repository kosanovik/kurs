# Функция с переменным числом аргументов
from tkinter.font import names


def multy(first, *args):
    # print(len(args)) # подсчет чмсла аргументов
    # print(args) #  можем обращаться к каждому аргументу по индексу, либо перебором в цикле
    # if len(args) == 0:
    #     return 0
    if not args:
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result

def calc(*args, operator="+"):
    match operator:
        case "+":
            result = 1
            for i in args:
                result *= i
        case "*":
            result = 1
            for i in args:
                result *= i
        case _: # случай по default
            return -float("inf")
    return result


def fio(name, surname):
    return f"{name} {surname}"
print(fio("Остап", "Бендер")) # Именованный аргумент только через обращение по имени
print(fio(surname="Бендер", name="Остап"))

def sandwich(type_of_meal, with_omion=False, with_tomato=False):
    print("Булочка")
    if with_omion:
        print("лук")
    print(type_of_meal)
    if with_tomato:
        print("помидоры")
    print("Булочка")

def print_any(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(k, "=", v)

print_any(1,2, name="Дмитрий", age=27)

sandwich("котлета", with_omion=True)

print(multy(1, 2, 3, 4)) # умножение 1*2*3*4
print(multy(-5.4, 3.2, 4.7))
print(multy(2, 3.2))
print(calc(1, 2, 3))


# Возврат нескольких значений из функции
# При распоковке "*" может быть только одна
# from tkinter.font import names
#
#
# def coordinates() -> tuple:
#     return 5.4, 3.2, 3.8, 7.2, 4.6
#
# x, y, *rest = coordinates() # распаковка. *rest - список каких то значений
# print(f"x = {x}, y = {y}, rest={rest}")
#
# *name, surname = "Остап Сулейман Бендер".split()
# print(name, surname)

# Применяем is на практике

# def print_array(array: list, start: int=None):
#     if start > len(array):
#         return
#     if start is None:
#         for i in array:
#             print(i)
#     else:
#         for i in range(start, len(array)):
#             print(array[i])
#
# a = [1, 2, 3]
# print_array(a, 0)

# Оператор is: a is b -> когда a и b - один и тот же объект
# Словарь такде изменяем как и множество со списком

# my_refregirator = ["колбаса", "сыр", "масло"]
# # his_refregirator = ["колбаса", "сыр", "масло"]
# his_refregirator = my_refregirator.copy() # [:]
# # my_refregirator += ["мясо"]
# print(his_refregirator)
# print(my_refregirator is his_refregirator)
# print(my_refregirator == his_refregirator)
# print(id(my_refregirator) == id(his_refregirator))# без id Одинаково
# temp = None
# print(type(temp))
# # if temp is None:
# print(temp is None)

# my_refregirator = ["колбаса", "сыр", "масло"]
# his_refregirator = ["колбаса", "сыр", "масло"]
# print(id(my_refregirator) == id(his_refregirator)) # без id Одинаково

# d = {"a": 1}
# print(id(d))
# d["a"] += 1
# print(id(d))

# a = [0]
# print(id(a))
# a[0] += 1
# print(id(a))


# return vs yield - return возвращает значение и завершает работу, yield возвращает, но не завершает работу, создает генератар,

# def print_goodbay(arg):
#     print("Goodbay", end=" ")
#
# def print_cruel(arg):
#     print("cruel", end=" ")
#
# def print_word(arg):
#     print("word", end=" ")
#
# def main():
#     print_goodbay(1)
#     print_cruel(1)
#     print_word(1)
#
# main()

# def generate_list():
#     for i in range(5):
#         yield i # генератор (возвращает, но не заверщает)
#
# array = tuple(generate_list())

# Области видимости
# PI = 3.1415
# shadows name "square" from outer scope

# square = "Дворцовая площадь"
#
# def greet(name):
#     print("Привет,", name)
#     name = "друг"
#     print("Здравствуй,", name)
#
# def square_area(lenght, width):
#     area = lenght * width
#     print(f"Площадь площади {square} = {area}")
#
# def circle_lenght(radius):
#     perimetr = 2 * PI * radius
#     print(f"Длина окружности с радиусом {radius} = {perimetr:.2f}")
#
# def print_array(array: list) -> None: # использование имени внешней переменной внутри функции крайне не рекомендуется
#     for item in array: # если array заменить на words
#         print(item)
#
# # Главная функция
# def main():
#     area = "Дворцовая площадь"
#     print(f"Площадь площади, где", area)
#     square_area(320, 240)
#     print("Ну что? Встречаемся, где", area)
#
# words = ["Привет", "мир"]
# PI = 3.14
# greet("Пётр")
# print("Давай встретимся, где", square)
# square_area(320, 240)
# print("Ну что? Встречаемся, где Дворцовая площадь")
# circle_lenght(5)
# print_array(words)
# print_array(["a", "b", "c"])


# a = [1, 2]
#
# def change_array():
#     a[0] = 0
#
# change_array()
# print(a)
#
#
#
#
# num_to_str = {
#
#
#     0: 'ноль',
#     1: 'один',
#     2: 'два',
#     3: 'три',
#     4: 'четыре',
#     5: 'пять',
#     6: 'шесть',
#     7: 'семь',
#     8: 'восемь',
#     9: 'девять',
#     10: 'десять',
#     11: 'одиннадцать',
#     12: 'двенадцать',
#     13: 'тринадцать',
#     14: 'четырнадцать',
#     15: 'пятнадцать',
#     16: 'шестнадцать',
#     17: 'семнадцать',
#     18: 'восемнадцать',
#     19: 'девятнадцать',
#     20: 'двадцать',
#     30: 'тридцать',
#     40: 'сорок',
#     50: 'пятьдесят',
#     60: 'шестьдесят',
#     70: 'семьдесят',
#     80: 'восемьдесят',
#     90: 'девяносто'
# }
#
# def number_to_words(n: int) -> str:
#
#
#     """
#
#
#     Функция, принимающая число и возвращающее его словами
#
#
#     :param n: двузначное числоAdd commentMore actions
#
#
#     :return: это число словами
#
#
#     """
#
#
#     if len(str(n)) > 2:
#
#
#         return 'Введите двузначное число'
#
#
#     if len(str(n)) == 1 or n in num_to_str:
#
#
#         return num_to_str[int(n)]
#
#
#     return num_to_str[int(str(n)[0] + '0')] + ' ' + num_to_str[int(str(n)[1])]
#
#
#
#
#
#
#
#
# print(number_to_words(33))
