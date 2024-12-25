from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/<path:file>/')
def get_file(file):
    print(file)
    #return f'your file is {file}'
    return f'your file is {escape(file)}'


if __name__ == '__main__':
    app.run(debug=True)