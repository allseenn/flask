from flask import Flask, request, render_template, url_for, abort, flash, redirect, make_response
from pathlib import PurePath, Path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Задание No1

@app.get('/01/')
def name():
    return render_template('01.html')

@app.post('/01/')
def hello():
    return f'Hello {request.form.get("name")}'

# Задание No2

@app.get('/02/')
def file_img():
    return """
<a href='/022/'>
    <img src='https://ftp.yandex.ru/mirrors/ftp.kde.org/unstable/icons/dragon.jpg' class='col-12 col-md-6 img-fluid rounded-circle' alt='Моё фото'>
</a>
"""

@app.get('/022/')
def file_upload():
    return render_template('02.html')
@app.post('/022/')
def file_uploaded():
    file = request.files.get('file')
    file.save(PurePath.joinpath(Path.cwd(), 'uploads', file.filename))
    return f'file: {file.filename} is uploaded'

# Задание No3

@app.get('/03/')
def login():
    return render_template('03.html')

@app.post('/03/')
def login_check():
    if request.form.get('name') == request.form.get('password'):
        return hello()
    else:
        return "error"
    
# Задание No4

@app.get('/04/')
def text():
    return render_template('04.html')

@app.post('/04/')
def text_check():
    return str(len(request.form.get('text').split()))

# Задание No5

@app.route('/05/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        return str(eval(request.form.get('first') + request.form.get('action') + request.form.get('second')))
    return render_template('05.html')

# Задание No6

@app.route('/06/', methods=['POST', 'GET'])
def age():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        return 'allowed' if age > 17 else abort(403)

    return render_template('06.html')

# Задание No7

@app.route('/07/', methods=['POST', 'GET'])
def square():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return f'Квадрат числа {num} равен {num**2}'
    return render_template('07.html')

# Задание No8

app.secret_key = b'12345'
@app.route('/08/', methods=['GET', 'POST'])
def flashka():
    if request.method == 'POST':
        flash(f'Привет, {request.form.get("name")}!', 'success')
    return render_template('08.html')

# Задание No9

@app.route('/09/', methods=['GET', 'POST'])
def cook():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'warning')
            return redirect(url_for('cook'))
        elif not request.form['email']:
            flash("Неверная почта", 'danger')
            return redirect(url_for('cook'))
        
        # Обработка данных формы
        response = make_response(redirect(url_for('cook')))
        response.set_cookie('username', request.form['name'])
        return response
    if name := request.cookies.get('username'):
        flash(f'{name}, привет!', 'success')
    return render_template('09.html')

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    response = make_response(redirect(url_for('cook')))
    response.delete_cookie('username')
    return response

@app.errorhandler(403)
def limita(e):
    return "Not allowed!", 403

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)

