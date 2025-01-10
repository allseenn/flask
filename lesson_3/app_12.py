from flask import Flask
from flask_wtf.csrf import CSRFProtect

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)