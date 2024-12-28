import os
from flask import Flask, redirect, render_template, url_for
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab6 import populate_offices
from lab7 import lab7

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'другой-секретный-секрет')
app.config['DB_TYPE'] = os.environ.get('DB_TYPE', 'postgres')

with app.app_context():
    populate_offices()

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404
@app.errorhandler(500)
def server_error(err):
    return "ошибка сервера", 500


@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title> НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
           НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <div>
                <ol>
                    <li>
                        <a href="/lab1">Первая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab2">Вторая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab3">Третья лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab4">Четвертая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab5">Пятая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab6">Шестая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab7">Седьмая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab1/student">Студент</a>
                    </li>
                    <li>
                        <a href="/lab1/python">Про Python</a>
                    </li>
                    <li>
                        <a href="/lab1/custom">Любимая игра бати</a>
                    </li>
                </ol>
            </div>
        </main>

        <footer>
            &copy; Бобоев Михаил, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=False)