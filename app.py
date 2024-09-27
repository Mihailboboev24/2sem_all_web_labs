from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start ():
    return redirect("/menu", code=302)

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
                </ol>
            </div>
        </main>

        <footer>
            &copy ; Бобоев Михаил, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title> Бобоев Михаил Ниматбоевич. Лабораторная 1</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, Лабораторная работа 1</h1>
        </header>

        <div style="margin: 10px 0;">
            Flask — фреймворк для создания веб-приложений на языке<br>
            программирования Python, использующий набор инструментов<br>
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так<br>
            называемых микрофреймворков — минималистичных каркасов<br>
            веб-приложений, сознательно предоставляющих лишь самые базовые<br>
            возможности.
        </div>
        <a href="/menu">Меню</a>
        
        <footer style="margin-top: 20px;">
            &copy; Бобоев Михаил , ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """

