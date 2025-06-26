# break, continue

def get_height():
    """
    Запрашивает ввод роста, пока не будет введено корректное значение.
    """
    while True:
        try:
            height = float(input("Введите ваш рост в метрах: "))
            if 0.5 < height < 2.5:  # Пример: рост должен быть между 0.5 и 2.5 метрами
                return height
            else:
                print("Некорректный рост. Пожалуйста, введите значение в диапазоне от 0.5 до 2.5.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

# Получение роста
user_height = get_height()
print(f"Ваш рост: {user_height} м")