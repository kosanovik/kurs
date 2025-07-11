





# # Периодические задачи
# import schedule # расписание с английского
# import datetime
#
# i = 1
#
# def job():
#     global i
#     print(f"Скрипт запустился {i}-раз")
#     i += 1
#     t = datetime.datetime.now()
#     print('Время:', t.strftime('%H:%M:%S'))
#
# schedule.every(1).seconds.do(job)
#
# while True:
#     schedule.run_pending()






# Протоколы
# Протокол совокупность правил, регламентирущих функционал передачи данных между компонентов компьютерной сети
# TCP / IP
# TCP - transmission Control Protocol (TCP) (протокол управления передачи) - управляет потоками, проверяет чтобы были пакеты собраны и не были повреждены
# IP - Internet Protocol - разбивает сообщения (посылки) на пакеты (IP-дейтограммы), определяет маршруты, принимает и обрабатывает
# HTTP(S) - протокол передачи гипертекста (Huper Text Transfer Protocol (Secured))
# FTP - file transfer protocol
# SMTP - Simpole Mail Transfer Protocol
# Хост-система
# 1. Обязательная (дружественная для ПК) - IP-адрес: 195(сети различного класса).34.32.11(адрес пк в сети)
# 2. Необязательная (дружественная для пользователя) - DNS (Domain Name System)
# https://www.yandex(доменное имя).msk.ru(принадлежность)
# nic.ru / reg.ru / whois.ru(com)
# ASCII
# URL - Uniform Resourse Locator
# http(s)://домен.зона/page1/?param1=value1&param2=value2

# ./images/
# ../images/
# dir, cp(copy), mkdir(make), rm(delete), mv(move)

# import sys
#
# print('Я', sys.argv[0], 'и мой аргумент', sys.argv[1])
#
# if len(sys.argv) >= 2:
#     match sys.argv[1]:
#         case 'p':
#             print('Привет')
#         case 'g':
#             print('Пока')
#         case _:
#             print('Не понял')


# ООП

#       Условия:
# 	Базовый класс Animal с методом make_sound().
# 	Классы-наследники: Dog, Cat, Elephant с переопределением звуков.
# 	Класс Zoo хранит список животных и метод make_all_sounds().
# 	Класс BankAccount с атрибутами: _owner_name, balance.
# 	Методы: deposit(amount), withdraw(amount), get_balance().

# from abc import ABC, abstractmethod
#
#
# class Animal:
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Гаф"
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Мяу"
#
#
# class Elephant(Animal):
#     def make_sound(self):
#         return "Протрубил"
#
#
# class Zoo:
#     def __init__(self):
#         self.animals = []
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#
#     def make_all_sounds(self):
#         for animal in self.animals:
#             print(animal.make_sound())


# dog = Dog()
# cat = Cat()
# elephant = Elephant()
#
# zoo = Zoo()
#
# zoo.add_animal(dog)
# zoo.add_animal(cat)
# zoo.add_animal(elephant)
#
# zoo.make_all_sounds()




# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self._owner = owner
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Депозит пополнен на сумму {amount}")
#         else:
#             print(f"Нельзя вводить отрицательную сумму на депозит.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"с депозита снята сумма {amount}.")
#         else:
#             print(f"Не хватает средств. Овердрафт не доступен.")
#
# client1 = BankAccount("Jonh")
# client1.deposit(500)
# client1.withdraw(400)
# print("Остаток:", client1.get_balance())



#
# ООП (inheritance)
# класс, от которого наследуем: базовый, родительский, суперкласс
# класс, который наследуется называется производным и дочерним

# from math import pi
#
# from abc import ABC, abstractmethod
#
# class Shape(object):
#     def info(self):
#         print(f'Класс: {self.__class__.__name__}')
#
#     def area(self):
#         pass
#
#     def perimetr(self):
#         pass
#
# # Фигуры
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.name = 'круг'
#
#     def perimetr(self):
#         return round(2 * pi * self.radius, 2)
#
#     def area(self):
#         return round(pi * self.radius ** 2, 2)
#
#     def get_name(self):
#         return self.name
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.name = 'квадрат'
#
#     # def perimetr(self):
#     #     return 4 * self.side
#     #
#     # def area(self):
#     #     return self.side ** 2
#
# class Triangle(Square):
#     def __init__(self, side):
#         super().__init__(side)
#         self.side = side
#         self.name = "трекгольник"
#
#     def area(self):
#         return (self.side ** 2 * 3 ** 0.5) / 4
#
#     def perimetr(self):
#         return self.side * 3
#
#
# s = Square(5)
# print(s.area())
# print(s.perimetr())
# print(s.get_name())
# s.info()
#
# circle = Circle(5)
# print(circle.area())
# print(circle.perimetr())
# print(circle.get_name())
# circle.info()
#
# tr = Triangle(8)
# print(tr.area())
# print(tr.perimetr())
# print(tr.get_name())
# tr.info()



# __call__ - экземпляр класса становиться вызываемым
# (как функция)
# y = ax^2 + bx + c


# class SquareFunction:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a * x ** 2 + self.b * x + self.c
#
# s = SquareFunction(1, 2, 3)
# print(s(2))



# class Mytime:
#     def __init__(self, minutes, seconds):
#             self.seconds = seconds
#             self.minutes = minutes
#
#     def __add__(self, other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s // 60
#         s = s % 60
#         m = m % 60
#         return Mytime(m, s)
#
#     def __str__(self):
#         return f"<Time {self.minutes:02}:{self.seconds:02}>"
#
#
# t1 = Mytime(13, 15)
# t2 = Mytime(48, 25)
# print(t1 + t2)
#
# class Mytime:
#     def __init__(self, minutes, seconds):
#         if 0 <= minutes < 60:
#             self.minutes = minutes
#         if 0 <=seconds < 60:
#             self.seconds = seconds
#
#     def __str__(self):
#         return f"<Time {self.minutes}:{self.seconds}>"
#
#
# t1 = Mytime(13, 15)
# # t2 = Mytime(43, 25)
# print(t1)







# Объектно ориентированное программирование (ООП) (encapsulation)
# класс - прототип будущего объекта который описывает его свойства и поведение
# класс - данные и методы по их обработке
# экземпляр - объект пораждённый классом (объект экземпляр класса)
# атрибуты - делятся на свойства им методы
# Свойства классов
# Методы классов и анализ предыдущих вызовов
# Конструктор

# Геттеры и сеттеры

# from lib import Sorter
#
# s = Sorter()
#
# s.add_word('так')
# s.add_word('привет')
# s.add_word('пока')
# s.add_word('здорово')
#
# print(s.result())

# from lib import Separator
#
# s = Separator()
#
# for i in range(20):
#     s.add_num(i)
#
# print(s.get_even())

# from lib import Clicker
#
# cl = Clicker()
#
# cl.click()
# cl.click()
# cl.click()
#
# print(cl.get_counter())
# cl.reset()
# print(cl.get_counter())

# Статичные члены класса
# from lib import Car
#
# car = Car()
#
# print(dir(car))

# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# print('В парке машин:', Car.get_counter())

# from lib import Person
#
# p = Person()
# p.set_age(7897)
# print(p.get_name())
# p.person_info()

# p._age = 856
# print(p._age)
# print(p._name)


# from lib import Car
#
# # class Car:
# #     def __init__(self, brand="Noname", model="NoModel", color="NoColor"):
# #         self.brand = brand # "Skoda"
# #         self.model = model # "Octavia"
# #         self.color = color # "red"
# #         self.engine_on = False
# #
# #     def start_engine(self):
# #         self.engine_on = True  # пока не сработает
# #
# #     def drive_to(self, place):
# #         if self.engine_on:
# #             print(f'Едем в {place} на {self.brand} {self.model}')
# #         else:
# #             print('Двигатель не заведён, не едем')
#
#
# car = Car("Skoda", "Octavia", "red")
# car.start_engine()
# # car.engine_on = True
# car.drive_to('город')
#
# car2 = Car()
# car2.start_engine()
# car2.drive_to('город')


# class Greater:
#     def hello(self, name="Noname") -> None:
#         print('Привет,', name)
#
#     def goodbye(self):
#         print("Пока!")
#
#
# g = Greater()
# g.hello("Ольга")
# g.goodbye()
#
# g2 = Greater()
# g2.hello()
# g2.goodbye()

# # создание класса
# class Fruit:
#     pass
#
#
# a = Fruit() # экземпляр
# b = Fruit()
# с = Fruit()
#
# a.name = "Яблоко"
# a.weight = 120
# # a = 3
# # print(a.__class__.__name__.)
# b.name = "Банан"
# b.weight = 140
#
# print(a.name)
# print(с.weight)





# Регулярные выражения (поиск по паттерну)
# Regular Expressions (re)
# r-строка - raw-string ("сырая" строка)
# Квантификатор (quantity)
# {m} - ровно m раз
# {m,} - m раз и более
# {,n} - не более n раз
# {m,n} - от m до n (без пробела)
# ? - от нуля до одного (аналог {0,1})
# * - от нуля до бесконечности (32767) {0,}
# + - от 1 до бесконечности (32767) {1,}
# http://regex101.com

# import re
# import requests
#
# pattern = r'<img[^>]+src="([^">]+)"'
# # Сначала проверили
# # test_string = '<img height="50" width="150" src="images/bg.jpg">'
# html = requests.get('https://skillbox.ru').text
# result = re.findall(pattern, html)
# print(result)


# Убираем все знаки препинания
# def remove_punctuation(input_str: str) -> str:
#     # методом sub() заменяем все найденные совпадения пустой строкой и возвращаем "очищенную"
#     # :param input_str: строка со знаками припинания
#     # :return: строку, очищенную от зн. преп.
#     return re.sub(r"[^\w\s]", "", input_str)
# test_string = "Язык Python, являясь интуитивно понятным, прост для изучения! Ну и PEP8"

# pattern = r"[,.:!;]"
# test_string = "   яблоко    ;   груша, банан:   слива   !  абрикос"
# # test_string = "".join(test_string.split()) # убрали все пробелы
# result = re.split(pattern, test_string)
# # через map
# # result = list(map(lambda x: x.strip(), result))
# # через списочное выражение (list comprehension)
# result = sorted(x.strip() for x in result)
# print(result)

# дз - регулярные выражения кот убирают знаки припинания

# import re

# text = "Привет, мир! Как дела?"
# clean_text = re.sub(r'[^\w\s]', '', text)
# print(clean_text)  # Вывод: "Привет мир Как дела"

# r'[^\w\s]' — это регулярное выражение, которое означает:
# ^ — отрицание (исключение).
# \w — соответствует любому слову (буквы, цифры, подчеркивание).
# \s — соответствует любому пробельному символу (пробел, табуляция, новая строка).
# Таким образом, [^\w\s] соответствует любому символу, который не является словом или пробелом, то есть знакам препинания.
# re.sub(r'[^\w\s]', '', text) — заменяет все найденные знаки препинания на пустую строку.

#####################################################################

# import re

# pattern = r"\b\w{4}\b" # все слова из 4х символов
# pattern = r"\d" # все цифры от 0 до 9
# pattern = r"\d{3}" # три цифры подряд
# pattern = r"начало!\Z" # на что заканчивается
# pattern = r"[0-5][0-9]" # две идущие подряд
# pattern = r"[а-яА-Я]" # все буквы от а до я и от А до Я
# pattern = "[^ерм]" # вывести все не включая ерм - исключить символы
# pattern = r"\((.+?)\)" # вытащить текст из скобок
# pattern = "o{2,5}"
# pattern = "Go{2,}gle" # Google где 2 буквы o и более
# pattern = r"стеклянн?ый" # 2я Н может присутствовать
# "Жадный" и ленивый квантификатор (greedy quantifier)

# pattern = r"<img.*>" # жадный квантификатор
# pattern = r"<img.?>" # ленивый (lazy, non-greedy) квантификатор
# pattern = r"<img[^>]+src="([^">]+)" # только путь к картинке

# test_string = "Картинка <img src=bg.jpg> в тексте</p>"
# test_string = "стекляный, стеклянный, оловянный, серебряный"

# test_string = "Google, Gooogle, Goooogle"
# test_string = "Поиск по образцу (pattern)"
# test_string = "Время - 07:45"

# pattern = "<p>(.*?)</p>" # содержимое абзаца html

# pattern = r"<p[^>]*>(.*)</p>" # более универсальная запись. содержимое абзаца html с атрибутами

# test_string = "<b>Вот начало: </b><p>Содержимое</p><i>b и т.д.</i>"
# test_string = "<b>Центириуем</b><p align=center>Содержимое</p>"


# result = re.search(pattern, test_string)
# result = re.findall(pattern, test_string)
# Ternary if (тернарный условный оператор)
# print("Цифры есть") if result else print("Цифр нет")
# print(result)




# Линтеры - контролирует следование хорошим практикам
# Flake8
# pip install flake8
# (flake8-bugbear - для нахождения распространенных логических ошибок в коде)
# (pep8-naming - проверяет имена на соответствие pep8)
# pip install flake8-bugbear pep8-naming




# Библиотека pymorphy
# pip install pymorphy3
# pip install -U pymorphy3-dicts-ru

# from pymorphy3 import MorphAnalyzer
#
# form = MorphAnalyzer().parse('бутылка')[0]
#
# for btl in reversed(range(99)):
#     print(f'В холодильнике {btl + 1} {form.make_agree_with_number(btl + 1).word} пива')
#     print('Возьмём одну и выпьем')
#     if btl % 10 == 1 and btl != 11:
#         remain = 'Осталась'
#     else:
#         remain = 'Осталось'
#     print(f'{remain} {btl} {form.make_agree_with_number(btl).word} пива.')


# Исключения (runtime - время исполнения программы)
# try:
#   что пытаемся сделать
# except:
#   обрабатываем исключения
#   если исключения не было
# finally:
#   выполняется в любом случае
###################################################
# flag = False  # открывался ли на запись
#
# try:
#     fo = open('information.txt', encoding='utf-8')
# except FileNotFoundError:
#     fo = open('information.txt', 'wt', encoding='utf-8')
#     flag = True
#     print('Файл не обнаружен и создан с параметрами по умолчанию')
# # with open('information.txt', 'wt', encoding='utf-8') as fo:
# #     fo.write('По умолчанию')
# else:
#     print('Файл открыт успешно. Читаем его и закрываем.')
#     print(fo.read())
#     fo.close()
# finally:
#     if flag:  # если файл был открыт на запись
#         fo.write('По умолчанию')
#         fo.close()
#         print('Продолжаем работать.')

# Задача 1
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# try:
#     index = int(input("Введите индекс: "))
#     if not -len(lst) < index < len(lst) - 1:
#         raise ValueError("Индекс вне диапозона")
#     res = lst[index]
#     print(f"Число по индексу {index}: {lst[index]}")
# except ValueError as exp:
#     if exp.args[0].startswith("invalid literal"):
#         print(f"Вводить надо числа")
#     else:
#         print(exp)

# Практикум (обучаемый словарь)

# import pickle
#
# # минимальная версия, если файл dict.dat отсутствует
# voc = {
#     'стол': 'table',
#     'стул': 'chair',
# }
#
#
# # функция для распечатки словаря
# def print_voc():
#     print('Сейчас словарь содержит: ')
#     for k, v in voc.items():
#         print(k, '—', v)  # Alt + 0151
#
# # загружаем словарь из файла
# try:
#     with open('dict.dat', 'rb') as dump_in:
#         voc = pickle.load(dump_in)
# except FileNotFoundError:
#     with open('dict.dat', 'wb') as dump_out:
#         pickle.dump(voc, dump_out)
#     print('Создан минимальный словарь: ')
#     print_voc()
#
# while True:
#     temp = input('\nВведите слово для перевода или "#" для завершения: ')
#     word = temp.strip().lower()
#     if word == '#' or word == '№':
#         break
#     if word in voc.keys():
#         translate = voc[word]
#         print(f'Слово "{word}" переводится как {translate}.\n')
#     else:
#         print(f'Значение слова {word} отсутствует в словаре.')
#         newkey = f'А как слово {word} переводится.\n'
#         newkey += 'Если ничего не вводите нажмите ENTER,\n '
#         newkey += 'или введите его здесь: '
#         new_word = input(newkey)
#
#         if new_word != '' or len(new_word) > 2:
#             voc[word] = new_word
#             print(f'Слово {word} с переводом {new_word} внесено в словарь')
#         else:
#             print('Ничего не введено или слишком короткое слово')
#             continue
#
# # Сохранить словарь
# with open('dict.dat', 'wb') as dump_out:
#     pickle.dump(voc, dump_out)
#
# print('До новых встреч!!!')

# import pickle
#
# from docxcompose.utils import word_to_python_date_format
#
# # минимальная версия, если файл dict.dat отсутствует
# voc = {
#     "стол": "table",
#     "стул": "chair",
# }
#
# # функция для расчета словаря
# def print_voc():
#     print("Сейчас словарь содержит: ")
#     for k, v in voc.items():
#         print(k, "-", v) # Alt + 0151
#
# # загружаем словарь из файла
# try:
#     with open("dict.dat", "rb") as dump_in:
#         voc = pickle.load(dump_in)
# except FileNotFoundError:
#     with open("dict.dat", "wb") as dump_out:
#         pickle.dump(voc, dump_out)
#     print("Создан минимальный словарь: ")
#     print_voc()
#
# while True:
#     temp = input("\nВведите для перевода или # для завершения: ")
#     word = temp.strip().lower()
#     if word == "#" or word == "№":
#         break
#     if word in voc.keys():
#         translate = voc[word]
#         print(f"Слово {word} переводится как {translate}.\n")
#     else:
#         print(f"Значение слова {word} отсутствует в словаре.")
#         newkey = f"А как слово {word} переводится. "
#         newkey += "Если ничего невводите нажмите ENTER,\n "
#         newkey += "или введите его здесь: "
#         new_word = input(newkey)
#
#         if new_word != "" or len(new_word) > 2:
#             voc[word] = new_word
#             print(f"Слово {word} с переводом {new_word} внесено в словарь")
#         else:
#             print("Ничего не введено или слишком короткое слово")
#             continue
#
# # Сохранить словарь
# with open("dict.dat", "wb") as dump_out:
#     pickle.dump(voc, dump_out)
#
# print("До новых встреч")


# Задача 2
# while True:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     try:
#         result = int(a) / int (b)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!!!")
#     except ValueError:
#         print("Нужно вводить числа...")
#         print(f"A введено: {a} и {b} :(")
#     else:
#         print(result)
#         break

    # a = input("Введите первое число: ")
    # b = input("Введите второе число: ")
    #
    # if a.isdigit() and b.isdigit():
    #     if int(b) == 0:
    #         print("На ноль делить нельзя")
    #     else:
    #         print(int(a) / int(b))
    #         break
    # else:
    #     print("Вводить надо только целые числа.")


# Утверждения (assertions)
# В основном - для нужд тестирования
# try:
#     text = input("Введите текст: ")
#     assert len(text) > 3 # это утверждение
# except AssertionError:
#     print("Слишком короткий текст")


# "Бросаемся" исключениями - (throw) raise
# max_val = 10
# min_val = 1
#
# try:
#     val = int(input(f"Введите целое число от {min_val} до {max_val}: "))
#     if not min_val < val < max_val:
#         raise ValueError("Введенное число вне диапозона")
#     print(f"Введенное число {val} лежит в заданном диапозоне")
# except ValueError as exp:
#     print("Надо быть внимательнее:", exp)

# print("Остаток от деления:")
# loop = True
# while loop:
#     try:
#         value = int(input("На что делим число 10:"))
#         res  = 10 % value
#         print(f"Остаток от деления 10 на {value} = {res}")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
#     except ValueError:
#         print("Надо вводить только целые числа")
#     except Exception as exp:
#         print("Произошло исключение:",
#               exp.__class__.__name__,
#               exp)
#     else:
#         loop = False




# Файлы - набор данных, сохраненный на определенном носителе в виде определенной структуры (имя+расширение)
# Файлы и ОС
# name.txt
# t - текстовый файл
# b - бинарные файлы (jpg, avi, mp3)
# w - write (запись, если файл не существует, то он создается, если был, то в нем все стирается)
# a - append (запись в конец - дозапись)
# r - read (чтение (по умолчанию))
# print(*args, sep=' ', end='\n', file=None, flush=False)
# from itertools import count

# from path_lib import *
#
# print(img_dir)


# import pickle
# import pprint

# d = {
#     "стол": "table",
#     "стул": "chair"
# }

# сериализация
# with open("dictfile.dat", "wb") as p:
#     # d - что сериализуем
#     # p - куда сериализуем
#     pickle.dump(d, p)

# десуриализация
# with open("dictfile.dat", "rb") as p:
#     d = pickle.load(p)
#
# pprint.pprint(d, width=15)


# res = [] # пустой список
#
# with open("info.txt", "rt") as f:
#     while temp := f.readline().rstrip("\n"):
#         res += temp.split(", ")
#
# # res = list(map(lambda x: x.rstrip("\n"), res))
# # res = set(res)
#
# res = sorted(int(x) for x in set(res)) # отсортированный список
#
# print(res)



# import os
#
# path = os.getcwd()
# os.chdir(path + "/images")
#
# all_files = [f for f in os.listdir(".") if f.endswith(".jpg")]
# os.chdir("..")
#
# print(all_files)


# path = os.getcwd() # get current working directory
# print(path)
#
# os.chdir("..") # на уровень выше
# os.chdir(path + "/images")
# print(os.getcwd())


# "Мягкое" создание директории (вместо mkdirs)
# os.makedirs("libs", exist_ok=True)
# print(os.path.exists("libs")): # проверка существования пути
#     os.rmdir("libs")
# os.rmdir("libs")

# Открытие с менеджером контекста
# with open("info.txt", "rt", encoding="utf-8") as fo:
#     text = fo.read()
#     lst = text.splitlines()
#     print(lst)
# Проследит, чтобы тест закрылся

# Построчное чтение №1
# while text := fo.readline():
#    print(text.rstrip("\n"))
# Построчное чтение №2
# lst = fo.readlines()
# lst = map(lambda x: x.strip("\n"), lst)
# Построчное чтение №3
# text = fo.read()
# lst = text.splitlines()

# print(lst)
# fo = open("info.txt", "at", encoding="utf-8")

# fo.write(" Хороший текст.") # будет добавляться столько раз сколько будет запускаться

# print("\nA вот b еще одна строка.", file=fo)

# text = fo.read(11)
# fo.read(6)
# text += fo.read(8)
# print("Вот, что было в файле", end=": ")
# print(text)
# fo.close()

# fo = open("info.txt", "wt", encoding="utf-8")
#
# print(fo.mode)
# print(fo.name)
# print(fo.encoding)
#
# count = fo.write("Этот текс будет в файле!")
# print("В файл записано", count, ",байт!")
#
# fo.close()





# Пишем и подключаем свои модули
# from . lib import summ - из текущей директории
# from .. lib import summ - уровнем выше
# from . lib import summ - относительный импорт
# import lib
# lib.diff()

# from package_1 import * # для __all__ (* - greet)
# import package_1

# from package_1 import greet, add
#
# print(greet("Мир!"))
# print(add(3, 7))
# print(package_1.module._hidden_fubction())

# from lib import summ
#
# def main():
#     print(summ(7, 3))
#
#
# if __name__ == "__main__":
#     print(summ(7, 3))

# print(__name__)


# Работа с формулами:
# ...
# ws["A1"] = "=SUM(A1:A10)"

# Чтение данных
# from openpyxl import load_workbook
# wb = load_workbook("Docs/employees.xlsx")
# ws = wb.active
#
# rows_count = ws.max_row # число заполненных строк
#
# for row in ws.iter_rows(values_only=True):
#     fio, pos, dept = row
#     print(f"Фамилия: {fio}, Должность: {pos}, Отдел: {dept}")


# Запись данных в существующий файл
# from openpyxl import load_workbook
# # Открываем (загружаем) рабочую книгу
# wb = load_workbook("docs/report.xlsx")
#
# # Активный лист
# ws = wb.active
# # Можно и по имени обратиться
# # ws = wb["Отчёт"]
#
# # Заголовки
# ws["A1"] = "ФИО"
# ws["B1"] = "Должность"
# ws["C1"] = "Отдел"
#
# # Данные
# employees = [
#     ["Иванов И.И.", "Менеджер", "Продажи"],
#     ["Петров И.И.", "Бухгалтер", "Финансы"],
#     ["Сидоров И.И.", "Аналитик", "IT"]
# ]
#
# for row, data in enumerate(employees, start=2):
#     ws.cell(row=row, column=1, value=data[0])
#     ws.cell(row=row, column=2, value=data[1])
#     ws.cell(row=row, column=3, value=data[2])
#
# wb.save("Docs/employees.xlsx")


# # Способы записи
# ws["F1"] = "Привет мир"
# ws.cell(row=1, column=3, value="Привет")
#
# wb.save("docs/newtable.xlsx")
#
#
# # Пустой Exel-файл
# from openpyxl import Workbook
#
# wb = Workbook() # wb - Workbook
#
# ws = wb.active
# ws.title = "Отчёт"
#
# wb.save("docs/report.xlsx")

# from docxtpl import DocxTemplate
#
# # Загрузка шаблона
# doc = DocxTemplate("Docs/template.docx")
#
# # Данные для подстановки в шаблон
# content = {
#     "company": "ООО Монолит",
#     "employee": "Петров Д.И.",
#     "position": "Менеджер",
#     "date": "01/01/2025"
# }
#
# doc.render(content)
# doc.save("docs/about.docx")

# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.shared import Cm, Inches, Mm, Pt # Для размеров
#
# doc = Document() # Сщздание экземпляра документа
#
# # Добавление заголовка
# doc.add_heading("Отчет за месяц", 1)
# paragraph = doc.add_paragraph()
# paragraph = doc.add_paragraph("В этом отчете представлены")
# # run - что-то внутри абзаца
# paragraph.add_run(" ключевые показатели").bold  = True
# # Новый абзац для списка
# paragraph = doc.add_paragraph()
# paragraph_format = paragraph.paragraph_format
# paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
# # Маркированный
# paragraph = doc.add_paragraph("Первый пункт", style="List Bullet")
# paragraph = doc.add_paragraph("Второй пункт", style="List Bullet")
# # Нумерованный
# paragraph = doc.add_paragraph("Первый пункт", style="List Number")
# paragraph = doc.add_paragraph("Второй пункт", style="List Number")
#
# paragraph = doc.add_paragraph()
#
# # Добавляем таблицу
# table = doc.add_table(rows=3, cols=3)
# # Заполняем
# for i, row in enumerate(table.rows):
#     for j, cell in enumerate(table.columns):
#         cell.text = f"Строка {i + 1}, Столбец {j + 1}"
#
# paragraph = doc.add_paragraph()
# doc.add_picture("images/sunny_day.jpg", width=Mm(105))
#
# doc.save("Docs/report.docx")





# Графика
# PIL - Python Imagine Library. python3 -m pip install --upgrade pip - обновление установщика - обработка растровых изображений
# pip freeze > requiremets.txt - создание файла зависимости
# pip install -r requiremets.txt - установка списка библиотек
# # RGB (0...255, 0...255, 0...255)
# # thumbnail

# from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
#
# orig = Image.open('images/python.jpg').convert('RGB')
# # Размытие
# blur_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# blur_image.show()
#
# # Усиление резкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image = enchancer.enhance(4.0)
# sharpened_image.show()
#
# # Получить контуры
# edges = orig.filter(ImageFilter.FIND_EDGES)
# edges.show()


# from PIL import Image, ImageDraw, ImageFont
#
# orig = Image.open("images/sunny_day.jpg").convert("RGB")
#
# up = orig.crop((0, 0, 600, 200))
# down = orig.crop((0, 200, 600, 400))
#
# new = Image.new("RGB", (600, 400))
#
# new.paste(down, (0, 0))
# new.paste(up, (0, 200))
#
# new.show()

# from PIL import Image, ImageDraw, ImageFont
#
# # https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
# W = 600
# H = 400
#
# image = Image.new('RGB',
#                   (W, H),
#                   (0, 163, 232))
#
# draw = ImageDraw.Draw(image)
#
# text = 'Солнечный день'
# # draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
# draw.circle((600, 0), 100, fill='yellow')
# font = ImageFont.truetype(
#     font='fonts/Geisha.ttf',  # можно использовать любой установленный шрифт
#     size=50
# )
# # Получаем размеры текста
# _, _, w, h = draw.textbbox((0, 0), text, font=font)
#
# # Рассчитываем позицию для центрирования
# x = (W - w) // 2
# y = (H - h) // 2
#
# draw.text((x, y), text, fill=(255, 255, 0), font=font)
#
# image.show()
# image.save('images/sunny_day.jpg')

# from PIL import Image, ImageDraw # Image - главный составной компонет библиотеки
#
# # RED = (255, 0, 0)
# POLY = [(50, 50), (150, 50), (180, 120)]
#
# image = Image.new("RGB",
#                   (600, 400),
#                   (0, 163, 232))

# draw = ImageDraw.Draw(image)
#
# draw.line((0, 0, 600, 400), fill=(255, 0, 0), width=5)
# draw.line((600, 0, 0, 400), fill=(255, 0, 0), width=5)
# draw.rectangle((10, 10, 590, 390), outline=(255, 0, 0), width=10)
# draw.ellipse((10, 10, 590, 390), outline=(255, 0, 0), width=10)
# draw.polygon(POLY, outline="green", width=15)
#
# draw.text((100, 100), "Текст", fill=(255, 0, 0)) # как увеличить текст ДЗ + голубое небо 600х400 + текст солнечный день
#
#
# image.save("images/blue_1.jpg")

# image = Image.open('images/python.jpg')
#
#
# x, y = image.size
# mode = image.mode
# pixels = image.load() # загрузить таблицу пикселей
#
# print(f"Ширина = {x}, высота = {y}")
# print(f"Цветовая схема: {mode}")


# image_rotate = image.rotate(0) # поворот
# image_flipe = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# cropped = image.crop((250, 0, 550, 300)) # функция обрезания

# resized = image.resize((350, 300))

# # Gryscale
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         average = (r+g+b // 3)
#         pixels[i, j] = average, average, average

# # Негатив
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = 255 - r, 255 - g, 255 - b

# # Инверсия
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = g, b, r

# resized.save("images/python2.jpg")

# from pprint import pprint
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# pprint(matrix)

# import datetime as dt
#
# my_time = dt.time(12, 26,33)
# print(my_time)
# my_day = dt.date(2025, 7,4)
# print(my_day)
# my_day_time = dt.datetime.combine(my_day, my_time)
# print(my_day_time)
#
# date1 = dt.date(2025, 6,15)
# date2 = dt.date(2025, 7,3)
# delta = date2 - date1
# print(delta)


# print(dt.datetime.now())
# print(dt.datetime.now().date())
# print(dt.datetime.now().time())
#
# print(type(dt.datetime.now().time()))

# time = dt.datetime.now() # сырое время
#
# ftime = time.strftime("%d/%m/%y")
# ftime1 = time.strftime("%H:%M")
#
# print("Сегодня", ftime)
# print("Время", ftime1)



# import random as r
# r.seed(5) # отправная точка
# print(r.random())

# import random as r
#
# N = 8
#
# abc = "qweqlkdsfgdgdfgdfgdslkfg"
# num = '1234567890'
# spec = "#$@&"
#
#
# abc = list(abc)
# num = list(num)
# spec = list (spec)
#
# r.shuffle(abc)
#
# temp = abc[:N - 3]
# temp.append(r.choice(abc).upper())
# temp.append(r.choice(num))
# temp.append(r.choice(spec))
# r.shuffle(temp)
# res = "".join(temp)
#
# print(res)

# abc = "qweqlkdsfgdgdfgdfgdslkfg"
#
# lst = list(abc) + ["1", "2"] + ["#", "$"]
# r.shuffle(lst)
# res = "".join(lst[:8])
#
# print(res)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = r.sample(lst, k=5)
# print(res)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for _ in range(10):
#     print(r.sample(lst, k=5))

# zara = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684","\u2685"]
#
# for _ in range(10):
#     print(r.choice(zara), r.choice(zara))
#
# import random as r
#
# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
#
# keys = list(d.keys())
# key = r.choice(keys)
# print(d[key])
#
#
# import random as r
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# res = r.choice(lst)
# print(res)
#
# print(r.choice(['Орёл', "Решка"]))
# print(r.choice('Орёл'))

# for _ in range(10):
#     # print(r.randint(0, 10))
#     print(r.randrange(0, 10, 2))

# import math as m
# print("Число Пи:", m.pi)

# from math import *
# # from math import pi
# # from math import sqrt
# print("Число Пи:", pi)
# print("Капдратный корень 4:", sqrt(4))
# print("Синус 30:", round(sin(radians(30)), 2))
# print("Гипотинуза для 3 и 2: ", hypot(3, 2))

# print(dir(m))
# print(help(m.cos))

# lst = [1, 1, 2, 3, 5]
# res = sum([1, 2, 3])
# print(res)
# min_value = min(lst)
# max_value = max(lst)
# print(res, min_value, max_value)




# Черепашья графика

# strings = [d.strip("\n") for d in sys.stdin.readlines()]
# length = len(strings) # сколько строк
# rem = length % 3
#
# if rem:
#     strings = strings[:length - rem]
#
# for x in range(0, length - rem, 3):
#     summ = sum(len(a) for a in strings[x:x + 3])
#     result = []
#     for s in strings[x:x + 3]:
#         temp = s.lower().split()
#         result += filter(lambda a: len(a) % 2 == summ % 2, temp)
#     result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]
#     print(*result, sep=". ")





# import turtle as t # псевдоним
#
# N = 50
# t.speed(0)
# colors = ["red", "purple", "blue", 'green', "yellow", "orange"]

# t.bgcolor("black")
# angle = 360 // len(colors) - 1
#
# for x in range(200):
#     t.pencolor(colors[x % len(colors)]) # цвет для каждого витка свой
#     t.width(x // 100 + 1)
#     t.forward(x)
#     t.left(angle)

# t.penup()
# t.goto(100, 200)
# t.pendown()

# for _ in range(N):
#     t.forward(100)
#     t.right(360 // N)

# for _ in range(N):
#     t.circle(60)
#     t.right(360 // N)

# def square(side):
#     for _ in range(4):
#         t.forward(100)
#         t.right(90)
#
#
# def flower():
#     for _ in range(36):
#         t.circle(50)
#         t.right(10)
#
# def tree(lenght): # рекурсивное дереао
#     if lenght < 10:
#         return
#     t.forward(lenght)
#     t.left(30)
#     tree(lenght * 0.7)
#     t.right(60)
#     tree(lenght * 0.7)
#     t.left(30)
#     t.backward(lenght)
#
# t.left(90)
# tree(100)



# for _ in range(N):
#     square(100)
#     t.right(360 // 5)

# flower()


# t.mainloop()

# Рекурсия - функция вызывает сама себя
# def factorial(count): # 5! = 1 * 2 * 3 * 4 * 5 new*
#     result = 1
#     for i in range(2, count + 1):
#         result *= i
#     return result

# def factorial(x):
#     if x == 1 or x == 0:
#         return 1
#     return x * factorial(x - 1)
#
# for x in range(10):
#     print(x, factorial(x))


# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>: <выражение>
# словарные аргументы
# потоковый ввод sys.stdin (Ctrl + D)

# import sys
#
# data = [d.strip('\n') for d in sys.stdin.readlines()]
#
# temp =[] # индекс строки в data и число слов в виде кортежей
# for i, s in enumerate(data):
#     temp.append((i, len(s.split())))
# print(temp)
# temp.sort(key=lambda x:x[1])
# index = temp[0][0]
# res = sorted(data[index].split())
# print(*res, sep="-")

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
