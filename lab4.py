from flask import Blueprint, render_template, request, redirect, url_for
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
    {'login': 'King', 'password': '123456'},
    {'login': 'Various Artist', 'password': '111'},
    {'login': 'Sergo', 'password': 'Sektor'},
    {'login': 'Energy', 'password': 'Doom'},
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab4/login.html', authorized=False)
    login = request.form.get('login')
    password = request.form.get('password')
    if login == 'alex' and password == '123':
        return render_template('lab4/login.html', login=login, authorized=True)
    for user in users:
        if login == user['login'] and password == user['password']:
            return render_template('lab4/login.html', login=login, authorized=True)
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False)