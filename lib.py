from symtable import Class
from tkinter.ttk import Separator


# def summ(a, b):
#     return a + b
#
# def diff(a, b):
#     return a - b
#
# if __name__ != "__main__":
#     print("Это библиотека, а исполняемый - main.py")

class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def result(self):
        # список слов, отсортированный по длине
        return sorted(self.words, key=lambda x: len(x), reverse=True)


class Separator:
    def __init__(self):
        self.odd = []
        self.even = []  # чётные

    def add_num(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even


class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Car:
    counter = 0  # статическое свойство (счетчик машин)
    def __init__(self, brand="Noname", model="NoModel", color="NoColor"):
        self.brand = brand # "Skoda"
        self.model = model # "Octavia"
        self.color = color # "red"
        self.engine_on = False
        Car.counter += 1

    def start_engine(self):
        self.engine_on = True  # пока не сработает

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model}')
        else:
            print('Двигатель не заведён, не едем')

    @staticmethod
    def get_counter():
        return Car.counter


class Person:
    def __init__(self, name='Bill', age=1):
        # свойства (поля) класса
        self._name = name
        self._age = age

    # setters
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст — ', new_age)

    # getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Человек с именем {self._name}. Возраст: {self._age}')