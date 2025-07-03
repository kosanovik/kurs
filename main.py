# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>: <выражение>
# словарные аргументы
# потоковый ввод sys.stdin (Ctrl + D)

import sys

data = [d.strip('\n') for d in sys.stdin.readlines()]

temp =[] # индекс строки в data и число слов в виде кортежей
for i, s in enumerate(data):
    temp.append((i, len(s.split())))
print(temp)
temp.sort(key=lambda x:x[1])
index = temp[0][0]
res = sorted(data[index].split())
print(*res, sep="-")

# import sys
# # for line in sys.stdin:
# # print(line)
# data = sys.stdin.readlines()
# data = [d.strip("\n") for d in data]
# print(data)  - тоже самое что ниже

# any - любой элемент коллекции вернул True
# all - все элементы коллекции вернули True

# print(all([1, 2, 3])) # все элементы нулевые
# print(all([1, 2, 0])) # один элемент нулевой
# print(all([1]))
#
# words = "один два три".split() # > 3
# list_for_analize = list(map(lambda x: len(x) > 2, words))
# print(all(list_for_analize))


# fruits = ["арбуз", "ананас", "банан", "еживика", "арбуз", "малина"]
#
# print(sorted(fruits, key=lambda s: (len(s), s[-1]))) # сортировка по длине, по последней букве
#
# goods = [
#     ["Утюг", 1500, 2],
#     ["Фен", 1000, 5],
#     ["Телевизор", 8000, 3]
# ]
#
# print(sorted(goods, key=lambda s: (s[1], s[2], s[0])))

# numbers = [1, 2, 3, 4, 5] # list(range(1, 6))
# squares = {n: n ** 2 for n in numbers}
# print(squares)
#
# numbers = range(1, 11)
# squares = {n: n ** 2 for n in numbers if n % 2 == 0}
# print(squares)
#
# source_dict = {
#     "x": 1,
#     "y": 2,
#     "z": 3,
# }
#
# dest_dict = {k: v * 2 for k, v in source_dict.items()}
# print(dest_dict)


# ENGLISH_ABC = set([chr(ch) for ch in range(ord("a"), ord("z") + 1)])
# RUSSIAN_ABC = set([chr(ch) for ch in range(ord("а"), ord("я") + 1)] + ["ё"])
# # print(ENGLISH_ABC)
# # print(RUSSIAN_ABC)
# # ABC = ENGLISH_ABC ^ RUSSIAN_ABC ^ set(map(str.upper, ENGLISH_ABC))
# ABC = ENGLISH_ABC ^ RUSSIAN_ABC ^ set([x.upper() for x in ENGLISH_ABC]) ^ set([x.upper() for x in RUSSIAN_ABC])
# print(ABC)

# txt = "Я знаю, что я ничего не знаю. Но другие не знают и этого. А значит, я знаю больше, чем они."
# d = {}
#
#
# def remove_punctuation(text):
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, text))
#
#
# def get_words(text: str) -> list:
#     return remove_punctuation(text).split()
#
#
# def long_words(text, length=4) -> filter:
#     return filter(lambda word: len(word) >= length, get_words(text))
#
# words = get_words(txt)
#
# # Считаем частоту слов
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
#
# res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
#
# for k, v in res.items():
#     print(k, v)

# print(list(long_words(txt)))

# Функция как объект
# передается в другие функции: функции высшего порядка

# Функция критерия одбора элементов списка
# Критерий: длина слова > 6

# def is_longer_six(word):
#     return len(word) > 6
# is_longer_six = lambda word: len(word) > 6
#
#  def is_ferst_letter_a(word):
#      return word[0] == "а"
# is_ferst_letter_a = lambda word: word[0] == "а"

# Критерий - вхождение подстроки
# в астности "ан"
# def string_contains(s): # HW
#     return "ан" is s
# string_contains = lambda s: "ан" is s
#
# words = ["В", "этом", "списке", "останутся", "слова", "длина", "которых", "больше", "шесьт"]
#
# fruits = ["арбуз", "ананас", "банан", "еживика", "малина"]
#
# result = list(filter(lambda word: len(word) > 6, words))
# print(result)
#
# def square(num):
#     return num ** 2
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -> 123456789
# # nums_str = map(str, nums)
# res = "".join(map(str, nums))
# # res = "".join(nums_str)
# print(res)
#
# squares = map(square, nums)
# print(list(squares))
#
# res = list(filter(lambda x: x[0] == "а", fruits))
# print(res)
#
# res = list(filter(lambda s: "ан" in s, fruits))
# print(res)
#
# for word in filter(is_longer_six, words):
#     print(word)

# в одну строку вывести список квадратных чисел от 3 до 15
# [9, 16,25...]
# res = list(map(lambda y: y ** 2, range(3, 16)))
# res = [y ** 2 for y in range(3, 16)]
# print(res)
#
# long_words = [word for word in words if len(word) > 6]
# print(long_words)


# печатник = print
# печатник("Привет Мир")

# Функция с переменным числом аргументов
# from tkinter.font import names
#
#
# def multy(first, *args):
#     # print(len(args)) # подсчет чмсла аргументов
#     # print(args) #  можем обращаться к каждому аргументу по индексу, либо перебором в цикле
#     # if len(args) == 0:
#     #     return 0
#     if not args:
#         return 0
#     result = 1
#     for arg in args:
#         result *= arg
#     return result
#
# def calc(*args, operator="+"):
#     match operator:
#         case "+":
#             result = 1
#             for i in args:
#                 result *= i
#         case "*":
#             result = 1
#             for i in args:
#                 result *= i
#         case _: # случай по default
#             return -float("inf")
#     return result
#
#
# def fio(name, surname):
#     return f"{name} {surname}"
# print(fio("Остап", "Бендер")) # Именованный аргумент только через обращение по имени
# print(fio(surname="Бендер", name="Остап"))
#
# def sandwich(type_of_meal, with_omion=False, with_tomato=False):
#     print("Булочка")
#     if with_omion:
#         print("лук")
#     print(type_of_meal)
#     if with_tomato:
#         print("помидоры")
#     print("Булочка")
#
# def print_any(*args, **kwargs):
#     for i in args:
#         print(i)
#     for k, v in kwargs.items():
#         print(k, "=", v)
#
# def profile(name, surname, city,*children, **additional):
#     print(f"Имя: {name}")
#     print(f"Фамилия: {surname}")
#     print(f"Из города: {city}")
#     if len(children) > 0:
#         print("Дети:", ", ".join(children))
#     if "hobbie" in additional:
#         print("Хобби:", additional["hobbie"])
#     # print("Хоби:", end=": ")
#     # print(additional)
#
# profile("Дмитрий", "Колесов", "СПб", "Мария", "просто Мария", hobbie="Филателия")

# print_any("Дмитрий", "Колесов", city="Москва", age=27)

# sandwich("котлета", with_omion=True)

# print(multy(1, 2, 3, 4)) # умножение 1*2*3*4
# print(multy(-5.4, 3.2, 4.7))
# print(multy(2, 3.2))
# print(calc(1, 2, 3))


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
