from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_13 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dac238ac08a088965ebd9d0741c816571b357bcf67c5f1a2ae9a070900995a65'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Hi'

@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)