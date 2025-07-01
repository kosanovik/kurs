# Функции (Do not Repeat Yourself)
# Scope (local or global(как можно меньше глобальных переменных))
# Синтаксис
# def <имя функции>([параметры]):
#     команды

# в функцию передается глобальная переменная


person = "Пётр" # глобальная
count = 0


def greet_to_name(name="noname"):
    print("Привет,", name)
    print(count)


def increment():
    global count
    count += 1


def print_list(array=None):
    if array is None:
        array = []
    for item in array:
        print(item)


increment()
greet_to_name("name")
print_list()
