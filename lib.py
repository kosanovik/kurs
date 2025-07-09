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


# class Separator:
#     def __init__(self):
#         self.odd = []
#         self.even = []
#
#     def add_num(self, num):
#         pass
#
#     def get_odd(self, num):
#         pass
#
#     def get_even(self):


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