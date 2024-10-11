from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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

@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title> Бобоев Михаил Ниматбоевич. Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
        
        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href="/lab1/student">/lab1/student</a></li>
            <li><a href="/lab1/python">/lab1/python</a></li>
            <li><a href="/lab1/custom">/lab1/custom</a></li>
        </ul>
        
        <footer>
            &copy; Бобоев Михаил , ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title> Студент </title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            <h1>Бобоев Михаил Ниматбоевич</h1>
        </header>
        <main>
            <img src="''' + url_for('static', filename='ngtu_logo.png') + '''" alt="Логотип НГТУ">
        </main>
        <footer>
            &copy; Бобоев Михаил, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title> Про Python </title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            <h1>Про язык программирования Python</h1>
        </header>
        <main>
            <p>Python — это высокоуровневый язык программирования общего назначения. Его синтаксис прост и позволяет разработчикам писать коды быстрее по сравнению с другими языками программирования. Python активно используется в области искусственного интеллекта, веб-разработки, анализа данных и других сферах.</p>
            <p>Основные достоинства Python — это поддержка различных парадигм программирования, широкий набор библиотек и высокая читаемость кода. Это делает его популярным выбором для программистов всех уровней.</p>
            <img src="''' + url_for('static', filename='python_logo.jpg') + '''" alt="Логотип Python">
        </main>
        <footer>
            &copy; Бобоев Михаил, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/custom")
def custom():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title> На выбор студента </title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            <h1>Фаллаут 4</h1>
        </header>
        <main>
            <p>Fallout 4 — компьютерная игра в жанре action/RPG, разработанная Bethesda Game Studios и изданная Bethesda Softworks. Является частью серии Fallout. Игра была выпущена 10 ноября 2015 года на Windows, PlayStation 4 и Xbox One.</p>
            <p>Основная часть игры происходит в 2287 году, спустя 210 лет после ядерной войны, уничтожившей большую часть населения Земли. 2 Действие разворачивается в постапокалиптическом Бостоне и его окрестностях (Содружество Массачусетс).</p>
            <img src="''' + url_for('static', filename='fallout_4.jpg') + '''" alt="Кастомное изображение">
        </main>
        <footer>
            &copy; Бобоев Михаил, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['подсолнух', 'папортоник', 'незабудка', 'лопух']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return 'такого цветка нет', 404
    else:
        return 'цветок: ' + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, number_lab, group_student, number_course = 'Бобоев Михаил', 2, 'ФБИ-24', 3
    fruits = [
        {'name': 'папая', 'price': 84},
        {'name': 'слива', 'price': 124},
        {'name': 'апельсины', 'price': 89},
        {'name': 'арбуз', 'price': 43},
        {'name': 'ежевика', 'price': 231}
    ]
    return render_template('example.html', name=name, group_student=group_student, number_course=number_course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)
    
if __name__ == "__main__":
    app.run(debug=False)