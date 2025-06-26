# break, continue




num = 3 # число, которое надо угадать
flag = True # флаг изменяет значение по событию
var = ""

print("Я загадал чило, угадай его!")

while True:
    var = int(input("Ваше значение: "))
    if var == num:
        print("Ура, Угадал!")
        break
    elif var > num:
        print("Число больше загаданного")
    else:
        print("Число меньше загаданного")

print("Приходи еще!")