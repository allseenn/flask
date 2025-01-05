from flask import Flask, request, render_template, url_for, abort, flash
from pathlib import PurePath, Path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Задание No1
# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.

@app.get('/01/')
def name():
    return render_template('01.html')

@app.post('/01/')
def hello():
    return f'Hello {request.form.get("name")}'

# Задание No2
# Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться форма для загрузки изображений.

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
# - Создать страницу, на которой будет форма для ввода логина и пароля
# - При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.

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
# - Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# - При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

@app.get('/04/')
def text():
    return render_template('04.html')

@app.post('/04/')
def text_check():
    return str(len(request.form.get('text').split()))

# Задание No5
# - Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# - При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.

@app.route('/05/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        return str(eval(request.form.get('first') + request.form.get('action') + request.form.get('second')))
    return render_template('05.html')

# Задание No6
# - Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# - При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.

@app.route('/06/', methods=['POST', 'GET'])
def age():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        return 'allowed' if age > 17 else abort(403)

    return render_template('06.html')

# Задание No7
# - Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# - При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное число и его квадрат.

@app.route('/07/', methods=['POST', 'GET'])
def square():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return f'Квадрат числа {num} равен {num**2}'
    return render_template('07.html')

# Задание No8
# - Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# - При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет выведено "Привет, {имя}!".

app.secret_key = b'12345'
@app.route('/08/', methods=['GET', 'POST'])
def flashka():
    if request.method == 'POST':
        flash(f'Привет, {request.form.get("name")}!', 'success')
    return render_template('08.html')

@app.errorhandler(403)
def limita(e):
    return "Not allowed!", 403

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)