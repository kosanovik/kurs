# Введение во Flask
# MVC-(Model View Controller)
#
from fileinput import filename
from tkinter import image_names

from flask import Flask, url_for


app = Flask(__name__)
debug = False

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


@app.route("/image")
def show_image():
#    return '<img src="./static/images/python.jpg">'
    return f'<img src="{url_for('static', filename='images/python2.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""<!DOCTYPE html>
            <html lang="ru">
                <head><meta charset="UTF-8">
                <title>Картинка Питона</title>
            </head>
            <body>
                <img src="{url_for('static', filename='images/python2.jpg')}" alt="Python">
            </body>
            </html>
    """

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=debug) # localhost - 127.0.0.1