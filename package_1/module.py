# module.py
# Функция публичная - т.е. к ней можно обращаться с любого места
def greet(name):
    return f"Привет, {name}"

# Скрытая функция (we're all consenting adults here)
def _hidden_fubction():
    return "Для внутреннего пользования"