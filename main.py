# Введение во Flask
# MVC-(Model View Controller)
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - заменяет все на сервере из контекста запроса ("заменить")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных

from flask import Flask, url_for, request
import sqlite3

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


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()

# Так делать не будем
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)

# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - десятичная дробь
# <path:p> - может содержать слеши для указания пути
# <uuid:id> - строка-идентификатор (16 - байт в HEX-формате)
@app.route('/greeting/<user>/<int:id_num>')
def greeting(user, id_num):
    return f"Привет, {user} с id={id_num}"


@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return 'Нет номера записи'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    # print(result)
    name, city = result
    cur.close()
    con.close()
    return f'''<table border="1">
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>'''


@app.route('/form-test', methods=["POST", "GET"])
def form_test():
    if request.method == "GET":
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == "POST":
        # print(request.form['gender'])
        # print(request.form['email'])
        print(request.form)
        return "Форма успешно отправлена"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=debug) # localhost - 127.0.0.1