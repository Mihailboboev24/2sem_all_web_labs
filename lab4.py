from flask import Blueprint, render_template, request, redirect, url_for, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/addition-form')
def addition_form():
    return render_template('lab4/addition-form.html')

@lab4.route('/lab4/addition', methods=['POST'])
def addition():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 0
    if x2 == '': x2 = 0
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/addition.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/multiplication-form')
def multiplication_form():
    return render_template('lab4/multiplication-form.html')

@lab4.route('/lab4/multiplication', methods=['POST'])
def multiplication():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 1
    if x2 == '': x2 = 1
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/multiplication.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/subtraction-form')
def subtraction_form():
    return render_template('lab4/subtraction-form.html')

@lab4.route('/lab4/subtraction', methods=['POST'])
def subtraction():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/subtraction.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/subtraction.html', x1=x1, x2=x2, result=result)
    
@lab4.route('/lab4/exponentation-form')
def exponentation_form():
    return render_template('lab4/exponentation-form.html')

@lab4.route('/lab4/exponentation', methods=['POST'])
def exponentation():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/exponentation.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 != 0 and x2 != 0:
        result = x1 ** x2
        return render_template('lab4/exponentation.html', x1=x1, x2=x2, result=result)
    return render_template('lab4/exponentation.html', error='Оба поля равны нулю!')

tree_count = 0
MAX_TREES = 10  # Максимальное количество деревьев

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'POST':
        operation = request.form.get('operation')
        if operation == 'cut' and tree_count > 0:  # Уменьшаем, если деревьев больше нуля
            tree_count -= 1
        elif operation == 'plant' and tree_count < MAX_TREES:  # Увеличиваем, если меньше MAX_TREES
            tree_count += 1
        
        # После изменения значения счетчика делаем редирект на GET-запрос страницы
        return redirect(url_for('lab4.tree'))
    
    # Обрабатываем GET-запрос, отображая страницу с текущим значением счетчика
    return render_template('lab4/tree.html', tree_count=tree_count)

users = [
    {'login': 'King', 'password': '123456', 'name': 'Eremin Zahar', 'gender': 'male'},
    {'login': 'Various Artist', 'password': '111', 'name': 'Bon Jovi', 'gender': 'male'},
    {'login': 'Sergo', 'password': 'Sektor', 'name': 'Sergei', 'gender': 'male'},
    {'login': 'Energy', 'password': 'Doom', 'name': 'Doomslayer', 'gender': 'male'},
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized=True
            name = session.get('name', '')
        else:
            authorized=False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    elif not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)


    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

    
@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        # Получаем температуру
        temperature = request.form.get('temperature')
        # Проверяем, была ли введена температура
        if temperature is None or temperature.strip() == '':
            message = "Ошибка: не задана температура"
            snow = 0
        else:
            # Преобразуем температуру в число
            temperature = int(temperature)
            
            # Проверка диапазона температуры
            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
                snow = 0
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
                snow = 0
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С"
                snow = 3
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°С"
                snow = 2
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°С"
                snow = 1
        return render_template('/lab4/fridge.html', message=message, snow=snow)
    # Обработка GET-запроса для загрузки страницы
    return render_template('/lab4/fridge.html', message=None, snow=0)