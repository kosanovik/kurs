# Введение во Flask
# MVC-(Model View Controller)
#
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    print("Вызвана функция index")
    return "Привет, Flask"


@app.route("/about")
def about():
    print("Вызвана функция about")
    return "О нас"

@app.route("/countdown")
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append("Полетели!!!")
    print("Вызвана функция countdown")
    return "<br>".join(lst)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True) # localhost - 127.0.0.1