from flask import Flask, redirect, render_template, url_for
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

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
                        <a href="/lab2">Вторая лабораторная</a>
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
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Ошибка 404</h1>
        <p>Цветка с таким номером нет</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
''', 404
    else:
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Информация о цветке</h1>
        <p>Цветок: {flower_list[flower_id]}</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
'''

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

@app.route('/lab2/add_flower/')
def add_flower_without_name():
    return 'вы не задали имя цветка', 400
@app.route('/lab2/flowers/')
def list_flowers():
    flower_count = len(flower_list)
    return render_template('flowers.html', flower_list=flower_list, flower_count=flower_count)
@app.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear()  # Очищаем список
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен</h1>
        <p>Все цветы были удалены из списка&#128532;</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
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
    

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum = a + b
    razn = a - b
    umn = a * b
    dele = a / b if b != 0 else 'деление на 0'
    step = a ** b
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Расчёт с параметрами:</h1>
        <p>Сумма: {a} + {b} = {sum}</p>
        <p>Разность: {a} - {b} = {razn}</p>
        <p>Умножение: {a} X {b} = {umn}</p>
        <p>Деление: {a} / {b} = {dele}</p>
        <p>Возведение в степень: {a}<sup>{b}</sup> = {step}</p>
    </body>
</html>
'''
# Функция Flask redirect перенаправляет пользователя на другой маршрут
@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')
@app.route('/lab2/calc/<int:a>')
def calc_redirect(a):
    return redirect(url_for('calc', a=a, b=1))


books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 417},
    {"author": "Джон Стейнбек", "title": "Гроздья гнева", "genre": "Социальный роман", "pages": 464},
    {"author": "Фрэнсис Скотт Фицджеральд", "title": "Великий Гэтсби", "genre": "Роман", "pages": 180},
    {"author": "Герман Мелвилл", "title": "Моби Дик", "genre": "Приключенческий роман", "pages": 635},
    {"author": "Даниэль Дефо", "title": "Робинзон Крузо", "genre": "Приключения", "pages": 320},
    {"author": "Артур Конан Дойл", "title": "Шерлок Холмс. Собрание сочинений", "genre": "Детектив", "pages": 944},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Жюль Верн", "title": "Двадцать тысяч лье под водой", "genre": "Фантастика", "pages": 456},
    {"author": "Чарльз Диккенс", "title": "Приключения Оливера Твиста", "genre": "Социальный роман", "pages": 554}
]

@app.route('/lab2/books/')
def book_list():
    return render_template('books.html', books=books)

movies = [
    {"title": "Начало", "description": "Фантастический триллер о мире снов и манипуляций сознанием.", "image": "inception.jpg"},
    {"title": "Зелёная миля", "description": "Драма о тюремной охране и необычном заключённом с даром исцеления.", "image": "green_mile.jpg"},
    {"title": "Побег из Шоушенка", "description": "История о надежде и дружбе заключённых в тюрьме.", "image": "shawshank_redemption.jpg"},
    {"title": "Темный рыцарь", "description": "Фильм о Бэтмене, который сталкивается с Джокером в Готэме.", "image": "dark_knight.jpg"},
    {"title": "Форрест Гамп", "description": "История простого человека с богатым жизненным опытом.", "image": "forrest_gump.jpg"}
]

@app.route('/lab2/movies/')
def movie_list():
    return render_template('movies.html', movies=movies)
    

if __name__ == "__main__":
    app.run(debug=False)