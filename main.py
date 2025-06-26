# Циклы:
# while
# while <условие>:
# команды
# for

counter = 0 # обнуляем счётчик
# цикл из 5 итераций
while counter < 5:
    print(f"Итерация номер: {counter + 1}")
    # counter = counter + 1 # инкремент
    counter += 1 # инкремент (краткая запись)
print(f"Итого в counter уже {counter + 1}")
print("Обратный отсчет:")
while counter > 0:
    print(f"Итерация номер: {counter}")
    # counter = counter + 1 # инкремент
    counter += 1 # инкремент (краткая запись)