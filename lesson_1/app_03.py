from flask import Flask

app = Flask(__name__)


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'path to file: {file}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)