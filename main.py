# match - case (3.10 >)
print("Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо")


while True:
    ch = input("Ваш выбор: ")
    match ch:
        case "L" | "l" | "Д" | "д":
            print("Свернули налево")
        case "R" | "r" | "К" | 'к':
            print("Свернули направо")
        case "F" | "f" | "А" | "а":
            print("Пошли прямо")
        case "Й" | "й" | "Q" | "q":
            print("До свидания!")
            break
        case _: # degault
            print("Выбор не ясен")