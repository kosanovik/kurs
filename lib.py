def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

if __name__ != "__main__":
    print("Это библиотека, а исполняемый - main.py")

class Car:
    def __init__(self, brand="Noname", model="NoModel", color="NoColor"):
        self.brand = brand # "Skoda"
        self.model = model # "Octavia"
        self.color = color # "red"
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True  # пока не сработает

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model}')
        else:
            print('Двигатель не заведён, не едем')