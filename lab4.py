from flask import Blueprint, render_template, request
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