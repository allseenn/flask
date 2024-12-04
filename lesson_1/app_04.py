from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>/')
def hello(name='stranger'):
    return f'Hello, {name.capitalize()}!'

@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'path to file: {file}'

@app.route('/number/<float:num>')
def set_number(num):
    print(type(num))
    return f'The number is {num}'