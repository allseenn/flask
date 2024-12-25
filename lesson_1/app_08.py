from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/if/')
def show_if():
    context = {
        'title': 'If',
        'user': 'Hariton',
        'number': 10
    }
    return render_template('show_if.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)