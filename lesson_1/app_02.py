from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='stranger'):
    return f'Hello, {name.capitalize()}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)