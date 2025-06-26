num = 3 # число, которое надо угадать
flag = True # флаг изменяет значение по событию

print("Я загадал чило, угадай его!")

while flag:
    var = int(input("Ваше значение: "))
    if var == num:
        print("Ура, Угадал!")
        flag = not flag # флаг инвертирован
        # аналогично flag = False
    elif var > num:
        print("Число больше загаданного")
    else:
        print("Число меньше загаданного")

print("Приходи еще!")