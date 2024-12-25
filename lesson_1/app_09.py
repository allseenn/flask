from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/for/')
def show_for():
    context = {
        'title': 'Circle',
        'user': 'Hariton',
        'number': 10,
        'poem': ['Вот не думал, не гадал',
                 'программистом взял да стал',
                 'Хитрый знаю я язык',
                 'Я к другому не привык!']
    }
    return render_template('show_for.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

